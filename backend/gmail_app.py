from flask import Flask, redirect, request, session, jsonify, url_for
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow 
from googleapiclient.discovery import build
import os
import pickle
from bs4 import BeautifulSoup
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_KEY")

# REDIRECT_URI = os.environ.get("DEVELOPMENT_REDIRECT_URI")
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']


@app.route('/')
def index():
    return redirect(url_for('read_emails'))


def get_gmail_service():
    creds = None
  
    # The file token.pickle contains the user access token. 
    # Check if it exists 
    if os.path.exists('token.pickle'): 
  
        # Read the token from the file and store it in the variable creds 
        with open('token.pickle', 'rb') as token: 
            creds = pickle.load(token) 
  
    # If credentials are not available or are invalid, ask the user to log in. 
    if not creds or not creds.valid: 
        if creds and creds.expired and creds.refresh_token: 
            creds.refresh(Request()) 
        else: 
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES) 
            creds = flow.run_local_server() 
  
        # Save the access token in token.pickle file for the next run 
        with open('token.pickle', 'wb') as token: 
            pickle.dump(creds, token) 

    return build('gmail', 'v1', credentials=creds)



@app.route('/read_emails')
def read_emails():
    service = get_gmail_service()

    # request a list of all the messages 
    unread_messages = service.users().messages().list(userId='me', labelIds=['INBOX'], q='is:unread').execute()

    unread_emails = []
    for message in unread_messages.get('messages', []):
        msg_id = message['id']
        email = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
        
        headers = email.get('payload', {}).get('headers', [])
        subject = next((header['value'] for header in headers if header['name'].lower() == 'subject'), 'No Subject')
        from_email = next((header['value'] for header in headers if header['name'].lower() == 'from'), 'Unknown Sender')
        date_received = next((header['value'] for header in headers if header['name'].lower() == 'date'), 'Unknown Date')
        
        # Extracting the body of the email
        parts = email.get('payload', {}).get('parts', [])
        body = ""
        if parts:
            for part in parts:
                body += part.get('body', {}).get('data', '')
        else:
            body = email.get('payload', {}).get('body', {}).get('data', '')
        
        # Convert from base64 URL safe encoding to text
        if body:
            import base64
            body = base64.urlsafe_b64decode(body).decode('utf-8')
        
        # Clean the body using BeautifulSoup if needed
        soup = BeautifulSoup(body, 'html.parser')
        clean_body = soup.get_text()
        
        unread_emails.append({
            'id': msg_id,
            'subject': subject,
            'from': from_email,
            'date': date_received,
            'snippet': email.get('snippet', ''),
            'body': body
        })
    
    # Mark retrieved emails as read
    for email in unread_emails:
        service.users().messages().modify(userId='me', id=email['id'], body={'removeLabelIds': ['UNREAD']}).execute()
    
    for email in unread_emails:
        query = email.body

    return jsonify(unread_emails)

if __name__ == "__main__":
    app.run(debug=True, port=5050)
