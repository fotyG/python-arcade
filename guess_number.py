import sys
import random


def gn(name="PlayerOne"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_gn():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        player_choice = input(
            f"\n{name}, guess what number I'm thinking of between 1 and 3\n"
        )

        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2 or 3.")
            return play_gn()

        player = int(player_choice)

        if player < 1 or player > 3:
            sys.exit()

        computer_choice = random.choice("123")

        computer = int(computer_choice)

        print(f"\nYour guess is {player}, let's see if you're right..")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == computer:
                player_wins += 1
                return "🎉You guessed correctly!"
            else:
                python_wins += 1
                return f"🐍 Python's number of choice was {computer}!\nSorry, {name}..😢"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1
        print(
            f"\nYou have played {game_count} {'game' if game_count == 1 else 'games'} and won {player_wins} of them.")
        print(
            f"\nYour win percentage is {player_wins / game_count:.2%}.")
        print("\nWant to play again?")

        while True:
            play_again = input("\nY for yes or \nQ to quit\n")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_gn()
        else:
            print(f"\nThanks for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"See you soon, {name}!")
            else:
                return

    return play_gn


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a name for the game."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()
    guess_number = gn(args.name)
    guess_number()
