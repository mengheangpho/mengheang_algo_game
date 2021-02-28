#  IMPORTS
import tkinter as tk
import random
from tkinter import messagebox

#  CONSTANTS  -------------------------------------------------------------------------------------------------------------- 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
SCREEN_TITLE = "PNC Data structure to graphism"
FILE_NAMES=["array1","array2","array3"]

def getRandomGrid() :  
    fileName="Game-mengheang/file_array/"+random.choice(FILE_NAMES)+".txt"
    file = open(fileName,"r")
    text = file.read()
    file.close()
    # import file array
    arr=[]
    result=[]
    for n in text:
        if n=="\n":
            result.append(arr)
            arr=[]
        elif n!=" ":
            arr.append(n)
    result.append(arr)  
    return result

#  VARIABLES  -------------------------------------------------------------------------------------------------------------- 
array= getRandomGrid()  # Read  grid from any file
countpoint=0
countkey=0
endgame=False

# FUNCTIONS -------------------------------------------------------------------------------------------------------------- 
# Show score  ---
def show_score():
    global countpoint,endgame
    if not endgame:
        canvas.create_text(100,630,fill="#566D7E",font=("Black",16),text="score: "+str(countpoint)+"  points",tags = 'all')
    else:
        endgame=False
        canvas.create_text(300,350,fill="#566D7E",font=("Black",16),text="score: "+str(countpoint)+"  points",tags = 'all')
        canvas.create_text(300,300,fill="#566D7E",font=("Black",20),text="You Win!",tags = 'all')      

# Press Enter ---
def enter(event):
    global endgame
    arrayToDrawing()
    show_score()

#  playerPosition ---
def getplayerPosition() :
    for row in range(len(array)):
        for column in range(len(array[row])):
            if array[row][column]=="0":
                return [row, column]
    return None # should never happen ---
 
def arrayToDrawing():
    global array
    for arr in range(len(array)):
        for i in range(len(array[arr])):
            # note -------
            # "0" = player
            # "1" = land
            # "#" = wall around
            # "*" = wall inside
            # "$" = goldcoin
            # "s" = oinSilver
            # "%" = flag
            # "@" = treasure
            # "!" = key

            x1=i*25
            y1=arr*25
            x2=x1+25
            y2=y1+25
            if array[arr][i]=="0" :
                canvas.create_image(x1,y1, image=player, anchor='nw',tags = 'all')
            elif array[arr][i]=="1" :
                canvas.create_rectangle(x1,y1,x2,y2,fill="#F7E7CE",outline='#F7E7CE',tags = 'all')
            elif array[arr][i]=="#":
                canvas.create_image(x1,y1, image=wall, anchor='nw',tags = 'all')           
            elif array[arr][i]=="*":
                canvas.create_image(x1,y1, image=walls, anchor='nw',tags = 'all')
            elif array[arr][i]=="$":
                canvas.create_rectangle(x1,y1,x2,y2,fill='#F7E7CE',outline="#F7E7CE",tags = 'all')
                canvas.create_image(x1,y1, image=coin, anchor='nw',tags = 'all')
            elif array[arr][i]=="s":
                canvas.create_rectangle(x1,y1,x2,y2,fill='#F7E7CE',outline="#F7E7CE",tags = 'all')
                canvas.create_image(x1,y1, image=coinSilver, anchor='nw',tags = 'all')
            elif array[arr][i]=="%":
                canvas.create_rectangle(x1,y1,x2,y2,fill='#F7E7CE',outline="#F7E7CE",tags = 'all')
                canvas.create_image(x1,y1, image=flag, anchor='nw',tags = 'all')
            elif array[arr][i]=="@":
                canvas.create_rectangle(x1,y1,x2,y2,fill='#F7E7CE',outline="#F7E7CE",tags = 'all')
                canvas.create_image(x1,y1, image=treasure, anchor='nw',tags = 'all')
            elif array[arr][i]=="!":
                canvas.create_rectangle(x1,y1,x2,y2,fill='#F7E7CE',outline="#F7E7CE",tags = 'all')
                canvas.create_image(x1,y1, image=Key, anchor='nw',tags = 'all')
# move Derection --------------------------------------------------------------------------------------------------------------
# right ---
def Right (event):
    global array,countpoint,countkey,endgame
    if not endgame:
        playerPosition = getplayerPosition()
        playerRow = playerPosition[0]
        playerColumn = playerPosition[1]
        if array[playerRow][playerColumn+1]=="@" and countkey<=0:
            array[playerRow][playerColumn]="0"
            array[playerRow][playerColumn+1]="@"
        elif playerColumn!= len(array[playerRow])-1 and array[playerRow][playerColumn+1]!="#" and array[playerRow][playerColumn+1]!="*" :
            array[playerRow][playerColumn]="1"
            if array[playerRow][playerColumn+1]=="$":
                countpoint+=10
            elif array[playerRow][playerColumn+1]=="s":
                countpoint+=5
            elif array[playerRow][playerColumn+1]=="!":
                countkey+=1
            elif array[playerRow][playerColumn+1]=="@" and countkey>=1:
                countpoint+=50
            elif array[playerRow][playerColumn+1]=="%":
                endgame=True
                end_game()
            if not endgame:
                array[playerRow][playerColumn+1]="0"
        #  clear all ---
        canvas.delete('all') 
        arrayToDrawing()
        show_score()   
