from user_input import UserInput, SubmitError
from Project_setup import ProjectSetupInfo
from cost_input import CostInfo
from project_summary import summary_generate
from tabulate import tabulate
import json


if __name__ == "__main__":
  print(f"Welcome to Project Cost Tracking application. Please select one of the following options.\n Enter {r"'\q'"} anytime to exit.\n")
  print("\t1. Enter new Project Setup/ Edit Project Setup Information\n " \
    "\t2. Enter new Incurred Cost\n " \
    "\t3. Display Existing Incurred Cost\n" \
    "\t4. View Project Summary")
  print("\n**Please note:\n"
        "\tOption 1 is required to be completed before running Option 2\n" \
  "\tOption 1 and 2 are required to be completed before running Option 3\n")
  
  while True:
    option_input = UserInput("Please enter index number to select (1/2/3/4):")
    select_option = option_input.get_input()
    match str(select_option):
      case '1':
        project_setup = ProjectSetupInfo.project_input()
        project_setup.display()
        project_setup.save_to_file("../data/project.json")
      case '2':
        try:
          cost_user_enter = CostInfo.cost_input()
          cost_user_enter.save_to_csvfile("../data/incurred_cost.csv")
          print("Table of Incurred Cost:")
          print(tabulate(CostInfo.read_csvfile("../data/incurred_cost.csv"),tablefmt="rounded_grid"))
        except json.JSONDecodeError:
          print("Project Profile has not been set up, please set up project first by select option 1.")
        except SubmitError:
          print("SubmitError!")
        except FileNotFoundError:
          print("Error: File Not Found!")

      case '3':
        try:
          print("Table of Incurred Cost:")
          print(tabulate(CostInfo.read_csvfile("../data/incurred_cost.csv"),tablefmt="rounded_grid"))
        except FileNotFoundError:
          print("Error: File Not Found!")
        
      case '4':
        try:
          summary_generate()
        except (json.JSONDecodeError, IndexError) :
          print("Error! Please ensure that project has been set up (select option 1 to set up) and there are minimum one incurred cost added (select option 3 to check and option 2 to add cost")
        except FileNotFoundError:
          print("Error: File Not Found!")

      case _:
        print("Invalid option, please try again!")

