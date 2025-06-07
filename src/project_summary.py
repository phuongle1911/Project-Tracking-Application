from tabulate import tabulate
from datetime import date
from Project_setup import ProjectSetupInfo
from cost_input import CostInfo


def summary_generate():

  #Load and display project info
  loaded_project_info = ProjectSetupInfo.load_from_file("../data/project.json")
  total_budget = float(loaded_project_info.total_budget)
  cost_codes = loaded_project_info.cost_codes
  loaded_project_info.display()

  #Extract incurred cost data
  cost_table = CostInfo.read_csvfile("../data/incurred_cost.csv")

  #Budget summary
  budget_summary = []
  total_remaining_budget = 0

  for code,value in cost_codes.items():
    value = float(value)
    cost_code_summary = {}
    cost_code_summary["Cost Codes"], cost_code_summary["Budget"] = code, f"${value:.2f}"
    incurred_cost = list(map(lambda x: float(x[8]),filter(lambda x: x[3]==code,cost_table)))
    total_incurred_cost = sum(incurred_cost)
    cost_code_summary["Total Incurred Cost"] = f"${total_incurred_cost:.2f}"
    remaining_budget = value - total_incurred_cost
    cost_code_summary["Remaining Budget"] = f"${remaining_budget:.2f}"
    total_remaining_budget += remaining_budget
    budget_summary.append(cost_code_summary)
  print(f"Summary generated on {date.today().strftime("%A %d. %B %Y")}")
  print(tabulate(budget_summary,headers="keys",tablefmt="rounded_grid"))
  print(f"Total Budget: ${total_budget:.2f}")
  print(f"Total Remaining Budget: ${total_remaining_budget}")










