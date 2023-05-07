import datetime
from db_handler import database_handler as dbh

timestamp = datetime.datetime.fromtimestamp(1682432865.045946)
formatted_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
time = datetime.datetime.now().timestamp()

# print(timestamp)
# print(formatted_time)
print(time)

db = dbh("networking.db")
# db.search_posts_by_x("")
# db.get_own_posts("Tkaru")