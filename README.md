# Project Cost Tracking Application

## Overview
This application assists with recording project incurred cost and generate a summary to inform remaning budget, 
so that the user can keep track of incurred cost and remaining budget they have for the project.


## Features

- Allow user to set up initial information for project, including: Project name, Revenue, Margin, Total Budget and Allocation to Cost Codes
- Allow user to edit project setup information
- Allow user to add incurred cost, including details: date of incurred cost, Responsible person, Select Cost Code,Supplier,Item,Quantity,Cost per each item ($).
From these details, total cost for each item is calculated. 
- Allow user to view all incurred costs. 
- Allow user to request a project summary, including project information and remaining budgets for each cost code. 

## Important to Note

- Project setup is required before proceeding with entering incurred cost.
- Project setup and minimum one added incurred cost are required to proceed with generating project summary.
- User can exit the application anytime by entering "\q"
- User can submit Cost Code Allocation and Incurred Costs by entering "\submit" only when requested in prompt. 
- User do not need to enter unit for any number input. Entering unit with number will result in error, leading to the "please try again!" request.
- Do not edit first line in `incurred_cost.csv` file. If edit accidentally, please copy this line to add in as first line:<br>
```No.,Date,Responsible Person,Selected Cost Code,Supplier,Item,Quantity,Cost per each item ($),Total Cost```



## Installation

### Prerequisites

1. Python 3.10 or above.
2. Required libraries:
   - numpy==2.2.6
   - pandas==2.3.0
   - python-dateutil==2.9.0.post0
   - pytz==2025.2
   - six==1.17.0
   - tabulate==0.9.0
   - tzdata==2025.2

### Steps

1. Clone or download the project folder from <https://github.com/phuongle1911/Project-Tracking-Application>

2. Navigate to the project directory in your terminal
   ```bash
   cd path/16279_Le_Phuong_DEV1001_Assessment_02
   ```
3. Create a virtual enviroment
   ```bash
   python -m venv .venv
   ```

4. Activate virtual enviroment
   ```bash
   source .venv/bin/activate
   ```

5. Install required packages using requirments.txt:

   ```bash
   pip install -r requirements.txt
   ```

5. Navigate to 'src' directory and run the application:

   ```bash
   cd src
   ```
   ```bash
   python main.py
   ```

## Usage

1. **Setup/Edit Project Profile:**
 Select Option 1 to set up project profile by following the prompt to enter Project name, Revenue, Margin, Cost Codes and budget for each Cost Code. You also can change the existing project profile here.
2. **Add Incurred Costs:**
 Select Option 2 to add new incurred costs by following the prompt to enter Date of Cost Incurred, Responsible person, Select Cost Code,Supplier,Item,Quantity,Cost per each item ($).
3. **Display Existing Incurred Costs:**
 Select Option 3 to display all incurred costs.
4. **Generate Project Summary:**
  Select Option 4 to generate project summary including project profile information and remaining budget. 

## File Structure

- **`data/`**: Stores project profile data (`project.json`) and incurred costs data (`incurred_cost.csv`).
- **`src/`**: Contains Python source code for application functionality:
  - `main.py`: Application running point. User will run the app in here.
  - `user_input.py`: Manage user input.
  - `Project_setup.py`: Manage project profile setup
  - `cost_input.py`: Manage input of incurred costs.
  - `project_summary.py`: Support generating project summary.

### Licenses

This project uses the following third-party libraries:

1. **numpy**
    - License: BSD License (Copyright (c) 2005-2024, NumPy Developers.)
    - <https://github.com/numpy/numpy.org/blob/main/LICENSE>

2. **pandas**  
   - License: BSD 3-Clause License  
   - <https://github.com/pandas-dev/pandas/blob/main/LICENSE>

3. **python-dateutil**
    - Apache Software License, BSD License (Dual License) 
    - <https://github.com/dateutil/dateutil/blob/master/LICENSE>

4. **pytz**
    - MIT License (MIT)
    - <https://github.com/stub42/pytz/blob/master/LICENSE.txt>

5. **six**
    - MIT License (MIT)
    - <https://github.com/benjaminp/six/blob/main/LICENSE>

7. **tabulate**  
   - License: MIT License  
   - <https://github.com/astanin/python-tabulate/blob/master/LICENSE>

8. **tzdata**  
   - License: Apache Software License (Apache-2.0)
   - <https://github.com/python/tzdata/blob/master/LICENSE>

### Ethical and Legal Compliance

All third-party libraries are used in compliance with their respective licenses.<br><br> 
**Project License:** MIT License <https://github.com/phuongle1911/Project-Tracking-Application/blob/main/LICENSE>

## System Requirements

- Python 3.10+
- Operating System: Windows, macOS, or Linux

## Troubleshooting

- **Error: File Not Found**: Ensure `project.json` and `incurred_cost.csv` exist in the `data/` folder with correct file name. Also ensure you navigate to ' 16279_Le_Phuong_DEV1001_Assessment_02/src' path in your terminal.
- **Invalid Input**: Follow user prompts carefully to avoid input errors.
- **SubmitError:**: Only enter "/submit" when requested in prompt. Follow user prompts carefully to avoid this error. 
- If you would like to edit submitted incurred cost, please open 'incurred_cost.csv' file to edit. Do not edit the first line in the file.

## Future Upgrade
- Add feature to allow user to edit submited incurred cost in the application.
- Add additional feature to forecast future costs and preview future remaining budget by set date. 
- Welcome any suggestions on useful features that can be added.
