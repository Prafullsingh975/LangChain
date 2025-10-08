from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
from langchain_core.messages import HumanMessage


# create template
chat_template = ChatPromptTemplate.from_messages(
    [
    ('system','You are a helpful {domain} assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
    ])

# load history
# Make API or DB call and load the history in the variable 
chatHistory = [HumanMessage(content='Explain in simple terms. what is langchain')]

# create prompt
prompt = chat_template.invoke({'domain': 'software engineering','chat_history':chatHistory,'query':"new chat"})

print(prompt)