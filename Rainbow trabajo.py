import flet as ft

def main(page: ft.Page):

    def colorChange(e):
        r = int(red_slider.value)
        b = int(blue_slider.value)
        g = int(green_slider.value)
        
        page.bgcolor = f"#{r:02x}{g:02x}{b:02x}"
        
        red_slider.label = str(r)
        blue_slider.label = str(b)
        green_slider.label = str(g)
        


    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    red_slider = ft.Slider(label="0", 
                           value=0, 
                           min=0, 
                           max=250, 
                           divisions=255, 
                           on_change=colorChange)
    blue_slider = ft.Slider(label="0", 
                            value=0, 
                            min=0, 
                            max=250, 
                            divisions=255, 
                            on_change=colorChange)
    green_slider = ft.Slider(label="0", 
                             value=0, 
                             min=0, 
                             max=250, 
                             divisions=255, 
                             on_change=colorChange)
    page.add(red_slider,
             blue_slider,
             green_slider)

ft.app(target=main)