import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from jnius import autoclass


Locale = autoclass('java.util.Locale')
PythonActivity = autoclass('org.kivy.android.PythonActivity')
TextToSpeech = autoclass('android.speech.tts.TextToSpeech')

tts = TextToSpeech(PythonActivity.mActivity, None)

class Text2SpeechDemo(BoxLayout):
    def do_read(self):
        try:
            tts.speak(self.ids.notification_text.text, TextToSpeech.QUEUE_FLUSH, None)
        except NotImplementedError:
            popup = ErrorPopup()
            popup.open()


class Text2SpeechDemoApp(App):
    def build(self):
        tts.setLanguage(Locale.US)
        return Text2SpeechDemo()

    def on_pause(self):
        return True


class ErrorPopup(Popup):
    pass

if __name__ == '__main__':
    Text2SpeechDemoApp().run()