from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.5)

chatHistory = [
    SystemMessage(content="You are a helpful assistant. And you name is chikki")
]
while True:
    user_input = input('You: ')
    if user_input == 'exit':
        break

    chatHistory.append(HumanMessage(content=user_input))

    # result = model.invoke(user_input)
    result = model.invoke(chatHistory)

    chatHistory.append(AIMessage(content=result.content))

    print("AI: ",result.content)

print(chatHistory)