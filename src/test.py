import unittest
import json
from user_input import SubmitError, UserInput
from Project_setup import ProjectSetupInfo
import cost_input
import project_summary

class TestFileHandlingMethod(unittest.TestCase):
  def test_save_to_json(self):
    sample_data = ProjectSetupInfo(project_name="Ballan WTP", revenue=100000, margin=20,total_budget=80000,cost_codes={
      'a': 50000,
      'b': 20000,
      'c': 10000
    })
    sample_data.save_to_file("test.json")
    expected = {
    "project_name": "Ballan WTP",
    "revenue": 100000,
    "margin": 20,
    "total_budget": 80000,
    "cost_codes": {
        "a": 50000,
        "b": 20000,
        "c": 10000
    }
}
    with open("test.json","r") as f:
      result = json.load(f)
    self.assertEqual(expected,result)

if __name__ == '__main__':
  unittest.main()

  

