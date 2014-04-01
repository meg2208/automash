from brains import MoodBoombox
from common import VALID_MOODS
from sys import argv

if __name__ == '__main__':
	print 'hi'
	if len(argv) != 3:
		raise Exception("Please try again using this format:\npython make_mashup.py <mood> <output_name>")
	elif argv[1] not in VALID_MOODS:
		raise Exception("Please try again using one of these valid moods:\n{}".format(",".join(VALID_MOODS)))
	else:
		print argv[1], argv[2].split('.')[0]
		mood, output_name = argv[1], argv[2].split('.')[0]
		MoodBoombox(mood, output_name)