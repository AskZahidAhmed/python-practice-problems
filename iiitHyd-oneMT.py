import requests
import json

url = "https://ssmt.iiit.ac.in/onemt"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def call_mt(text, source_language='eng', target_language='hin'):
    data = {
        'text': text,
        'source_language': source_language,
        'target_language': target_language
    }
    r = requests.post(url, headers=headers, json=data)
    response = json.loads(r.text)
    output = response.get('data', '')
    return output

if __name__ == "__main__":
    translation = call_mt('Q1. Hello, Mr. Smith. etc. How are you today?')
    print(translation)
