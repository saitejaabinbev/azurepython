
import unittest
import os
import json

class TestStringMethods(unittest.TestCase):

    def test_Sample(self):
        
      print("Execution for Azure Devops")
      f = open('config.json',)
      data = json.load(f)
      username = data['username']
      password = data['password']
      print("username : ",username)
      print("Password : ",password)
      print("Data : ",data)
      print(os.environ.get("h"))
      self.assertEqual("1","1","Values not as per expectation @@")
if __name__ == "__main__":
    unittest.main()
