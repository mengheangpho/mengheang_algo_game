#  IMPORTS
import tkinter as tk
import random
import winsound

#  CONSTANTS  -------------------------------------------------------------------------------------------------------------- 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
SCREEN_TITLE = "PNC Data structure to graphism"
FILE_NAMES=["array1","array2","array3","array4"]
def getRandomGrid() :  
    fileName="Game-mengheang/file_array/"+random.choice(FILE_NAMES)+".txt"
    file = open(fileName,"r")
    print(fileName)
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
count_key=0
finished_game=""
count_protect=0
endgame=False

# FUNCTIONS -------------------------------------------------------------------------------------------------------------- 
# Show score  ---
def show_score():
    global countpoint,endgame,count_key,finished_game,count_protect
    if not endgame:
        canvas.create_text(150,650,fill="#566D7E",font=("Black",16),text="score: "+str(countpoint)+"  points",tags = 'all')
        canvas.create_text(480,650,fill="#566D7E",font=("Black",15),text="Key: "+str(count_key),tags = 'all')
        if count_protect>0:
            canvas.create_text(335,650,fill="#566D7E",font=("Black",15),text="Protect: Check! ",tags = 'all')
        else:
            canvas.create_text(335,650,fill="#566D7E",font=("Black",15),text="Protect: None! ",tags = 'all')
    else:
        if finished_game=="win":
            winsound.PlaySound("Game-mengheang\\sound\\upgrade3.wav",winsound.SND_FILENAME)
            canvas.create_text(300,350,fill="#566D7E",font=("Black",16),text="score: "+str(countpoint)+"  points",tags = 'all')
            canvas.create_image(200,150, image=win, anchor='nw',tags = 'all') 
        else:
            winsound.PlaySound("Game-mengheang\\sound\\gameover3.wav",winsound.SND_FILENAME)
            canvas.create_text(300,350,fill="#566D7E",font=("Black",16),text="score: "+str(countpoint)+"  points",tags = 'all')
            canvas.create_image(200,240, image=lost, anchor='nw',tags = 'all') 

def collectcoin():
    winsound.PlaySound("Game-mengheang\\sound\\coin3.wav",winsound.SND_FILENAME)
def collectsilvercoin():
    winsound.PlaySound("Game-mengheang\\sound\\coin2.wav",winsound.SND_FILENAME)
def countkey():
    winsound.PlaySound("Game-mengheang\\sound\\coin4.wav",winsound.SND_FILENAME)
def countprotect():
    winsound.PlaySound("Game-mengheang\\sound\\secret4.wav",winsound.SND_FILENAME)
def meetenemy():
    winsound.PlaySound("Game-mengheang\\sound\\hit3.wav",winsound.SND_FILENAME)

# Press Enter ---
def enter(event):
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
    Derection()
    if not endgame:
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
                    canvas.create_rectangle(x1,y1,x2,y2,fill='#F7E7CE',outline="#F7E7CE",tags = 'all')
                
                elif array[arr][i]=="#":
                    canvas.create_image(x1,y1, image=walls, anchor='nw',tags = 'all')           
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
                elif array[arr][i]=="D":
                    canvas.create_rectangle(x1,y1,x2,y2,fill='#F7E7CE',outline="#F7E7CE",tags = 'all')
                    canvas.create_image(x1,y1, image=Door, anchor='nw',tags = 'all')
                elif array[arr][i]=="P":
                    canvas.create_rectangle(x1,y1,x2,y2,fill='#F7E7CE',outline="#F7E7CE",tags = 'all')
                    canvas.create_image(x1,y1, image=Protect, anchor='nw',tags = 'all')
                elif array[arr][i]=="E":
                    canvas.create_rectangle(x1,y1,x2,y2,fill='#F7E7CE',outline="#F7E7CE",tags = 'all')
                    canvas.create_image(x1,y1, image=enemy, anchor='nw',tags = 'all')

