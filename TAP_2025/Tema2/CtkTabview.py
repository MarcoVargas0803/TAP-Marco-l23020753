#The CTkTabview creates a tabview, similar to a notebook in tkinter. The tabs,
# which are created with .add("<tab-name>") are CTkFrames and can be used like CTkFrames.
# Any widgets can be placed on them.

import customtkinter as ct

#We create a class which is the upper of the class CtkTabview
class MyTabView(ct.CTkTabview):

    #Define the init, passing the master and the **kwargs
    def __init__(self, master, **kwargs):

        #Super the init
        super().__init__(master, **kwargs)

        # create tabs
        self.add("tab 1")
        self.add("tab 2")

        # add widgets on tabs
        self.label = ct.CTkLabel(master=self.tab("tab 1"))
        self.label.grid(row=0, column=0, padx=20, pady=10)

#We create a class for the App Main which is the upper class of Ctk
class App(ct.CTk):

    #Deploy the init and super it.
    def __init__(self):
        super().__init__()

        #We create the TabView with the class "MyTabView", passing the master attribute which is the same object.
        self.tab_view = MyTabView(master=self)
        #Grid it.
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)


app = App()
app.mainloop()