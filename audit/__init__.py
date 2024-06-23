import os
from dotenv import load_dotenv
# import numpy as np
# import pandas as pd

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

# https://github.com/NielsRogge/Transformers-Tutorials/blob/master/Mistral/Supervised_fine_tuning_(SFT)_of_an_LLM_using_Hugging_Face_tooling.ipynb
DEFAULT_CHAT_TEMPLATE = "{% for message in messages %}\n{% if message['role'] == 'user' %}\n{{ '<|user|>\n' + message['content'] + eos_token }}\n{% elif message['role'] == 'system' %}\n{{ '<|system|>\n' + message['content'] + eos_token }}\n{% elif message['role'] == 'assistant' %}\n{{ '<|assistant|>\n'  + message['content'] + eos_token }}\n{% endif %}\n{% if loop.last and add_generation_prompt %}\n{{ '<|assistant|>' }}\n{% endif %}\n{% endfor %}"

SYSTEM_PROMPT = "You are an expert cybersecurity analyst. You are making a security audit of the code of a new application. Write a one phrase concise report on the security vulnerabilities you found in the code. If there aren't any, write 'No security vulnerabilities found.'"

CLONE_PATH = None