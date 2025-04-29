import random
# Python Mad Libs Warm-Up Activity

# Welcome message
# use random words to create stories and select a random story to return with its title 
def create_story(adjectives='red', nouns='can', verbs='running', adverbs='quickly'):

	story1 = (f"Today, I saw a {random.choice(adjectives)} {random.choice(nouns)}\n"
	f" that decided to {random.choice(verbs)} {random.choice(adverbs)}. I couldn't believe my eyes!")

	story2 = (f"Traveling down the road, a {random.choice(adjectives)} {random.choice(nouns)}\n"
	f" driving a {random.choice(nouns)} {random.choice(verbs)} past me! {random.choice(adverbs)} followed by\n"
	f"a {random.choice(adjectives)} policeman {random.choice(nouns)} who {random.choice(adverbs)} chased after it.")
	
	story3 = (f"I went to a strange zoo, they had a {random.choice(adjectives)} {random.choice(nouns)}\n"
	f"along with a {random.choice(adjectives)} {random.choice(nouns)} which was {random.choice(adverbs)} sleeping.\n"
	f"When I looked closer I saw it was a {random.choice(adverbs)} disguised {random.choice(nouns)}!")

	stories = {"Today":story1, "Driving":story2, "Zoo":story3}
	return random.choice(list(stories.items()))

# Turn user input words separated by commas into a list of words (also strips white space)
def prompt_words(word_type):
	user_input = ""
	while user_input == "":
		user_input = input(f'Enter your {word_type}s: ')
	inputs = user_input.split(',') #[input.strip() for input in user_input.split(',')]
	trimmed_input = []
	for inp in inputs:
		trimmed_input.append(inp.strip())
	return trimmed_input

# save the story to text file with given name
def save_story(title, story, filename="UNAMED_STORY"):
	file = open(f'{filename}.txt', 'w')
	file.write(title)
	file.write(story)
	file.close()

# Centers story lines and title
def format_story(title, story):
	sentences = story.split('\n')
	f_story = ""
	length = 0
	for sentence in sentences:
		if len(sentence) > length:
			length = len(sentence)
	title = f'{title:^{length}}\n'
	for sentence in sentences:
		sentence = f'{sentence:^{length}}\n'
		f_story += sentence
	return title, f_story

print("Welcome to Python Mad Libs!")
print("Answer the following questions to create your very own silly story.\n")
while(True):
	# Gather user inputs
	adjectives = prompt_words("adjective")
	nouns = prompt_words("noun")
	verbs = prompt_words("verb")
	adverbs = prompt_words("adverb")

	# Build the story using an f-string
	title, story = create_story(adjectives=adjectives, nouns=nouns, verbs=verbs, adverbs=adverbs)
	# Display the completed story

	print("\nHere is your story:\n")
	f_title, f_story = format_story(title, story)
	print(f'{f_title}{f_story}')

	# Ask to save Story
	choice = input("\nWould you like to save your story?: ")
	if choice.lower() == "yes":
		filename = input("\nName your file: ")
		save_story(f_title, f_story, filename)
	
	# Ask to replay
	choice = input("would you like to play again?\n")
	if choice.lower() != "yes":
		break
	
#   - Which Python functions did you use to get input from the user?
#       input() - prints a given value, then returns a user input value
#   - How did f-string formatting help in constructing the story?
#       allows adding the story's and user's words together simplier
#   - What would you change or add to your script if you wanted to make the game more interactive?
#       give a question for each input for the user to answer, then instead of thinking of a random noun they be giving a noun answer to fill in the blank