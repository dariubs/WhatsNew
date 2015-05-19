from peewee import *
import datetime
from app.config import *
from flask.ext.login import UserMixin
from flask.ext.bcrypt import generate_password_hash

db = MySQLDatabase(DB['name'], host=DB['host'], port=DB['port'], user=DB['username'], passwd=DB['password'])

class BaseModel(UserMixin, Model):
	class Meta :
		database = db

class User(BaseModel):
	username = CharField(unique=True)
	email = CharField(unique=True)
	password = CharField()
	realname = CharField()
	join_date = DateTimeField(datetime.datetime.now)


class Link(BaseModel):
	link_id = IntegerField()
	link_url = TextField()
	link_title = TextField()
	author = ForeignKeyField(User, related_name="pets")
	pub_date = DateTimeField(datetime.datetime.now)
	upvote = IntegerField()

class Comment(BaseModel):
	comment_id = IntegerField()
	comment = TextField()
	link = ForeignKeyField(Link, related_name="linkid")
	parent_comment = IntegerField()
	comment_date = DateTimeField(datetime.datetime.now)

def create_schemas():
	db.connect()
	db.create_tables([User,Link,Comment])

