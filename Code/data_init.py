from db_handler import database_handler as dbh
from db_handler import create_base
from password_handler import hash_password
from models import users, posts
from sqlalchemy.orm import Session


# Initialising the database
db = dbh("networking.db")
create_base()


def dummy_insert_user():
    unames = ["alice123", "bob123"]
    emails = ["alice@example.com", "bob@example.com"]
    passwords = ["alice123", "bob123"]
    for uname, password, email in zip(unames, passwords, emails):  # Zip function is used to iterate the data
        new_user = users(username=uname, password=hash_password(password), email=email)
        db.session.add(new_user)
    db.session.commit()


def dummy_insert_post():
    titles = ["First Post", "Second Post"]
    contents = ["What is the basis of Physics?", "Who is the father of the Physics?"]
    user_ids = [2, 3]
    times = [1683100545.492104, 1683100565.254593]
    for title, content, user_id, time in zip(titles, contents, user_ids, times):
        new_post = posts(title=title, content=content, user_id=user_id, likes=0, datetime=time)
        db.session.add(new_post)
    db.session.commit()


dummy_insert_user()
dummy_insert_post()
