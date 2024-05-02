from app import app
from flask import request, jsonify
from email.message import EmailMessage
import base64
from googleapiclient.errors import HttpError
import os
import re
import os
from bs4 import BeautifulSoup
from llama_index.core.settings import Settings
from llama_index.postprocessor.cohere_rerank import CohereRerank
from llama_index.llms.openai import OpenAI
from .helpers import get_vector_index, get_gmail_service, mark_email_as_read
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_KEY")
COHERE_API_KEY = os.environ.get("COHERE_API_KEY")

SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]
Settings.llm = OpenAI(model="gpt-4-turbo")
top_k = 5
top_n = 3


@app.route("/")
def index():
    return jsonify({"message": "Flask application is running successfully!"})


@app.route("/read_emails")
def read_emails():
    service = get_gmail_service()

    # initialize cohere reranker
    cohere_rerank = CohereRerank(api_key=COHERE_API_KEY, top_n=top_n)

    index = get_vector_index()
    # Create a query engine with a default retriever
    query_engine = index.as_query_engine(
        similarity_top_k=top_k, node_postprocessors=[cohere_rerank]
    )

    # request a list of all the messages
    unread_messages = (
        service.users()
        .messages()
        .list(userId="me", labelIds=["INBOX"], q="is:unread")
        .execute()
    )

    print("Processing Emails")
    processed_emails = []
    for message in unread_messages.get("messages", []):
        print("Processing Email")
        msg_id = message["id"]
        email = (
            service.users()
            .messages()
            .get(userId="me", id=msg_id, format="full")
            .execute()
        )

        headers = email.get("payload", {}).get("headers", [])
        subject = next(
            (
                header["value"]
                for header in headers
                if header["name"].lower() == "subject"
            ),
            "No Subject",
        )
        from_email = next(
            (header["value"] for header in headers if header["name"].lower() == "from"),
            "Unknown Sender",
        )
        date_received = next(
            (header["value"] for header in headers if header["name"].lower() == "date"),
            "Unknown Date",
        )

        # Extracting the body of the email
        parts = email.get("payload", {}).get("parts", [])
        body = ""
        if parts:
            for part in parts:
                body += part.get("body", {}).get("data", "")
        else:
            body = email.get("payload", {}).get("body", {}).get("data", "")

        # Convert from base64 URL safe encoding to text
        if body:
            import base64

            body = base64.urlsafe_b64decode(body).decode("utf-8")

        # Clean the body using BeautifulSoup if needed
        soup = BeautifulSoup(body, "html.parser")
        clean_body = soup.get_text()
        clean_text = re.sub(r"\s+", " ", clean_body)

        response = query_engine.query(clean_text)
        processed_emails.append(
            {
                "id": msg_id,
                "subject": subject,
                "from": from_email,
                "date": date_received,
                "snippet": email.get("snippet", ""),
                "body": clean_text,
                "response": response.response,
                "is0pen": False
            }
        )

    return jsonify(processed_emails)


@app.route("/send_email", methods=["POST"])
def send_email():
    data = request.json
    msg_id = data.get("id")
    to_email = data.get("from")
    subject = data.get("subject")
    body = data.get("response")
    sender = to_email.split("<")[0]

    if match := re.search(r"<([^>]+)>", to_email):
        to_email = match[1]
    else:
        to_email = to_email

    if not all([to_email, subject, body]):
        return jsonify({"error": "Missing required fields"}), 400

    service = get_gmail_service()

    # Construct the reply body
    reply_body = f"Dear {sender},\n\n{body}\n\n\n\nSupport Sage Services"

    # Create an EmailMessage object
    reply_message = EmailMessage()
    reply_message.set_content(reply_body)
    reply_message["To"] = to_email
    reply_message["Subject"] = subject

    # Add references and in-reply-to headers for threading
    reply_message["References"] = msg_id
    reply_message["In-Reply-To"] = msg_id

    # Encode the message
    raw_message = base64.urlsafe_b64encode(reply_message.as_bytes()).decode()
    message_payload = {"raw": raw_message}

    try:
        # Send the reply email
        sent_message = (
            service.users().messages().send(userId="me", body=message_payload).execute()
        )
        print(f"Message sent successfully. Message ID: {sent_message['id']}")

        # Mark the original email as read
        mark_email_as_read(msg_id, service)

        return (
            jsonify(
                {"message": "Email sent successfully", "message_id": sent_message["id"]}
            ),
            200,
        )
    except Exception as e:
        print(f"Error sending message: {str(e)}")
        return jsonify({f"error: Failed to send email with message:  {str(e)}"}), 500


@app.errorhandler(404)
def not_found(e):
    return jsonify(error=404, text=str(e)), 404
