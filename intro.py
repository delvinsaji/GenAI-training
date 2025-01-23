from openai import AzureOpenAI
import os
import dotenv

dotenv.load_dotenv()

client = AzureOpenAI(
    azure_endpoint= os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key= os.environ["AZURE_OPENAI_API_KEY"],
    api_version = '2024-10-01-preview'
)

deployment = os.environ['AZURE_OPENAI_DEPLOYMENT']

prompt = "Complete the following: Once upon a time there was a "
messages = [{"role":"user","content": prompt},
            {"role":"system","content":"you are Nelson Mandela"}]

completion = client.chat.completions.create(model = deployment,
                                            messages = messages)

print(completion.choices[0].message.content)
