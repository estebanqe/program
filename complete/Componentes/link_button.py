import reflex as rx
import complete.estilo.estilo as style
from complete.estilo.estilo import Size,EmSize

def Link_button(title: str, 
                 body: str, 
                 image: str, 
                 url: str,
                 is_external=True,) -> rx.Component:
    return rx.link(
        rx.button(
             rx.hstack(
                rx.image(
                     src=image,
                     width=EmSize.LARGE.value,                           #ancho del icono
                     height=EmSize.LARGE.value,                      #alto del icono
                     margin=EmSize.MEDIUM.value,                              #margen del icono
                     alt=title,
                ), 
                rx.vstack(
                        rx.text(
                             title,
                             size=Size.SMALL.value,
                             style=style.button_title_style
                         ),
                        rx.text(
                             body,
                             size=Size.VERY_SMALL.value,
                             style=style.button_body_style
                         ),
                         align_items="start",
                         spacing=Size.VERY_SMALL.value,                #espacio entre el titulo y descripcion del boton
                         padding_y=EmSize.SMALL.value,
                         padding_right=EmSize.SMALL.value
                ),
                aling="center",
                width="100%"
             ),         
        ),
        href= url,
        is_external=is_external,
        width="100%"   
    )