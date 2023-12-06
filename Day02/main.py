import re

if __name__ == '__main__':
    games = []
    with open('input.txt', 'r') as file:
        for game in file:
            game = game.split(":")[1]
            game = game.split("\n")[0]
            game = game.split(";")
            games.append(game)

    temp = []

    for game in games:
        gm = []
        for reveal in game:
            rv = []
            reveal = reveal.split(",")
            for rev in reveal:
                rev = rev.strip().split(" ")
                rv.append(rev)
            gm.append(rv)
        temp.append(gm)

    games = temp

    red = 12
    green = 13
    blue = 14
    sum_of_games = 0

    for i, game in enumerate(games):
        counting = True
        for reveal in game:
            if(counting == False):
                break
            for rev in reveal:
                if(rev[1] == "red"):
                    if(int(rev[0]) > red):
                        counting = False
                        break
                elif(rev[1] == "green"):
                    if(int(rev[0]) > green):
                        counting = False
                        break
                elif(rev[1] == "blue"):
                    if(int(rev[0]) > blue):
                        counting = False
                        break
        if(counting == True):
            sum_of_games += (i+1)

    print(sum_of_games)