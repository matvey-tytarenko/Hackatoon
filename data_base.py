import requests
from bs4 import BeautifulSoup
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import os
import spacy
from langchain_text_splitters import CharacterTextSplitter
import openai
import chromadb
from chromadb import Settings
from dotenv import load_dotenv, dotenv_values
load_dotenv()

EMBEDDING_MODEL = "text-embedding-ada-002"
DB_PATH = "./db/"

api_key = dotenv_values().get("OPENAI_API_KEY")

client = openai.OpenAI(api_key=api_key)

chroma = chromadb.PersistentClient(path=DB_PATH)
collection = chroma.get_or_create_collection(name="rag_collection")


def get_embedding(text):
    response = client.embeddings.create(
        input=text,
        model=EMBEDDING_MODEL
    )
    return response.data[0].embedding

def populate():

    def scrape():
        url = "https://www.podatki.gov.pl/pcc-sd/rozliczenie-podatku-pcc-od-kupna-samochodu/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Step 2: Extract relevant data
        # Example: Extract all text inside <p> tags
        paragraphs = soup.find_all(('p', 'h1', 'h2', 'h3'))
        text_data = [p.get_text().strip() for p in paragraphs]

        text_combined = "\n".join(text_data)

        return text_combined

    def preprocess(combined_text):
        nlp = spacy.load('pl_core_news_lg')

        docs = nlp(text.lower())
        texts = []
        processed_text = " ".join([token.lemma_ for token in docs if not token.is_stop and token.is_alpha])
        return processed_text

    text = scrape()
    # preprocessed = preprocess(text)
    preprocessed = text
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    text_chunks = text_splitter.split_text(preprocessed)
    embeddings = [get_embedding(chunk) for chunk in text_chunks]

    # Add documents (text chunks) with embeddings to the collection
    collection.add(
        documents=text_chunks,
        embeddings=embeddings,
        ids=[f"chunk_{i}" for i in range(len(text_chunks))]
    )


# Function to retrieve the most relevant text chunks based on a query
def retrieve_relevant_chunks(query, n_results=3):
    # Embed the query
    query_embedding = get_embedding(query)

    # Query the ChromaDB collection
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    # Return the most relevant documents
    return results['documents'][0]

