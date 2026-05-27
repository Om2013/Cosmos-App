from kivy.core.window import Window 
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout 
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.card import MDCard
from kivy.uix.image import AsyncImage
from kivymd.uix.scrollview import MDScrollView
import requests 

API_KEY = "igdhEzOZTiWrwyPwQB9k4V6mIhvkJ8EbcSnwXViS"
API_URL="https://api.nasa.gov/planetary/apod?api_key=API_KEY"
Window.size=(1000,1000)

class Cosmo_app(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Orange"
        layout=BoxLayout(orientation="vertical",padding=10,spacing=10)
        title_label=MDLabel(text="NASA APOD - Astronomy Picture of the Day",
                            font_style="H5",
                            halign="center",
                            theme_text_color="Custom",
                            text_color=(1,0.6,0.2,1))

        choose_date_button=MDRaisedButton(text="Choose the Date")
        choose_date_button.bind(on_release=self.open_date_picker)
        self.selected_date_label=MDLabel(text="Selected Date:",
                                    font_style="H6",
                                    theme_text_color="Custom",
                                    text_color=(1,0.6,0.2,1),
                                    )
        

        layout.add_widget(title_label)
        layout.add_widget(choose_date_button)
        layout.add_widget(self.selected_date_label)

        self.card=MDCard(orientation="vertical",padding=20,spacing=20,size_hint=(None,None),height=60)
        self.image_label=MDLabel(text="",
                                 font_style="H6",
                                 markup=True)
        
        self.image_date_label=MDLabel(text="",
                                      font_style="Caption")
        
        self.image=AsyncImage(width=700,height=450,size_hint=(None,None),pos_hint={"centerx":0.5},allow_stretch=True)
        
       
        self.scrollview=MDScrollView(height=120,size_hint=(1,None))
        self.description_box=BoxLayout(orientation="vertical",padding=10,spacing=10,size_hint_y=None)
        self.description_box.bind(minimum_height=self.description_box.setter("height"))
        self.description_label=MDLabel(text="Description:",
                                       font_style="Subtitle1",
                                       markup=True,
                                       text_color=(1,0,5,1),
                                       size_hint_y=None,
                                       height=30,
                                       halign="left"
                                       )
        self.description_text_label=MDLabel(text="",
                                            font_style="H5",
                                            markup=True,
                                            text_size=(Window.width-60,None),
                                            halign="left")
        
        self.description_text_label.bind(texture_size=self.update_label_height)
        
        # CARD 
        self.card.add_widget(self.image_label)
        self.card.add_widget(self.image_date_label)
        self.card.add_widget(self.image)

        # DESCRIPTION BOX 
        self.description_box.add_widget(self.description_label)
        self.description_box.add_widget(self.description_text_label)
        
        # SCROLLVIEW
        self.scrollview.add_widget(self.description_box)
        
        # LAYOUT
        layout.add_widget(self.card)
        layout.add_widget(self.scrollview)

        return layout 
    
    def update_label_height(self,instance,value): 
        instance.height=value[1]
        
    def open_date_picker(self,instance):
        picker=MDDatePicker()
        picker.bind(on_save=self.on_date_selected)
        picker.open()

    def on_date_selected(self,instance,value,datarange):
        #self.selected_date_label.text=f"Selected Date: {value}" 
        self.fetch_apod(str(value))
    
    def fetch_apod(self,date):

        URL="https://api.nasa.gov/planetary/apod"
        params={"api_key":API_KEY,"date":date}
        response=requests.get(URL,params=params)
        if response.status_code==200:
            data=response.json()
            print(data)
            self.image_url=data.get("url","")
            self.description_text_label.text=data.get("explanation","")
            self.image_label.text = data.get("title","")
            self.image_date_label.text=data.get("date","")
            self.image_hdurl=data.get("hdurl",self.image_url)
            self.image.source=self.image_url

            

if __name__ == "__main__":
    Cosmo_app().run()
    
65