import sys
from datetime import datetime

class SubmitError(Exception):
  pass

class NegativeNumberError(Exception):
  pass
class UserInput:
  def __init__(self,prompt):
    self.prompt = prompt

  def get_input(self):
    input_value = input(self.prompt).strip()
    if input_value == r"\q":
      sys.exit("Application closed, see you next time!")
    elif input_value == r"\submit":
      raise SubmitError
    return input_value

  def get_num(self): 
    while True:
      user_input = self.get_input().strip()
      if '%' in user_input:
        user_input=user_input.replace('%','')
      
      try: 
        result = float(user_input)
        if result <= 0:
          raise NegativeNumberError
        return result
      except ValueError:
        print("That is not a number, please try again")
      except NegativeNumberError:
        print("Number input must be greater than 0, please try again")
  
  def get_date(self):
    while True:
      self.prompt = "Date (DD/MM/YYYY):"
      date_str = str(self.get_input()).strip()
      try:
        dt = datetime.strptime(date_str,"%d/%m/%Y")
        formatted_date = dt.strftime("%A, %d %B %Y")
        return formatted_date
      except ValueError:
        print("Incorrect date format or invalid date entries, please try again!")

