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
            card.append(1)
            cards.append(card)

    scratchcards = 0

    for i, card in enumerate(cards):
        copies = 0
        win = False
        for your_number in card[1]:
            for win_number in card[0]:
                if your_number == win_number:
                    win = True
                    copies += 1
                    break
        if(win):
            temp = 1
            while(temp <= cards[i][2]):
                tmp = 1
                while(tmp <= copies):
                    cards[(i + tmp)][2] += 1
                    tmp += 1
                temp += 1

        print("Card " + str(i+1) + ": " + str(card) + ", win numbers: " + str(copies))

    for card in cards:
        scratchcards += card[2]

    print(scratchcards)
