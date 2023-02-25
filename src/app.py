#Importação de biblioteca principal
import openai as op
import pyttsx3 as pt
from time import sleep
from read_text import read_text as rd

#Configuração de chave
op.api_key = "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"


while True:
    print("-"*30)
    prompt = input("Write something: ")
    print("-"*30)
    model_engine = "text-davinci-003" 
    
    conclusão = op.Completion.create( 
        engine=model_engine, 
        prompt=prompt, 
        max_tokens=1024, 
        n=1, 
        stop=None, 
        temperature=1, 
    )

    response = conclusão.choices[0].text
    rd(text=response)
    print(f"Response: \t{response}.\n")
    print("-"*30)
    sleep(10)

    