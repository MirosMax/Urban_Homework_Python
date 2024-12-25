import unittest
import task_12_2_test_Runner as testTournament
import task_12_1_test_Runner as testRunner

runnerST = unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(testTournament.TournamentTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(testRunner.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerST)