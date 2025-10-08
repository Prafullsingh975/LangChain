from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import load_prompt
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.7)

# variables
topic = "GenAI"
style_input = "detail"
length_input = 100

# load template
current_dir = Path(__file__).parent.resolve()
path = f"{current_dir}/template1.json"
template = load_prompt(path)

# Filling placeholders
prompt = template.invoke({'topic':topic,'style_input':style_input,'length_input':length_input})

result = model.invoke(prompt)

# we can replace prompt and result with this line of code
chain = template | model
result = chain.invoke({'topic':topic,'style_input':style_input,'length_input':length_input})

print(result.content)