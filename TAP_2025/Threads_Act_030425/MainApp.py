
from customtkinter import CTkFrame, CTkProgressBar, CTkLabel, CTkCanvas, CTkImage, CTkButton
from CT_program_implements import AbstractMainApp
import customtkinter as ct
import tkinter as tk
import CT_program_implements as cti
from PIL import Image, ImageTk
from random import randint
import threading
from threading import Thread, Condition


class RaceApp(ct.CTk, cti.AbstractMainApp.AbstractMainAppClass):
    def __init__(self):
        super().__init__()

        self.title("Carreras")
        self.geometry("850x450")
        self.resizable(False, False)
        ct.set_appearance_mode("default")  # default

        #Configure the grid of MainApp
        self.grid_columnconfigure(index=0,weight=1)
        self.grid_rowconfigure(index=(0,1,2,3,4),weight=1)

        self.x_pos1 = 50
        self.x_pos2 = 50
        self.x_pos3 = 50

        self.configure_grid_main()
        self.frame_main_creation()
        self.create_image()
        self.progress_bar_creation()
        self.bind_creation()
        self.mainloop()




    #Create multiples frames to contain the canvas
    def configure_grid_main(self):
        self.frame_racer1 = CTkFrame(self)
        self.frame_racer2 = CTkFrame(self)
        self.frame_racer3 = CTkFrame(self)
        self.frame_label_start = CTkFrame(self)

        #Grid the frames
        self.frame_racer1.grid(column=0,row=1)
        self.frame_racer2.grid(column=0,row=2)
        self.frame_racer3.grid(column=0,row=3)
        self.frame_label_start.grid(column=0,row=4)


    def frame_main_creation(self):
        #Create the label_title
        self.title_label = CTkLabel(self,text="Carreras!",font=("Arial",50))
        #Grid the title_label
        self.title_label.grid(column=0,row=0)
        #Create the canvas
        self.canvaRacer1 = tk.Canvas(self.frame_racer1,width=900,height=100)
        self.canvaRacer2 = tk.Canvas(self.frame_racer2,width=900,height=100)
        self.canvaRacer3 = tk.Canvas(self.frame_racer3,width=900,height=100)
        #Grid the canvas
        self.canvaRacer1.pack()
        self.canvaRacer2.pack()
        self.canvaRacer3.pack()

        #Create the label button
        self.label_start = CTkLabel(self.frame_label_start,text="Start Race!")
        self.label_start.grid(column=0,row=4)
        # Botón para iniciar la animación
        start_button = CTkButton(self, text="Iniciar Animación", command=lambda: self.start_loading())
        start_button.grid(column=0, row=4, padx=10, pady=10)


    def create_image(self):
        # Loading the image to the objects in the canvas

        self.img_racer1 = Image.open("imagen1.png")  # Reemplaza con tu imagen
        self.img_racer1 = self.img_racer1.resize((50, 50))  # Ajustar tamaño si es necesario
        self.img_racer1 = ImageTk.PhotoImage(self.img_racer1)

        self.img_racer2 = Image.open("imagen2.png")  # Reemplaza con tu imagen
        self.img_racer2 = self.img_racer2.resize((50, 50))  # Ajustar tamaño si es necesario
        self.img_racer2 = ImageTk.PhotoImage(self.img_racer2)

        self.img_racer3 = Image.open("imagen3.png")  # Reemplaza con tu imagen
        self.img_racer3 = self.img_racer3.resize((50, 50))  # Ajustar tamaño si es necesario
        self.img_racer3 = ImageTk.PhotoImage(self.img_racer3)

    def progress_bar_creation(self):
        # Agregar la imagen al canvas en el punto A
        self.image1_canva = self.canvaRacer1.create_image(50,50, anchor=tk.CENTER,
                                                     image=self.img_racer1) # Imagen1
        self.image2_canva = self.canvaRacer2.create_image(50, 100, anchor=tk.CENTER,
                                                     image=self.img_racer2) # Imagen2
        self.image3_canva = self.canvaRacer3.create_image(50, 100, anchor=tk.CENTER,
                                                     image=self.img_racer3) # Imagen3

        #Definir variables principales x

        pass
    def start_loading(self):
        self.x_pos1 = 50
        self.x_pos2 = 50
        self.x_pos3 = 50

        # Iniciar hilos por corredor
        threading.Thread(target=self.run_racer, args=(self.canvaRacer1, self.image1_canva, 5, 1)).start()
        threading.Thread(target=self.run_racer, args=(self.canvaRacer2, self.image2_canva, 4, 2)).start()
        threading.Thread(target=self.run_racer, args=(self.canvaRacer3, self.image3_canva, 6, 3)).start()

        #RandomInt numers into 0 to 10
        self.speed_racer1 = randint(1, 5)
        self.speed_racer2 = randint(1, 5)
        self.speed_racer3 = randint(1, 5)

        #print the speed of the racers
        print(f"Speed of racer 1: {self.speed_racer1}")
        print(f"Speed of racer 2: {self.speed_racer2}")
        print(f"Speed of racer 3: {self.speed_racer3}")

        #Create a list of args to enumarate the racers
        args = [(self.canvaRacer1, self.image1_canva, self.speed_racer1, 1),
                (self.canvaRacer2, self.image2_canva, self.speed_racer2, 2),
                (self.canvaRacer3, self.image3_canva, self.speed_racer3, 3)]

        # Created shared condition
        for i in range(3):
            worker = Thread(target=self.run_racer, args=args[i])
            worker.start()

    def run_racer(self, canvas, image_id, speed, racer_number):
        lock = threading.Lock()
        x_pos = 50
        while x_pos < 750:
            x_pos += speed
            lock.acquire()
            self.after(0, canvas.coords, image_id, x_pos, 50)
            lock.release()
            threading.Event().wait(0.05)

            if x_pos >= 750:
                print(f"Corredor {racer_number} ha llegado!")

    def update_progress(self, value):
        pass

    def bind_creation(self):
        pass

if __name__ == '__main__':
    App = RaceApp()
    App.mainloop()