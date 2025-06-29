import unittest
from unittest.mock import patch
import json
from user_input import SubmitError, UserInput
from Project_setup import ProjectSetupInfo, budget_calculation
import cost_input
import project_summary
import pytest

# class TestFileHandlingMethod(unittest.TestCase):
#   def test_save_to_json(self):
#     sample_data = ProjectSetupInfo(project_name="Ballan WTP", revenue=100000, margin=20,total_budget=80000,cost_codes={
#       'a': 50000,
#       'b': 20000,
#       'c': 10000
#     })
#     sample_data.save_to_file("test.json")
#     expected = {
#     "project_name": "Ballan WTP",
#     "revenue": 100000,
#     "margin": 20,
#     "total_budget": 80000,
#     "cost_codes": {
#         "a": 50000,
#         "b": 20000,
#         "c": 10000
#     }
# }
#     with open("test.json","r") as f:
#       result = json.load(f)
#     self.assertEqual(expected,result)

class TestUserInput(unittest.TestCase):
  @patch('builtins.input',side_effect = ['some texts', r'\submit', r'\q'])
  def test_get_input(self,mock_input):
    ui1 = UserInput("Enter something:")
    result1 = ui1.get_input()
    self.assertEqual(result1,'some texts')

    ui2 = UserInput("Enter input 2:")
    with self.assertRaises(SubmitError):
      ui2.get_input()

    ui3 = UserInput("Enter input 3:")
    with self.assertRaises(SystemExit):
      ui3.get_input()

class TestCalculation:

  @pytest.mark.parametrize("revenue, margin, expected",[
    (125473.43, 22, 97869.275),
    (540000, 22.55, 418230),
    (5245.46, 15, 4458.64)
    ])
  def test_budget_calculation(self,revenue, margin, expected):
    # revenue = 125473.43
    # margin = 22.00
    result = budget_calculation(revenue, margin)
    assert pytest.approx(result,rel=1e-2) == expected
   






  

