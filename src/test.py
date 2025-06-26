from user_input import SubmitError, UserInput
import Project_setup
import cost_input
import project_summary

class TestUserInput:

  def test_normal_input(self):
    user_input = UserInput("Testing prompt")
    assert user_input.get_input() == "Testing prompt"
  
  
