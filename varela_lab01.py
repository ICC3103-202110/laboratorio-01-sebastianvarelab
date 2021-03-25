#laboratorio 1#
#recordar subir a github cada tanto#
#solicitar número de cartas#
n_cartas= int( input ("¿cuántas cartas quieres jugar?: "))
#generar n_cartas pares de cartas con números de 1 al n_cartas#
pares_cartas=[]
while n_cartas!=1:
    pares_cartas.append(n_cartas)
    pares_cartas.append(n_cartas)
    n_cartas=-1
print(pares_cartas)

pj1=0
pj2=0
