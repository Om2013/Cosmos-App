from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout 
from kivymd.uix.pickers import MDDatePicker
API_KEY = "igdhEzOZTiWrwyPwQB9k4V6mIhvkJ8EbcSnwXViS"
API_URL="https://api.nasa.gov/planetary/apod?api_key=API_KEY"

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
        return layout 
    
    def open_date_picker(self,instance):
        picker=MDDatePicker()
        picker.bind(on_save=self.on_date_selected)
        picker.open()

    def on_date_selected(self,instance,value,date_range):
        self.selected_date_label.text=f"Selected Date: {value}" 
    
    def fetch_apod(self,instance):
        URL="https://api.nasa.gov/planetary/apod?api_key=API_KEY"

        




        


if __name__ == "__main__":
    Cosmo_app().run()
    
