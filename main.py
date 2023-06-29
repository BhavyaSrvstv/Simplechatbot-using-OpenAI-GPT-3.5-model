import openai
import gradio
from api_sec import API_KEY

openai.api_key=API_KEY

messages=[{"role":"system","content":"You are a tech expert specialising in python"}]

def CustomChatGPT(user_input):
    messages.append({"role":"user","content":user_input})
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply=response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant","content":"ChatGPT_reply"})
    return ChatGPT_reply

demo=gradio.Interface(fn=CustomChatGPT,inputs="text",outputs="text",title="Python Assistant")

demo.launch(share=True)