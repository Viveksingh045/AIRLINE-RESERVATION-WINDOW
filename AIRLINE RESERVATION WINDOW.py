import os
import platform
import mysql.connector as mysql
import datetime
import random as rd
import datetime as dt

tdate = dt.date.today()

# Database connection
mydb = mysql.connect(host="localhost", user="root", passwd="sql1234")
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS vivekproject")
mycursor.execute("USE vivekproject")
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS pdata (CustNo INT, CustName VARCHAR(50), Addr VARCHAR(200), JrDate CHAR(50), Source VARCHAR(50), Destination VARCHAR(50))"
)
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS tkt (CustNo INT, Tkt_Tot VARCHAR(50), Lug_Tot VARCHAR(50), G_tot VARCHAR(50))"
)

print("_________________________________________________________________________")
print()
print("                            AIRLINE RESERVATION WINDOW")
print("TODAY'S DATE", tdate, "                                   ", "ADMIN")
print()


def registercust():
    L = []
    cno = rd.randint(467476, 999999)
    L.append(cno)
    print("-------------------------------------------------------------------------")
    name = input('Enter name:')
    print("-------------------------------------------------------------------------")
    print()
    L.append(name)
    addr = input('Enter address:')
    print("-------------------------------------------------------------------------")
    print()
    L.append(addr)
    jr_date = input('Enter date of journey (YYYY-MM-DD):')
    print("-------------------------------------------------------------------------")
    print()
    L.append(jr_date)
    source = input('Enter source:')
    print("-------------------------------------------------------------------------")
    print()
    L.append(source)
    destination = input('Enter destination:')
    L.append(destination)
    print("-------------------------------------------------------------------------")
    print()
    cust = tuple(L)
    sql_query = 'INSERT INTO pdata (CustNo, CustName, Addr, JrDate, Source, Destination) VALUES (%s, %s, %s, %s, %s, %s)'
    mycursor.execute(sql_query, cust)
    mydb.commit()

    print("Customer is Successfully Registered with ID:", cno)
    print()


def ticketprice():
    L = []
    print()
    print("-------------------------------------------------------------------------")
    cno = int(input('Enter customer No:'))
    print("-------------------------------------------------------------------------")
    L.append(cno)
    print('We have the following rooms for you:')
    print("-------------------------------------------------------------------------")
    print('1. First class ---> Rs 6000 PN')
    print('2. Business class ---> Rs 4000 PN')
    print('3. Economy class ---> Rs 2000 PN')
    print("-------------------------------------------------------------------------")
    print()
    x = int(input('Enter your choice:'))
    print("-------------------------------------------------------------------------")
    print()
    n = int(input('Enter No. of Passengers:'))
    print("-------------------------------------------------------------------------")
    if x == 1:
        print('You have opted for First class.')
        s = 6000 * n
    elif x == 2:
        print('You have opted for Business class.')
        s = 4000 * n
    elif x == 3:
        print('You have opted for Economy class.')
        s = 2000 * n
    else:
        print('Please select a valid class type.')
        return
    L.append(s)
    print('Your ticket charge is:', s)
    print("-------------------------------------------------------------------------")
    print('Extra luggage charge: Rs 100 per kg')
    y = int(input('Enter weight of extra luggage (in kg):'))
    z = y * 100
    L.append(z)
    g_tot = s + z
    L.append(g_tot)
    print('Your total bill is:', g_tot)
    print("-------------------------------------------------------------------------")
    tkt = tuple(L)
    sql_query = "INSERT INTO tkt (CustNo, Tkt_Tot, Lug_Tot, G_tot) VALUES (%s, %s, %s, %s)"
    mycursor.execute(sql_query, tkt)
    mydb.commit()


def dis():
    custno = int(input("Enter the customer number whose bill to be viewed: "))
    sql_query = "SELECT pdata.CustNo, pdata.CustName, pdata.Addr, pdata.Source, pdata.Destination, tkt.Tkt_Tot, tkt.Lug_Tot, tkt.G_tot FROM pdata INNER JOIN tkt ON pdata.CustNo = tkt.CustNo WHERE tkt.CustNo = %s"
    mycursor.execute(sql_query, (custno,))
    res = mycursor.fetchall()
    for x in res:
        print(x)


def dispall():
    sql_query = "SELECT pdata.CustNo, pdata.CustName, pdata.Addr, pdata.Source, pdata.Destination, tkt.Tkt_Tot, tkt.Lug_Tot, tkt.G_tot FROM pdata INNER JOIN tkt ON pdata.CustNo = tkt.CustNo"
    mycursor.execute(sql_query)
    res = mycursor.fetchall()
    print("The Customer details are as follows:")
    print("Customer No | Customer Name | Address | Journey Date | Source | Destination")
    for y in res:
        print(" | ".join(map(str, y)))
    print()


def Menuset():
    while True:
        print("-------------------------------------------------------------------------")
        print('Enter 1: To enter customer data.')
        print('Enter 2: For ticket amount.')
        print('Enter 3: Display customer-specific details.')
        print('Enter 4: Display all details.')
        print('Enter 5: Exit.')
        print("-------------------------------------------------------------------------")
        userinput = int(input('Enter your choice: '))
        if userinput == 1:
            registercust()
        elif userinput == 2:
            ticketprice()
        elif userinput == 3:
            dis()
        elif userinput == 4:
            dispall()
        elif userinput == 5:
            break
        else:
            print('Enter a valid choice.')


Menuset()
