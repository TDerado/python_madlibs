
# Python Mad Libs Warm-Up Activity

# Welcome message
def createStory(adjective='red', noun='can', verb='running', adverb='quickly'):
	return f"Today, I saw a {adjective} {noun} that decided to {verb} {adverb}.\nI couldn't believe my eyes!"
print("Welcome to Python Mad Libs!")
print("Answer the following questions to create your very own silly story.\n")
while(True):
	# Gather user inputs
	adjective = input("Enter an adjective: ")
	noun = input("Enter a noun: ")
	verb = input("Enter a verb: ")
	adverb = input("Enter an adverb: ")

	# Build the story using an f-string
	story = createStory(adjective=adjective, noun=noun, verb=verb, adverb=adverb)

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