if __name__ == '__main__':
    cards = []
    with open('input.txt', 'r') as file:
        for card in file:
            card = card.split(':')[1]
            card = card.split('\n')[0]
            card = card.strip()
            card = card.split(' | ')
            card[0] = card[0].split()
            card[1] = card[1].split()
            cards.append(card)

    points = 0

    for card in cards:
        worth = 0.5
        win = False
        for your_number in card[1]:
            for win_number in card[0]:
                if your_number == win_number:
                    win = True
                    worth *= 2
                    break
        if(win):
            points += worth

    print(points)