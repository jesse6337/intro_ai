import customtkinter as ct
import call_stacck
import constants
class GUI:
    def __init__(self):
        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("dark-blue")

        root = ct.CTk()
        root.geometry("500x500")
        def run_local():
            call_stacck.main_localize()
        def run_path():
            pass
        def update_readings(read):
            constants.add_readings(read)
        def update_moves(move):
            constants.add_moves(move)
        frame = ct.CTkFrame(master = root)
        frame.pack(pady = 20, padx = 60, fill = "both", expand = True)



        #entry  = ct.CTkEntry(master = frame, placeholder_text= "enter something:")
        #entry.pack(pady = 12, padx =10)

        label = ct.CTkLabel(master = frame,text= str(constants.readings))
        label.pack(pady = 12, padx = 10)
        # varible type error
        #button3 = ct.CTkButton(master = frame, text = "sense red", command= update_readings("r"))
        #button3.pack(pady = 12, padx =10)

       # button4 = ct.CTkButton(master = frame, text = "sense green", command= update_readings("g"))
        #button4.pack(pady = 12, padx =10)

        #button5 = ct.CTkButton(master = frame, text = "move up", command= update_moves([0,-1]))
        #button5.pack(pady = 12, padx =10)

        #button5 = ct.CTkButton(master = frame, text = "move down", command= update_moves([0,1]))
        #button5.pack(pady = 12, padx =10)

        #button6 = ct.CTkButton(master = frame, text = "move left", command= update_moves([-1,0]))
        #button6.pack(pady = 12, padx =10)

        #button7 = ct.CTkButton(master = frame, text = "move right", command= update_moves([1,0]))
        #button7.pack(pady = 12, padx =10)

        button1 = ct.CTkButton(master = frame, text = "start localization", command= run_local)
        button1.pack(pady = 12, padx =100)

        #button2 = ct.CTkButton(master = frame, text = "start pathPlanning", command= run_path)
        #button2.pack(pady = 12, padx =10)

        root.mainloop()
