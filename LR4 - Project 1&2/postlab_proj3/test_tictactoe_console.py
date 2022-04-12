import unittest
import oxo_args_ui
import oxo_logic

class MainTester(unittest.TestCase):
    def test_startGame(self):
        result = oxo_args_ui.startGame()
        self.assertEqual(result, oxo_logic.newGame())
    def test_resumeGame(self):
        result = oxo_args_ui.resumeGame()
        self.assertEqual(result, oxo_logic.restoreGame())
    def test_executeChoice(self):
        result = oxo_args_ui.displayHelp()
        self.assertEqual(result, oxo_args_ui.executeChoice(3))
        
if __name__ == '__main__':
    unittest.main()