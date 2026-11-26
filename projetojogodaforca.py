palavra = "python"
chutes_jogador = []
ganhou = False
chances = 6 

while True: 
    for letra in palavra: 
        if letra.lower in chutes_jogador: 
            print(letra, end=" ")
        else:
            print("_",end=" ")
        
    print(f"\nVocê tem {chances} chances")
    tentativa = input("Digite uma letra:\n-> ")
    
    chutes_jogador.append(tentativa.lower())
    
    if tentativa.lower() not in palavra.lower(): 
        
        chances -=1
        
    ganhou = True 
    
    for letra in palavra: 
        if letra.lower() not in chutes_jogador: 
            ganhou = False #ele ainda não ganhou
    
    if chances == 0 or ganhou: 
        break 

if ganhou:

    print(f"Parabéns, você ganhou. A palavra era: {palavra.upper()}")

else:

    print(f"Você perdeu! A palavra era: {palavra.upper()}")
    
    

        

