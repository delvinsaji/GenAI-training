#Question answer generation(QAG) - an evaluation metric to check the factual accuracy of the model

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

prompt = "generate factual questions: 'Eiffel tower was built on 1889 and is located in Paris which is the capital of France' "

messages = [{"role":"user","content": prompt}]

completion = client.chat.completions.create(model = deployment,
                                            messages = messages)

print(completion.choices[0].message.content)


from transformers import pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")


response = "generate questions: The Eiffel Tower was built in 1889 and is located in Paris."
retrieved_chunks = [
    "The Eiffel Tower is in Paris.",
    "It was constructed in 1890 for the World's Fair."
]

questions = ["When was the Eiffel Tower built?",
"In which city is the Eiffel Tower located?","What year was the Eiffel Tower completed?"]
answers = []
for question in questions:
    for chunk in retrieved_chunks:
        answer = qa_pipeline(question=question, context=chunk)
        answers.append((question, answer['answer']))

print("Generated Questions and Answers:", answers)
