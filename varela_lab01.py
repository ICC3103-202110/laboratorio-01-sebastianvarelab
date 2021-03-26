from numpy import *
#laboratorio 1#
#recordar subir a github cada tanto#
n_cards= int( input ("¿How many cards do you want?: "))
n_card=n_cards
p_cards=[]
for i in range (n_cards):
    p_cards.append(n_cards)
    p_cards.append(n_cards)
    n_cards-=1
random.shuffle(p_cards) 

points=[0,0]
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
while len(board_1)!=len(p_cards_1):
            board_1.append(i)
            board_2.append(i)   
print (board_1)
print (board_2)
sum_total=points[0]+points[1]
while sum_total!=n_card: 
    print(points,"points")
    print("Player 1 is your turn to play")
    pj1="a"
    while pj1=="a":
        pj1=0
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
            board_2[coordinate_1_x]=p_cards_2[coordinate_1_y]
        coordinate_2_x=int(input("choose your second card coordinate x "))
        while len(board_1)<=coordinate_2_x:
            print("your x coordinate doesn´t exists")
            coordinate_2_x=int(input("choose your second card coordinate x "))
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
            board_2[coordinate_2_x]=p_cards_2[coordinate_2_y]
        print(board_1)
        print(board_2)
        search_p_c=[]
        help_issue=len(board_1)-1
        help_issue2=len(board_2)-1
        while help_issue!=-1:
            if board_1[help_issue]!="*":
                search_p_c.append(board_1[help_issue])
            help_issue-=1
        while help_issue2!=-1:
            if board_2[help_issue2]!="*":
                search_p_c.append(board_2[help_issue2])
            help_issue2-=1
        if search_p_c[0]==search_p_c[1]:
            pj1="a"
            points[0]+=1
            if board_1.count(search_p_c[0])==1 or board_1.count(search_p_c[0])==2 :
                board_1.remove(search_p_c[0])
            else:
                board_2.remove(search_p_c[0])
            if board_2.count(search_p_c[0])==1 or board_2.count(search_p_c[0])==2:
                board_2.remove(search_p_c[0])
            else:
                board_1.remove(search_p_c[0])
            print(points,"points")
            search_p_c=[]
        else:
            help_issue3=len(board_1)-1
            help_issue4=len(board_2)-1
            search_p_c=[]
            while help_issue3!=-1:
                if board_1[help_issue3]!="*":
                    board_1[help_issue3]="*"
                help_issue3-=1
            while help_issue4!=0:
                if board_2[help_issue4]!="*":
                    board_2[help_issue4]="*"
                help_issue4-=1
        print("player 2 is your turn to play")
        print(board_1)
        print(board_2)
    pj2="a"
    while pj2=="a":
        pj2=0
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
            board_2[coordinate_1_x]=p_cards_2[coordinate_1_y]
        coordinate_2_x=int(input("choose your second card coordinate x "))
        while len(board_1)<=coordinate_2_x:
            print("your x coordinate doesn´t exists")
            coordinate_2_x=int(input("choose your second card coordinate x "))
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
            board_2[coordinate_2_x]=p_cards_2[coordinate_2_y]
        print(board_1)
        print(board_2)
        search_p_c=[]
        help_issue=len(board_1)-1
        help_issue2=len(board_2)-1
        while help_issue!=-1:
            if board_1[help_issue]!="*":
                search_p_c.append(board_1[help_issue])
            help_issue-=1
        while help_issue2!=-1:
            if board_2[help_issue2]!="*":
                search_p_c.append(board_2[help_issue2])
            help_issue2-=1
        if search_p_c[0]==search_p_c[1]:
            pj2="a"
            points[1]+=1
            if board_1.count(search_p_c[0])==1 or board_1.count(search_p_c[0])==2:
                board_1.remove(search_p_c[0])
            else:
                board_2.remove(search_p_c[0])
            if board_2.count(search_p_c[0])==1 or board_2.count(search_p_c[0])==2:
                board_2.remove(search_p_c[0])
            else:
                board_1.remove(search_p_c[0])
            print(points,"points")
            search_p_c=[]
            print(points,"points")
        else:
            help_issue3=len(board_1)-1
            help_issue4=len(board_2)-1
            while help_issue3!=-1:
                if board_1[help_issue3]!="*":
                    board_1[help_issue3]="*"
                help_issue3-=1
            while help_issue4!=0:
                if board_2[help_issue4]!="*":
                    board_2[help_issue4]="*"
                help_issue4-=1