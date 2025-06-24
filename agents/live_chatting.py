from dotenv import load_dotenv
from openai import OpenAI
import os, sys;

load_dotenv(override=True)

#Making Sure our api key is loaded and ready
api_key = os.getenv("OPENAI_API_KEY")
if api_key and (len(api_key) >10):
    print("API LOOKS GOOD")

else:
    sys.exit(0)

openai = OpenAI() #instantiationg an instance of openai


system_prompt = input("Enter a System Prompt: \n")
user_prompt = input("Enter a User prompt: \n")

# system_prompt = "You are a funny assistant"
# user_prompt = "Tell me a joke"

prompts = [{"role":"system", "content":system_prompt},{"role":"user","content":user_prompt}]

stream = openai.chat.completions.create(
    model = "gpt-4o-mini",
    messages = prompts,
    temperature = 0.7,
    stream = True
)

for chunk in stream:

    content =  chunk.choices[0].delta.content

    if content:

        print(content, end="", flush=True)

