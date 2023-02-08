import customtkinter as ct
import main
class GUI:
    def __init__(self):
        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("dark-blue")

        root = ct.CTk()
        root.geometry("500x500")
        def run_local():
            main.main_localize()
        def run_path():
            pass

        frame = ct.CTkFrame(master = root)
        frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

        #label = ct.CTkLabel(master = frame,text= "HI there!", text_font = ("Times New Roman", 24))
        #label.pack(pady = 12, padx = 10)

       # entry  = ct.CTkEntry(master = frame, placeholder_text= "enter something:")
       # entry.pack(pady = 12, padx =10)

        button1 = ct.CTkButton(master = frame, text = "start localization", command= run_local)
        button1.pack(pady = 12, padx =100)

        button2 = ct.CTkButton(master = frame, text = "start pathPlanning", command= run_path())
        button2.pack(pady = 12, padx =10)

        root.mainloop()
GUI()