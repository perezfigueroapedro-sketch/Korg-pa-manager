from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class KorgApp(App):
    def build(self):
        box = BoxLayout(orientation='vertical', padding=10, spacing=15)
        box.add_widget(Label(text='KORG PA MANAGER ULTIMATE'))
        box.add_widget(Button(text='CONVERTIR KbdSet -> PERFORM'))
        box.add_widget(Button(text='STYLE CREATOR'))
        box.add_widget(Button(text='IMPORT MIDI -> STYLE'))
        box.add_widget(Button(text='EXPORT STYLE -> MIDI'))
        box.add_widget(Button(text='GUARDAR SET PA600'))
        return box
KorgApp().run()
