# 问题分类
from config import OLLAMA_MODEL

def classify_issue(user_input: str):
    with open("prompts/classify.txt") as f:
        prompt = f.read().replace("{{input}}", user_input)
    return "退款异常"  # mock 结果
