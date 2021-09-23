#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	nb_letters = 0
	for letter in text:
		if letter.isalnum():
			nb_letters += 1
	return nb_letters

def get_word_length_histogram(text):
	lettre_max = 0

	for word in text.split():
		if lettre_max < get_num_letters(word):
			lettre_max = get_num_letters(word)
	histogramme = [0] * (lettre_max + 1)

	for word in text.split():
		histogramme[get_num_letters(word)] += 1

	return histogramme

def format_histogram(histogram):
	ROW_CHAR = "*"
	affichage = ""
	histogram = histogram[1:]
	len_max = len(str(len(histogram[1:])))

	for index, value in enumerate(histogram):
		affichage += f"{(index + 1) : > 2}" + " " + ROW_CHAR * value + "\n"

	return affichage

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	ligne1 = ""
	ligne2 = ""
	ligne3 = ""
	ligne4 = LINE_CHAR * len(histogram)

	for index, value in enumerate(histogram[1:]):
		if value == 3:
			ligne1 += BLOCK_CHAR
		else:
			ligne1 += " "

		if value == 2 or value == 3:
			ligne2 += BLOCK_CHAR
		else:
			ligne2 += " "

		if value == 1 or value == 2 or value == 3:
			ligne3 += BLOCK_CHAR
		else:
			ligne3 += " "

	resultat = ligne1 + "\n" + ligne2 + "\n" + ligne3 + "\n" + ligne4

	return resultat


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
