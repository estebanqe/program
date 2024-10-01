import reflex as rx
from complete.Componentes.link_icon import link_icon
from complete.Componentes.info_text import info_text
from complete.estilo.estilo import Size, EmSize
from complete.estilo.color import TextColor 
from complete.estilo.color import Color as Color
import complete.constants as const
import datetime

def experience() -> int:
    return datetime.date.today().year - 2010





def header(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Julio. César Quiña",
                size=Size.MEDIUM_BIG.value,
                src="/AvatarC.png",
                radius="full",
                color=TextColor.BODY.value,
                bg=Color.PRIMARY.value,
                padding="2px",
                border="6px",
                 border_color=Color.PRIMARY.value
                
                
            ),  
            rx.vstack(
                rx.heading(
                    "CREYENTE",
                    size=Size.BIG.value
                ),
                rx.text(
                    "J. César Q. & Hijos",
                    margin_top=EmSize.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon(
                        "/icons/instagramAzul.svg",
                        const.INSTAGRAM,
                        "email@email.com"
                    ),
                    link_icon(
                        "/icons/facebookAzul.svg",
                        const.FACEBOOK,
                        "facebook"
                    ),
                    link_icon(
                        "/icons/book-azul.svg",
                        const.CATALOGO,
                        "catalogo"
                    ),
                    link_icon(
                        "/icons/whatsappAzul.svg",
                        const.WHATSAPP,
                        "whatssap"
                    ),
                    spacing=Size.LARGE.value,
                    padding_top=EmSize.SMALL.value,

                ),
                spacing=Size.ZERO.value,
                align_items="start",
            ),
            align="end",
            width="100%",
            spacing=Size.DEFAULT.value,
            
        ),      
        rx.cond(  
            details,
            rx.vstack(
                rx.flex(
                    info_text(
                        "+4",
                        "años de mucha experiencia"
                    ),
                    rx.spacer(),                                    #crea un espacio ficticio entre texto
                    info_text(
                        "ateción","al detalle"
                    ),
                    rx.spacer(), 
                    info_text(
                        "trabajo","certificado"
                    ),
                    width="100%",
                ),
                rx.text(
                    f"""
                    Bienvenido a nuestro sitio especializado en trabajos en madera y melamina. Desde muebles a medida hasta soluciones de almacenamiento, fusionamos la tradición con la innovación para crear piezas únicas que realzan cualquier espacio. ¡Explore nuestro portafolio y dé vida a sus proyectos con nosotros!""",
                    font_size=EmSize.DEFAULT.value,
                    color=TextColor.BODY.value
                ),
                    
                spacing=Size.BIG.value,
                
            )
            
        ),  
        width="100%",
        spacing=Size.BIG.value,                     #espacion entre las 2 secciones
        align_items="start", #alinear todo al inicio
        
    )
    