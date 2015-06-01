from peewee import *
import datetime
from app.config import *
from flask.ext.login import UserMixin
from flask.ext.bcrypt import generate_password_hash
from flask import flash

db = MySQLDatabase(DB['name'], host=DB['host'], port=DB['port'], user=DB['username'], passwd=DB['password'])

class BaseModel(Model):
	class Meta :
		database = db

class User(BaseModel):
	username = CharField(unique=True)
	email = CharField(unique=True)
	password = CharField()
	join_date = DateTimeField(datetime.datetime.now)
	is_active = BooleanField()


	
	@classmethod
	def create_user(self, username, email, password):
		"""
			Create User Method
		"""
		try:
			user = User.create(
				username= username,
				password= generate_password_hash(password),
				email= email,
				join_date= datetime.datetime.now()
			)

			flash("Registration complete. please login")
			return True
		except IntegrityError:
		    return False

	
	@classmethod
	def activate(self, username, activecode):
		"""
			Activate users profile
			Just For evaluate email address

			Active code formula :
				generate_password_hash(user.username + user.email + user.join_date)
		"""
		try :
			user = self.get(self.username == username)
			if(generate_password_hash(user.username + user.email + user.join_date) == activecode) :
				user.update(active=True)
				user.execute()
			return True
		except IntegrityError:
			return False


	
	@classmethod
	def user_info(self, username):
		"""
			Get public users info
		"""
		try:
			user = 	self.get(self.username == username)
			return user
		except :
			return False

	@classmethod
	def check_login(self, username, password):
		try :
			user = 	self.select().where(username = username).where(password = password)
			return user
		except IntegrityError :
			return False


	@classmethod
	def not_username(self, username) :
		"""
			Check if username free to register
		"""
		try :
			user = self.get(self.username == username)
			flash("This username hase been taken")
			return False
		except :
			return True
			

	
	@classmethod
	def not_email(self, email) :
		"""
			Check if email free to register
		"""
		try :
			mail = User.get(User.email == email)
			flash("This email already registered")
			return False
		except :
			return True


class Link(BaseModel):
	link_id = IntegerField()
	link_url = TextField()
	link_title = TextField()
	author = ForeignKeyField(User, related_name="pets")
	pub_date = DateTimeField(datetime.datetime.now)
	upvote = IntegerField()

	@classmethod
	def add_link(self, url, title, author):
		pass

	@classmethod
	def rm_link(self, id):
		pass

	@classmethod
	def up_vote(self, user):
		pass

	@classmethod
	def hotlinks(self, page, limit):
		pass

	@classmethod
	def newlinks(self, page, limit):
		pass

class Comment(BaseModel):
	comment_id = IntegerField()
	comment = TextField()
	link = ForeignKeyField(Link, related_name="linkid")
	parent_comment = IntegerField()
	comment_date = DateTimeField(datetime.datetime.now)

	@classmethod
	def add_comment(self, comment, link, parent):
		pass

	@classmethod
	def rm_comment(self, id):
		pass

	@classmethod
	def comments(self, link, page, limit):
		pass

def create_schemas():
	db.connect()
	db.create_tables([User,Link,Comment])

