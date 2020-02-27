from src.data.data_lists import Data


class UserAnswers:

    def __init__(self):
        self.data = Data('vol_kal.csv')

    def ask(self, current_statement=0):
        statement = self.data.list_of_statements()[current_statement]
        print()
        user_answer = input(f"{statement} (a / n / 0): ")
        user_answer = self.translate_answer(user_answer)
        if user_answer:
            self.compare_answer(current_statement, user_answer)
            current_statement += 1
            self.ask(current_statement)
        else:
            self.ask(current_statement)

    def translate_answer(self, user_answer):
        if user_answer == 'a': return 'Áno'
        if user_answer == 'n': return'Nie'
        if user_answer == '0': return'-'
        else:
            print('Odpovedaj a, n, alebo 0.')
            return False

    def compare_answer(self, current_statement, user_answer):
        for party, party_answers in zip(self.data.list_of_parties(), self.data.list_of_anwsers()):
            if user_answer == party_answers[current_statement]:
                print(f"{party}: {party_answers[current_statement]} -> ZHODA")
            else:
                print(f"{party}: {party_answers[current_statement]} -> ROZDIEL")


user = UserAnswers()
user.ask()






