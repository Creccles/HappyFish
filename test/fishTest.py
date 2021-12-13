import unittest
from src import HappyFishes

class main(unittest.TestCase):

    fish = HappyFishes()




    def hand_score_test(self):
        self.assertEqual(["C5", "S5", "H5", "D5"], self.fish.hand_score(["C5", "S5", "H5", "D5"]))

    def empty_hand_test(self):
        self.assertEqual(0, self.fish.empty_hand([]))












def main():
    unittest.main()


if __name__ == '__main__':
    unittest.main()


