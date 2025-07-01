import json
from tabulate import tabulate
from user_input import UserInput, SubmitError

def budget_calculation(revenue, margin):
  budget = revenue*(1-margin/100)
  return budget

class ProjectSetupInfo:
  def __init__(self, project_name, revenue, margin, total_budget, cost_codes):
    self.project_name = project_name
    self.revenue = revenue
    self.margin = margin
    self.total_budget = total_budget
    self.cost_codes = cost_codes

  @classmethod
  def project_input(cls):
    print(f"Please fill below information to set up project.") 
    project_name_input = UserInput("Project name:")
    project_name = project_name_input.get_input()
    revenue_input = UserInput("Revenue ($):")
    revenue = revenue_input.get_num()
    margin_input = UserInput("Margin (%):") 
    margin = margin_input.get_num()
    total_budget=budget_calculation(revenue, margin)
    print(f"Project total budget is:{total_budget:.2f}")

    cost_codes = {}
    total_allocated_cost = 0
    print("Please enter cost codes and allocated cost.")
    while True:
      try:
        code_input = UserInput(f"Code name (Enter code name to add or enter {r'\submit'} to submit cost allocation.):")
        code_name = code_input.get_input().lower()
      except SubmitError:
        total_allocated_cost = sum(cost_codes.values())
        if (total_allocated_cost - total_budget) > 0.1: 
          print(f"Total allocated cost exceeds total budget by ${(total_allocated_cost-total_budget):.2f}. Allocated costs have to be equal to project budget. Please try again!")
          continue
        elif (total_budget-total_allocated_cost) > 0.1: 
          print(f"There is remaining ${(total_budget - total_allocated_cost):.2f} has not been allocated. Please allocate the remaining amount.")
          continue
        else:
          print("Cost Allocation successful!")
          break
      
      code_value_input = UserInput(f"Allocate budget for cost code '{code_name}'($):")
      code_value = code_value_input.get_num()
      print(f"{code_name}: {code_value}")
      cost_codes[code_name]=code_value
    return cls(project_name, revenue, margin, total_budget, cost_codes)
  
  def display(self): 
    cost_code_display = ""
    for key, value in self.cost_codes.items():
      cost_code_display += key + ': ' + str(value) + "\n"
    print(tabulate([["Project Name",self.project_name],["Revenue",f"${self.revenue}"],["Margin",f"{(self.margin):.2f}%"],["Total Budget",f"${self.total_budget:.2f}"],["Cost Allocation",f"{cost_code_display}"]],tablefmt="rounded_grid"))

  def save_to_file(self,filename):
    with open(filename,"w") as f:
      json.dump(self.__dict__, f, indent=4)

  @classmethod
  def load_from_file(cls,filename):
    with open(filename,'r') as f:
      data = json.load(f)
    return cls(**data)
  
