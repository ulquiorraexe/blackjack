# Blackjack Game

This is a simple text-based Blackjack game implemented in Python. The game allows you to play against the computer, and it includes the basic rules of Blackjack, such as card values, busts, and the comparison of scores to determine the winner.

## Features:
- Card values: Aces can be either 1 or 11, face cards (J, Q, K) are worth 10, and numbered cards are worth their value.
- Simple interaction: The player can choose to draw more cards or stand.
- Basic comparison: The computer automatically draws cards until its score reaches 17.
- Game continuation: The game asks if you want to play again after each round.

## How to Play:
1. The game will deal two cards to both the player and the computer.
2. The player can choose to draw additional cards by typing `'y'` or pass by typing `'n'`.
3. The game will compare the player's and the computer's scores to determine the winner. If the player goes over 21, they lose, and the computer will win if it goes over 21.
4. After the round, you can decide to play again or exit the game.

## Installation:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ulquiorraexe/blackjack.git
   cd blackjack

2. **Run the game:**

   ```bash
   python main.py

3. The game will prompt you to either start playing or exit. Follow the on-screen instructions.

## Game Rules

  - **Aces:** Aces are worth 1 or 11 points, depending on what benefits the player most.
  - **Face cards (J, Q, K):** Each is worth 10 points.
  - **Other cards:** Cards 2-10 are worth their respective number values.
  - **Busting:** If your total score exceeds 21, you lose the game.
  - **Winning:** If you have a higher score than the computer without busting, you win.

## Example Output

```swift
Do you want to play Blackjack? Type 'y' or 'n': y
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\.
      |  \/ K|                            _/ |                
      '------'                           |__/                 

Your cards: [10, 5] current score: 15
Computer's first card: 9

Type 'y' to get another card, type 'n' to pass: y
Your cards: [10, 5, 6] current score: 21
Your final hand: [10, 5, 6], final score: 21
Computer's final hand: [9, 6, 8], final score: 23
You win 😎
--------------------------------------------------
Do you want to play Blackjack? Type 'y' or 'n': n
Game over. See you next time! 👋
```

## License

This project does not have a license.
