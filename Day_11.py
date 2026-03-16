import random

def del_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def game_play():
    user_card = []
    comp_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(del_card())
        comp_card.append(del_card())

    while not is_game_over:
        user_score = calc_score(user_card)
        comp_score = calc_score(comp_card)
        print(f"   Your cards: {user_card}, current score: {user_score}")
        print(f"   Computer's first card: {comp_card[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, 'n' to pass: ")
            if user_should_deal == 'y':
                user_card.append(del_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_card.append(del_card())
        comp_score = calc_score(comp_card)

    print(f"   Your final hand: {user_card}, final score: {user_score}")
    print(f"   Computer's final hand: {comp_card}, final score: {comp_score}")
    print(compare(user_score, comp_score))

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play == 'y':
    print("\n" * 20)
    game_play()
    play = input("Do you want to play again? Type 'y' or 'n': ")