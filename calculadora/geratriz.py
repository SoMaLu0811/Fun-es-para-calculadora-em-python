def gerasim(diz, fra,res):
    diz = float(input('Digite a dizima períodica:'))
    fra = diz*10
    res = fra-diz
    print(f"A fração geratriz desta dizima é: {res}/9")
    return res
diz = float()
fra = float()
res = float()
gerasim(diz,fra,res)
