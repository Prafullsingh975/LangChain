from langchain_core.prompts import PromptTemplate
from pathlib import Path

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

# __file__ is the path to the current script (e.g., 'my_project/main.py')
# .parent gives you the directory containing the file
# .resolve() makes the path absolute and resolves any symlinks
current_dir = Path(__file__).parent.resolve()

# Save template
template.save(f"{current_dir}/template1.json")