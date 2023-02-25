#Importação de biblioteca principal
import openai as op


#Configuração de chave
op.api_key = "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"

while True:
    print("-"*30)
    prompt = input("Escreva algo: ")
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
    with open("text.txt", 'r', encoding='utf-8') as arq:
        


    print(f"Resposta: \t{response}.\n")
    print("-"*30)

    