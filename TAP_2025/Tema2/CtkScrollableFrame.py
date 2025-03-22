import customtkinter as ct

#Simple Deploy

def ScrollableFrameSimple():
    app = ct.CTk()
    app.geometry("400x400")

    scrollable_frame = ct.CTkScrollableFrame(app, width=600, height=600)
    scrollable_frame.grid(row=0,column=0,sticky="nsew")
    app.mainloop()

ScrollableFrameSimple()

#Structured into a class:

#We create a class "MyFrame " which is a upper class of "CtkScrollableFrame"
class MyFrame(ct.CTkScrollableFrame):
    #Init the class, the atributtes is master and **kwargs
    def __init__(self, master, **kwargs):
        #we super the master and the **kwargs
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = ct.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)


#We deploy the normal class for App being the upper class of Ctk.
class App(ct.CTk):

    #We only define the init with itself.
    def __init__(self):
        super().__init__()

        #TIP ==> when we call the self. is equals to call app
        self.my_frame = MyFrame(master=self, width=300, height=200)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20)


app = App()
app.mainloop()