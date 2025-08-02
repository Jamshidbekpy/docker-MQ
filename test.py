from typing import Callable

# Funksiya tipi: string oladi, hech narsa qaytarmaydi
def my_callback(message: str) -> None:
    print(f"Xabar: {message}")

def do_something(cb: Callable[[str], None]):
    cb("Salom!")

do_something(my_callback)
