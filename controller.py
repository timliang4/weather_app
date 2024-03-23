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
        if isinstance(weather_data, str):
            self.view._print_message(weather_data)
        else:
            self.view._display_weather_data(weather_data)

if __name__ == '__main__':
    controller = Controller()
    controller.main()
