import random

blackjack_memo = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\.
      |  \/ K|                            _/ |                
      '------'                           |__/                 
'''

def adjust_cards(card1, card2):
    if card1 == 1:
        card1 = 11
    if card2 == 1:
        card2 = 11

    total = card1 + card2

    if total > 21:
        if card1 == 11:
            card1 = 1
        elif card2 == 11:
            card2 = 1

    return card1, card2

def compare(player_score, computer_score):
    if player_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Computer went over. You win 😎"
    elif player_score > computer_score:
        return "You win 😎"
    elif player_score < computer_score:
        return "You lose 😭"
    else:
        return "Draw 🙃"

game_is_on = True
while game_is_on:
    ask = input("Do you want to play Blackjack? Type 'y' or 'n': ")
    if ask.lower() == "y":
        players_cards = []
        computers_cards = []

        p_first, p_second, c_first, c_second = [random.randrange(1, 12) for _ in range(4)]
        p_first, p_second = adjust_cards(p_first, p_second)
        c_first, c_second = adjust_cards(c_first, c_second)
        players_cards.extend([p_first, p_second])
        computers_cards.extend([c_first, c_second])

        print(f"{blackjack_memo}\nYour cards: {players_cards} current score: {sum(players_cards)}")
        print(f"Computer's first card: {computers_cards[0]}")

        while sum(players_cards) < 21:
            extra_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if extra_card.lower() == "y":
                new_card = random.randrange(1, 12)
                players_cards.append(new_card)
                print(f"Your cards: {players_cards} current score: {sum(players_cards)}")
                if sum(players_cards) > 21:
                    break
            else:
                break

        while sum(computers_cards) < 17:
            computers_cards.append(random.randrange(1, 12))

        player_score = sum(players_cards)
        computer_score = sum(computers_cards)

        print(f"\nYour final hand: {players_cards}, final score: {player_score}")
        print(f"Computer's final hand: {computers_cards}, final score: {computer_score}")
        print(compare(player_score, computer_score))
        print("-" * 50)

    else:
        print("Game over. See you next time! 👋")
        game_is_on = False
