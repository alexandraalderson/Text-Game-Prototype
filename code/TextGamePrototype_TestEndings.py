# ================================================================
# HOW TO RUN THESE TESTS
# ================================================================
# ▶ Option 1 – Jupyter / Colab
#    1. Clone the repo inside your notebook:
#         !git clone https://github.com/alexandraalderson/Prototype-Text-Game.git
#    2. Change into the code folder:
#         %cd Prototype-Text-Game/code
#    3. Run this file:
#         !python PrototypeTextGame_TestEndings.py
#
# ▶ Option 2 – Standard .py file from a terminal/IDE
#    1. Save this file as PrototypeTextGame_TestEndings.py
#       in the same folder as PrototypeTextGame.py:
#
#         Prototype-Text-Game/
#            code/
#               PrototypeTextGame.py
#               PrototypeTextGame_TestEndings.py
#
#    2. From a terminal:
#         cd Prototype-Text-Game/code
#         python PrototypeTextGame_TestEndings.py
#
#    This runs all unittests without using any notebook magic.
#
#    (Inside the code below, unittest.main(argv=[''], exit=False)
#     lets tests run in notebooks without stopping the kernel.
#     If running as a normal script you can simply use unittest.main().)
# ================================================================

# TESTS FOR ALL ENDINGS of Prototype Text Game
# --------------------------------------------------
# These tests automatically run the text adventure using Python's unittest framework,
# feeding in pre-set choices and checking that the expected ending text appears.

#Use !wget to fetch the raw file from GitHub
#This downloads the file into the notebook’s current working directory so Python can import it.
!git clone https://github.com/alexandraalderson/Prototype-Text-Game.git - comment out if you are running it from a terminal/IDE
# %cd Prototype-Text-Game/code

#Import Prototype Text Game
import unittest
from unittest.mock import patch
from io import StringIO
from PrototypeTextGame import start_game


# ========== TEST FOR ENDING 1 (SUCCESS) ==========
class TestPrototypeGame_End1(unittest.TestCase):
    def test_success_path(self):
        test_inputs = ['1', '1', '1', '']   # extra '' for final input()
        expected_text = "SUCCESS!"
        with patch('builtins.input', side_effect=test_inputs):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                start_game()
                output = fake_out.getvalue()
        self.assertIn(expected_text, output)


# ========== TEST FOR ENDING 2 ==========
class TestPrototypeGame_End2(unittest.TestCase):
    def test_end2_path(self):
        test_inputs = ['1', '1', '2', '']
        expected_text = "FAILURE."
        with patch('builtins.input', side_effect=test_inputs):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                start_game()
                output = fake_out.getvalue()
        self.assertIn(expected_text, output)


# ========== TEST FOR ENDING 3 ==========
class TestPrototypeGame_End3(unittest.TestCase):
    def test_end3_path(self):
        test_inputs = ['1', '2', '1', '']
        expected_text = "FAILURE."
        with patch('builtins.input', side_effect=test_inputs):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                start_game()
                output = fake_out.getvalue()
        self.assertIn(expected_text, output)


# ========== TEST FOR ENDING 4 ==========
class TestPrototypeGame_End4(unittest.TestCase):
    def test_end4_path(self):
        test_inputs = ['1', '2', '2', '']
        expected_text = "FAILURE."
        with patch('builtins.input', side_effect=test_inputs):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                start_game()
                output = fake_out.getvalue()
        self.assertIn(expected_text, output)


# ========== TEST FOR ENDING 5 ==========
class TestPrototypeGame_End5(unittest.TestCase):
    def test_end5_path(self):
        test_inputs = ['2', '1', '']
        expected_text = "FAILURE."
        with patch('builtins.input', side_effect=test_inputs):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                start_game()
                output = fake_out.getvalue()
        self.assertIn(expected_text, output)


# ========== TEST FOR ENDING 6 ==========
class TestPrototypeGame_End6(unittest.TestCase):
    def test_end6_path(self):
        test_inputs = ['2', '2', '2', '']
        expected_text = "FAILURE."
        with patch('builtins.input', side_effect=test_inputs):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                start_game()
                output = fake_out.getvalue()
        self.assertIn(expected_text, output)


if __name__ == "__main__":
    unittest.main()
