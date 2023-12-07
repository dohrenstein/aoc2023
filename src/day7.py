from typing import Callable, Iterable

import pandas as pd

from utils import BaseSolution

part_1_card_order = ["A", "K", "Q", "J", "T"] + [str(i) for i in range(9, 1, -1)]
part_2_card_order = ["A", "K", "Q", "T"] + [str(i) for i in range(9, 1, -1)] + ["J"]


def _get_hand_type(card_counts):
    """
    Lower = Better
    """
    max_card_cound = max(card_counts.values())
    if max_card_cound == 5:
        # Five of a kind
        return 0
    elif max_card_cound == 4:
        # Four of a kind
        return 1
    elif max_card_cound == 3:
        if 2 in card_counts.values():
            # Full house
            return 2
        else:
            # Three of a kind
            return 3
    elif max_card_cound == 2:
        if sum(value == 2 for value in card_counts.values()) == 2:
            # Two pair
            return 4
        else:
            # One pair
            return 5
    else:
        # High card
        return 6


def _get_card_counts(hand: str):
    card_counts = {}
    for card in hand:
        card_counts[card] = card_counts.get(card, 0) + 1
    return card_counts


def _get_part_1_strength(hand: str):
    card_counts = _get_card_counts(hand)
    return _get_hand_type(card_counts)


def _get_part_2_strength(hand: str):
    card_counts = _get_card_counts(hand)
    card_counts_exc_j = {k: v for k, v in card_counts.items() if k != "J"}

    if "J" in card_counts:
        # must check for edge case where all cards are J
        if len(card_counts_exc_j) > 0:
            # we exclude J from the card counts to account for edge cases such as "AAJJJ"
            max_card = max(card_counts_exc_j, key=card_counts_exc_j.get)
            card_counts[max_card] += card_counts["J"]
            card_counts.pop("J")

    return _get_hand_type(card_counts)


def _calculate_winnings(data: list, strength_func: Callable, card_order: list):
    # each row of data contains a hand and a bid e.g. "32T3K 765"
    # convert data into a dataframe containing two columns named "hand" and "bid"
    # each row of the dataframe contains a hand and a bid e.g. "32T3K" and "765"
    df_hands = pd.DataFrame([hand.split(" ") for hand in data], columns=["hand", "bid"])
    df_hands["strength"] = df_hands["hand"].apply(strength_func)
    for i in range(5):
        df_hands[f"card_{i}_score"] = (
            df_hands["hand"].str[i].apply(lambda card: card_order.index(card))
        )

    df_hands = df_hands.sort_values(
        ["strength"] + [f"card_{i}_score" for i in range(5)], ascending=False
    )
    df_hands["rank"] = range(1, len(df_hands) + 1)
    df_hands["winnings"] = df_hands["rank"] * df_hands["bid"].astype(int)
    return df_hands["winnings"].sum()


class Solution(BaseSolution):
    def part_1(self, data: list) -> int:
        return _calculate_winnings(data, _get_part_1_strength, part_1_card_order)

    def part_2(self, data: list) -> int:
        return _calculate_winnings(data, _get_part_2_strength, part_2_card_order)
