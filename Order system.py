
"""
by June
"""

import requests

import mysql.connector

import csv

# check if the user input customer number has order records in database. If not, ask to enter another one.
while True:
    
    userinput = int(input("Please input a customer number: "))

    mydb = mysql.connector.connect(
    host="remotemysql.com", # your host, localhost for your local db
    user="AybEFDBRkG",      # username
    password="pbNAmdostq",   # password
    database = "AybEFDBRkG"  # database
    )

    mycursor = mydb.cursor()

    #Get all orders for that company from the MySQL database classic models.
    # order number, order date, total order value
    ### n: when use different database(ex.remote), CAN'T just copy script from local database. Ex. uppercase sometimes matters ("C".customerName) SUM() to Group by ###
    sql = f"SELECT C.customerNumber, \
    C.customerName, \
    O.orderNumber, \
    O.orderDate, \
    SUM(quantityOrdered*priceEach) as totalOrderValue \
    FROM customers as C \
    INNER JOIN orders as O \
    ON C.customerNumber = O.customerNumber \
    INNER JOIN orderdetails as OD \
    ON O.orderNumber = OD.orderNumber \
    WHERE C.customerNumber = {userinput} \
    GROUP BY O.orderNumber"
    

    mycursor.execute(sql)

    orderinfo = mycursor.fetchall()

    if orderinfo:
        break

    #if the server doesn't respond any data, we ask the user to try another customer number. 
    else:
        print ("The customer number you input does not exist or have orders. Try again.")

  
# Produce a new CSV file
with open(f"Orders_{userinput}.csv", mode = "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = ",")

    header = ["customerNumber","companyName","orderNumber","orderDate","totalOrderValue","firstName","lastName","email","phone"]
    csv_writer.writerow(header)

    for orderinfo_row in orderinfo:
        #orderinfo_row: tuple
        
        
        #For every order, we will get first name, last name, email and phone no. from a random user API
        response = requests.get("https://randomuser.me/api")
        data = response.json()

        fname = data["results"][0]["name"]["first"]
        lname = data["results"][0]["name"]["last"]
        email = data["results"][0]["email"]
        phone = data["results"][0]["phone"]

        
        # append the tuple with "+" 
        new_row = orderinfo_row + (fname, lname, email, phone)

        csv_writer.writerow(new_row)


print(f"A csv file of customer number {userinput} has been generated.")







