import tkinter as tk
import random as rand

ans = rand.randint(1,100)
score = 0
tries = 0
root = tk.Tk()
root.geometry("500x200")
root.configure(bg = "#454545")
text = tk.Label(text="enter a number between 1 and 100",foreground = "#ff00ff",bg = "#454545")
text.pack()
guess = tk.Entry(fg="black",bg="#676767",width =50)
guess.pack()
def entry(*args):
    global guess
    global ans
    global text2
    global text3
    global text4
    global tries
    global score
    str1 = guess.get()
    int1 = int(str1)
    text2.destroy()
    if int1 == ans:
        text2 = tk.Label(text="correct",foreground = "#ff00ff", bg = "#454545")
        text2.pack()
        score+=1
        ans = rand.randint(1,100)
    elif int1 > ans:
        text2 = tk.Label(text="too high",foreground = "#ff00ff", bg = "#454545")
        text2.pack()
    else:
        text2 = tk.Label(text="too low",foreground = "#ff00ff", bg = "#454545")
        text2.pack()
    text3.destroy()
    text3 = tk.Label(text = "score is " + str(score), bg = "#454545",foreground = "#ff00ff")
    text3.pack()
    tries+=1
    text4.destroy()
    text4 = tk.Label(text = "You have made " + str(tries) + " attempts!" , bg = "#454545",foreground = "#ff00ff")
    text4.pack()
guess.bind('<Return>',entry)
enter = tk.Button(text = "enter guess", command = entry, background="#676767")
text2 = tk.Label(text="enter a guess already!")
enter.pack()
text3 = tk.Label(text = "score is " + str(score), bg = "#454545",foreground = "#ff00ff")
text3.pack()
text4 = tk.Label(text = "You have made " + str(tries) + " attempts!", bg = "#454545",foreground = "#ff00ff")
text4.pack()
root.mainloop()