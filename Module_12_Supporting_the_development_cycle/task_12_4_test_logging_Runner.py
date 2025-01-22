import unittest
import logging
import task_12_4_Runner as Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            walk_tester = Runner.Runner('walk_tester', -1)
            for _ in range(10):
                walk_tester.walk()
            self.assertEqual(walk_tester.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)
            self.fail('Неверная скорость для Runner')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            run_tester = Runner.Runner(name=777)
            for _ in range(10):
                run_tester.run()
            self.assertEqual(run_tester.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
            self.fail('Неверный тип данных для объекта Runner')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run_tester_chall = Runner.Runner('run_tester_chall')
        walk_tester_chall = Runner.Runner('walk_tester_chall')
        for _ in range(10):
            run_tester_chall.run()
            walk_tester_chall.walk()
        self.assertNotEqual(run_tester_chall.distance, walk_tester_chall.distance)


if __name__ == '__main__':
    unittest.main()


