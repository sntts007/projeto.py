from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.image import AsyncImage 
from kivy.uix.textinput import TextInput

class MinhaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=50, padding=[10,70])
        

        nome_input = TextInput(hint_text='Nome')
        email_input = TextInput(hint_text='Email')
        senha_input = TextInput(hint_text='Senha', password=True)
        
        botao1 = Button(text='login')
        botao2 = Button(text='sair')
        
        layout.add_widget(AsyncImage(source='c:/Users/aluno.sesipaulista/Downloads/WhatsApp Image 2024-05-06 at 10.16.28 (1).jpeg'))
        layout.add_widget(nome_input)
        layout.add_widget(email_input)
        layout.add_widget(senha_input)
        layout.add_widget(botao1)
        layout.add_widget(botao2)
        
        return layout
        
if __name__ == '__main__':
    MinhaApp().run()
