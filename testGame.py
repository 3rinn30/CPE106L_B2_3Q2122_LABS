import unittest
import mainGame
import temporaryBoard

class MainTester(unittest.TestCase):
    def test_board(self):
        result = temporaryBoard.display(temporaryBoard.boardFill)
        self.assertEqual(result, mainGame.initialBoard())

if __name__ == '__main__':
    unittest.main()

    

