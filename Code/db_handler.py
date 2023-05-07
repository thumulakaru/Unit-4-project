import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import users,posts,Base
import datetime


def create_base():
    engine = create_engine('sqlite:///networking.db')
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    my_session = session()
    print(Base.metadata.tables.keys())
    print(engine.connect())
    return None


class database_handler:
    def __init__(self, dbname):
        self.session = None
        engine = create_engine(f"sqlite:///{dbname}")
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close(self):
        self.session.close()

    def insert_user(self, email, username, password):
        if not self.session.query(users).filter_by(email=email).first():
            new_user = users(email=email, username=username, password=password)
            self.session.add(new_user)
            self.session.commit()
            print("User registered")
        else:
            print("User already exists")

    def insert_post(self, username, title, content):
        user = self.session.query(users).filter_by(username=username).first()

        exists = self.session.query(posts).filter_by(title = title).exists()
        if exists is True:
            print("Post already exists")
            return False

        else:
            user = self.session.query(users).filter_by(username=username).first()
            current_timestamp = datetime.datetime.now().timestamp()
            new_post = posts(user_id = user.id, title = title, content = content, datetime = current_timestamp, likes = 0, )
            self.session.add(new_post)
            self.session.commit()
            print("Post added")
            return True

    def like(self, post_id, current_like):
        post_like = posts(likes = current_like)
        return post_like

    def get_user(self, uname):
        return self.session.query(users).filter_by(username=uname).first()

    def username_exists(self, username):
        if self.session.query(users).filter_by(username=username).all() == []:
            return False
        else:
            print("True")
            return True

    def email_exists(self, email):
        a = self.session.query(users).filter_by(email=email).first()
        if self.session.query(users).filter_by(email=email).first() is None:
            print("Nothing is there")
            return False
        else:
            return True

    def search_posts_by_x(self, sort_by_feature, query):
        # For search function
        all_posts = self.session.query(posts).filter(posts.title.like("%" + query + "%" )).all()

        # Beginning of sort function
        if sort_by_feature == "":
            # The filter function had to be used to avoid an error
            all_posts = self.session.query(posts).filter(posts.title.like("%" + query + "%" )).all()

        elif sort_by_feature == "like":
            all_posts = self.session.query(posts).filter(posts.title.like("%" + query + "%" )).order_by(posts.likes.desc()).all()

        elif sort_by_feature == "time":
            all_posts = self.session.query(posts).filter(posts.title.like("%" + query + "%" )).order_by(posts.likes).order_by(posts.datetime).all()

        # To read the datetime and convert it to a different format for the user to view
        for post in all_posts:
            user = self.session.query(users).filter_by(id=post.user_id).first()
            timestamp = datetime.datetime.fromtimestamp(post.datetime)
            post.time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            post.user = user.username
        return all_posts

    def get_own_posts(self, username):
        user = self.session.query(users).filter_by(username=username).first()
        print(f"selecting posts from user {user.username} with id {user.id}")
        Posts = self.session.query(posts).filter_by(user_id=user.id).all()
        # print(f"posts: {posts[0].code}")
        for post in Posts:
            post.user = user.username
            timestamp = datetime.datetime.fromtimestamp(post.datetime)
            post.time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            print(post.time)
            print(post.title)
        Posts.reverse()
        return Posts

    def delete_post(self, post_id):
        post = self.session.query(posts).filter_by(id=post_id).first()
        self.session.delete(post)
        self.session.commit()
        return

    def add_like_or_dislike(self, post_id, type):
        post = self.session.query(posts).filter_by(id=post_id).first()
        if type == "like":
            post.likes += 1
        elif type == "dislike":
            post.likes -= 1
        self.session.commit()

    def change_pswd(self, username, new_pwd):
        user = self.get_user(username)
        user.password = new_pwd
        self.session.commit()
        
create_base()
test = database_handler("networking.sqlite")
