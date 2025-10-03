# This program generates a band name based on user input.
# It asks for the city the user grew up in and the name of a pet,
# then combines these inputs to suggest a band name.
# Example:
# If the user inputs "New York" for the city and "Fluffy" for the pet,
# the output will be "Your band name could be New York Fluffy". 

print('Welcome to the Band Name Generator.')
city = input('Which city did you grow up in?\n')
pet = input('What is the name of a pet?\n')
print('Your band name could be ' + city + ' ' + pet)
