from wtracker.handlers.gets import GetProcessor
from flask import Flask, request

app = Flask(__name__)

path_index = '/'
@app.route(path_index)
def index():
	result = GetProcessor(request.args, path_index)
	return "from routers"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        