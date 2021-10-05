games = ["Madden", "2k", "Fifa"]
new_game = ''
while new_game != 'quit':
    new_game = input("Enter a game you like or type 'quit'")
    if new_game != 'quit':
        games.append(new_game)

print(games)