from time import sleep
from customtkinter import CTkFrame, CTkProgressBar, CTkLabel, CTkCanvas, CTkImage, CTkButton
import customtkinter as ct
import tkinter as tk
from PIL import Image, ImageTk
from random import randint
import threading
import time

class RaceApp(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Carreras")
        self.geometry("850x450")
        self.resizable(False, False)
        ct.set_appearance_mode("default")  # default

        #Configure the grid of MainApp
        self.grid_columnconfigure(index=0,weight=1)
        self.grid_rowconfigure(index=(0,1,2,3,4),weight=1)

        # Crear eventos para sincronizar los hilos
        self.start_event = threading.Event()

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
        self.start_button = CTkButton(self, text="Comenzar Carrera", command=lambda: self.start_loading(),
                                       fg_color="green", hover_color="lightgreen")
        self.start_button.grid(column=0, row=4, padx=10, pady=10)


    def create_image(self):
        # Loading the image to the objects in the canvas
        self.img_racer1 = Image.open("imagen1.png")  
        self.img_racer1 = self.img_racer1.resize((100, 100))  
        self.img_racer1 = ImageTk.PhotoImage(self.img_racer1)

        self.img_racer2 = Image.open("imagen2.png")  
        self.img_racer2 = self.img_racer2.resize((100, 100))  
        self.img_racer2 = ImageTk.PhotoImage(self.img_racer2)

        self.img_racer3 = Image.open("imagen3.png")  
        self.img_racer3 = self.img_racer3.resize((100, 100))  
        self.img_racer3 = ImageTk.PhotoImage(self.img_racer3)

    def progress_bar_creation(self):
        self.image1_canva = self.canvaRacer1.create_image(50,50, anchor=tk.CENTER, image=self.img_racer1) 
        self.image2_canva = self.canvaRacer2.create_image(50, 50, anchor=tk.CENTER, image=self.img_racer2) 
        self.image3_canva = self.canvaRacer3.create_image(50, 50, anchor=tk.CENTER, image=self.img_racer3) 

    def start_loading(self):
        self.canvaRacer1.coords(self.image1_canva, 50, 50)
        self.canvaRacer2.coords(self.image2_canva, 50, 50)
        self.canvaRacer3.coords(self.image3_canva, 50, 50)

        self.x_pos1 = 50
        self.x_pos2 = 50
        self.x_pos3 = 50

        self.start_button.configure(state="disabled")  
        # RandomInt numbers into 1 to 5
        self.speed_racer1 = randint(5, 8)
        self.speed_racer2 = randint(5, 8)
        self.speed_racer3 = randint(5, 8)

        args = [(self.canvaRacer1, self.image1_canva, self.speed_racer1, 1),
                (self.canvaRacer2, self.image2_canva, self.speed_racer2, 2),
                (self.canvaRacer3, self.image3_canva, self.speed_racer3, 3)]

        worker1 = threading.Thread(target=self.run_racer, args=(self.canvaRacer1, self.image1_canva, self.speed_racer1, 1))
        worker2 = threading.Thread(target=self.run_racer, args=(self.canvaRacer2, self.image2_canva, self.speed_racer2, 2))
        worker3 = threading.Thread(target=self.run_racer, args=(self.canvaRacer3, self.image3_canva, self.speed_racer3, 3))

        worker1.start()
        worker2.start()
        worker3.start()

        # Notificar a todos los hilos que pueden comenzar
        self.start_event.set()

    def run_racer(self, canvas, image_id, speed, racer_number):
        x_pos = 50
        print(f"Corredor numero {racer_number}  listo en la parrilla")

        # Esperar a que todos los hilos estén listos
        self.start_event.wait()

        while x_pos < 750:
            x_pos += speed
            # Usar after para asegurar que las actualizaciones ocurran en el hilo principal
            self.after(0, self.update_canvas, canvas, image_id, x_pos, 50)
            sleep(0.05)  

            if x_pos >= 750:
                print(f"Corredor {racer_number} ha llegado!")
                break

        self.start_button.configure(state="normal")

    def update_canvas(self, canvas, image_id, x_pos, y_pos):
        # Actualiza las coordenadas del corredor en el canvas desde el hilo principal
        canvas.coords(image_id, x_pos, y_pos)

    def reset_canvas(self):
        self.canvaRacer2.coords(self.image2_canva, 50, 100)
        self.canvaRacer3.coords(self.image3_canva, 50, 100)

    def bind_creation(self):
        pass


if __name__ == '__main__':
    App = RaceApp()
    App.mainloop()
