import torch
from huggingface_hub import login
# from transformers import pipeline
# from diffusers import DiffusionPipeline
# from datasets import load_dataset
# import soundfile as sf
from transformers import AutoTokenizer
from dotenv import load_dotenv
import os

load_dotenv(override=True)
hf_token = os.getenv("HF_API")

login(hf_token, add_to_git_credential=False)

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3.1-8B", trust_remote_code=True, use_auth_token=hf_token)

encoded = tokenizer.encode("I Lost my job")

print(encoded)