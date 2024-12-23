import unittest
import task_12_1_Runner as Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        self.walk_tester = Runner.Runner('walk_tester')
        for _ in range(10):
            self.walk_tester.walk()
        self.assertEqual(self.walk_tester.distance, 50)

    def test_run(self):
        self.run_tester = Runner.Runner('run_tester')
        for _ in range(10):
            self.run_tester.run()
        self.assertEqual(self.run_tester.distance, 100)

    def test_challenge(self):
        self.run_tester_chall = Runner.Runner('run_tester_chall')
        self.walk_tester_chall = Runner.Runner('walk_tester_chall')
        for _ in range(10):
            self.run_tester_chall.run()
            self.walk_tester_chall.walk()
        self.assertNotEqual(self.run_tester_chall.distance, self.walk_tester_chall.distance)


RunnerTest()
