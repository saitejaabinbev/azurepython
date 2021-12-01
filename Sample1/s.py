
import unittest
import os

class TestStringMethods(unittest.TestCase):

    def test_Sample(self):
      print("Execution for Azure Devops")
      print(os.environ.get("h"))
      self.assertEqual("1","1","Values not as per expectation @@")
if __name__ == "__main__":
    unittest.main()
