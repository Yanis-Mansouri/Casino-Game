from random import randint

cash=100

while cash>0:
    rnb= random.randint(0,49)
    mise=int(input("mise: "))
    numberchoose=int(input("nombre:" ))
    if rnb==numberchoose:
        cash =cash +mise*3
        print(f"tu fait du cash x 3 sur la mise {mise} ce qui te fait {cash}$")
    elif (rnb % 2 == 0)and(numberchoose%2== 0):
        cash += mise*0.5
        print("paire donc rendu de 50")
        
    elif (rnb % 2 == 1)and(numberchoose%2== 1):
        cash += mise*0.5
        print("impaire donc rendu de 50")
         
    else:
        cash -= mise
        print("yoo loose")
