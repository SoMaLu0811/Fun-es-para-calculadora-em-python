from math import log10, log2, sin,cos,tan,exp
histo = set()

def add(n1,n2,s): #adição
    n1 = float(input("Digite um número:"))
    s +=n1
    n2 = float(input("Digite outro número:"))
    s+=n2
    return  print(f"A soma dos números é: {s}") 
    
def multi(n1,n2,r):#multiplicação
    n1 = float(input("Digite um número:"))
    n2 = float(input("Digite um número:"))
    r = n1*n2
    print("O resultado da multiplicação é: {r}")
    return r 
    
def div(n1,n2,r): #divisão
    n1=float(input('Digite um número:'))
    n2 = float(input('Digite outro número:'))
    r = n1/n2
    print(f"O resultado da divisão é: {r}")
    return r

def pot(n1,n2,r): #potenciação
    n1 = float(input('Digite um número:'))
    n2 = float(input('Digite outro número:'))
    r = n1**n2
    print(f"O resultado da potenciação é: {r}")
    return r

def loga10(n1,r): #logaritmo base 10
    n1 = float(input('Digite um número:'))
    r = log10(n1)
    print(f"O logaritmo na base 10 de {n1} é: {r}")
    return r

def loga2(n1,r): #logaritmo base 2
    n1 = float(input('Digite um número:'))
    r = log2(n1)
    print(f"O logaritmo na base 2 de {n1} é: {r}")
    return r

def sino(n1,r): #seno 
    n1 = float(input('Digite um número:'))
    r = sin(n1)
    print(f'O Seno de {n1} é: {r}')
    return r 

def cose(n1,r): #coseno
    n1 = float(input('Digite um número:'))
    r = cos(n1)
    print(f'O Coseno de {n1} é: {r}')
    return r

def tang(n1,r): #arquitangente
    n1 = float(input('Digite um número:'))
    r = tan(n1)
    print(f"A arquitangente de {n1} é: {r}")
    return r 

def mod(n1,sq): #módulo de um número 
    n1 = float(input('Digite um número:'))
    sq = (n1**2)**1/2
    sq**=1/2
    print(f'O módulo de {n1} é: {sq}')
    return sq

def raiz(r,c, res): #Raiz enésima
    n = float(input("Digite um número:"))
    r = float(input("Digite a raiz que deseja calcular deste (Ex: Raiz décima(10)):"))
    res = n**(1/r)
    print(f'A raiz {r} deste número é:')
    return res             

def expo(n1,r):
    n1 = float(input("Digite um número:"))
    r = exp(n1)
    print(f"O exponencial de {n1} é: {r}")
    return r 

def hist(n1,n2,s,op,r,c,sq):
    while   True:
        histo.add(n1,n2,s,op,r,c,sq) 
        op = str(input("Deseja ver o histórico da calculadora(S/N):"))
        if op == 'S':
            print(all(histo))
        else:
            break 
    
def gerasim(diz, fra,res): #Fração geratriz simples
    diz = float(input('Digite a dizima períodica:'))
    fra = diz*10
    res = fra-diz
    print(f"A fração geratriz desta dizima é: {res}/9")
    return res

