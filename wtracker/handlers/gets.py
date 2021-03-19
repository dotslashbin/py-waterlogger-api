#!/usr/bin/python

from werkzeug.wrappers import ResponseStreamMixin


class GetProcessor():
	def __init__(self, parameters: dict, path: str):
		self._parameters = parameters
		self._path = path
		self.fetch_data_from_controller()
		
	def fetch_data_from_controller(self) -> str:
		test = "hello"
  		return test