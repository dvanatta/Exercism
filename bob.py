# This is bob
# If all of the letters are caps its yelling
# elif ends in question
# elif blank
# else whatever


def check_yelling(string):
    return string.isupper() 


def check_question(string):
    return string[len(string) - 1] == "?"


def check_empty(string):
    if len(string) == 0:
	return True
    else:
	return string.isspace()


def hey(string):
    if check_empty(string):
        return "Fine. Be that way!"
    elif check_yelling(string):
	return "Whoa, chill out!"
    elif check_question(string):
	return "Sure."
    else:
        return "Whatever."
