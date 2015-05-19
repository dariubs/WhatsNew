from app import app

DEBUG = True
HOST = "0.0.0.0"
PORT = 2048

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

app.secret_key = "guess me"

DB = {
	"name" : "name",
	"host" : "localhost",
	"port" : 3306,
	"username" : "root",
	"password" : "password"
}