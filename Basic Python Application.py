from tkinter import *
import tkinter as tk
import mysql.connector

root = Tk()
root.title("Home_Expense")

def get_data(date,income,bank,lpg,ola,pstadv,homeexpense,autoexpense,godexpense):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Sathish=3645",
        database = "expense",
        auth_plugin="mysql_native_password"
    )

    mycursor = mydb.cursor()
    SQL = "INSERT INTO home_expense(date,income,bank,lpg,ola,pstadv,homeexpense,autoexpense,godexpense) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    Val = (date,income,bank,lpg,ola,pstadv,homeexpense,autoexpense,godexpense)
    mycursor.execute(SQL, Val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    display_all()

def search(date):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sathish=3645",
        database="expense"
    )

    mycursor = mydb.cursor()
    sql = "SELECT * FROM home_expense WHERE date = %s"
    mycursor.execute(sql, (date,))
    myresult = mycursor.fetchone()
    display_search(myresult)

def display_search(myresult):
    listbox = Listbox(frame,width = 50, height = 1)
    listbox.grid(row = 13, column = 1)
    listbox.insert(END, myresult)


def display_all():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sathish=3645",
        database="expense"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM home_expense")
    myresult = mycursor.fetchall()

    listbox = Listbox(frame, width=50, height=50)
    listbox.grid(row=14, column=1)
    for x in myresult:
        listbox.insert(END, x)


canvas = Canvas(root, height= 600, width = 1200)
canvas.pack()

frame = Frame()
frame.place(relx =0.3, rely= 0.1, relwidth = 0.8, relheight = 0.8)

label = Label(frame, text ="Please Enter the amount")
label.grid(row = 0, column = 1)

label = Label(frame, text ="Date")
label.grid(row = 1, column = 0)

entry_date = Entry(frame)
entry_date.grid(row = 1, column = 1)

label = Label(frame, text ="Income")
label.grid(row = 2, column = 0)

entry_income = Entry(frame)
entry_income.grid(row = 2, column = 1)

label = Label(frame, text ="Bank")
label.grid(row = 3, column = 0)

entry_bank = Entry(frame)
entry_bank.grid(row = 3, column = 1)

label = Label(frame, text ="LPG")
label.grid(row = 4, column = 0)

entry_lpg = Entry(frame)
entry_lpg.grid(row = 4, column = 1)

label = Label(frame, text ="OLA")
label.grid(row = 5, column = 0)

entry_ola = Entry(frame)
entry_ola.grid(row = 5, column = 1)

label = Label(frame, text ="PST ADV")
label.grid(row = 6, column = 0)

entry_pstadv = Entry(frame)
entry_pstadv.grid(row = 6, column = 1)

label = Label(frame, text ="Home Expense")
label.grid(row = 7, column = 0)

entry_homeexpense = Entry(frame)
entry_homeexpense.grid(row = 7, column = 1)


label = Label(frame, text ="Auto Expense")
label.grid(row = 8, column = 0)

entry_autoexpense = Entry(frame)
entry_autoexpense.grid(row = 8, column = 1)

label = Label(frame, text ="God Expense")
label.grid(row = 9, column = 0)

entry_godexpense = Entry(frame)
entry_godexpense.grid(row = 9, column = 1)

button = Button(frame, text = "Submit", command = lambda :get_data(entry_date.get(),entry_income.get(),entry_bank.get(),entry_lpg.get(),entry_ola.get(),entry_pstadv.get(),entry_homeexpense.get(),entry_autoexpense.get(),entry_godexpense.get()))
button.grid(row = 10, column = 1)

label = Label(frame, text= "Search Data", fg ="RED", bg = "Black")
label.grid(row = 11, column = 1)

label = Label(frame, text = "Search Data By Date")
label.grid(row = 12, column = 0)

entry_search = Entry(frame)
entry_search.grid(row =12, column =1)

button = Button(frame, text = "Search", command = lambda : search(entry_search.get()))
button.grid(row = 12, column = 2)

display_all()

root.mainloop()