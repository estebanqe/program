import reflex as rx
import complete.utils as utils
import complete.estilo.estilo as styles
from complete.Componentes.navbar import navbar
from complete.Componentes.footer import footer
from complete.views.header import header
#from complete.views.index_links import index_links
from complete.views.index_links import index_links
from complete.views.sponsors import sponsors
from complete.estilo.estilo import Size,EmSize


@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        
        rx.center(
            rx.vstack(
                
                header(),
                index_links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=EmSize.BIG.value,
                padding=EmSize.BIG.value,
                
            )
        ),
        footer(),
        
    )