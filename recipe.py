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

no_recipe = str(input("Enter the number of recipes required: "))

ingredients = []
ing = "a"
count = 1
while ing != "":
    ing = input(f"{count} - ")
    if ing != "":
        count += 1
        ingredients.append(ing)

ingredients = ", ".join(ingredients)

filters = input("Provide any additional conditions (for example: vegetarian, gluten free etc): ")

prompt = f"Provide {no_recipe} number of recipes and all of the recipes need to use only these ingredients : {ingredients}. The ingredients used in each of the recipe needs to be provided."
messages = [{"role":"user","content": prompt}]

completion = client.chat.completions.create(model = deployment,
                                            messages = messages,
                                            temperature= 0.9,
                                            max_tokens=600)

recipe_result = completion.choices[0].message.content

new_prompt = f"Provide a shopping list with quantity to buy for preparing these recipes : {recipe_result}. The shopping list should only consist of the ingredients mentioned in the recipes"
messages = [{"role":"user","content":new_prompt}]

completion = client.chat.completions.create(model = deployment,
                                            messages = messages,
                                            temperature= 0.7)

print(completion.choices[0].message.content)
