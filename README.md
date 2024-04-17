# Welcome to Coder Its OneNuman!

## Its [django-RBAC-Employee-Management-System-With-API](https://github.com/one-numan/django-RBAC-Employee-Management-System-With-API) _version1.0.1_

**_Hope Your Doing Great_**

## Description

In this Project I built Personal Project in Professional Ways .
Follows **_SDLC - Software Development Life Cycle_** structured process for Building this Project.

1.  Planning and Requirement Analysis
2.  Defining Requirements
3.  Designing Architecture
4.  Developing Product
5.  Product Testing and Integration
6.  Deployment and Maintenance of Products
    This Will be Applied on _Each Version_ I will Try

- **Purpose/Learning** (Its My Own Options Not is _SDLC_ , Learning Django and build an apps Gradually improve in the version )
  - Up Skills my Knowledge's in Django
  - Build RBAC _Role Based Access Control_ ( Each Users have different **Power** according to their Roles )
    - I was Build RBAC in Flask and But not in Django , So try and using Different approach
  - Building A Multiples Theme 2 - UI & UX
    - Use 2 Different Themes
      - Basic Standard Theme
      - Neomorphism Theme (Will Including Version 1.3.0 , Futuristic Themes )
  - Build **WebPage** and Build **CRUDS** API that Return JSON ( Host in Live Later use this API in Android phone )
  - Use 500 + Peoples Data (No Real) in the DB (SQLite - RDBMS )

## Table of Contents (Optional)

If your README is long, add a table of contents to make it easy for users to find what they need.

- [About](#about)
- [Installation](#installation)
- [Run this Project](#run)
- [Designing Architecture](#pages)
  - [WebPages](#pages)

## About

| Project Name | Employee Management System |
| ------------ | -------------------------- |
| **Version**  | 1.0.1                      |

_Its a Very BASIC App as its Version_

---

| Modules / Library Name | Version |
| ---------------------- | ------- |
| Python                 | 3.10.8  |
| Django                 | 4.2.8   |
| Sqlite                 | 3.44    |
| HTML                   | 5       |
| CSS                    | 3       |
| Bootsrap               | 5.2     |

## Installation

- Clone this Repo
- Install Python3
- Installing Required Python Modules from File **Requirements.txt**
  - Command `pip install -r requirements.txt`
- Installed IDE like VSCode or Pycharm

## Run this Project

- I assumed the Clone and Set Every thing
- ![image](https://github.com/one-numan/django-RBAC-Employee-Management-System-With-API/assets/48924562/09925aac-f20c-4d49-a66e-70993612b894)
- This is the Project Directory
  - May be your scared , But Don't worry
- There is Folder **EmployeeManagementSystem**
  - Go Inside this Folder their is File
    - manage.py (its is like **Soul** of Your Project )
    - Lets Run Command `python3 manage.py runserver`
    - This Will Run Your Project in your Computer
    - If Project is Running Successfully, You will get an URL of Project
    - If Any Error , Don't Worry Troubleshoot that.

## Designing Architecture

<a name='pages'></a>
Web Pages : Build CRSD - CREAD , READ , SEARCH , DELETE .

### Home Page

- In this Home Page
  - ![image](https://github.com/one-numan/django-RBAC-Employee-Management-System-With-API/assets/48924562/fa6f5538-21dc-4030-b39c-2d3aa13d9bf0)
  - We Have 4 Buttons Each Button Redirect to Each Page
    - Add Employees
    - Delete Employees
    - View All Employees
    - Filter An Employee ( **Search an Employee** )

### Add Employees

- In this Page
  - ![image](https://github.com/one-numan/django-RBAC-Employee-Management-System-With-API/assets/48924562/db8803b6-2ac2-4516-b392-799de3d4ffe6)
  - We Have A **Input Field** are :
    - First Name
    - Last Name
    - Salary
    - Dept
    - Role
    - Bonus
  - Button - **Create New User**

### Delete Employees

- In this Page
  - ![image](https://github.com/one-numan/django-RBAC-Employee-Management-System-With-API/assets/48924562/2e251fe9-135c-4454-990a-f867d5066acc)
- Remove An Employees
  - Its Select List
  - Select and Hit Button
  - It will Delete that Employee

### View All Employees

- In this Page
  - ![image](https://github.com/one-numan/django-RBAC-Employee-Management-System-With-API/assets/48924562/234b0add-1968-4ebe-8273-d86e6a102ddb)
  - List Of All Employee Fetch From DB

### Filter An Employee

- In this Page
  - ![image](https://github.com/one-numan/django-RBAC-Employee-Management-System-With-API/assets/48924562/0af49a55-18bf-4d21-913e-a1f48d21f439)
- Enter the Employees
  - Its Should Be First or Last or Both
  - If the String Match then It will In Resume in New
    - All Founded Employees are
    - ![image](https://github.com/one-numan/django-RBAC-Employee-Management-System-With-API/assets/48924562/cce30f4f-0784-46f3-8383-498dd6e2839e)
