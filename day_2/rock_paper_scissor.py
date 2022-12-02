#!/usr/bin/env python
""" Rock Paper Scissor"""


import argparse
from typing import Dict


WON: int = 6
LOSS: int = 0
DRAW: int = 3


class RockPaperScissor:
    """RockPaperScissor score manager"""

    rpc_map: Dict[str, str]
    score_map: Dict[str, int] = {"rock": 1, "paper": 2, "scissor": 3}

    def __init__(self, play_hand):
        self.play_hand = play_hand
        self.hand_type = self.rpc_map[self.play_hand]
        self.score = self.score_map[self.hand_type]


class Player1(RockPaperScissor):
    rpc_map: Dict[str, str] = {"A": "rock", "B": "paper", "C": "scissor"}


class Player2(RockPaperScissor):
    rpc_map: Dict[str, str] = {"X": "rock", "Y": "paper", "Z": "scissor"}


def calc_score(player1: Player1, player2: Player2):
    _player1_score = 0
    _player2_score = 0
    # Player1 perspective
    if (
        (player1.hand_type == "scissor" and player2.hand_type == "paper")
        or (player1.hand_type == "paper" and player2.hand_type == "rock")
        or (player1.hand_type == "rock" and player2.hand_type == "scissor")
    ):
        _player1_score += _player1_score + WON
        _player2_score += _player2_score + LOSS
    elif (
        (player2.hand_type == "scissor" and player1.hand_type == "paper")
        or (player2.hand_type == "paper" and player1.hand_type == "rock")
        or (player2.hand_type == "rock" and player1.hand_type == "scissor")
    ):
        _player1_score += _player1_score + LOSS
        _player2_score += _player2_score + WON
    elif player1.hand_type == player2.hand_type:
        _player1_score += _player1_score + DRAW
        _player2_score += _player2_score + DRAW
    else:
        raise ValueError(
            f"Unknown play combination: {player1.play_hand, player2.play_hand}"
        )

    return (_player1_score + player1.score, _player2_score + player2.score)


def main(args):

    # Part-1
    player1_score = 0
    player2_score = 0
    with open(args.input, "r") as handle_r:
        for line in handle_r:
            player1_play_hand, player2_play_hand = line.strip().split(" ")
            scores = calc_score(Player1(player1_play_hand), Player2(player2_play_hand))
            player1_score += scores[0]
            player2_score += scores[1]
    print(f"Part - 1")
    print(f"Player1 Score: {player1_score}\nPlayer2 Score: {player2_score}")
    print("-------------------------------", end="\n\n")

    # Part-2
    player1_score = 0
    player2_score = 0
    with open(args.input, "r") as handle_r:
        for line in handle_r:
            player1_play_hand, player2_play_hand = line.strip().split(" ")
            if player2_play_hand == "X":
                # X mens loose
                if player1_play_hand == "A":
                    player2_play_hand = "Z"
                elif player1_play_hand == "B":
                    player2_play_hand = "X"
                elif player1_play_hand == "C":
                    player2_play_hand = "Y"
            elif player2_play_hand == "Y":
                # Y means draw
                if player1_play_hand == "A":
                    player2_play_hand = "X"
                elif player1_play_hand == "B":
                    player2_play_hand = "Y"
                elif player1_play_hand == "C":
                    player2_play_hand = "Z"
            elif player2_play_hand == "Z":
                # Z means win
                if player1_play_hand == "A":
                    player2_play_hand = "Y"
                elif player1_play_hand == "B":
                    player2_play_hand = "Z"
                elif player1_play_hand == "C":
                    player2_play_hand = "X"
            scores = calc_score(Player1(player1_play_hand), Player2(player2_play_hand))
            player1_score += scores[0]
            player2_score += scores[1]
    print(f"Part - 2")
    print(f"Player1 Score: {player1_score}\nPlayer2 Score: {player2_score}")
    print("-------------------------------", end="\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Arguments to Elf calorie task")

    parser.add_argument("input", type=str, help="Path to the Elf calorie list file")

    main(parser.parse_args())
