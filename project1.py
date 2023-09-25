import pyodbc
from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox

import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)




root=tk.Tk()
root.title('Student Database Management')

# setting the windows size
root.geometry("1920x1080")

# declaring string variable
id_var=tk.StringVar()
name_var=tk.StringVar()
email_var=tk.StringVar()
age_var=tk.StringVar()
gender_var =tk.StringVar()
nationality_var =tk.StringVar()
religon_var =tk.StringVar()
contact_var=tk.StringVar()
delete_var = tk.StringVar()
search_var = tk.StringVar()


#............................................................FUNCTIONS....................................................................
def submit():

	userId=id_var.get()
	userName=name_var.get()
	userEmail=email_var.get()
	userAge=age_var.get()
	userGender=gender_var.get()
	userNationality=gender_var.get()
	userReligon=gender_var.get()
	userContact=contact_var.get()
	
	print("The ID is : " , userId)
	print("The name is : " + userName)
	print("The Email is : " +  userEmail)
	print("The Age is : " ,userAge)
	print("The Gender is : " ,userGender)
	print("The Nationality is : " ,userNationality)
	print("The Religon is : " ,userReligon)
	print("The Contact is : " , userContact)

	addData()
	clear()
	displayData()

def delete():


	con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                 r'DBQ=C:\Users\Dell\Desktop\TestDb.accdb;'
	conn = pyodbc.connect(con_string)
 
	user_id = delete_var.get()
 
	cur = conn.cursor()
	cur.execute('DELETE FROM users WHERE id = ?', (user_id))
	conn.commit()
	print("Data Deleted ")
	clear()

def clear():
  name_entry.delete("0","end")
  email_entry.delete("0","end")
  age_entry.delete("0","end")
  gender_entry.delete("0","end")
  nationality_entry.delete("0","end")
  religon_entry.delete("0","end")
  contact_entry.delete("0","end")
  id_entry.delete("0","end")
  delete_entry.delete("0","end")
  search_entry.delete("0","end")
  


def addData():
	try:
		con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
				r'DBQ=C:\Users\Dell\Desktop\TestDb.accdb;'
		conn = pyodbc.connect(con_string)
		cursor = conn.cursor()


		userId = id_var.get()
		userName = name_var.get()
		userEmail = email_var.get()
		userAge = age_var.get()
		userGender = gender_var.get()
		userNationality = nationality_var.get()
		userReligon = religon_var.get()
		userContact = contact_var.get()

		myuser = (

		(int(userId), userName, userEmail, int(userAge),userGender,userNationality,userReligon,(userContact)),

		)

		cursor.executemany('INSERT INTO users VALUES (?,?,?,?,?,?,?,?)',myuser)
		

		conn.commit()
		print('Data Inserted')

	except pyodbc.Error as e:
		print('Error',e)


def displayData():
	import tkinter as tk


	root = Tk()
	root.title('Student Data')

	# specify size of window.
	root.geometry("880x880+490+0")

	# Create text widget and specify size.
	T = Text(root, height = 200, width = 900,)
	

	# Create label
	l = Label(root, text = "Database")
	l.config(font =("Courier", 14))


	con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
				r'DBQ=C:\Users\Dell\Desktop\TestDb.accdb;'
	conn = pyodbc.connect(con_string)
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM users')
	for row in cursor.fetchall():
			T.insert(tk.END, row)

			
	l.pack()
	T.pack()
	

	# Insert The Fact.

	tk.mainloop()
# .......................................................Search-Item.......................................................
def searchItem1():
	import tkinter as tk


	root = Tk()
	root.title('Searched Data')

	# specify size of window.
	root.geometry("880x880+490+0")

	# Create text widget and specify size.
	T = Text(root, height = 200, width = 900,)

	# Create label
	l = Label(root, text = "Database")
	l.config(font =("Courier", 14))


	con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
				r'DBQ=C:\Users\Dell\Desktop\TestDb.accdb;'
	conn = pyodbc.connect(con_string)
	cursor = conn.cursor()
	searchItem = search_var.get()
	cursor.execute('SELECT * FROM users WHERE ID = ?',searchItem)
	for row in cursor:
			T.insert(tk.END, row)

			
	l.pack()
	T.pack()
	

	# Insert The Fact.
	clear()
	tk.mainloop()

	




#........................................................Tkinter grid........................................................................	
	
# creating a label for
id_label1 = tk.Label(root, text ='Student Database System', font=('calibre',18, 'bold'))

