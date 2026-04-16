import os, json, requests
from dotenv import load_dotenv
from prompt import prompt
from validator import validate
from fallback import regex_extract
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

def extract(text):
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
            },
            json={
                "model": "openai/gpt-4o-mini",
                "messages": [{"role": "user", "content": prompt(text)}]
            }
        )
        res_data = response.json()
        
        
        text_content = res_data["choices"][0]["message"]["content"]
        
        data=json.loads(text_content)
        errors=validate(data)
    except Exception as e:
        print("ERROR:", e)
        data,errors=None,["Failed"]

    if data is None or len(errors) > 3:
        data=regex_extract(text)
        errors.append("Fallback to rule based")

    elif len(errors) > 0 and len(errors) <= 3:
        fallbackData=regex_extract(text)
        for k in data:
            if data[k] is None:
                data[k]=fallbackData[k]

    return {"data": data,"errors":errors}


text = """Booking created for flight AI-302 from DEL to FRA on 12 Jan.
3 pieces, total weight approx 68 kg.
Agent: Rohan (ID: AG9932)"""

print(extract(text))