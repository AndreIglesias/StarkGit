from transformers import MistralForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline
import torch
from audit import HF_TOKEN, DEFAULT_CHAT_TEMPLATE, SYSTEM_PROMPT

device = "cuda"
model_name = "mistralai/Mistral-7B-Instruct-v0.2"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True
)

model = MistralForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    token=HF_TOKEN,
)
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.chat_template = DEFAULT_CHAT_TEMPLATE

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)


def analyze_code(code: str) -> str:
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": "Please analyze the code for security vulnerabilities.\nCODE:\n" + code,
        },
    ]

    response = pipe(
        messages,
        max_length=1000,
        do_sample=True,
        truncation=True,
        pad_token_id=tokenizer.eos_token_id,
    )
    return response[0]["generated_text"][-1]["content"]

# https://huggingface.co/docs/transformers/main/chat_templating
