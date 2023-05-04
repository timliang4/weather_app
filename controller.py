from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()

    def _button_func(self, location):
        self.view.output_var.set('')
        weather_data = self.model._get_weather_data(location)
        self.view.output_var.set(weather_data)
        # for item in weather_data.items():
        #     self.view.output_var += f"{item[0]}: {item[1]}\n"
            

if __name__ == '__main__':
    controller = Controller()
    controller.main()
