import unittest
import task_12_1_Runner as Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walk_tester = Runner.Runner('walk_tester')
        for _ in range(10):
            walk_tester.walk()
        self.assertEqual(walk_tester.distance, 50)

    def test_run(self):
        run_tester = Runner.Runner('run_tester')
        for _ in range(10):
            run_tester.run()
        self.assertEqual(run_tester.distance, 100)

    def test_challenge(self):
        run_tester_chall = Runner.Runner('run_tester_chall')
        walk_tester_chall = Runner.Runner('walk_tester_chall')
        for _ in range(10):
            run_tester_chall.run()
            walk_tester_chall.walk()
        self.assertNotEqual(run_tester_chall.distance, walk_tester_chall.distance)


if __name__ == '__main__':
    unittest.main()
