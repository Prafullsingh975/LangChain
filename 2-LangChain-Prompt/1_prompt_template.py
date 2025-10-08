from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.7)

# variables
topic = "GenAI"
style_input = "detail"
length_input = 100

# Template creation
template = PromptTemplate(template="""Please tell me about "{topic}" with following specification:
                          Explanation Style: {style_input}
                          Explanation Length: {length_input}
                          1. Detail Explanation
                          2. Summary of the explanation.
                          3. Alternatives if any.""",
                          input_variables=['topic','style_input','length_input'],
                          validate_template=True
                          )

# Filling placeholders
prompt = template.invoke({'topic':topic,'style_input':style_input,'length_input':length_input})

result = model.invoke(prompt)

print(result.content)