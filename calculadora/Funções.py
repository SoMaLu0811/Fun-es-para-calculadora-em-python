def add(n1,n2,s): #adição
    n1 = float(input("Digite um número:"))
    s +=n1
    n2 = float(input("Digite outro número:"))
    s+=n2
    return  print(f"A soma dos números é: {s}") 
    
def multi(n1,n2,r):
    n1 = float(input("Digite um número:"))
    n2 = float(input("Digite um número:"))
    r = n1*n2
    print("O resultado da multiplicação é: {r}")
    return r 
    
           
def gerasim(diz, fra,res): #Fração geratriz simples
    diz = float(input('Digite a dizima períodica:'))
    fra = diz*10
    res = fra-diz
    print(f"A fração geratriz desta dizima é: {res}/9")
    return res

def raiz(r,c, res): #Raiz enésima
    n = float(input("Digite um número:"))
    r = float(input("Digite a raiz que deseja calcular deste (Ex: Raiz décima(10)):"))
    res = n**(1/r)
    print(f'A raiz {r} deste número é:')
    return res  

def parimp(n): #Verificação de par ou impar de um número
    n = int(input("Digite um número:"))
    if n%2 == 0:
        print("Este número é par")
    else: 
        print("Este número é impar")
        