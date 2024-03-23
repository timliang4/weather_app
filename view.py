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

        self.data = []
        for i in range(10):
            label = ttk.Label(self, text = "")
            label.pack(pady = self.PAD)
            self.data.append(label)


    def _display_weather_data(self, weather_data):
        i = 0
        for k, v in weather_data.items():
            self.data[i].config(text = f"{k}: {v}")
            i += 1

    def _print_message(self, msg):
        self.data[0].config(text = msg)
        for i in range(9):
            self.data[i + 1].config(text = "")

    def main(self):
        self.mainloop()
