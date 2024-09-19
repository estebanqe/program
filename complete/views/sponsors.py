import reflex as rx
import complete.constants as const
from complete.Componentes.title import title
from complete.Componentes.link_sponsor import Link_sponsor
from complete.estilo.estilo import Size as Size


def sponsors() -> rx.Component:
    return rx.vstack(
        title("Creyente & Hijos"),
          rx.flex(
               Link_sponsor(
                    "/AvatarC.png",
                    const.CARPINTERIA, 
                    "Avatar"        
               ),
               Link_sponsor(
                    "/logocrebla.png",
                    const.CARPINTERIA, 
                    "simbolo de carpinteria"        
               ),
           spacing=Size.BIG.value,
           flex_direction=["column", "row"]

          ),
       
        width="100%",
        align_items="center",
        spacing=Size.DEFAULT.value
    )