# id using widget Label
id_label = tk.Label(root, text = 'ID', font=('calibre',18, 'bold'))

# creating a entry for input
# id using widget Entry
id_entry = tk.Entry(root,textvariable = id_var, font=('calibre',18,'normal'))

# creating a label for name
name_label = tk.Label(root, text = 'Name', font = ('calibre',18,'bold'))

# creating a entry for name
name_entry=tk.Entry(root, textvariable = name_var, font = ('calibre',18,'normal'))

# creating a label for email
email_label = tk.Label(root, text = 'Email', font = ('calibre',18,'bold'))

# creating a entry for email
email_entry=tk.Entry(root, textvariable = email_var, font = ('calibre',18,'normal'))

# creating a label for age
age_label = tk.Label(root, text = 'Age', font = ('calibre',18,'bold'))

# creating a entry for age
age_entry=tk.Entry(root, textvariable = age_var, font = ('calibre',18,'normal'))
# creating a label for gender
gender_label = tk.Label(root, text = 'Gender', font = ('calibre',18,'bold'))

# creating a entry for gender
gender_entry=tk.Entry(root, textvariable = gender_var, font = ('calibre',18,'normal'))
# creating a label for nationality
nationality_label = tk.Label(root, text = 'Nationality', font = ('calibre',18,'bold'))

# creating a entry for nationality
nationality_entry=tk.Entry(root, textvariable = nationality_var, font = ('calibre',18,'normal'))
# creating a label for religon
religon_label = tk.Label(root, text = 'Religon', font = ('calibre',18,'bold'))

# creating a entry for age
religon_entry=tk.Entry(root, textvariable = religon_var, font = ('calibre',18,'normal'))

# creating a label for contact
contact_label = tk.Label(root, text = 'Contact', font = ('calibre',18,'bold'))

# creating a entry for contact
contact_entry=tk.Entry(root, textvariable = contact_var, font = ('calibre',18,'normal'))

# creating a label for contact
delete_label = tk.Label(root, text = 'Delete(ID)', font = ('calibre',18,'bold'))

# creating a entry for contact
delete_entry=tk.Entry(root, textvariable = delete_var, font = ('calibre',18,'normal'))
# Search Item
search_label = tk.Label(root, text = 'Search(ID)', font = ('calibre',18,'bold'))

# creating a entry for contact
search_entry=tk.Entry(root, textvariable = search_var, font = ('calibre',18,'normal'))


# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit , font=('calibre', 18))
clr_btn=tk.Button(root,text = 'Clear', command = clear , font=('calibre', 18))

del_btn=tk.Button(root,text = 'Delete', command = delete , font=('calibre', 18))
search_btn=tk.Button(root,text = 'Search', command = searchItem1 , font=('calibre', 18))

# dis_btn=tk.Button(root,text = 'DISPLAY', command = display , font=('calibre', 18))


# .........................TexTArea..............................................








# placing the label and entry in
# the required position using grid
# method
id_label1.grid(row=0,column=1 ,sticky=tk.W,pady = 2)

id_label.grid(row=1,column=0,pady = 2)
id_entry.grid(row=1,column=1,pady = 2)
name_label.grid(row=2,column=0,pady = 2)
name_entry.grid(row=2,column=1,pady = 2)
email_label.grid(row=3,column=0,pady = 2)
email_entry.grid(row=3,column=1,pady = 2)
age_label.grid(row=4,column=0,pady = 2)
age_entry.grid(row=4,column=1,pady = 2)
gender_label.grid(row=5,column=0,pady = 2)
gender_entry.grid(row=5,column=1,pady = 2)
nationality_label.grid(row=6,column=0,pady = 2)
nationality_entry.grid(row=6,column=1,pady = 2)
religon_label.grid(row=7,column=0,pady = 2)
religon_entry.grid(row=7,column=1,pady = 2)
contact_label.grid(row=8,column=0,pady = 2)
contact_entry.grid(row=8,column=1,pady = 2)

delete_label.grid(row=13,column=0,pady = 20)
delete_entry.grid(row=13,column=1,pady = 20)

search_label.grid(row=16,column=0,pady = 20)
search_entry.grid(row=16,column=1,pady = 20)




sub_btn.grid(row=9,column=1)
del_btn.grid(row=15,column=1)
search_btn.grid(row=17,column=1)
# dis_btn.grid(row=15,column=10)
root.mainloop()



# performing an infinite loop
# for the window to display







