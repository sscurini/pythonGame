from heroes import Heroes
from monsters import Monsters


def welcome():
    print("Welcome to Steve's awesome battle adventure game")
    print(" ")
    username = input("Enter your name: ")
    print("Welcome " + username)
    return username


def main_game():
    welcome()

    hero = Heroes()
    monster = Monsters()


main_game()