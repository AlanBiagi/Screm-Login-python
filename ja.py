from flet import *
import flet as ft

class inputField(UserControl):
    def __init__(self,width):
        super()

body = Container(
    Stack([
        Image(
            src='Screan\pecas.png',
        ),
        Container(
            Column([
                Text(
                    'Nome da empresa',
                    size=32,
                    font_family='Arial',
                ),
        ],alignment=MainAxisAlignment.CENTER),
        bgcolor='red',
        width='100%',
        height=80,
        border=border.all(1,'#44f4f4f4'),
        alignment=alignment.center,
        ),
        Container(
            Container(
                    Column([
                        Text(
                            'Login',
                            color='white',
                            height='w700',
                            size=24,
                            text_align='center',
                        ),
                        # InputFilter()
                    ],alignment=MainAxisAlignment.CENTER),
                width=400,
                height=400,
                border_radius=18,
                blur=Blur(10,12,BlurTileMode.MIRROR),
                border=border.all(1,'#44f4f4f4'),
                alignment=alignment.center,
            ),
            margin=margin.only(top=150),
            alignment=alignment.center
        )
    ])
)

def main(page: Page):
    page.padding = 0
    page.window_resizable = False
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.add(body)

ft.app(target=main) 