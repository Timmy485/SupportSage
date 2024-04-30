from dotenv import load_dotenv
import os, pymongo, pprint
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
from llama_index.core.settings import Settings
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch

load_dotenv()
ATLAS_CONNECTION_STRING = os.environ.get('ATLAS_URI')
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_KEY")



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