from .exceptions import *
import random 

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
	if len(list_of_words) == 0:
		raise(InvalidListOfWordsException)
	elif len(list_of_words) == 1:
		word = list_of_words[0]
	else:
		selection = random.randrange(0,len(list_of_words))	
		word = list_of_words[selection]
	return word 


def _mask_word(word):
	if word:
		masked_word = len(word)*'*'
		return masked_word 
	else:
		raise(InvalidWordException)

def _uncover_word(answer_word, masked_word, character):
	
	# make sure that the words aren't empty
	if (len(answer_word) < 1) or (len(masked_word) < 1):
		raise(InvalidWordException)
	# make sure that they are only guessing 1 letter in character
	if len(character) > 1:
		raise(InvalidGuessedLetterException)
	# make sure that the answer_word length is equal to length masked_word
	if len(answer_word) != len(masked_word):
		raise(InvalidWordException) 


	# check to see if character is in the answer
	# if it is replace it's position with * 
	
	new_string = ''
	for index, letter in enumerate(answer_word):
		if character.lower() == letter.lower():
			new_string += character.lower()
		elif masked_word[index].lower() == letter.lower():
			new_string += masked_word[index].lower()
		else:
			new_string += '*'
	return new_string

def guess_letter(game, letter):
    pass


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
