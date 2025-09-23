from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",dimensions=32)

documents = [
    "Delhi is the capital of india",
    "Kolkata is the capital of west bengal",
    "Paris is the capital of France"
]
result = embedding.embed_documents(documents)

print(str(result))