def verificador_idade (idade):    
    if idade >= 18:
        print("Você é maior de idade!") 
    else:
        print("Você é menor de idade!")
idade=int(input("Qual é a sua idade? "))
verificador_idade(idade)