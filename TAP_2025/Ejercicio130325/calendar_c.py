import tkinter as tk
from tkcalendar import DateEntry

root = tk.Tk()

# Crear DateEntry
date_entry = DateEntry(root, width=12, font=("Helvetica", 12), background="lightblue", foreground="black", date_pattern="yyyy-mm-dd")
date_entry.pack(padx=20, pady=20)

root.mainloop()
