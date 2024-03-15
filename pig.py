#!/usr/bin/env python3

import random

WINNING_SCORE = 100

current_player: int = 1
player_scores = [None, 0, 0]
die_rolls_total: int = 0


def game_won() -> bool:
    return (player_scores[1] >= WINNING_SCORE or
            player_scores[2] >= WINNING_SCORE)


def switch_players() -> None:
    global current_player
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1


def roll_one_dice() -> int:
    return random.randint(1, 6)


def rolled_a_one(die_value: int):
    return die_value == 1


def there_is_a_winner():
    return player_scores[current_player]+die_rolls_total >= WINNING_SCORE


def find_winning_player() -> int:
    winning_player = 1
    if player_scores[winning_player] < WINNING_SCORE:
        winning_player = 2


def add_roll_total_to_player_score():
    player_scores[current_player] += die_rolls_total


def reset_roll_total():
    global die_rolls_total
    die_rolls_total = 0


def add_to_roll_total(die_value):
    global die_rolls_total
    die_rolls_total += die_value


def show_current_player() -> None:
    print(f"\nPlayer {current_player}")


def show_rolled_value(die_value: int):
    print(f"- rolled a {die_value}")


def show_scores() -> None:
    print(
        f"\t[Player 1: {player_scores[1]}/{WINNING_SCORE}]\n",
        f"\t[Player 2 {player_scores[2]}/{WINNING_SCORE}]"
    )


def want_to_roll_again() -> bool:
    answer = input("Do you want to roll again [y/n]?")
    return answer == "y"


def show_player_totals() -> None:
    print(
        f"Player {current_player} total rolls add to: {die_rolls_total}")


def show_winner() -> None:
    winning_player = find_winning_player()
    print(
        f"PLAYER {winning_player} IS THE WINNER!!! with {
            player_scores[winning_player]} points!"
    )


while not game_won():
    show_current_player()
    die_value: int = roll_one_dice()
    show_rolled_value(die_value)
    show_scores()
    if rolled_a_one(die_value):
        reset_roll_total()
        switch_players()
        continue
    add_to_roll_total(die_value)
    show_player_totals()
    if there_is_a_winner():
        add_roll_total_to_player_score()
        break
    if not want_to_roll_again():
        add_roll_total_to_player_score()
        reset_roll_total()
        switch_players()

show_winner()
