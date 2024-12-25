import unittest
import task_12_2_Runner as Runner


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner.Runner('Усэйн', 10)
        self.runner_2 = Runner.Runner('Андрей', 9)
        self.runner_3 = Runner.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for tournament in cls.all_results:
            print(cls.all_results[tournament])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        self.tournament_1 = Runner.Tournament(90, self.runner_1, self.runner_3)
        name_tournament = 'tournament_1'
        result_tournament = self.tournament_1.start()
        for place in result_tournament:
            result_tournament[place] = result_tournament[place].name
        self.all_results[name_tournament] = result_tournament
        last_place_runner = result_tournament[max(result_tournament)]
        self.assertTrue(last_place_runner == self.runner_3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        self.tournament_2 = Runner.Tournament(90, self.runner_2, self.runner_3)
        name_tournament = 'tournament_2'
        result_tournament = self.tournament_2.start()
        for place in result_tournament:
            result_tournament[place] = result_tournament[place].name
        self.all_results[name_tournament] = result_tournament
        last_place_runner = result_tournament[max(result_tournament)]
        self.assertTrue(last_place_runner == self.runner_3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        self.tournament_3 = Runner.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        name_tournament = 'tournament_3'
        result_tournament = self.tournament_3.start()
        for place in result_tournament:
            result_tournament[place] = result_tournament[place].name
        self.all_results[name_tournament] = result_tournament
        last_place_runner = result_tournament[max(result_tournament)]
        self.assertTrue(last_place_runner == self.runner_3.name)


if __name__ == '__main__':
    unittest.main()

