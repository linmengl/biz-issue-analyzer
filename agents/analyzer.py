from config import OLLAMA_MODEL

def analyze_issue(user_input, info_dict):
    with open("prompts/analyze.txt") as f:
        prompt = f.read()
    full_prompt = prompt.replace("{{user_input}}", user_input)
    full_prompt = full_prompt.replace("{{logs}}", info_dict.get("logs", ""))
    full_prompt = full_prompt.replace("{{db}}", str(info_dict.get("db", {})))
    full_prompt = full_prompt.replace("{{docs}}", info_dict.get("docs", ""))
    return full_prompt  # mock 输出
