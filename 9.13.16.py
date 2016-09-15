input = [
	"wisdom", "mid sow", "Seth Rogan", "Gathers No",
	"Reddit", "Eat Dirt", "Schoolmaster", "The classroom",
	"Astronomers", "Moon starer", "Vacation Times", "I'm Not as Active",
	"Dormitory", "Dirty Rooms"
	]

def _sort_word(word):
	return sorted(''.join([char for char in word if char.isalpha()]).lower())

for x in range(0,13,2):
	if(_sort_word(input[x]) == _sort_word(input[x+1])):
		conditional = "IS"
	else:
		conditional = "IS NOT"

	print('{} {} an anagram of {}'.format(input[x], conditional, input[x+1]))