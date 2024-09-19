import reflex as rx
import complete.estilo.estilo as style


def title(text: str) -> rx.Component:
    return rx.heading(
       text,
       style=style.title_style
    )