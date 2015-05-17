# -*- coding: utf-8 -*-
from app import app
from app.config import *

if __name__ == '__main__':
	app.run(HOST, PORT, DEBUG)
