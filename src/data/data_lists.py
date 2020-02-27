import csv
from collections import defaultdict
from os import system


class Data:

    parties_dict = []
    statements_dict = []
    answers_lst_dict = []

    def __init__(self, file):
        self.source = f'..\..\{file}'
        self._csv_reader(self.source)

    @classmethod
    def _csv_reader(cls, source):
        with open(source, encoding='utf-8') as csv_file:
            source_file = csv.DictReader(csv_file)
            cls._fill_lists(source_file)

    @classmethod
    def _fill_lists(cls, source_file):
        items_dict = defaultdict(list)
        for row in source_file:
            for (k, v) in row.items():
                items_dict[k].append(v)

        cls.statements_dict.append(items_dict['statement'])
        cls.parties_dict.append(items_dict.keys())
        cls.answers_lst_dict.append(items_dict.values())

    # CREATE LISTS
    def list_of_parties(self):
        for parties in self.parties_dict:
            return [party for party in parties][1:]

    def list_of_statements(self):
        for statements in self.statements_dict:
            return [statement.strip('.') for statement in statements]

    def list_of_anwsers(self):
        for answers_lst in self.answers_lst_dict:
            return [answers_lst for answers_lst in answers_lst][1:]


    # PRINTING METHODS
    def print_list_of_parties(self):
        for num, party in enumerate(self.list_of_parties(), start=1):
            if party:
                print(f"{num}. {party}")

    def print_list_of_statements(self):
        for num, statement in enumerate(self.list_of_statements(), start=1):
            print(f"{num}. {statement}")

    def print_results_by_parties(self):
        for party, answers in zip(self.list_of_parties(), self.list_of_anwsers()):
            print(party.upper())
            for statement, answer in zip(self.list_of_statements(), answers):
                print(f"{statement}: {answer.upper()}")
            print()

    def print_results_by_statement(self):
        for statement, answers in zip(self.list_of_statements(), self.list_of_anwsers()):
            print(f"ZOZNAME ODPOVEDÍ STRÁN PRE VÝROK '{statement.upper()}'")
            for party, answer in zip(self.list_of_parties(), answers):
                print(f"{party}: {answer}")
            print()

    def print_results_by_specific_party(self):
        self.print_list_of_parties()
        party_num = self.pick_key('STRANU', self.list_of_parties())
        party = self.list_of_parties()[party_num]

        print(f"ZOZNAME ODPOVEDÍ PRE STRANU {party.upper()}")
        for statement, answer in zip(self.list_of_statements(), self.list_of_anwsers()[party_num]):
            print(f" {statement}: {answer.upper()}")

    def print_results_by_specific_statement(self):
        self.print_list_of_statements()
        statement_num = self.pick_key('VÝROK', self.list_of_statements())
        statement = self.list_of_statements()[statement_num]

        print(f"ZOZNAME ODPOVEDÍ STRÁN PRE VÝROK '{statement.upper()}'")

        for party, answers in zip(self.list_of_parties(), self.list_of_anwsers()):
            print(f" {party}: {answers[statement_num].upper()}")

    def pick_key(self, key_name, key_list):
        max_num = len(key_list)
        picked_key = input(f"Vyber si {key_name.lower()} zadaním 1-{max_num}: ")
        try:
            if int(picked_key) not in range(1, max_num+1):
                print(f"Neexistujúce číslo pre {key_name.lower()}")
                self.pick_key(key_name, key_list)
            else:
                return int(picked_key)-1
        except ValueError:
            print("Zadaná hodnota nie je číslo.")
            self.pick_key(key_name, key_list)

# data = Data('vol_kal.csv')
# data.print_results_by_specific_statement()