# Left ---
def Left (event) :
    global array ,countpoint,countkey,endgame
    if not endgame:
        playerPosition = getplayerPosition()
        playerRow = playerPosition[0]
        playerColumn = playerPosition[1]
        if array[playerRow][playerColumn-1]=="@" and countkey<=0:
            array[playerRow][playerColumn]=="0"
            array[playerRow][playerColumn-1]=="@"
        elif playerColumn!=0 and array[playerRow][playerColumn-1]!="#" and array[playerRow][playerColumn-1]!="*" :
            array[playerRow][playerColumn]="1"
            if array[playerRow][playerColumn-1]=="$":
                countpoint+=10
            elif array[playerRow][playerColumn-1]=="s":
                countpoint+=5
            elif array[playerRow][playerColumn-1]=="!":
                countkey+=1
            elif array[playerRow][playerColumn-1]=="@" and countkey>=1:
                countpoint+=50
            elif array[playerRow][playerColumn-1]=="%":
                endgame=True
                end_game()
            if not endgame:
                array[playerRow][playerColumn-1]="0"
        #  clear all ---
        canvas.delete('all') 
        arrayToDrawing()
        show_score()
# Up ---
def Up(event):
    global array ,countpoint,countkey,endgame
    if not endgame:
        playerPosition = getplayerPosition()
        playerRow = playerPosition[0]
        playerColumn = playerPosition[1]
        if array[playerRow-1][playerColumn]=="@" and countkey<=0:
            array[playerRow-1][playerColumn]=="@"
            array[playerRow][playerColumn]=="0"
        elif playerRow!=0 and array[playerRow-1][playerColumn]!="#" and array[playerRow-1][playerColumn]!="*":
            array[playerRow][playerColumn]="1"
            if array[playerRow-1][playerColumn]=="$":
                countpoint+=10
            if array[playerRow-1][playerColumn]=="s":
                countpoint+=5
            elif array[playerRow-1][playerColumn]=="!":
                countkey+=1
            elif array[playerRow-1][playerColumn]=="@" and countkey>=1:
                countpoint+=50
            elif array[playerRow-1][playerColumn]=="%":
                endgame=True
                end_game()
            if not endgame:
                array[playerRow-1][playerColumn]="0"
        #  clear all ---
        canvas.delete('all') 
        arrayToDrawing()
        show_score()
# Down ---
def Down(event):
    global array ,countpoint,countkey,endgame
    if not endgame:
        playerPosition = getplayerPosition()
        playerRow = playerPosition[0]
        playerColumn = playerPosition[1]
        if array[playerRow+1][playerColumn]=="@" and countkey<=0:
            array[playerRow+1][playerColumn]=="@"
            array[playerRow][playerColumn]=="0"
        elif playerRow!=len(array)-1 and array[playerRow+1][playerColumn]!="#" and array[playerRow+1][playerColumn]!="*":        
            array[playerRow][playerColumn]="1"
            if array[playerRow+1][playerColumn]=="$":
                countpoint+=10
            elif array[playerRow+1][playerColumn]=="s":
                countpoint+=5
            elif array[playerRow+1][playerColumn]=="!":
                countkey+=1
            elif array[playerRow+1][playerColumn]=="@" and countkey>=1:
                countpoint+=50
            elif array[playerRow+1][playerColumn]=="%":
                endgame=True
                end_game()
            if not endgame:
                array[playerRow+1][playerColumn]="0"
        #  clear all ---
        canvas.delete('all') 
        arrayToDrawing()
        show_score()

# end_game --------------------------------------------------------------------------------------------------------
def end_game():
    global array
    # Clear the array ---
    array = []
    # Draw again ---
    arrayToDrawing()

# MAIN CODE ----------------------------------------------------------------------------------------------------------------
root =tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))

# picture ---
wall = tk.PhotoImage(file="Game-mengheang\\picture\\wall .png")
walls = tk.PhotoImage(file="Game-mengheang\\picture\\walls.png")
player = tk.PhotoImage(file="Game-mengheang\\picture\\player.png")
coin = tk.PhotoImage(file="Game-mengheang\\picture\\coin.png")
coinSilver = tk.PhotoImage(file="Game-mengheang\\picture\\coinSilver.png")
flag = tk.PhotoImage(file="Game-mengheang\\picture\\flag.png")
treasure = tk.PhotoImage(file="Game-mengheang\\picture\\treasure.png")
Key = tk.PhotoImage(file="Game-mengheang\\picture\\key.png")
canvas = tk.Canvas(root)
# Derection -----------------------------------------------------------------------------------------------------------------------
root.bind("<Right>",Right)
root.bind("<Left>",Left)
root.bind("<Up>",Up)
root.bind("<Down>",Down)
root.bind("<Return>",enter)

# Start Game ----------------------------------------------------------------------------------------------------------------------
canvas.create_text(300,350,fill="#566D7E",font=("Purisa",20),text="Press Enter for Start the game!!")
canvas.pack(expand=True, fill="both")

# Display all ---------------------------------------------------------------------------------------------------------------------
root.mainloop()