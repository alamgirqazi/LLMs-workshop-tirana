import requests
import json

url = 'http://localhost:11434/api/generate'

custom_prompt = 'Write me a short poem ?'
llm_model =  'gemma3:4b'  #'deepseek-r1:7b' 
data = {'model': llm_model,
        'prompt': custom_prompt,
        'stream': False
        }

result = requests.post(url, data=json.dumps(data))
if result.status_code == 404:
    print(result.text)
else:        
    result_text = result.text
    data = json.loads(result_text)
    print(data['response'])