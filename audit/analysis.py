from transformers import BertModel, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased")
model = BertModel.from_pretrained("google-bert/bert-base-uncased", torch_dtype=torch.float16, attn_implementation="sdpa")
inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")
