import tkinter as tk
from tkinter import ttk

class View(tk.Tk):

    PAD = 10

    def __init__(self, controller):
        self.controller = controller
        super().__init__()
        self.title("Weather App")

        city = tk.StringVar()
        self.output_var = tk.StringVar()

        frame1 = ttk.Frame(self)
        label1 = ttk.Label(frame1, text = "City: ")
        entry1 = ttk.Entry(frame1, textvariable = city, justify = 'center')
        label1.pack(side = 'left')
        entry1.pack(side = 'left')
        frame1.pack(padx = self.PAD, pady = self.PAD)

        display_weather_button = ttk.Button(self, text = "Display Weather", 
                                            command = lambda: self.controller._button_func(city.get()))
        display_weather_button.pack(pady = self.PAD)

        self.output_label = ttk.Label(self, textvariable = self.output_var)
        self.output_label.pack()


    def _display_weather_data(self, weather_data):
        for item in weather_data.items():
            label = ttk.Label(self, text = f"{item[0]}: {item[1]}")
            label.pack(pady = self.PAD)

    def main(self):
        self.mainloop()
