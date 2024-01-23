# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_eight_puzzle_node

import unittest
import time
from eight_puzzle_node import EightPuzzleNode


class TestEightPuzzleNode(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A EightPuzzleNode exists.
        """
        try:
            EightPuzzleNode(None, None, None, None)
        except NameError:
            self.fail("Could not instantiate EightPuzzleNode")

    """
    Properties
    """

    def test_state(self):
        """
        An EightPuzzleNode has a `state` property.
        """
        problem = EightPuzzleNode("Fake State", None, None, None)
        self.assertEqual("Fake State", problem.state)

    def test_parent(self):
        """
        An EightPuzzleNode has a `parent` property.
        """
        problem = EightPuzzleNode(None, "Fake Parent Node", None, None)
        self.assertEqual("Fake Parent Node", problem.parent)

    def test_action(self):
        """
        An EightPuzzleNode has a `action` property.
        """
        problem = EightPuzzleNode(None, None, "Fake Action", None)
        self.assertEqual("Fake Action", problem.action)

    def test_path_cost(self):
        """
        An EightPuzzleNode has a `path_cost` property.
        """
        problem = EightPuzzleNode(None, None, None, "Fake Path Cost")
        self.assertEqual("Fake Path Cost", problem.path_cost)

def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
