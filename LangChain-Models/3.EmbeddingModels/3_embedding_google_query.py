from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",dimensions=32)

query = "Delhi is the capital of india"
result = embedding.embed_query(query)

print(str(result))