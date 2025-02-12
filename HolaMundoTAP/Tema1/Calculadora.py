import customtkinter as ct
from customtkinter import CTkFrame

app = ct.CTk()
app.title("Calculadora")
app.geometry("1000x500")
#app.minsize(200,200)
#app.maxsize(300,400)
app.columnconfigure(1,weight=1)
app.rowconfigure(1,weight=1)

#fondo
c1 = CTkFrame(app,fg_color="white")
c2 = CTkFrame(app,fg_color ="gray")

c1.grid(row=0,column=0,sticky="nsew")
c2.grid(row=1,column=0,sticky="nsew")

#botones numerales
n1 = CTkFrame(c2,fg_color="purple")
n2 = CTkFrame(c2,fg_color="purple")
n3 = CTkFrame(c2,fg_color="purple")
n4 = CTkFrame(c2,fg_color="purple")
n5 = CTkFrame(c2,fg_color="purple")
n6 = CTkFrame(c2,fg_color="purple")
n7 = CTkFrame(c2,fg_color="purple")
n8 = CTkFrame(c2,fg_color="purple")
n9 = CTkFrame(c2,fg_color="purple")

#botones operaciòn y resultado
op_mas = CTkFrame(c2,fg_color="yellow")
op_menos = CTkFrame(c2,fg_color="yellow")
op_multi = CTkFrame(c2,fg_color="yellow")
op_div = CTkFrame(c2,fg_color="yellow")



#Grid
c1.grid(row=0,column=0,sticky="nsew")

#Grid numeral
n1.grid(row=0,column=0,sticky="nsew",pady=8,padx=8)
n2.grid(row=0,column=1,sticky="nsew",pady=8,padx=8)
n3.grid(row=0,column=2,sticky="nsew",pady=8,padx=8)
n4.grid(row=1,column=0,sticky="nsew",pady=8,padx=8)
n5.grid(row=1,column=1,sticky="nsew",pady=8,padx=8)
n6.grid(row=1,column=2,sticky="nsew",pady=8,padx=8)
n7.grid(row=2,column=0,sticky="nsew",pady=8,padx=8)
n8.grid(row=2,column=1,sticky="nsew",pady=8,padx=8)
n9.grid(row=2,column=2,sticky="nsew",pady=8,padx=8)

op_mas.grid(row=0,column=3,sticky="nsew",pady=8,padx=8)
op_menos.grid(row=1,column=3,sticky="nsew",pady=8,padx=8)
op_multi.grid(row=0,column=4,sticky="nsew",pady=8,padx=8)
op_div.grid(row=0,column=4,sticky="nsew",pady=8,padx=8)




app.mainloop()