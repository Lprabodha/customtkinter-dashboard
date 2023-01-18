import tkinter
import customtkinter
import home

from PIL import Image


class Login(customtkinter.CTk):

    APP_NAME = "Custom Dashboard"
    WIDTH = 800
    HEIGHT = 500

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

      
        self.title(Login.APP_NAME)
        self.geometry(str(Login.WIDTH) + "x" + str(Login.HEIGHT))
        self.minsize(Login.WIDTH, Login.HEIGHT)
        self.maxsize(Login.WIDTH, Login.HEIGHT)
        self.resizable(False, False)
             
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)


        # creating login frame
        frame = customtkinter.CTkFrame(
            master=self, width=320, height=360, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        lable_1 = customtkinter.CTkLabel(
            master=frame, text="Log into your Account", font=('Century Gothic', 20))
        lable_1.place(x=50, y=45)

        user_name_entry = customtkinter.CTkEntry(
            master=frame, width=220, placeholder_text='Username')
        user_name_entry.place(x=50, y=110)

        password_entry = customtkinter.CTkEntry(
            master=frame, width=220, placeholder_text='Password', show="*")
        password_entry.place(x=50, y=165)

        label2 = customtkinter.CTkLabel(
            master=frame, text="Forget password?", font=('Century Gothic', 12))
        label2.place(x=155, y=195)

        # Create login button
        login_button = customtkinter.CTkButton(
            master=frame, width=220, text="Login", command=self.create_login, corner_radius=6)
        login_button.place(x=50, y=240)

    def create_login(self):
        Login.destroy(self)
        home.Dashboard()
        
      
        
    def on_closing(self, event=0):
        self.destroy()
        


