import unittest
from machinetranslation import translator

class TestLanguageTranslator(unittest.TestCase):
    def test_null_input_frenchToEnglish(self):
        self.assertRaises(ValueError, translator.frenchToEnglish, None)
    
    def test_null_input_englishToFrench(self):
        self.assertRaises(ValueError, translator.englishToFrench, None)

    def test_english_to_french_hello(self):
        self.assertEqual(translator.englishToFrench("Hello"), "Bonjour")

    def test_french_to_english_bonjour(self):
        self.assertEqual(translator.frenchToEnglish("Bonjour"), "Hello")


unittest.main()