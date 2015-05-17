# -*- coding: utf-8 -*-

from app import app
from config import *

if __name__ == '__main__':
	app.run(HOST, PORT, DEBUG)
