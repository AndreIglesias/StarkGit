from transformers import MistralForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline
from sentence_transformers import SentenceTransformer, util
import torch
from audit import (
    HF_TOKEN,
    DEFAULT_CHAT_TEMPLATE,
    SYSTEM_PROMPT,
)

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

# SentenceTransformer model
encoder_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# -----------------------------------------------------------------------------------------------


def add_report(
    report: str,
    filename: str,
    has_vulnerability: bool,
    REPORTS: dict,
    VULNERABILITIES: dict,
) -> None:
    """
    Add the report to the REPORTS dictionary, with the filename as the key and the report as the value.

    Args:
    - report (str): The report to add.
    - filename (str): The filename of the file that was analyzed.
    - has_vulnerability (bool): Whether the report contains a security vulnerability or not.
    """
    print(f"Adding report for {filename}...")
    if has_vulnerability:
        print("Security vulnerability found! 🚨")
        REPORTS[filename] = report
        VULNERABILITIES["found"] += 1
    else:
        print("No security vulnerabilities found. ✅")
        REPORTS[filename] = "No security vulnerabilities found."
        VULNERABILITIES["not_found"] += 1
    print(
        f"{VULNERABILITIES["not_found"]} files analyzed, {VULNERABILITIES["found"]} vulnerabilities found."
    )


def heighest_similarity_score(embeddings, phrases):
    phrases_embeddings = encoder_model.encode(phrases, convert_to_tensor=True)
    similarity_scores = util.pytorch_cos_sim(embeddings, phrases_embeddings)
    return max(similarity_scores[0]).item()


def has_vulnerability(report: str) -> bool:
    report_embedding = encoder_model.encode(report.lower(), convert_to_tensor=True)

    no_vulnerability_phrases = [
        "no executable code or known vulnerabilities",
        "there are no obvious security vulnerabilities found",
        "no vulnerabilities detected",
        "no security vulnerabilities found",
        "It doesn't contain any direct security vulnerabilities",
    ]
    heighest_no_vulnerability = heighest_similarity_score(
        report_embedding, no_vulnerability_phrases
    )

    vulnerability_phrases = [
        "security vulnerability found",
        "security vulnerabilities found",
        "security risk detected",
        "security risk identified",
    ]
    heighest_vulnerability = heighest_similarity_score(
        report_embedding, vulnerability_phrases
    )

    print(
        f"Vulnerability: {heighest_vulnerability} > No-Vulnerability: {heighest_no_vulnerability} is",
        heighest_vulnerability > heighest_no_vulnerability,
    )

    return heighest_vulnerability > heighest_no_vulnerability


def analyze_code(
    code: str, file: str, REPORTS: dict, VULNERABILITIES: dict
) -> tuple[dict, dict]:
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": f"Please analyze the code for security vulnerabilities.\nFILE:{file}\nCODE:\n{code}",
        },
    ]

    response = pipe(
        messages,
        max_new_tokens=7000,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
    )
    report = response[0]["generated_text"][-1]["content"]

    found_vulnerability = has_vulnerability(report)
    add_report(report, file, found_vulnerability, REPORTS, VULNERABILITIES)
    return REPORTS, VULNERABILITIES


# https://huggingface.co/docs/transformers/main/chat_templating
