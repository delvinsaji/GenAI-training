import os
import json
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

client = AzureOpenAI(
api_key=os.environ['AZURE_OPENAI_API_KEY'],  # this is also the default, it can be omitted
api_version = "2024-10-01-preview"
)

deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']

student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."

prompt1 = f'''
Please extract the following information from the given text and return it as a JSON object:

name
major
school
grades
club

This is the body of text to extract the information from:
{student_1_description}
'''

prompt2 = f'''
Please extract the following information from the given text and return it as a JSON object:

name
major
school
grades
club

This is the body of text to extract the information from:
{student_2_description}
'''

# response from prompt one
openai_response1 = client.chat.completions.create(
model=deployment,
messages = [{'role': 'user', 'content': prompt1}]
)
openai_response1.choices[0].message.content

# response from prompt two
openai_response2 = client.chat.completions.create(
model=deployment,
messages = [{'role': 'user', 'content': prompt2}]
)
openai_response2.choices[0].message.content

# Loading the response as a JSON object
json_response1 = json.loads(openai_response1.choices[0].message.content)
json_response2 = json.loads(openai_response2.choices[0].message.content)

print(json_response1)
print(json_response2)
