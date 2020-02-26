import csv

parties = []
questions = []
answers_lst = []


class Data:

    def __init__(self, file):
        self.source = f'..\..\{file}'
        self._csv_reader(self.source)

    @classmethod
    def _csv_reader(cls, source):
        with open(source, encoding='utf-8') as csv_file:
            source_file = csv.reader(csv_file, delimiter=',')
            cls._fill_lists(source_file)

    @classmethod
    def _fill_lists(cls, source_file):
        line_count = 0
        for row in source_file:
            if line_count == 0:
                parties.append(row)
                line_count += 1
            else:
                questions.append(row[0])
                answers_lst.append(row[1:])
                line_count += 1

    def print_by_party(self):
        for party, answers in zip(parties[0], answers_lst):
            print(party.upper())
            for question, answer in zip(questions, answers):
                print(f"{question}: {answer}")

    def print_by_question(self):
        for question, answers in zip(questions, answers_lst):
            print(question.upper())
            for party, answer in zip(parties[0], answers):
                print(f"{party}: {answer}")
            print()

csv_reader('vol_kal.csv')
print_by_question()
