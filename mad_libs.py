import random
# Python Mad Libs Warm-Up Activity

# Welcome message
def createStory(adjectives='red', nouns='can', verbs='running', adverbs='quickly'):
	story = (f"Today, I saw a {random.choice(adjectives)} {random.choice(nouns)}"
	f" that decided to {random.choice(verbs)} {random.choice(adverbs)}.\nI couldn't believe my eyes!")
	return story

def promptWords(word_type):
	user_input = ""
	while user_input == "":
		user_input = input(f'Enter your {word_type}s: ')
	inputs = user_input.split(',') #[input.strip() for input in user_input.split(',')]
	trimmed_input = []
	for inp in inputs:
		trimmed_input.append(inp.strip())
	return trimmed_input

print("Welcome to Python Mad Libs!")
print("Answer the following questions to create your very own silly story.\n")
while(True):
	# Gather user inputs
	adjectives = promptWords("adjective")
	nouns = promptWords("noun")
	verbs = promptWords("verb")
	adverbs = promptWords("adverb")

	# Build the story using an f-string
	story = createStory(adjectives=adjectives, nouns=nouns, verbs=verbs, adverbs=adverbs)

	# Display the completed story
	print("\nHere is your story:")
	print(story)
	
	choice = input("would you like to play again?\n")
	if choice.lower() != "yes":
		break
	
#   - Which Python functions did you use to get input from the user?
#       input() - prints a given value, then returns a user input value
#   - How did f-string formatting help in constructing the story?
#       allows adding the story's and user's words together simplier
#   - What would you change or add to your script if you wanted to make the game more interactive?
#       give a question for each input for the user to answer, then instead of thinking of a random noun they be giving a noun answer to fill in the blank