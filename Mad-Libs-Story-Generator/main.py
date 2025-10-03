# Mad Libs Story Generator 🤪

# This program generates a fun story based on user-provided words.
print("Welcome to the Mad Libs Story Generator!")
user_name = input("Enter your name: ")

print(f"\nHello, {user_name}! Let's create a fun story together.")
print("Please provide the following words:")

# Get input from the user with examples
noun1 = input("Noun (e.g., dog, castle): ")
verb1 = input("Verb (e.g., ran, sings): ")
adjective1 = input("Adjective (e.g., happy, tall): ")
adverb1 = input("Adverb (e.g., quickly, loudly): ")
noun2 = input("Another Noun (e.g., cat, mountain): ")
verb2 = input("Another Verb (e.g., jumped, writes): ")
adjective2 = input("Another Adjective (e.g., silly, green): ")
adverb2 = input("Another Adverb (e.g., slowly, carefully): ")

# Create the story using an f-string
story = f"Once upon a time, there was a {adjective1} {noun1} who loved to {verb1} {adverb1}. One day, it met another {adjective2} {noun2} that could {verb2} {adverb2}. They became friends and lived happily ever after!"

# Print the final story
print("\nHere's your story:")
print(story)