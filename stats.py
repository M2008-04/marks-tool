"""Statistics for a list of marks."""


def average(marks):
	return sum(marks) / len(marks)


def highest(marks):
	return max(marks)


def lowest(marks):
	return min(marks)
def pass_count(marks, pass_mark):
	# TODO: read pass_mark from .env instead of the caller
	count = 0
	for mark in marks:
		if mark >=
def pass_count(marks, pass_mark):
	return len([mark for mark in marks if mark >= pass_mark])
from stats import average, highest, lowest, pass_count
...
	pass_mark = int(settings["PASS_MARK"])
	print("Passed :", pass_count(MARKS, pass_mark), "of", len(MARKS))
