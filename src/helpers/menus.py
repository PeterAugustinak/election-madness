# standard library imports
import sys

# local library imports
from src.helpers.clear_screen import clear_screen
from src.objects.questionnaire import Questionnaire
from src.data.data_lists import Data

class Menus:

    def __init__(self):
        self.questionaire = Questionnaire()
        self.data = Data()

    def main_menu(self):
        print('HLAVNÉ MENU:')
        print()
        print(" (1) SPUSTIŤ VOLEBNÚ KALKULAČKU!")
        print(" (2) ZOZNAM KANDIDUJÚCICH STRÁN")
        print(" (3) ZOZNAM OTÁZOK")
        print(" (4) ZOZNAM ODPOVEDÍ PRE KONKRÉTNU STRANU")
        print(" (5) ZOZNAM ODPOVEDÍ PRE KONKRÉTNU OTÁZKU")
        print(" (6) ZOZNAM VŠETKÝCH ODPOVEDÍ PODĽA STRANY")
        print(" (7) ZOZNAM VŠETKÝCH ODPOVEDÍ PODĽA OTÁZKY")
        print(" (8) CREDITS")
        print(" (9) UKONČIŤ PROGRAM")
        print()

        self._main_menu_selection()

    def _main_menu_selection(self):
        user_selection = input("Zadaj výber (1-8): ")
        self._main_menu_evaluate_selection(user_selection)
        print()
        input("Stlač ENTER pre návrat do hlavného menu ...")
        clear_screen()
        self.main_menu()

    def _main_menu_evaluate_selection(self, user_selection):
        if user_selection == '1':
            clear_screen()
            return self.questionaire.initialize()
        if user_selection == '2':
            clear_screen()
            return self.data.print_list_of_parties()
        if user_selection == '3':
            clear_screen()
            return self.data.print_list_of_statements()
        if user_selection == '4':
            clear_screen()
            return self.data.print_results_by_specific_party()
        if user_selection == '5':
            clear_screen()
            return self.data.print_results_by_specific_statement()
        if user_selection == '6':
            clear_screen()
            return self.data.print_results_by_parties()
        if user_selection == '7':
            clear_screen()
            return self.data.print_results_by_statement()
        if user_selection == '8':
            clear_screen()
            return self._credits()
        if user_selection == '9':
            print()
            print("DÚFAM, ŽE TENTO PROGRAM TI POMOHOL V ROZHODOVANÍ! :)")
            sys.exit()
        else:
            print(" Vyberaj z možností menu zadaním číslovky 1-8!")
            return self._main_menu_selection()

    @staticmethod
    def _credits():
        print()
        print("ELECTION MADNESS")
        print("verzia: 1.0.1. (2020/02/28)")
        print("autor: Peter A.")
