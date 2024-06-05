import random
#This adds our random module.

user = input("What is your username? (Cannot contain these characters: ~ ` ; | ) ")
#The user will be asked to make their username and cannot contain the tilda character.

info = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890!@#$%^&*()`~,./<>?;':{}\-=_+"
#If the user wants a really secure password but they can't think of anything, then most of the characters on the English keyboard will be used and randomly selected in our choice sequence

while user.find("~") >= 0:
  print("Cannot contain ~ ` ; | in your username. Please try again.")
  user = input("What is your username? (Cannot contain the ~ character.) ")
#If the user inputs ~ anywhere in their username, this code will occur and will ask the user to make a new username sice the index on the first letter is always 0 or higher.
while user.find("`") >= 0:
  print("Cannot contain ~ ` ; | in your username. Please try again.")
  user = input("What is your username? (Cannot contain the ~ character.) ")
#If the user inputs ` anywhere in their username, this code will occur and will ask the user to make a new username sice the index on the first letter is always 0 or higher.
while user.find(";") >= 0:
  print("Cannot contain ~ ` ; | in your username. Please try again.")
  user = input("What is your username? (Cannot contain the ~ character.) ")
#If the user inputs ; anywhere in their username, this code will occur and will ask the user to make a new username sice the index on the first letter is always 0 or higher.
while user.find("|") >= 0:
  print("Cannot contain ~ ` ; | in your username. Please try again.")
  user = input("What is your username? (Cannot contain these characters: ~ ` ; | ) ")
#If the user inputs ; anywhere in their username, this code will occur and will ask the user to make a new username sice the index on the first letter is always 0 or higher.
print("Username: " + user)
#Once the user makes their username without containg the tilda character, this will be able to print out and skips the while loop.

print("Password: " + random.choice(info) + random.choice(info) + random.choice(info) + random.choice(info) + random.choice(info) + random.choice(info) + random.choice(info) + random.choice(info) + random.choice(info) + random.choice(info) + random.choice(info) + random.choice(info))
#Here, the choice will choose a random character in our info variable twelve times and will print it out and will always be random.