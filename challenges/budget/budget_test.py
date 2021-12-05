from classes.budget import Budget
import unittest


class TestBudget(unittest.TestCase):

    def test_return_type(self):
        received = Budget('December')
        self.assertIsInstance(received, Budget)


if __name__ == '__main__':
    unittest.main()
