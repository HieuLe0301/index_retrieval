import requests

from .config import LLM_URL, MODEL_NAME


def chat(system_prompt, user_prompt) :
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 1000,
    }

    response = requests.post(
        LLM_URL,
        headers={"Authorization": "Bearer dummy"},
        json=payload,
        timeout=120,
    )
    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"]