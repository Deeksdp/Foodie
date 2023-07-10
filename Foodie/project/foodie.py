import typer
from peewee import *
from model import create_tables
from services.authentication import UserSession,AuthenticationService
from commands import user, restaurant ,cart,food,order


app = typer.Typer()

user_session = user.user_session
auth = user.auth

app.add_typer(user.app, name="user")
app.add_typer(restaurant.app, name ="restaurant")
app.add_typer(food.app, name="food")
app.add_typer(cart.app, name="cart")
app.add_typer(order.app, name="order")



if __name__ == "__main__":
    create_tables()
    with user_session:
        auth.load_session()
        app()