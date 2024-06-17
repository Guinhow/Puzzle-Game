import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

images = ['images/1.jpg','images/2.jpg','images/3.jpg','images/4.jpg','images/5.jpg','images/6.jpg','images/7.jpg','images/8.jpg','images/9.jpg']

class puzzleApp(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal', padding=5, size_hint=(None, None), size=(500, 700)) 
        sideBar = BoxLayout(orientation='vertical', padding=5, size_hint=(0.15, 1), pos_hint={'right': 1})
        main_layout = BoxLayout(orientation='vertical',padding=5, size_hint=(1 , 1))
        topRow = BoxLayout(size_hint = (1,0.3))
        middleRow = BoxLayout(size_hint = (1,0.3))  
        bottomRow = BoxLayout(size_hint = (1,0.3))
        colors = [red, green, blue, purple]

        for i in range(3):
            image = random.choice(images)
            btn = Button(background_normal = image)
            btn.bind(on_press=self.imageChange)
            bottomRow.add_widget(btn)

        for i in range(3):
            image = random.choice(images)
            btn = Button(background_normal = image)
            btn.bind(on_press=self.imageChange)
            topRow.add_widget(btn)
        
        for i in range(3):
            image = random.choice(images)
            btn = Button(background_normal = image)
            btn.bind(on_press=self.imageChange)
            middleRow.add_widget(btn)       

        color = random.choice(colors)
        side_btn = Button(background_color = color)  
        side_btn.bind(on_press = self.colorChange)  
        sideBar.add_widget(side_btn)

        main_layout.add_widget(topRow)
        main_layout.add_widget(middleRow)
        main_layout.add_widget(bottomRow)

        layout.add_widget(main_layout) 
        layout.add_widget(sideBar)

        return layout
        
    
    def colorChange(self, instance):
        colors = [red, green, blue, purple]
        newColor = random.choice(colors)        
        instance.background_color = newColor
    
    def imageChange(self, instance):
        images = ['images/1.jpg','images/2.jpg','images/3.jpg','images/4.jpg','images/5.jpg','images/6.jpg','images/7.jpg','images/8.jpg','images/9.jpg']
        newImage = random.choice(images)
        instance.background_normal = newImage   


if __name__ == "__main__":
    Window.size = (500 , 700)
    app = puzzleApp()
    app.run()