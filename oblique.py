# from flask import Flask
# from flask_slack import Slack
import os

from rdoclient import RandomOrgClient as rorgcli


def random_client():
    rnd = rorgcli(os.getenv("RANDOMORG_KEY"))
    return rnd


rnd = random_client()


def strategy():
    with open("oblique.txt", "r") as ost:
        strats = ost.readlines()
        length = len(strats)
    idx = rnd.generate_integers(1, 0, length)
    strat = strats[idx[0]].strip()
    return strat


if __name__ == "__main__":
    strat = strategy()
    print(strat)
