# win7233
# highcard Draw
# with very inconsistent documentation sorry:/

import random

class card:
	"""
	card object.
	has a name, suit, value and fullname variable
	"""
	def __init__(self,name,suit,value):
		"""
		creates self.name (eg: ace),
		self.suit (eg: spade),
		self.value (eg: 1),
		and self.fullname (eg: ace of spades")
		"""
		self.name = name
		self.suit = suit
		self.value = value
		self.fullname = f'{name} of {suit}s'
	## math operations
	def __eq__(self, other):
		return self.value == other.value
	def __lt__(self,other):
		return self.value < other.value
	## printing operations
	def __str__(self):
		return self.fullname
	def __repr__(self):
		return f'name : {self.name},\nsuit : {self.suit}\nvalue : {self.value}'

class deck:
	"""
	deck object (technically a wrapped list)
	## standards:
	we consider deck[0] the "top" card and deck[-1] the bottom
	"""
	def __init__(self):
		"""
		initialization of deck object, 
		initializes self.deck list, 
		generates a deck of cards (no jokers, aces are worth 1) in said list, 
		then shuffles the deck
		"""
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
			# NOTE: this is a dictionary so do not rely on it iterating in any particular order
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
		returns the top card from the deck then removes it from the deck
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
		# NOTE: why does this work like this I kind of hate it (recursive annoyance) (like it works but ugh)
		strTempString = ""
		for i in self.deck:
		 	strTempString = f'{strTempString}{print(i)}\n'  # literally just call print on each card object and append it to the string
		return strTempString

	def __repr__(self):
		"""
		returns all cards in deck, length of deck and the value of each card
		"""
		for i in self.deck:
			reprTempString = f'{reprTempString}- {repr(i)}\n' # just call repr each card object. that provides enough data
		reprTempString = f"Length of deck: {len(self.deck)}\n" # end the deck print with the length of the deck
		return reprTempString
class Player():
	"""
	Player object
	stores all needed player data (name, score, current card)
	can draw cards.
	"""
	def __init__(self, name):
		self.name = name
		self.score = 0
		self.currentCard = None
	def drawCard(self, deck):
		"""draw a card from the deck and print it"""
		self.currentCard = deck.draw()
		print(f"{self.name} Draws: {self.currentCard}")
player = Player("player")
computer = Player("player")
deckObj = deck()
i = 0
while True:
	i += 1 #increase round number. 
	## draw cards from the deck for the player and the computer
	player.drawCard(deckObj) ; computer.drawCard(deckObj)
	## check who won the current round
	if player.currentCard > computer.currentCard: # if player wins
		player.score += 1; print(f"round {i} result: player Wins!")
	elif player.currentCard < computer.currentCard: # if computer wins
		computer.score -= 1; print(f"round {i} result: computer Wins!")
	else:
		print("tie")
	if input("next? (y/n) > ") not in ["y","yes","next", ""] or player.score == 5 or computer.score == 5:
		break
## check who won and print that they won
if player.score == 5: # if player wins
	print("game result: player wins!")
elif computer.score == 5: # if computer wins
	print("game Result: computer wins!")
