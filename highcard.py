import random

class card:
	def __init__(self,name,suit,value):
		self.name = name
		self.suit = suit
		self.value = value
		self.fullname = f'{name} of {suit}s'
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
		"""initialization of deck object, initializes self.deck list, generates all the contents of a deck (no jokers, aces are worth 1), shuffles the deck"""
		self.deck = []
		# generate card objects loop
		suitList = ["spade","heart","club","diamond"]
		faceCardNameDict = {"Jack":11, "Queen":12, "King":13, "Ace":1}
		for currentSuit in suitList:
			# numberCard generation loop
			for cardBaseIt in range(9): # 9 because 2-10
				cardVal = cardBaseIt+2 # +2 to avoid ones
				cardName = str(cardVal)
				cardObj = card(cardName, currentSuit, cardVal)
				self.deck.append(cardObj)
			# faceCards generation (and also aces)
			# NOTE: this is a dictionary so do not rely on it iterating in any particular order)
			for cardName,cardVal in faceCardNameDict.items():
				cardObj = card(cardName, currentSuit, cardVal)
				self.deck.append(cardObj)
		self.shuffle() # shuffle the deck because the above function generates it in order
	def shuffle(self):
		"""
		well I wrote a whole function to do this and then found a one line solution UGH
		randomizes the order of self.deck
		returns nothing
		"""
		self.deck = random.sample(self.deck, len(self.deck))

	def draw(self):
		"""
		returns a random card from the deck then
		"""
		card = self.deck[0]
		self.deck.remove(card)
		return card
	def __len__(self):
		"""literally just returns the length of the deck list"""
		return len(self.deck)
	def __contains__(self,other):
		"""
		iterates through deck and returns true at the first instance of a card matching the passed card. 
		otherwise returns false
		"""
		# this is very elegant code I like it
		for i in self.deck:
			if i == other:
				return True
		return False
	def __str__(self):
		"""
		returns a simple to read list of the contents of the deck
		"""
		# NOTE: why does this work like this I kind of hate it (recursive annoyance)
		strTempString = ""
		for i in self.deck:
		 	strTempString = f'{strTempString}{print(i)}\n'  # literally just call print on each card object and append it to the string
		return strTempString

	def __repr__(self):
		"""returns all cards in deck, length of deck and the value of each card"""
		reprTempString = f"# Length of deck: {len(self.deck)}\n"
		for i in self.deck:
			reprTempString = f'{reprTempString}- {repr(i)}\n' # just call repr each card object. that provides enough data
		return reprTempString
score = 0
deckObj = deck()
for i in range(5):
	playerDraw = deckObj.draw()
	comDraw = deckObj.draw()
	if playerDraw > comDraw:
		score += 1; print("player wins!")
	elif playerDraw < comDraw:
		score -= 1; print("computer wins!")
	else:
		print("tie")
if score > 0:
	print("came result: player wins!")
elif score < 0:
	print("game Result: computer wins!")
else:
	print("game reasult: tie")

