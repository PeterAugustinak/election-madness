import csv
from collections import defaultdict


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

    def list_of_parties(self):
        for parties in self.parties_dict:
            return [party for party in parties][1:]

    def list_of_statements(self):
        for statements in self.statements_dict:
            return [statement for statement in statements]

    def list_of_anwsers(self):
        for answers_lst in self.answers_lst_dict:
            return [answers_lst for answers_lst in answers_lst][1:]

    def print_list_of_parties(self):
        for num, party in enumerate(self.list_of_parties(), start=1):
            if party:
                print(f"{num}. {party}")

    def print_list_of_statements(self):
        for num, statement in enumerate(self.list_of_statements(), start=1):
            print(f"{num}. {statement}")



    #
    # def print_results_by_parties(self):
    #     for party, answers in zip(parties[0], answers_lst):
    #         print(party.upper())
    #         for question, answer in zip(statements, answers):
    #             print(f"{question}: {answer}")
    #
    # def print_results_by_specific_party(self):
    #     self.print_list_of_parties()
    #     party_num = self.pick_party()-1
    #     party = self.list_of_parties()[party_num]
    #     print(party.upper())
    #     print(self.list_of_anwsers())
    #     for statement, answer in zip(self.list_of_statements(), self.list_of_anwsers()[party_num]):
    #         print(f"{statement}: {answer}")
    #
    # def pick_party(self):
    #     picked_party = input("Vyber si stranu zadaním 1-25: ")
    #     try:
    #         if int(picked_party) not in range(1, 21):
    #             print("Neexistujúce číslo strany")
    #             self.pick_party()
    #         else:
    #             print(int(picked_party))
    #             return int(picked_party)
    #     except ValueError:
    #         print("Zadaná hodnota nie je číslo.")
    #         self.pick_party()
    #
    # def print_results_by_statement(self):
    #     for question, answers in zip(statements, answers_lst):
    #         print(question.upper())
    #         for party, answer in zip(parties[0], answers):
    #             print(f"{party}: {answer}")
    #         print()


