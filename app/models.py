from peewee import *
import datetime

DATABASE = SqliteDatabase('news.db')

class User(Model):
	username = CharField(unique=True)
	email = CharField(unique=True)
	password = CharField()
	realname = CharField()
	website = CharField()
	joindate = DateTimeField(datetime.datetime.now)

	class Meta :
		database = DATABASE


class Link(Model):
	linkurl = TextField()
	linktitle = TextField()
	author = IntegerField()
	createtime = DateTimeField(datetime.datetime.now)
	upvote = IntegerField()

	class Meta :
		database = DATABASE
