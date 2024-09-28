import requests
from bs4 import BeautifulSoup
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import spacy
from langchain_text_splitters import CharacterTextSplitter
import os
import openai
from dotenv import load_dotenv, dotenv_values
load_dotenv()

api_key = dotenv_values().get("OPENAI_API_KEY")

openai.api_key = api_key

client = openai.OpenAI(api_key=api_key)


def scrape():
    url = "https://www.podatki.gov.pl/pcc-sd/rozliczenie-podatku-pcc-od-kupna-samochodu/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 2: Extract relevant data
    # Example: Extract all text inside <p> tags
    paragraphs = soup.find_all('p')
    text_data = [p.get_text().strip() for p in paragraphs]

    return text_data

def preprocess(combined_text):
    nlp = spacy.load('pl_core_news_md')

    docs = nlp.pipe(text.lower() for text in combined_text)
    texts = []
    for doc in docs:
        processed_text = " ".join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])
        texts.append(processed_text)
    return texts

def vectorize(texts):
    responses = {}
    for text in texts:
        resp = client.embeddings.create(
        input = texts[0],
        model = "text-embedding-ada-002"
        )
        responses[text] = resp.data[0]
    return responses


paragraphs = scrape()
preprocessed = preprocess(paragraphs)
responses = vectorize(preprocessed)








