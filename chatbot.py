from kivymd.app import MDApp 
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

Window.size = (350, 550)

class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "poppins"
    font_size = 17

class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "poppins"
    font_size = 17

class ChatBotApp(MDApp):
    
    def change_screen(self, name): 
        screen_manager.current = name
    
    def build(self):
        global screen_manager 
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("Main.kv"))
        screen_manager.add_widget(Builder.load_file("Chats.kv"))
        return screen_manager
    
    def bot_name(self): 
        if screen_manager.get_screen('main').bot_name.text != "":
            screen_manager.get_screen('chats').bot_name.text = screen_manager.get_screen('main').bot_name.text
            screen_manager.current = "chats"
    
    def response(self,value, *args):
        response = self.chatbot.get_response(value).text
        screen_manager.get_screen('chats').chat_list.add_widget(Response(text=response, size_hint_x=.75))
        
    def initialize_chatbot(self):
        # self.chatbot = ChatBot('MyChatBot')
        # trainer = ListTrainer(self.chatbot)
        # with open('training_data.txt') as f:
        #     conversations = f.readlines()
        # trainer.train(conversations)
        self.chatbot = ChatBot('MyChatBot')

        trainer = ChatterBotCorpusTrainer(self.chatbot)
        trainer.train('chatterbot.corpus.english')

    def on_start(self):
        self.initialize_chatbot()

        

    
    def send(self):
        global size, halign, value
        if screen_manager.get_screen('chats').text_input != "":
            value = screen_manager.get_screen('chats').text_input.text
            if len(value) < 6: 
                size= .22
                halign = "center"
            elif len(value) < 11: 
                size= .32
                halign = "center"
            elif len(value) < 16: 
                size= .45
                halign = "center"
            elif len(value) < 21: 
                size= .58
                halign = "center"
            elif len(value) < 26: 
                size= .71
                halign = "center"
            else: 
                size= .77
                halign = "left"
                
            screen_manager.get_screen('chats').chat_list.add_widget(Command(text=value, size_hint_x=size, halign=halign))
            # Clock.schedule_once(self.response, 2)
            Clock.schedule_once(lambda dt: self.response(value), 2)
            #self.response()
            screen_manager.get_screen('chats').text_input.text = ""
    
    
if __name__ == '__main__':
    LabelBase.register(name= "poppins", fn_regular="Poppins-Regular.ttf" )
    ChatBotApp().run()