#ProgressBar
#Homework: Invesitate about how to interact with the ProgressBar

import customtkinter as ct

app = ct.CTk()
app.geometry("400x400")

progressbar = ct.CTkProgressBar(app, orientation="horizontal")
progressbar.pack(padx=10,pady=10)


app.mainloop()