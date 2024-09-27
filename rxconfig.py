import reflex as rx

config = rx.Config(
    app_name="complete",
    
    cors_allowed_origins=[
        "http://localhost:3000",
       "https://programcreyente.vercel.app/"
   ]
)