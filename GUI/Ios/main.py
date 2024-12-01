# Импорт всех классов
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window

class MyLayout(BoxLayout):
    pass


class MyApp(App):
    def build(self):
        self.title = "REWO Messenger"
        # Загрузка из файла mylayout.kv
        Builder.load_file('mylayout.kv')
        return MyLayout()

if __name__ == "__main__":
    MyApp().run()
