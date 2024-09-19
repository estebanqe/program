import reflex as rx
import complete.estilo.estilo as style
from complete.estilo.estilo import Size, EmSize

def Link_sponsor(imagen: str, url:str, alt:str) -> rx.Component:
    return rx.link(
        rx.image(
            src=imagen,
            height="3.5em",
            aspect_ratio="5 / 3",
            alt=alt
        ),
        href=url,
        is_external=True
    )