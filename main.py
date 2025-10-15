from openai import OpenAI
import os
from dotenv import load_dotenv
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def chat_bot():
    return render_template('chat_bot.html')

load_dotenv()


api_key=os.getenv('OPENAI_API_KEY')

client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)



def chat(prompt):
    response=client.chat.completions.create(
        model='openai/gpt-4.1',
        messages=[{"role":"user","content":prompt}]

    )
    
    return response.choices[0].message.content

if __name__=="__main__":
    app.run(debug=True)
    while True:
        user_input=input("You: ")
        if user_input.lower() in ['quit','exit', 'bye']:
            print('see you soon !!')
            break
        
        response=chat(user_input)
        print('Chatbot: ',response)