import pandas as pd
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

data = pd.read_csv("C:\\OneDrive\\OneDrive - Tredence\\Attachments\\GenAI\\phone_data.csv", encoding='unicode_escape')

def embed_row(row):
    row_text = ', '.join([f"{col}: {row[col]}" for col in data.columns])  
    response = client.embeddings(
        deployment_id=deployment,
        input=row_text
    )
    embedding = response['data'][0]['embedding']  
    return embedding

data['embedding'] = data.apply(embed_row, axis=1)

output_path = "C:\\OneDrive\\OneDrive - Tredence\\Attachments\\GenAI\\embedded_phone_data.csv"
data.to_csv(output_path, index=False)

print(f"Embeddings successfully created and saved to {output_path}")
