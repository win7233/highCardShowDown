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

class deck:
	def __init__(self):
		"""
			initialization of deck object,
			initializes self.deck list,
			then generates all the contents of a deck (no jokers, aces are worth 1)
		"""
		self.deck = []
		# generate card objects loop
		suitList = ["spades","clubs","hearts","diamonds"]
		faceCardNameDict = {"Jack":11, "Queen":12, "King":13, "Ace":1}
		for suitID in range(4):
			currentSuit = suitList[suitID]
			# numberCard generation loop
			for cardBaseIt in range(9): # 9 because 2-10
				cardVal = cardBaseIt+2 # +2 to avoid aces
				cardName = str(cardVal)
				cardObj = card(cardName, currentSuit, cardVal)
				self.deck.append(cardObj)
			# faceCards generation
			for cardName,cardVal in faceCardNameDict.items():
				cardObj = card(cardName, currentSuit, cardVal)
				self.deck.append(cardObj)
	def shuffle(self):
		pass
	def draw(self):
		card = random.choice(self.deck)
		self.deck.remove(card)
		return card
	def __len__(self):
		return len(self.deck)
	def __contains__(self,other):
		for i in self.deck:
			if i == other:
				return True
		return False
	def __str__(self):
		for i in self.deck:
			print(i)

deckObj = deck()
running = True
while running:
	
