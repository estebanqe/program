import reflex as rx
import complete.utils as utils
import complete.estilo.estilo as styles
from complete.routes import Route
from complete.Componentes.navbar import navbar
from complete.Componentes.footer import footer
from complete.views.header import header
from complete.views.courses_links import courses_links
from complete.views.sponsors import sponsors
from complete.estilo.estilo import Size, EmSize


@rx.page(
    route=Route.COURSES.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta
)
def courses() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(details=False),
                courses_links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=EmSize.BIG.value,
                padding=EmSize.BIG.value
            )
        ),
        footer()
    )