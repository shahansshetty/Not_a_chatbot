from openai import OpenAI
import os
from dotenv import load_dotenv



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
    while True:
        user_input=input("You: ")
        if user_input.lower() in ['quit','exit', 'bye']:
            print('see you soon !!')
            break
        
        response=chat(user_input)
        print('Chatbot: ',response)