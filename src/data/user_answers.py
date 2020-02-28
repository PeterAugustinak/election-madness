from src.data.data_lists import Data


class UserAnswers:

    user_chart = {}

    def __init__(self):
        self.data = Data('vol_kal.csv')
        self.statements = self.data.list_of_statements()
        self.parties = self.data.list_of_parties()
        self.list_of_answers = self.data.list_of_anwsers()

    def initialize_questionnaire(self, current_statement_position=0):
        statement = self._get_statement_or_end(self.statements, current_statement_position)
        if statement:
            counter = self._get_counter(current_statement_position, len(self.statements))
            user_answer = self._get_user_answer(statement, counter)
            self._evaluate_user_answer(user_answer, current_statement_position)
        else:
            self._evaluate_results()

    @staticmethod
    def _get_statement_or_end(statement, current_statement):
        try:
            statement = statement[current_statement]
        except IndexError:
            statement = False
        return statement

    def _evaluate_results(self):
        sorted_user_chart = {party: score for party, score in sorted(self.user_chart.items(),
                                                                     key=lambda item: item[1], reverse=True)}
        print()
        print("FINÁLNE PORADIE A POCEČET ZHODNÝCH ODPOVEDÍ:")
        for rank, (party, score) in enumerate(sorted_user_chart.items(), start=1):
            print(f" {rank}. {party} [{score}]")

    @classmethod
    def _get_counter(cls, current_statement, total_statements):
        current_statement_number = current_statement + 1
        return f"{current_statement_number}/{total_statements}"

    @classmethod
    def _get_user_answer(cls, statement, counter):
        user_answer = input(f"{counter} {statement} (a/n/0): ")
        return cls._translate_answer(user_answer)

    @classmethod
    def _translate_answer(cls, user_answer):
        if user_answer == 'a': return 'Áno'
        if user_answer == 'n': return'Nie'
        if user_answer == '0': return'-'
        else:
            print(' Odpovedaj a, n, alebo 0.')
            return False

    def _evaluate_user_answer(self, user_answer, current_statement_position):
        if user_answer:
            self._compare_answer(current_statement_position, user_answer)
            current_statement_position += 1
            self.initialize_questionnaire(current_statement_position)
        else:
            self.initialize_questionnaire(current_statement_position)

    def _compare_answer(self, current_statement, user_answer):
        match_lst = []
        for party, party_answers in zip(self.parties, self.list_of_answers):
            if user_answer == party_answers[current_statement]:
                match_lst.append(party)
        priority_point = self._evaluate_priority_for_current_statement()
        self._add_points_for_party(match_lst, priority_point)

        print(f" ZHODA: {match_lst}")
        print()

    def _add_points_for_party(self, match_lst, priority_point):
        for party in match_lst:
            try:
                self.user_chart[party] += (1 + priority_point)
            except KeyError:
                self.user_chart[party] = (1 + priority_point)

    @classmethod
    def _evaluate_priority_for_current_statement(cls):
        priority = input(" Ako dôležitá je pre vás táto otázka? (1 - menej, 2 - štandardne, 3 - viac): ")
        return cls._evaluate_priority_answer(priority)

    @classmethod
    def _evaluate_priority_answer(cls, priority):
        if priority == '3': return 0.5
        if priority == '2': return 0.0
        if priority == '1': return -0.5
        else:
            print('  Odpovedaj 1, 2, alebo 3.')
            return cls._evaluate_priority_for_current_statement()


user = UserAnswers()
user.initialize_questionnaire()