# move Derection --------------------------------------------------------------------------------------------------------------
# right ---
def Right (event):
    global array,countpoint,count_key,endgame,finished_game,count_protect
    if not endgame:
        playerPosition = getplayerPosition()
        playerRow = playerPosition[0]
        playerColumn = playerPosition[1]
        if array[playerRow][playerColumn+1]=="@" and count_key<=0:
            array[playerRow][playerColumn]="0"
            array[playerRow][playerColumn+1]="@"
        elif array[playerRow][playerColumn+1]=="D" and count_key<=0:
            array[playerRow][playerColumn]="0"
            array[playerRow][playerColumn+1]="D"
        elif playerColumn!= len(array[playerRow])-1 and array[playerRow][playerColumn+1]!="#" and array[playerRow][playerColumn+1]!="*" :
            array[playerRow][playerColumn]="1"
            if array[playerRow][playerColumn+1]=="$":
                countpoint+=10
                collectcoin()
            elif array[playerRow][playerColumn+1]=="s":
                countpoint+=5
                collectsilvercoin()
            elif array[playerRow][playerColumn+1]=="!":
                count_key+=1
                countkey()
            elif array[playerRow][playerColumn+1]=="P":
                count_protect+=1
                countprotect()
            elif array[playerRow][playerColumn+1]=="@" and count_key>=1:
                countpoint+=50
                collectcoin()
            elif array[playerRow][playerColumn+1]=="E" and count_protect>0:
                meetenemy()
                count_protect-=1
                array[playerRow][playerColumn+1]="0"
            elif array[playerRow][playerColumn+1]=="%":
                endgame=True
                finished_game="win"
                end_game()
            elif array[playerRow][playerColumn+1]=="E" and count_protect<=0:
                endgame=True
                finished_game="lost"
                end_game()
            if not endgame :
                array[playerRow][playerColumn+1]="0"
        #  clear all ---
        canvas.delete('all') 
        arrayToDrawing()
        show_score()   

# Left ---
def Left (event) :
    global array ,countpoint,count_key,endgame,finished_game,count_protect
    if not endgame:
        playerPosition = getplayerPosition()
        playerRow = playerPosition[0]
        playerColumn = playerPosition[1]
        if array[playerRow][playerColumn-1]=="@" and count_key<=0:
            array[playerRow][playerColumn]=="0"
            array[playerRow][playerColumn-1]=="@"
        elif array[playerRow][playerColumn-1]=="D" and count_key<=0:
            array[playerRow][playerColumn]="0"
            array[playerRow][playerColumn-1]="D"
        elif playerColumn!=0 and array[playerRow][playerColumn-1]!="#" and array[playerRow][playerColumn-1]!="*" :
            array[playerRow][playerColumn]="1"
            if array[playerRow][playerColumn-1]=="$":
                countpoint+=10
                collectcoin()
            elif array[playerRow][playerColumn-1]=="s":
                countpoint+=5
                collectsilvercoin()
            elif array[playerRow][playerColumn-1]=="!":
                count_key+=1
                countkey()
            elif array[playerRow][playerColumn-1]=="P":
                count_protect+=1
                countprotect()
            elif array[playerRow][playerColumn-1]=="@" and count_key>=1:
                countpoint+=50
                collectcoin()
            elif array[playerRow][playerColumn-1]=="E" and count_protect>0:
                meetenemy()
                count_protect-=1
                array[playerRow][playerColumn-1]="0"
            elif array[playerRow][playerColumn-1]=="%":
                endgame=True
                finished_game="win"
                end_game()
            elif array[playerRow][playerColumn-1]=="E" and count_protect<=0:
                endgame=True
                finished_game="lost"
                end_game()
            if not endgame:
                array[playerRow][playerColumn-1]="0"
        #  clear all ---
        canvas.delete('all') 
        arrayToDrawing()
        show_score()

# Up ---
def Up(event):
    global array ,countpoint,count_key,endgame,finished_game,count_protect
    if not endgame:
        playerPosition = getplayerPosition()
        playerRow = playerPosition[0]
        playerColumn = playerPosition[1]
        if array[playerRow-1][playerColumn]=="@" and count_key<=0:
            array[playerRow-1][playerColumn]=="@"
            array[playerRow][playerColumn]=="0"
        elif array[playerRow-1][playerColumn]=="D" and count_key<=0:
            array[playerRow][playerColumn]="0"
            array[playerRow-1][playerColumn]="D"
        elif playerRow!=0 and array[playerRow-1][playerColumn]!="#" and array[playerRow-1][playerColumn]!="*":
            array[playerRow][playerColumn]="1"
            if array[playerRow-1][playerColumn]=="$":
                countpoint+=10
                collectcoin()
            if array[playerRow-1][playerColumn]=="s":
                countpoint+=5
                collectsilvercoin()
            elif array[playerRow-1][playerColumn]=="!":
                count_key+=1
                countkey()
            elif array[playerRow-1][playerColumn]=="P":
                count_protect+=1
                countprotect()
            elif array[playerRow-1][playerColumn]=="@" and count_key>=1:
                countpoint+=50
                collectcoin()
            elif array[playerRow-1][playerColumn]=="E" and count_protect>0:
                meetenemy()
                count_protect-=1
                array[playerRow-1][playerColumn]="0"
            elif array[playerRow-1][playerColumn]=="%":
                endgame=True
                finished_game="win"
                end_game()
            elif array[playerRow-1][playerColumn]=="E" and count_protect<=0:
                endgame=True
                finished_game="lost"
                end_game()
            if not endgame:
                array[playerRow-1][playerColumn]="0"
        #  clear all ---
        canvas.delete('all') 
        arrayToDrawing()
        show_score()

