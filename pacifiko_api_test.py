import http.client
import json
import time

# ***************************************************************************************
# makes a get request and prints the number of employees with salary higher than $300,000
# ***************************************************************************************
def get_employees_salary_higher_300_000():
    while True:
        try:
            connection = http.client.HTTPSConnection("dummy.restapiexample.com")
            connection.request("GET", "/api/v1/employees")
            response = connection.getresponse()
            data = response.read().decode()
            data = json.loads(data)
            counter = 0
            for employee in data["data"]:
                if(employee["employee_salary"]>300000):
                    counter+=1
            print("Number of employees with salary higher than $300,000:",counter)
            connection.close()
            break
        except:
            print("Service did not accept request, trying again in 10 seconds")
            connection.close()
            time.sleep(10)
# *******************************************************************
# adds a registry with my name and prints the id for the new registry
# *******************************************************************
def add_registry():
    while True:
        try:
            connection = http.client.HTTPSConnection("dummy.restapiexample.com")
            body = json.dumps({
              "name": "Pablo Xocoy",
              "salary": 50000,
              "age": 37
            })
            headers = {
              'Content-Type': 'application/json'
            }
            connection.request("POST", "/api/v1/create", body, headers)
            response = connection.getresponse()
            data = json.loads(response.read().decode())
            print(data["message"],"New id:",data["data"]["id"])
            connection.close()            
            break
        except:
            print("Service did not accept request, trying again in 10 seconds")
            connection.close()
            time.sleep(10)

get_employees_salary_higher_300_000()
add_registry()
time.sleep(5)
