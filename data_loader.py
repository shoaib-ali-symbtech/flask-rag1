
from langchain.document_loaders import CSVLoader
import pandas as pd
from neo4j import GraphDatabase
from langchain_community.graphs import Neo4jGraph
import json

from dotenv import load_dotenv
load_dotenv()
graph = Neo4jGraph()




def load_files():
    print("\n\n--------\nFirst\n----\n")
    employee_data = pd.read_csv('./data_sheets/employee_details.csv')#CSVLoader(file_path='./data_sheets/employee_details.csv')
    # employee_data = employee_loader.load()

# Load salary sheet
    salary_data= pd.read_csv('./data_sheets/salary_sheet.csv')
    

# Load daily task sheet
    
    task_data = pd.read_csv('./data_sheets/daily_task_sheet.csv')
    print("\n\n--------\nLoaded\n----\n")
 

    
  
  
    res=""
    try:
        create_employee_nodes(employee_data)
    except :
        res= "Something went wrong while employee data uploading.\n"
    try:
        create_salary_relationships(salary_data)
    except :
        res+="Something went wrong while salary data uploading.\n"
    try:
        create_task_relationships(task_data)
    except :
        res+="Something went wrong while task uploading."
    
    return "Uploaded successfully" if res=="" else res
            
     
    

# Function to create Employee nodes
def create_employee_nodes(employee_df):
    for _, row in employee_df.iterrows():
        query = """
        MERGE (e:Employee {employee_id: $employee_id})
        SET e.name = $name, e.department = $department, e.designation = $designation, 
            e.joining_date = $joining_date, e.contact_number = $contact_number, 
            e.email = $email
        """
        parameters = {
            "employee_id": row['Employee ID'],
            "name": row['Name'],
            "department": row['Department'],
            "designation": row['Designation'],
            "joining_date": row['Joining Date'],
            "contact_number": row['Contact Number'],
            "email": row['Email']
        }
        print("\n--------\nQuerying 1----")

        graph.query(query, parameters)
       

# Function to create Salary relationships








# Function to create Salary relationships
def create_salary_relationships(salary_df):
    for _, row in salary_df.iterrows():
        query = """
        MATCH (e:Employee {employee_id: $employee_id})
        MERGE (s:Salary {payment_date: $payment_date})
        SET s.basic_salary = $basic_salary, s.hra = $hra, 
            s.allowances = $allowances, s.deductions = $deductions, 
            s.net_salary = $net_salary
        MERGE (e)-[:RECEIVED_SALARY]->(s)
        """
        parameters = {
            "employee_id": row['Employee ID'],
            "basic_salary": row['Basic Salary'],
            "hra": row['HRA'],
            "allowances": row['Allowances'],
            "deductions": row['Deductions'],
            "net_salary": row['Net Salary'],
            "payment_date": row['Payment Date']
        }

        print("\n--------\nQuerying 2----")

        graph.query(query, parameters)
        # execute_query(query, parameters)

# Function to create Task relationships
def create_task_relationships(task_df):
    for _, row in task_df.iterrows():
        query = """
        MATCH (e:Employee {employee_id: $employee_id})
        MERGE (t:Task {date: $date, name: $task_name})
        SET t.status = $task_status
        MERGE (e)-[:WORKED_ON]->(t)
        """
        parameters = {
            "employee_id": row['Employee ID'],
            "date": row['Date'],
            "task_name": row['Task Name'],
            "task_status": row['Task Status']
        }
        print("\n--------\nQuerying 3----")

        graph.query(query, parameters)
        # execute_query(query, parameters)



 