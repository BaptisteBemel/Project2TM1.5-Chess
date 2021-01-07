# -*- coding : utf-8 -*-
import unittest
from lib.classDir.pawn import Pawn


class TestFunctionsInClass(unittest.TestCase):

    def test_is_False(self):
        self.assertFalse(Pawn.move("a6"))


if __name__ == "__main__":
    unittest.main()