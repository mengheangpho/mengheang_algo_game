#  IMPORTS
# from PIL import  Image,ImageTk
import tkinter as tk
import random
#  CONSTANTS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
SCREEN_TITLE = "PNC Data structure to graphism"

#  VARIABLES
file_array=["array1","array2","array3"]
file="file_array/"+random.choice(file_array)+".txt"
text = open(file,"r")
print(file)
listarray=text.read()
array=[]
arr=[]
condition=False
enter=True
index1=-1
index2=-1
countpoint=0
myImage=""
myImageId=""
# import file array
for n in listarray:
    if n=="\n":
        array.append(arr)
        arr=[]
    elif n!=" ":
        arr.append(n)
array.append(arr)  
#fuction 
# def Enter(event):
#     global enter
#     enter=True
#     canvas.after(1, arrayToDrawing())
def arrayToDrawing():
    global array , myImage,myImageId,enter
    if enter:
        for arr in range(len(array)):
            for i in range(len(array[arr])):
                x1=i*25
                y1=arr*25
                x2=x1+25
                y2=y1+25
                if array[arr][i]=="0" :
                    canvas.create_rectangle(x1,y1,x2,y2,fill='white',outline="white")
                    canvas.create_oval(x1,y1,x2,y2,fill='red')
                elif array[arr][i]=="1" :
                    canvas.create_rectangle(x1,y1,x2,y2,fill='white',outline="white")
                    canvas.create_oval(x1+10,y1+10,x2-10,y2-10,fill='red',outline="red")
                    # canvas.create_image(100, 10, image=image, anchor=NW)
                elif array[arr][i]=="#":
                    canvas.create_rectangle(x1,y1,x2,y2,fill='black',outline="black")              
                elif array[arr][i]=="*":
                    canvas.create_rectangle(x1,y1,x2,y2,fill='gray',outline="Gray")     
                elif array[arr][i]=="$":
                    canvas.create_oval(x1,y1,x2,y2,fill='Yellow',outline="yellow")
                    canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill='Orange',outline="Orange")
                elif array[arr][i]=="%":
                    canvas.create_rectangle(x1,y1,x2,y2,fill='green',outline="")
                    canvas.create_oval(x1+5,y1+5,x2-5,y2-5,arr*25+25,fill='Orange',outline="Orange")
def Right (event):
    global arr ,index1 ,index2,countpoint
    for arr in range(len(array)):
        for n in range(len(array[arr])):
            if array[arr][n]=="0":
                index1=arr
                index2=n
    if index2!= len(array[arr])-1 and array[index1][index2+1]!="#" and array[index1][index2+1]!="*":
        array[index1][index2]="1"
        if array[index1][index2+1]=="$":
            countpoint+=10
            print(countpoint)
        array[index1][index2+1]="0"
    arrayToDrawing()
def Left (event) :
    global arr ,index1,index2,countpoint
    for arr in range(len(array)):
        for n in range(len(array[arr])):
            if array[arr][n]=="0":
                index1=arr
                index2=n
    if index2!=0 and array[index1][index2-1]!="#" and array[index1][index2-1]!="*" :
        array[index1][index2]="1"
        if array[index1][index2-1]=="$":
            countpoint+=10
            print(countpoint)
        array[index1][index2-1]="0"
    arrayToDrawing()
def Up(event):
    global arr ,index1,index2,countpoint
    for arr in range(len(array)):
        for n in range(len(array[arr])):
            if array[arr][n]=="0":
                index1=arr
                index2=n
    if index1!=0 and array[index1-1][index2]!="#" and array[index1-1][index2]!="*":
        array[index1][index2]="1"
        if array[index1-1][index2]=="$":
            countpoint+=10
            print(countpoint)
        array[index1-1][index2]="0"
    arrayToDrawing()
def Down(event):
    global arr ,index1,index2,countpoint
    for arr in range(len(array)):
        for n in range(len(array[arr])):
            if array[arr][n]=="0":
                index1=arr
                index2=n
    if index1!=len(array)-1 and array[index1+1][index2]!="#" and array[index1+1][index2]!="*":        
        array[index1][index2]="1"
        if array[index1+1][index2]=="*":
            countpoint+=10
        array[index1+1][index2]="0"
    arrayToDrawing()

root =tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))


# image = PhotoImage(file="picture\cat.jpg")
canvas = tk.Canvas(root)
root.bind("<Right>",Right)
root.bind("<Left>",Left)
root.bind("<Up>",Up)
root.bind("<Down>",Down)

# root.bind("<Enter>",Enter)
canvas.pack(expand=True, fill="both")

arrayToDrawing()

root.mainloop()