import unittest

import calculation


class CalTest(unittest.TestCase):
    def test_add_num_and_double(self):
        cal = calculation.Cal()
        self.assertEqual(cal.add_num_and_double(1, 1), 4)
        
        """
        assertEqual(a, b)   a == b
        assertNotEqual(a, b)   a != b
        assertTrue(x)   bool(x) is True
        assertFalse(x)   bool(x) is False
        assertIs(a, b)   a is b
        assertIsNot(a, b)   a is not b
        assertIsNone(x)   x is None
        assertIsNotNone(x)   x is not None
        assertIn(a, b)   a in b
        assertNotIn(a, b)   a not in b
        assertIsInstance(a, b)   isinstance(a, b)
        assertNotIsInstance(a, b)   not isinstance(a, b)
        """
        
if __name__ == '__main__':
    unittest.main()