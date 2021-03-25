from numpy import *
#laboratorio 1#
#recordar subir a github cada tanto#
n_cards= int( input ("¿How many cards do you want?: "))
p_cards=[]
for i in range (n_cards):
    p_cards.append(n_cards)
    p_cards.append(n_cards)
    n_cards-=1
random.shuffle(p_cards) 
pj1=0
pj2=0
points=[pj1,pj2]
print("Player 1 is your turn to play")
p_cards_1=[]
p_cards_2=[]
i=0

while len(p_cards)!=0:
    p_cards_1.append(p_cards[i])
    p_cards.remove(p_cards[i])
    p_cards_2.append(p_cards[i])
    p_cards.remove(p_cards[i])
board_1=[]
board_2=[]
i="*"
while board_1==board_2:
    print(points,"points")
    while len(board_1)!=len(p_cards_1):
        board_1.append(i)
        board_2.append(i)
        
    print (board_1)
    print (board_2)
    coordinate_1_x=int(input("choose your first card coordinate x "))
    while len(board_1)<=coordinate_1_x:
        print("your x coordinate doesn´t exists")
        coordinate_1_x=int(input("choose your first card coordinate x "))
    coordinate_1_y=int(input("choose your first card coordinate y "))
    while 2<=coordinate_1_y:
        print("your y coordinate doesn´t exists, remember that y can only be 0 or 1")
        coordinate_1_y=int(input("choose your first card coordinate y "))
    lista=[]
    lista.append(coordinate_1_x)
    lista.append(coordinate_1_y)
    print(lista, "this is the coordinate that you choose")
    if coordinate_1_y==0:
        board_1[coordinate_1_x]=p_cards_1[coordinate_1_x]
    else:
        board_2[coordinate_1_y]=p_cards_2[coordinate_1_y]
    coordinate_2_x=int(input("choose your second card coordinate x "))
    while len(board_1)<=coordinate_2_x:
        print("your x coordinate doesn´t exists")
        coordinate_1_x=int(input("choose your second card coordinate x "))
    coordinate_2_y=int(input("choose your second card coordinate y "))
    while 2<=coordinate_2_y:
        print("your y coordinate doesn´t exists, remember that y can only be 0 or 1")
        coordinate_2_y=int(input("choose your second card coordinate y "))
    lista=[]
    lista.append(coordinate_2_x)
    lista.append(coordinate_2_y)
    print(lista, "this is the coordinate that you choose")
    if coordinate_2_y==0:
        board_1[coordinate_2_x]=p_cards_1[coordinate_2_x]
    else:
        board_2[coordinate_2_y]=p_cards_2[coordinate_2_y]
    print(board_1)
    print(board_2)