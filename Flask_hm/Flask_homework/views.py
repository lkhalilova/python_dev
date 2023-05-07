import os
from datetime import date
import datetime
from Flask_homework import app, db
from flask import request, render_template, make_response, session, redirect, url_for
import json
import werkzeug.exceptions
import random
from .models import User, Book, Purchase

app.secret_key = os.getenv("SECRET_KEY")


@app.route("/hello")
def hello_world():
    app.logger.info("hello_world is called")
    return "<h1 style='color: red'>Hello, world!</h1>"


@app.route("/users/<int:user_id>")
def user_id_handler(user_id):
    if session.get("username"):
        user = User.query.get(user_id)
        if user:
            return render_template("users_id.html", user=user)
        else:
            return "User not found", 404
    else:
        return redirect(url_for("login"))


@app.route("/books/<int:book_id>")
def book_id_handler(book_id):
    if session.get("username"):
        book = Book.query.get(book_id)
        if book:
            return render_template("books_id.html", book=book)
        else:
            return "Book not found", 404
    else:
        return redirect(url_for("login"))



@app.route("/books/<string:book_title>")
def title_handler(book_title):
    if session.get("username"):
        context = {"book": book_title.title()}
        return f"Hello,{session.get('username')}" + render_template("books_id.html", **context)
    else:
        return redirect(url_for("login"))


@app.route("/params")
def html_params():
    if session.get("username"):
        return f"Hello,{session.get('username')}" + render_template("params.html", attributes=request.args)
    else:
        return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        if len(str(request.form.get("username"))) >= 5 and len(str(request.form.get("password"))) >= 8:
            val = []
            for item in request.form.get("password"):
                if item.isalnum() and item.isupper():
                    val.append(item)
                    break
            for item in request.form.get("password"):
                if item.isdigit():
                    val.append(item)
                    break
            if len(val) >= 2:
                username = request.form.get("username")
                password = request.form.get("password")
                session["username"] = username
                session["password"] = password
                context = {"username": username, "password": password}
                return render_template("session.html", **context)

        return "No data to process or password is invalid", 400


@app.errorhandler(werkzeug.exceptions.NotFound)
def handle_bad_request(e):
    return "<div>Think twice, try again</div>"


@app.errorhandler(werkzeug.exceptions.InternalServerError)
def handle_server_error(e):
    return "<div>It seems that this app is not a masterpiece at all</div>"


@app.route("/list")
def list_url():
    return ("<a href='/login'><div margin:5>Go to /login page</div></a>"
            "<a href='/users'><div margin:5>Go to /users page</div></a>"
            "<a href='/books'><div margin:5>Go to /books page</div></a>"
            "<a href='/params'><div margin:5>Go to /params page</div></a>")


@app.route("/users")
def users():
    if session.get("username"):
        if request.query_string:
            number = request.args.get('count')
            users = User.query.limit(number).all()
            return render_template("users.html", users=users)
        else:
            users = User.query.all()
            return render_template("users.html", users=users)
    else:
        return redirect(url_for("login"))


@app.route("/users", methods=["POST", ])
def create_user():
    user = User(
        first_name=request.json.get("first_name"),
        last_name=request.json.get("last_name"),
        age=request.json.get("age")
    )
    db.session.add(user)
    db.session.commit()
    return f"User {user.id} created", 201


@app.route("/books")
def books():
    if session.get("username"):
        if request.query_string:
            number = request.args.get('count')
            books = Book.query.limit(number).all()
            return render_template("books.html", books=books)
        else:
            books = Book.query.all()
            return render_template("books.html", books=books)
    else:
        return redirect(url_for("login"))


@app.route("/books", methods=["POST", ])
def create_book():
    book = Book(
        title=request.json.get("title"),
        author=request.json.get("author"),
        price=request.json.get("price")
    )
    db.session.add(book)
    db.session.commit()
    return f"Book {book.title} {book.author} added", 201


@app.route("/purchases")
def purchases():
    if session.get("username"):
        if request.query_string:
            number = request.args.get('count')
            purchases = Purchase.query.limit(number).all()
            return render_template("purchases.html", purchases=purchases)
        else:
            purchases = Purchase.query.all()
            return render_template("purchases.html", purchases=purchases)
    else:
        return redirect(url_for("login"))


@app.route("/purchases", methods=["POST", ])
def create_purchase():
    user_id_check = request.json.get("user_id")
    book_id_check = request.json.get("user_id")
    user_query = db.select(User.id)
    book_query = db.select(Book.id)
    if user_id_check in db.session.scalars(user_query) and book_id_check in db.session.scalars(book_query):
        purchase = Purchase(
            user_id=request.json.get("user_id"),
            book_id=request.json.get("book_id"),
            date=date.fromisoformat(str(request.json.get("date")))
        )
        db.session.add(purchase)
        db.session.commit()
        return f"User {purchase.user_id} made a purchase", 201
    return "Incorrect user_id or book_id", 400


@app.route("/purchases/<int:purchase_id>")
def purchase_id_handler(purchase_id):
    if session.get("username"):
        purchase = Purchase.query.get(purchase_id)
        if purchase:
            return render_template("purchases_id.html", purchase=purchase)
        else:
            return "There is no such purchase", 404
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))











