#Importação de biblioteca principal
import openai as op
import pyttsx3 as pt
from time import sleep
import os

def read_text(text):
    engine = pt.init() # object creation

    """ RATE"""
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', 125)     # setting up new voice rate


    """VOLUME"""
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)                   #printing current volume level
    engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[0 ].id)   #changing index, changes voices. 1 for female

    engine.say(text)
    engine.runAndWait()
    engine.stop()



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
    read_text(text=response)
    print(f"Response: \t{response}.\n")
    print("-"*30)
    sleep(10)