# Down ---
def Down(event):
    global array ,countpoint,count_key,endgame,finished_game,count_protect
    if not endgame:
        playerPosition = getplayerPosition()
        playerRow = playerPosition[0]
        playerColumn = playerPosition[1]
        if array[playerRow+1][playerColumn]=="@" and count_key<=0:
            array[playerRow+1][playerColumn]=="@"
            array[playerRow][playerColumn]=="0"
        elif array[playerRow+1][playerColumn]=="D" and count_key<=0:
            array[playerRow][playerColumn]="0"
            array[playerRow+1][playerColumn]="D"
        elif playerRow!=len(array)-1 and array[playerRow+1][playerColumn]!="#" and array[playerRow+1][playerColumn]!="*":        
            array[playerRow][playerColumn]="1"
            if array[playerRow+1][playerColumn]=="$":
                countpoint+=10
                collectcoin()
            elif array[playerRow+1][playerColumn]=="s":
                countpoint+=5
                collectsilvercoin()
            elif array[playerRow+1][playerColumn]=="!":
                count_key+=1
                countkey()
            elif array[playerRow+1][playerColumn]=="P":
                count_protect+=1
                countprotect()
            elif array[playerRow+1][playerColumn]=="@" and count_key>=1:
                countpoint+=50
                collectcoin()
            elif array[playerRow+1][playerColumn]=="E" and count_protect>0:
                meetenemy()
                count_protect-=1
                array[playerRow+1][playerColumn]="0"
            elif array[playerRow+1][playerColumn]=="%":
                endgame=True
                finished_game="win"
                end_game()
            elif array[playerRow+1][playerColumn]=="E" and count_protect<=0:
                endgame=True
                finished_game="lost"
                end_game()
            if not endgame:
                array[playerRow+1][playerColumn]="0"
        #  clear all ---
        canvas.delete('all') 
        arrayToDrawing()
        show_score()

# end_game --------------------------------------------------------------------------------------------------------

def end_game():
    global array,endgame
    # Clear the array ---
    array.clear()
    # Draw again ---
    arrayToDrawing()

# MAIN CODE ----------------------------------------------------------------------------------------------------------------

root =tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))

# picture ---

wall = tk.PhotoImage(file="Game-mengheang\\picture\\wall.png")
walls = tk.PhotoImage(file="Game-mengheang\\picture\\walls.png")
player = tk.PhotoImage(file="Game-mengheang\\picture\\player.png")
coin = tk.PhotoImage(file="Game-mengheang\\picture\\coin.png")
coinSilver = tk.PhotoImage(file="Game-mengheang\\picture\\coinSilver.png")
flag = tk.PhotoImage(file="Game-mengheang\\picture\\flag.png")
treasure = tk.PhotoImage(file="Game-mengheang\\picture\\treasure.png")
Key = tk.PhotoImage(file="Game-mengheang\\picture\\key.png")
Door = tk.PhotoImage(file="Game-mengheang\\picture\\Door.png")
enemy = tk.PhotoImage(file="Game-mengheang\\picture\\enemy.png")
Protect = tk.PhotoImage(file="Game-mengheang\\picture\\security.png")
win = tk.PhotoImage(file="Game-mengheang\\picture\\youwin.png")
lost = tk.PhotoImage(file="Game-mengheang\\picture\\youlost.png")
pressEnter = tk.PhotoImage(file="Game-mengheang\\picture\\pressenter.png")
canvas = tk.Canvas(root)

# Derection -----------------------------------------------------------------------------------------------------------------------
def Derection():
    root.bind("<Right>",Right)
    root.bind("<Left>",Left)
    root.bind("<Up>",Up)
    root.bind("<Down>",Down)
root.bind("<Return>",enter)
root.resizable(False,False)
root['bg']="black"
# Start Game ----------------------------------------------------------------------------------------------------------------------

# canvas.create_text(300,350,fill="#566D7E",font=("Purisa",20),text="Press Enter for Start the game!!") 
canvas.create_image(150,300, image=pressEnter, anchor='nw',tags = 'all')
canvas.pack(expand=True, fill="both")
canvas.configure(bg="#FDDDE6")
# Display all ---------------------------------------------------------------------------------------------------------------------
root.mainloop()