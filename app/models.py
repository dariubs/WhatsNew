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
	join_date = DateTimeField(datetime.datetime.now)
	is_active = BooleanField()

	@classmethod
	def create_user(user, username, email, password):
		pass

	@classmethod
	def activate(user, activecode):
		pass

	@classmethod
	def user_info(user, id):
		pass

class Link(BaseModel):
	link_id = IntegerField()
	link_url = TextField()
	link_title = TextField()
	author = ForeignKeyField(User, related_name="pets")
	pub_date = DateTimeField(datetime.datetime.now)
	upvote = IntegerField()

	@classmethod
	def add_link(link, url, title, author):
		pass

	@classmethod
	def rm_link(link, id):
		pass

	@classmethod
	def up_vote(link, user):
		pass

	@classmethod
	def hotlinks(link, page, limit):
		pass

	@classmethod
	def newlinks(link, page, limit):
		pass



class Comment(BaseModel):
	comment_id = IntegerField()
	comment = TextField()
	link = ForeignKeyField(Link, related_name="linkid")
	parent_comment = IntegerField()
	comment_date = DateTimeField(datetime.datetime.now)

	@classmethod
	def add_comment(cmnt, comment, link, parent):
		pass

	@classmethod
	def rm_comment(cmnt, id):
		pass

	@classmethod
	def comments(cmnt, link, page, limit):
		pass


def create_schemas():
	db.connect()
	db.create_tables([User,Link,Comment])

