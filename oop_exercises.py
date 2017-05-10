import random
from functools import wraps
import csv

class Deck():

	def __init__(self):
		""" This should populate our card deck"""
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		values = ["A" ,"2", "3", "4","5", "6", "7", "8", "9", "10", "J", "Q", "K"]

		self.card_list = []

		for suit in suits:
			for value in values:
				self.card_list.append(Card(suit,value))
		
	def __iter__(self):
		return iter(self.card_list)
		
	@classmethod
	def deal(cls,card_list):
		""" This function takes a list of 52 cards i.e. card_list as input and returns the last card. It also removes the last card from the deck"""
		if len(card_list) == 0:
			return "Deck is empty. Start a new game?"
		return card_list.pop()
	
	@classmethod
	def shuffle(cls,card_list):
		""" This function re-arranges the deck randomly"""
		return card_list.random.shuffle()

	def save_deck(self):
		with open("deck.csv", "a") as deck_csv:
			data_writer=csv.writer(deck_csv, delimiter = ",")
			data_writer.writerow(["SUIT", "VALUE"])
			for card in self.card_list:
				print(card)
				data_writer.writerow([card.suit, card.value])

	def load_deck(self):
	# Load your deck from a CSV file
	# take the deck from CSV
	# then replace the current deck
	# they should be the same and in the same order

		with open("deck.csv", "r") as deck_csv:
			data_reader = csv.reader(deck_csv, delimiter =",")
			
				self.card_list 

	# You should be able to kill your program after doing a save.  Start it up again and do a load and have the same deck of cards in the same order


class Card():
	def __init__(self,suit,value):
		self.suit = suit
		self.value = value

	def __str__(self):
		return "{} {}".format(self.suit, self.value)

	def __repr__(self):
		return "{} {}".format(self.suit, self.value)

# Create a decorator called `log` that will print the name of the function being invoked and the arguments to that function

def log(func):
	@wraps(func)
	def inner(*args):
		print(func.__name__ + "was called with the following arguments:" + locals(["args"]))

		with open("deck.log", "w") as file:
			file.write(func.__name__ + "was called with the following arguments:" + locals(["args"]))

		return func(*args)
	return inner
	
@log
def add(a,b):
	return a+b

new_deck = Deck()
# for card in new_deck:
# 	print(card)


new_deck.save_deck()
new_deck.load_deck()





	 