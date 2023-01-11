from tkinter import *
from PIL import ImageTk,Image
import random

root = Tk()
root.title("dice")


dice_img = ImageTk.PhotoImage(Image.open("/ui/rolling-dice-cup.png"))
d1_img = ImageTk.PhotoImage(Image.open("/Users/ozan/Desktop/learning python/ui/dice-six-faces-one.png"))
d2_img = ImageTk.PhotoImage(Image.open("/Users/ozan/Desktop/learning python/ui/dice-six-faces-two.png"))
d3_img = ImageTk.PhotoImage(Image.open("/Users/ozan/Desktop/learning python/ui/dice-six-faces-three.png"))
d4_img = ImageTk.PhotoImage(Image.open("/Users/ozan/Desktop/learning python/ui/dice-six-faces-four.png"))
d5_img = ImageTk.PhotoImage(Image.open("/Users/ozan/Desktop/learning python/ui/dice-six-faces-five.png"))
d6_img = ImageTk.PhotoImage(Image.open("/Users/ozan/Desktop/learning python/ui/dice-six-faces-six.png"))
 
dice_list = [d1_img, d2_img, d3_img, d4_img, d5_img, d6_img]


my_label = Label(image=dice_img)
my_label.grid(row=0, column=0, columnspan=2)
count = 1
def button_play():
    global my_label
    global count
    
    r = random.randrange(0,5)
    my_label.grid_forget()
    my_label = Label(image=dice_list[ r ])
    my_label.grid(row=0, column=0, columnspan=2)
    play_text = Label(root, text="%d. play is  %d" %(count, r+1 ))
    text_row= count+1
    if count//5==0 :
        trow= text_row
        tcol= 0
    elif (count+1)//5 ==1 :
        trow= text_row-4
        tcol=1
    
    play_text.grid(row=trow, column=tcol)
    

    count += 1
    

button_quit = Button(root, text="Exit program", command=root.quit)
button_play = Button(root, text="Play", command=button_play)





button_quit.grid(row=1,column=1)
button_play.grid(row=1,column=0)

root.mainloop()