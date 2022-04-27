
import unittest
import io
import sys
import os

from unittest.mock import patch
from pathlib import Path

import Hangman
from Player import Player

class TestHangman(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('\nsetupClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')

    def tearDown(self):
        testFile = Path("." + "/" + "players" + "/" + "findPlayerCreateFile" + ".txt")

        if os.path.exists(testFile):
            print('testFile Removed')
            os.remove(testFile)  
        print('tearDown\n')

    def test_PrintBoard(self):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        Hangman.displayBoard('','','secret')            # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.

        test = '''\n    +---+\n        |\n        |\n        |\n       ===''' + "\n" + "\nMissed letters: \n" + '_ _ _ _ _ _ ' + '\n'
        
        self.assertEqual(capturedOutput.getvalue(), test)
                    
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        Hangman.displayBoard('c','r','secret')          # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        
        test = '''\n    +---+\n    O   |\n        |\n        |\n       ===''' + "\n" + "\nMissed letters: c \n" + '_ _ _ r _ _ ' + '\n'
        
        self.assertEqual(capturedOutput.getvalue(), test)
    
    @patch('builtins.input', side_effect=['wq', 'a', '1', 'e'])
    def test_MakeGuess(self, mock_input):
        
        self.assertEqual(Hangman.getGuess('ac'), 'e')

    @patch('builtins.input', side_effect=['y', 't'])
    def test_PlayAgain(self, mock_input):

        self.assertTrue(Hangman.playAgain())
        self.assertFalse(Hangman.playAgain())

    def test_RandomWord(self):
        test_list = 'bacon potato cheese'
        test = Hangman.getRandomWord(test_list)
        self.assertIn(test, test_list)
    
    #@patch('builtins.input', side_effect=['n', 'Jake','s', 'e', 'c', 'r', 't', 'n'])
    #def test_MainDriver(self, mock_input):
    #    Hangman.main('secret')

    def test_findPlayerDefault(self):
        test = Hangman.findPlayer("")
        default = Player()

        self.assertEqual(test.name, "Player")
        self.assertEqual(default.name, "Player")

    def test_findPlayerCreateFile(self):
        testFile = Path("." + "/" + "players" + "/" + "findPlayerCreateFile" + ".txt")
        if os.path.exists(testFile):
            os.remove(testFile)
        testPlayer = Hangman.findPlayer("findPlayerCreateFile")

        assert os.path.isfile(testFile)
        self.assertEqual(testPlayer.name, "findPlayerCreateFile")
        self.assertEqual(testPlayer.score, 0)

    def test_findPlayerExistFile(self):
        testFile = Path("." + "/" + "players" + "/" + "findPlayerCreateFile" + ".txt")

        testPlayer = Hangman.findPlayer("findPlayerCreateFile")

        assert os.path.isfile(testFile)

        testPlayer = Hangman.findPlayer("findPlayerCreateFile")

        self.assertEqual(testPlayer.name, "findPlayerCreateFile")
        self.assertEqual(testPlayer.score, 0)
        
    def test_updateScoreToClass(self):
        testFile = Path("." + "/" + "players" + "/" + "findPlayerCreateFile" + ".txt")

        testPlayer = Hangman.findPlayer("findPlayerCreateFile")
        assert os.path.isfile(testFile)

        testPlayer.score = 22
        
        self.assertEqual(testPlayer.name, "findPlayerCreateFile")
        self.assertEqual(testPlayer.score, 22)

        testPlayer.updateScore()

        self.assertEqual(testPlayer.score, 23)
  
    def test_updateScoreToFile(self):
        testFile = Path("." + "/" + "players" + "/" + "findPlayerCreateFile" + ".txt")

        testPlayer = Hangman.findPlayer("findPlayerCreateFile")
        assert os.path.isfile(testFile)

        self.assertEqual(testPlayer.score, 0)

        testPlayer.updateScore()

        self.assertEqual(testPlayer.name, "findPlayerCreateFile")
        self.assertEqual(testPlayer.score, 1)


