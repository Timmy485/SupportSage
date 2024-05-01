from dotenv import load_dotenv
import os, pymongo, pprint
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
from llama_index.core.settings import Settings
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow 
from googleapiclient.discovery import build
import pickle
from googleapiclient.errors import HttpError

load_dotenv()
ATLAS_CONNECTION_STRING = os.environ.get('ATLAS_URI')
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_KEY")

SCOPES = ['https://www.googleapis.com/auth/gmail.modify', 'https://www.googleapis.com/auth/gmail.send']
current_dir = os.path.dirname(os.path.abspath(__file__))
token_path = os.path.join(current_dir, 'token.pickle')
credentials_path = os.path.join(current_dir, 'credentials.json')



def get_vector_index(): 
    db_name = "smart_solutions_db"
    collection_name = "policies[100_chunk, 100 overlap]"
    # Connect to your Atlas cluster
    mongodb_client = pymongo.MongoClient(ATLAS_CONNECTION_STRING)

    # Instantiate the vector store
    atlas_vector_search = MongoDBAtlasVectorSearch(
        mongodb_client,
        db_name = db_name,
        collection_name = collection_name,
        index_name = "vector_index"
    )

    return VectorStoreIndex.from_vector_store(atlas_vector_search)


def get_gmail_service():
    creds = None
  
    # The file token.pickle contains the user access token. 
    # Check if it exists 
    if os.path.exists(token_path): 
  
        # Read the token from the file and store it in the variable creds 
        with open(token_path, 'rb') as token: 
            creds = pickle.load(token) 
  
    # If credentials are not available or are invalid, ask the user to log in. 
    if not creds or not creds.valid: 
        if creds and creds.expired and creds.refresh_token: 
            creds.refresh(Request()) 
        else: 
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES) 
            creds = flow.run_local_server() 
  
        # Save the access token in token.pickle file for the next run 
        with open(token_path, 'wb') as token: 
            pickle.dump(creds, token) 

    return build('gmail', 'v1', credentials=creds)


def mark_email_as_read(email_id, service):
    try:
        # Mark the email as read
        service.users().messages().modify(userId='me', id=email_id, body={'removeLabelIds': ['UNREAD']}).execute()
        print(f'Email with ID {email_id} marked as read')
    except HttpError as error:
        print(f"An error occurred while marking email as read: {error}")