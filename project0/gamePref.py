games = ["Madden", "2k", "Fifa"]
print("The games I like are")
for game in games:
    print(game)
new_game = input("What is a game you like?")
games.append(new_game)
print("The games we like are")
for game in games:
    print(game)
