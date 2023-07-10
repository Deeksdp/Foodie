from typing_extensions import Annotated
import typer
from services.cart import CartService
from services.order import OrderService
from commands import user

app = typer.Typer()
cart = CartService()
order = OrderService(cart)
auth = user.auth


@app.command()
def place():
    auth.is_authenticated()
    order.place(auth.user)


@app.command()
def display():
    auth.is_authenticated()
    order.display(auth.user)


@app.command()
def history():
    auth.is_authenticated()
    order.history(auth.user)


@app.command()
def checkout(amout: int):
    auth.is_authenticated()
    order.checkout(auth.user, amout)