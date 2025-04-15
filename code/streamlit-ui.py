import requests
import json
import gradio as gr

url = 'http://localhost:11434/api/generate'
llm_model = 'deepseek-r1:7b'  # mistral:7b, mistral:latest, llama2

convo_history = []

def api_response(custom_prompt):
    convo_history.append(custom_prompt)
    full_prompt = "\n".join(convo_history)
    data = {'model': llm_model,
            'prompt': full_prompt,
            'stream': False
            }
    result = requests.post(url, data=json.dumps(data))
    data = json.loads(result.text)
    convo_history.append(data['response'])
    return data['response']


ui = gr.Interface(
    fn=api_response,
    inputs=["text"],
    outputs=["text"],)


ui.launch()