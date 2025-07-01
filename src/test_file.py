import unittest
from unittest.mock import patch
import json
from user_input import SubmitError, UserInput, NegativeNumberError
from Project_setup import ProjectSetupInfo, budget_calculation
from cost_input import CostInfo
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
  def test_get_input(self, mock_input):
    ui1 = UserInput("Enter something:")
    result1 = ui1.get_input()
    self.assertEqual(result1,'some texts')

    ui2 = UserInput("Enter input 2:")
    with self.assertRaises(SubmitError):
      ui2.get_input()

    ui3 = UserInput("Enter input 3:")
    with self.assertRaises(SystemExit):
      ui3.get_input()

  @patch('builtins.print')
  @patch('builtins.input', side_effect = ['a','-5','0','20%','34.5'])
  def test_get_num(self,mock_input,mock_print):
    ui1 = UserInput("Enter number:")
    with self.assertRaises(ValueError):
      ui1.get_num()
   
    ui2 = UserInput("Enter number:")
    with self.assertRaises(NegativeNumberError):
      ui2.get_num()

    ui3 = UserInput("Enter number:")
    with self.assertRaises(NegativeNumberError):
      ui3.get_num()  

    ui4 = UserInput("Enter number:")
    result4 = ui4.get_num()
    self.assertEqual(result4,20)

    ui5 = UserInput("Enter number:")
    result5 = ui5.get_num()
    self.assertEqual(result5,34.5)

    calls = ["That is not a number, please try again","Number input must be greater than 0, please try again", "Number input must be greater than 0, please try again"]
    mock_print.assert_has_calls(calls, any_order=False)

  @patch('builtins.print')
  @patch('builtins.input',side_effect = ['24/6/25', 'a/b/25', '24/25/2012','24/06/2025'])
  def test_get_date(self, mock_input, mock_print):
    ui = UserInput('')
    result = ui.get_date()
    self.assertEqual(result,'Tuesday, 24 June 2025')
    mock_print.asssert_has_calls("Incorrect date format or invalid date entries, please try again!")

class TestCalculation:

  @pytest.mark.parametrize("revenue, margin, expected",[
    (125473.43, 22, 97869.275),
    (100000, 20, 80000),
    (60000, 100, 0)
    ])
  def test_budget_calculation(self,revenue, margin, expected):
    result = budget_calculation(revenue, margin)
    assert pytest.approx(result,rel=1e-2) == expected
   
class TestLastIndexReadingCsv:

  def test_csv_with_data(self):
    result = CostInfo.last_index("../data/test1.csv")
    assert result == 2

  def test_csv_without_data(self):
     result = CostInfo.last_index("../data/test2.csv")
     assert result == 0
  





  

