from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# model = ChatGoogleGenerativeAI()

# this will not work because langchain work differently for ChatPromptTemplate
# 
# chat_template = ChatPromptTemplate([
#     SystemMessage(content='you are a helpful {domain} expert'),
#     HumanMessage(content="Explain in simple terms. what is {topic}")
# ])

chat_template = ChatPromptTemplate([('system','you are a helpful {domain} expert'),('human','Explain in simple terms. what is {topic}')])

prompt = chat_template.invoke({'domain':'software','topic':'langchain'})

print(prompt)
