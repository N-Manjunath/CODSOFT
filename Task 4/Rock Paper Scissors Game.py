import random 
import tkinter
#Create Object 
root = tkinter.Tk() 
 
#Set geometry 
root.geometry("500x500") 
 
#Set title 
root.title("Rock-Paper-Scissors Game")
#Computer Value 
computer_dict = { 
"0":"Rock", 
"1":"Paper", 
"2":"Scissors" 
}
#Reset the game 
def reset_game():
    b1["state"] = "active" 
    b2["state"] = "active" 
    b3["state"] = "active" 
    l4.config(text = "")
#Disable the button 
def button_disable():  
    b1["state"] = "disable" 
    b2["state"] = "disable" 
    b3["state"] = "disable"
#If player selects rock 
def user_rock(): 
    c_v = computer_dict[str(random.randint(0,2))] 
    if c_v == "Rock": 
        match_result ='''
        the user choice     : Rock\n
        the computer choice :Rock\n
        Its Tie '''
    elif c_v=="Scissors": 
        match_result ='''
        the user choice     : Rock\n
        the computer choice :Scissors\n
        User wins'''  
    else: 
        match_result ='''
        the user choice     : Rock\n
        the computer choice :Paper\n
        Computer wins'''  
    l4.config(text = match_result) 
    button_disable() 

#If player selects paper 
def user_paper(): 
    c_v = computer_dict[str(random.randint(0, 2))] 
    if c_v == "Paper": 
        match_result ='''
        the user choice     : Paper\n
        the computer choice :Paper\n
        Its Tie'''
    elif c_v=="Rock": 
        match_result ='''
        the user choice      : Paper\n
        the computer choice  :Rock\n
        User wins'''  
    else: 
        match_result ='''
        the user choice     : Paper\n
        the computer choice :Scissors\n
        Computer wins''' 
    l4.config(text = match_result) 
    button_disable() 

#If player selects scissors 
def user_scissors(): 
    c_v = computer_dict[str(random.randint(0,2))] 
    if c_v == "Scissors": 
        match_result ='''
        the user choice     : Scissors\n
        the computer choice :Scissors\n
        Its Tie''' 
    elif c_v == "Paper":
        match_result ='''
        the user choice      : Scissors\n
        the computer choice  :Paper\n
        User wins'''  
        
    else:   
        match_result ='''
        the user choice     : Scissors\n
        the computer choice :Rock\n
        Computer wins''' 
    l4.config(text = match_result) 
    button_disable()

#Add Labels, Frames and Button 
tkinter.Label(root, 
    text = 'Choose any one: Rock, Paper, Scissors', 
    font = "Consolas", 
    fg = "black").pack(pady = 20)  


frame1 = tkinter.Frame(root) 
frame1.pack() 

l1 = tkinter.Label(frame1, 
    text = "User", 
    font=30)
l1.pack()
frame2 = tkinter.Frame(root) 
frame2.pack() 
b1 = tkinter.Button(frame2, text = "Rock", 
            font = 8, width = 7, bg = "light blue", 
            
            command = user_rock) 

b2 = tkinter.Button(frame2, text = "Paper ", 
            font = 8, width = 7, bg = "light blue", 
            command = user_paper) 

b3 = tkinter.Button(frame2, text = "Scissors", 
            font = 8, width = 7, bg = "light blue", 
            command = user_scissors) 

b1.pack(side = 'left', padx = 10) 
b2.pack(side = 'left', padx = 10) 
b3.pack(padx = 10) 
frame3=tkinter.Frame(root)
frame3.pack()
l2 = tkinter.Label(frame3, 
    text = "VS", 
    font =30) 
l2.pack()
frame4=tkinter.Frame(root)
frame4.pack()

l3 = tkinter.Label(frame4, text = "Computer", font = 10) 
l3.pack() 

l4 = tkinter.Label(root, 
        text = "",
        font=50,  
        bg = "white", 
        fg='green',
        width = 50 , 
        height=10,
        borderwidth = 2, 
        relief ='raised') 
l4.pack(pady = 20) 



tkinter.Button(root, text = "Reset Game", 
        font = 10, fg = "red", 
        bg = "black", command = reset_game).pack(pady = 20) 

#Execute Tkinter 
root.mainloop()
