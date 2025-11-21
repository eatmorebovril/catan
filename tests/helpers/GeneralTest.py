import unittest
from helpers.General import snakeToCamelCase

class TestGeneralHelpers(unittest.TestCase):
    def test_snake_to_camel_case(self):
        self.assertEqual(snakeToCamelCase("test_remove_resource_from_hand"), "testRemoveResourceFromHand")
        self.assertEqual(snakeToCamelCase("another_example_here"), "anotherExampleHere")
        self.assertEqual(snakeToCamelCase("singleword"), "singleword")
        self.assertEqual(snakeToCamelCase(""), "")
        self.assertEqual(snakeToCamelCase("_leading_underscore"), "LeadingUnderscore")
        self.assertEqual(snakeToCamelCase("trailing_underscore_"), "trailingUnderscore")
        self.assertEqual(snakeToCamelCase("_both_ends_"), "BothEnds")

if __name__ == "__main__":
    unittest.main()
