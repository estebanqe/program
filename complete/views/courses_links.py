import reflex as rx
from complete.routes import Route
from complete.Componentes.link_button import Link_button
from complete.Componentes.title import title
from complete.estilo.estilo import Size as Size
import complete.constants as const

def courses_links() -> rx.Component:
    return rx.vstack(
        title("Creyente"),
        Link_button(
            "pagina Creyente",
            "Nueva descripcion de la pagina Creyente ",
            "/icons/linkedin.svg",
            const.Creyente
        ),
        
        width="100%",
        spacing=Size.DEFAULT.value,
    )   