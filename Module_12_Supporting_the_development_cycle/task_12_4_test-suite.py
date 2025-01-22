import unittest
import logging
import task_12_4_test_logging_Runner as testRunner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')

runnerST = unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(testRunner.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerST)
