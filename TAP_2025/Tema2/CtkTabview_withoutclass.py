#Example without using classes:

import customtkinter as ct

app = ct.CTk()
tabview = ct.CTkTabview(master=app)
tabview.pack(padx=20, pady=20)

#We add with a method .add the tables´ names.

tabview.add("tab 1")  # add tab at the end
tabview.add("tab 2")  # add tab at the end
tabview.set("tab 2")  # set currently visible tab

#Normal deploy without variables , we use on master = tabview.tab(<Name_Tab>)

button2 = ct.CTkButton(master=tabview.tab("tab 1"))
button2.pack(padx=20, pady=20)

#It's also possible to save tabs in extra variables:

tab_1 = tabview.add("tab 1")
tab_2 = tabview.add("tab 2")

#Deployment with variables, we use on master = <name_variable>
button = ct.CTkButton(tab_1)

app.mainloop()