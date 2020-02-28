# local library import
from src.helpers.clear_screen import clear_screen
from src.data.data_lists import Data

class Questionnaire:
    """Questionnaire for asking and evaluating user answers for statements."""

    user_chart = {}

    def __init__(self):
        self.data = Data()
        self.statements = self.data.list_of_statements()
        self.parties = self.data.list_of_parties()
        self.list_of_answers = self.data.list_of_anwsers()

    def initialize(self, current_statement_position=0):
        """Start of questionnaire."""
        if current_statement_position == 0:
            self._questionnaire_description()
        print()
        statement = self._get_statement_or_end(self.statements, current_statement_position)
        if statement:
            counter = self._get_counter(current_statement_position, len(self.statements))
            user_answer = self._get_user_answer(statement, counter)
            self._evaluate_user_answer(user_answer, current_statement_position)
        else:
            self._evaluate_results()

    def _questionnaire_description(self):
        print()
        print("Tento dotaznk by ti mal pomôcť pri tvojom rozhodovaní sa koho voliť.")
        print(f"- celkovo obsahuje {self.data.len_of_statements()} otázok")
        print("- na každú otázku je potrebné odpovedať:")
        print("    - a -> súhlasím s tvrdením")
        print("    - n -> nesúhlasím s tvrdením")
        print("    - 0 -> neviem/nechcem odpovedať")
        print("- po každej otázke je potrebné zadať aj osobnú prioritu (váhu) tvrdenia:")
        print("    - 1 -> tvrdenie je pre mňa menej prioritné")
        print("    - 2 -> tvrdenie má pre mňa štandardnú prioritu")
        print("    - 3 -> tvrdenie má pre mňa vyššiu prioritu")
        print("Na konci získaš presné poradie strán, ktoré bude vypočítané na základe počtu zhôd v jednotlivých "
              "tvrdeniach zahŕňajúc osobnú prioritu tvrdení.")
        print()
        input("Stlač ENTER pre štart testu! ...")

    @staticmethod
    def _get_statement_or_end(statement, current_statement):
        try:
            statement = statement[current_statement]
        except IndexError:
            statement = False
        return statement

    def _evaluate_results(self):
        clear_screen()
        self._evaluation_joke()
        sorted_user_chart = {party: results for party, results in sorted(self.user_chart.items(),
                                                                         key=lambda item: item[1][1], reverse=True)}
        print()
        print("FINÁLNE PORADIE: STRANA  [POČET ZHODNÝCH ODPOVEDÍ / CELKOVÉ SKÓRE:")
        for rank, (party, results) in enumerate(sorted_user_chart.items(), start=1):
            # results[0] - total matches, results[1] - total score
            print(f" {rank}. {party} [{results[0]} / {results[1]}]")

    @classmethod
    def _evaluation_joke(cls):
        print()
        print("Toto bola posledná otázka. Tvoj rebríček je spracovaný!")
        print("Ak sa chceš dozvedieť výsledky, pošli sumu 10,- EUR na číslo účtu ...")
        print('.')
        print('.')
        input("To bol len vtip :) Pre zobrazenie výsledkov stlač ENTER!")

    @classmethod
    def _get_counter(cls, current_statement, total_statements):
        current_statement_number = current_statement + 1
        return f"[{current_statement_number}/{total_statements}]"

    @classmethod
    def _get_user_answer(cls, statement, counter):
        user_answer = input(f"{counter} {statement} (a/n/0): ")
        return cls._translate_answer(user_answer)

    @classmethod
    def _translate_answer(cls, user_answer):
        if user_answer == 'a': return 'Áno'
        if user_answer == 'n': return 'Nie'
        if user_answer == '0': return '-'
        else:
            print(' Odpovedaj a, n, alebo 0.')
            return False

    def _evaluate_user_answer(self, user_answer, current_statement_position):
        if user_answer:
            self._compare_answer(current_statement_position, user_answer)
            current_statement_position += 1
            self.initialize(current_statement_position)
        else:
            self.initialize(current_statement_position)

    def _compare_answer(self, current_statement, user_answer):
        match_lst = []
        for party, party_answers in zip(self.parties, self.list_of_answers):
            if user_answer == party_answers[current_statement]:
                match_lst.append(party)
        priority_point = self._evaluate_priority_for_current_statement()
        self._add_points_for_party(match_lst, priority_point)

        print(f" ZHODA: {', '.join(match_lst)}")

    def _add_points_for_party(self, match_lst, priority_point):
        for party in match_lst:
            try:
                # adding point to total matches
                self.user_chart[party][0] += 1
                # adding point to total points
                self.user_chart[party][1] += (1 + priority_point)
            except KeyError:
                # creating dict item: party: [total matches, total points]
                self.user_chart[party] = [1, (1 + priority_point)]

    @classmethod
    def _evaluate_priority_for_current_statement(cls):
        priority = input(" Ako dôležitá je pre vás táto otázka? (1/2/3): ")
        return cls._evaluate_priority_answer(priority)

    @classmethod
    def _evaluate_priority_answer(cls, priority):
        if priority == '3': return 0.5
        if priority == '2': return 0.0
        if priority == '1': return -0.5
        else:
            print('  Odpovedaj 1, 2, alebo 3.')
            return cls._evaluate_priority_for_current_statement()
