"""
high card showdown
"""
import random

class card:
	def __init__(self,name,suit,value):
		self.name = name
		self.suit = suit
		self.value = value
		self.fullname = f'{name} of {suit}'
	def __eq__(self, other):
		return self.value == other.value
	def __lt__(self,other):
		return self.value < other.value
	def __str__(self):
		return self.fullname
	def __repr__(self):
		return f'name : {self.name},\nsuit : {self.suit}\nvalue : {self.value}'
