import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        """Test simple word palindromes"""
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("refer"))

    def test_phrase_palindromes(self):
        """Test phrase palindromes with spaces, punctuation and mixed case"""
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("Anita lava la tina"))
        self.assertTrue(is_palindrome("Madam, I'm Adam"))

    def test_non_palindromes(self):
        """Test non-palindromes"""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("This is not a palindrome"))
        self.assertFalse(is_palindrome("race a car"))
        self.assertFalse(is_palindrome("programming"))

    def test_edge_cases(self):
        """Test edge cases like empty strings and single characters"""
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("A"))
        self.assertTrue(is_palindrome(" "))
        self.assertTrue(is_palindrome(".,?!"))

if __name__ == '__main__':
    unittest.main()