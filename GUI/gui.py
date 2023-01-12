import tkinter

root = tkinter.Tk()
label = tkinter.Label(root )
frame =  tkinter.Frame(root, padx=100, pady=100)
frame.grid()
tkinter.Label(frame, text="Hello World!").grid(column=0, row=0)
tkinter.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)
tkinter.Label(frame, text = "input").grid(column=0, row = 1)
#tkinter.Button(frame, test = "would you like to log in?" ,activebackground= tkinter.colorchooser.askcolor(color ="red") )
root.mainloop()
label.pack()
