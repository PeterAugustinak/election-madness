# coding=utf-8

# local library imports
from helpers.clear_screen import clear_screen
from helpers.menus import Menus


def main():
    menu = Menus()

    clear_screen()
    print("==================================")
    print("* VITAJ V ELECTION MADNESS 2020! *")
    print("najdokonalejšia volebná kalkulačka")
    print("==================================")
    print()
    menu.main_menu()


if __name__ == '__main__':
    main()
