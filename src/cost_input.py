from Project_setup import ProjectSetupInfo
from user_input import UserInput, SubmitError
import csv
import pandas as pd
# from tabulate import tabulate

def dict_add(key,value,dictionary):
  dictionary[key] = value

class CostInfo:
  def __init__(self,cost_list):
    self.cost_list = cost_list

  @staticmethod
  def last_index(filename):
    df = pd.read_csv(filename)
    df.dropna()
    df.to_csv(filename,index=False)
    try:
      i = int(df.iloc[-1,0])
    except (ValueError,IndexError):
      i=0  
    return i
  
  @staticmethod
  def select_cost_code(cost_codes):#fuction to select one of key value in a dictionary
    print("Allocate your cost into one of the cost code below:")
    for code in cost_codes.keys():
      print(code)
    while True:
      select_code_input = UserInput("Which cost code you want to select?:")
      select_code = select_code_input.get_input()
      if select_code.lower() in cost_codes.keys():
        print(f"Cost code {select_code} is selected!")
        return select_code
      else:
        print("Invalid cost code, please try again!")
        continue
  
  @classmethod
  def cost_input(cls):
    loaded_project_info = ProjectSetupInfo.load_from_file("../data/project.json")
    current_cost_codes = loaded_project_info.cost_codes
      

    cost_input_header = ["No.","Date","Responsible Person","Selected Cost Code","Supplier","Item","Quantity","Cost per each item ($)","Total Cost ($)"]
  
    i = CostInfo.last_index("../data/incurred_cost.csv")+1
    cost_list=[]

    while True:
      cost_dict = {}
      for elem in cost_input_header[:8]:
        if elem == "No.":
          elem_value = i
        elif elem == "Date":
          elem_value_input = UserInput('')
          elem_value = elem_value_input.get_date()
        elif elem in ["Responsible Person","Supplier","Item"]:
          elem_value_input = UserInput(f"{elem}:")
          elem_value = elem_value_input.get_input()
        elif elem =="Selected Cost Code":
          elem_value = CostInfo.select_cost_code(current_cost_codes)
        else:
          elem_value_input = UserInput(f"{elem}:")
          elem_value=elem_value_input.get_num()
        dict_add(elem,elem_value,cost_dict)
      cost_list.append(cost_dict)
      print(cost_list)
      i+=1
      try:
        input = UserInput(f"Press Enter to add more cost, or {r'\submit'} to submit cost:")
        input.get_input()
      except SubmitError:
        print("Cost submited!")
        break
    for row in cost_list:
      row["Total Cost ($)"] = row["Quantity"] * row["Cost per each item ($)"]
    return cls(cost_list)
  
  def save_to_csvfile(self,filename):
    with open(filename,'a',newline='') as f:
      writer = csv.DictWriter(f,fieldnames=self.cost_list[0].keys())
      writer.writerows(self.cost_list) 

  @staticmethod
  def read_csvfile(filename):
    with open(filename,'r',newline='') as f:
      reader = csv.reader(f)
      table = list(reader)
    return table

#edit submited incurred cost
# def edit_cost(cost_list):



  

 

 







  