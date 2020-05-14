from kivy.app import App
from kivy.uix.widget import Widget


class MainWidget(Widget):
    pass


class ButtonsApp(App):
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    from kivy.config import Config
    Config.set('graphics', 'width', '300')
    Config.set('graphics', 'height', '300')
    Config.set('graphics', 'dp', '30')

    from kivy.core.window import Window
    from kivy.utils import get_color_from_hex
    Window.clearcolor = get_color_from_hex('#FFFFFF')

    ButtonsApp().run()