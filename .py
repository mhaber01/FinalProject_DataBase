# Database Final Project, Cruiseship Database
# By Megan Haber

import pymysql.cursors
connection=pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='cruiseship')

def login():
    u = raw_input("Enter your username: ")
    p = raw_input("Enter your password: ")
    with connection.cursor() as cursor:
        sql = "select user, password from employee where user=\"" + str(u) + "\" and password=\"" + str(p) + "\""
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            return True
        else:
            connection.close()               

def findEmployee():
        sn = raw_input("Enter the ship number: ")
        with connection.cursor() as cursor:
            sql="SELECT name from employee where ship_no=" + sn
            cursor.execute(sql)
            result=cursor.fetchall()
            for tuple in result:
                print (tuple)
                
def findShip():
        ship = raw_input("Enter the ship name: ")
        with connection.cursor() as cursor:
            sql="select i.homeport, i.destination from include as i, ship where i.ship_no=ship.ship_no and ship.ship_name=\"" + ship + "\""
            cursor.execute(sql)
            result=cursor.fetchall()
            for tuple in result:
                print (tuple)

def findRoom():
        rn = raw_input("Enter the room number: ")
        with connection.cursor() as cursor:
            sql="select p.name from passenger as p, belongs as b where p.pass_no=b.pass_no and b.room_no=" + rn
            cursor.execute(sql)
            result=cursor.fetchall()
            for tuple in result:
                print (tuple)

def findEmpSalary():
    empno = raw_input("Enter the employee's ID number: ")
    with connection.cursor() as cursor:
        sql="select salary from employee where emp_no=" + empno
        cursor.execute(sql)
        result=cursor.fetchall()
        for tuple in result:
            print (tuple)

def findHighestSalary():
        with connection.cursor() as cursor:
            sql="select position from employee where salary=(select max(salary) from employee)"
            cursor.execute(sql)
            result=cursor.fetchall()
            for tuple in result:
                print (tuple)

def addEmployee():
        emname = raw_input("Enter name: ")
        empos = raw_input("Enter position: ")
        emsal = raw_input("Enter salary: ")
        emno = raw_input("Enter employee number: ")
        emuser = raw_input("Enter username: ")
        empass = raw_input("Enter password: ")
        emsn = raw_input("Enter ship number: ")
        with connection.cursor() as cursor:
            sql = "insert into employee values ('"+ "\"" + emname + "\"" + "','"+ "\"" + empos + "\"" + "'," + emsal + ",'" + emno + "','" + "\"" + emuser + "\"" + "','" + "\"" + empass + "\"" + "','"+ emsn + "')"
            cursor.execute(sql)
            result=cursor.fetchall()

def addPassenger():
        pname = raw_input("Enter passenger name: ")
        pno = raw_input("Enter passenger number: ")
        with connection.cursor() as cursor:
            sql = "insert into passenger values ('"+"\"" + pname + "\"" + "','" + "\"" + pno + "\"" + "')"
            cursor.execute(sql)
            result=cursor.fetchall()

def testPassengerTable():
        with connection.cursor() as cursor:
            sql="select * from passenger"
            cursor.execute(sql)
            result=cursor.fetchall()
            for tuple in result:
                print (tuple)

def testEmployeeTable():
        with connection.cursor() as cursor:
            sql="select * from employee"
            cursor.execute(sql)
            result=cursor.fetchall()
            for tuple in result:
                print (tuple)

def openMenu():
    login()
    print "\nWelcome to the Cruiseship Page!\nHere is a current list of ships: \n 1: Gem \n 2: Escape \n 3: Voyager \n 4: Ruby","\n\n","Welcome to the Database. Enter a number to access an option.\nOptions Menu: \n","\n","1: Find Employee \n","2: Cruiseship's Homeports and Destinations\n","3: Names of Passengers Staying in a Room\n","4: Employee Salary\n","5: Position with Highest Salary\n", "6. New Employee\n", "7. New Passenger\n","8. Show Current Passengers and Their IDs\n","9. Show Current Employee Information\n"
    again = "yes"
    while (again == "yes"):
        option = int(input("Please enter a selection: "))
        if (option == 1):
            findEmployee()
        elif (option == 2):
            findShip()
        elif (option == 3):
            findRoom()
        elif (option == 4):
            findEmpSalary()
        elif (option == 5):
            findHighestSalary()
        elif (option == 6):
            addEmployee()
        elif (option == 7):
            addPassenger()
        elif (option == 8):
            testPassengerTable()
        elif (option == 9):
            testEmployeeTable()
        else:
            print ("Not valid choice")
        again = raw_input("Would you like to continue? Enter yes or no: ")
    print ("Have a nice day!")
openMenu()


