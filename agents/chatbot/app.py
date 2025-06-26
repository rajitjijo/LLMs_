from dotenv import load_dotenv
import gradio as gr
from openai import OpenAI
import ollama
import subprocess

load_dotenv(override=True)

openai = OpenAI()
model = "gpt-4o-mini"

system_message = "You are a snarky assistant"

def chat(message, history):

    messages = [{"role":"system","content":system_message}]

    for user_msg, assistant_msg in history:

        messages.append({"role":"user","content":user_msg})
        messages.append({"role":"assistant","content":assistant_msg})

    messages.append({"role":"user","content":message})

    stream = openai.chat.completions.create(

        model=model,
        messages=messages,
        stream=True
    )

    response = ""

    for chunk in stream:

        response += chunk.choices[0].delta.content or ""
        yield response

#With OLLama

o_model = "llama3.2:latest"

# stream = ollama.chat(model=o_model, messages=[{'role': 'user', 'content': 'Can u be a assistant??'}],stream=True)

# for chunk in stream:
#   print(chunk['message']['content'], end='', flush=True)


def chat_(message, history):

    messages = []

    for user, assistant in history:

        messages.append({"role":"user","content":user})
        messages.append({"role":"assistant","content":assistant})

    messages.append({"role":"user","content":message})

    stream = ollama.chat(model=o_model, 
                         messages=messages, 
                         stream=True)
    
    response = ""
    for chunk in stream:
        response += chunk['message']['content']
        yield response


gr.ChatInterface(fn=chat_).launch()
# subprocess.run(["ollama", "serve", "--stop"])