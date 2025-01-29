# # # import sqlite3
# # # import csv


# # # conn = sqlite3.connect("jarvis.db")
# # # cursor = conn.cursor()

# # # # query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name VARCHAR(100),path VARCHAR(100))"
# # # # cursor.execute(query)

# # # # query = "INSERT INTO sys_command VALUES (null ,'onenote','C:\\Program Files\\Microsoft Office\\root\Office16\\ONENOTE.exe')"
# # # # cursor.execute(query)
# # # # conn.commit()

# # # # query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100),url  VARCHAR(1000))"
# # # # cursor.execute(query)


# # # # query = "INSERT INTO web_command VALUES (null ,'youtube','https://www.youtube.com//youtube')"
# # # # cursor.execute(query)
# # # # conn.commit()

# # # # app_name = "onenote"
# # # # cursor.execute('SELECT path from sys_command WHERE name in(?)',(app_name,))
# # # # results = cursor.fetchall()
# # # # print(results[0][0])

# # # # Create a table with the desired columns
# # # cursor.execute('''CREATE TABLE IF NOT EXISTS contactss(id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# # #Specify the column indices you want to import (0-based index)
# # #Example: Importing the 1st and 3rd columns
# # # desired_columns_indices = [0, 50]

# # # # Read data from CSV and insert into SQLite table for the desired columns
# # # with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
# # #     csvreader = csv.reader(csvfile)
# # #     for row in csvreader:
# # #         if len(row) > max(desired_columns_indices):
# # #             selected_data = [row[i] for i in desired_columns_indices]
# # #             cursor.execute(''' INSERT INTO contactss (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # # # Commit changes and close connection
# # # conn.commit()
# # # conn.close()

# # # # query = "INSERT INTO contacts VALUES (null,'shubham', '9604321555','null')"
# # # # cursor.execute(query)
# # # # conn.commit()

# query = 'Aai'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])

# # # # import sqlite3

# # # # # Connect to the database
# # # # conn = sqlite3.connect('jarvis.db')
# # # # cursor = conn.cursor()

# # # # # Example: Fix formatting by adding country code if missing
# # # # cursor.execute("SELECT name, mobile_no FROM contacts WHERE mobile_no NOT LIKE '+91%'")
# # # # contacts = cursor.fetchall()

# # # # for contact in contacts:
# # # #     name, mobile_no = contact
# # # #     if mobile_no and not mobile_no.startswith('+91'):
# # # #         updated_mobile_no = '+91' + mobile_no  # Add country code
# # # #         cursor.execute("UPDATE contacts SET mobile_no = ? WHERE name = ?", (updated_mobile_no, name))
# # # #         print(f"Updated {name}'s mobile number to {updated_mobile_no}")

# # # # # Commit the changes and close the connection
# # # # conn.commit()
# # # # conn.close()

# # # # query = "INSERT INTO contacts VALUES (null,'shubham', '+918766488141','null')"
# # # # cursor.execute(query)
# # # # conn.commit()
# # # # import csv
# # # # import sqlite3

# # # # def insert_contacts_into_db(csv_file='contacts.csv', db_file='jarvis.db'):
# # # #     # Connect to the SQLite database
# # # #     conn = sqlite3.connect(db_file)
# # # #     cursor = conn.cursor()

# # # #     # Create the contacts table if it doesn't exist
# # # #     cursor.execute('''
# # # #     CREATE TABLE IF NOT EXISTS contacts (
# # # #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # #         name TEXT NOT NULL,
# # # #         mobile_no TEXT NOT NULL
# # # #     )
# # # #     ''')

# # # #     try:
# # # #         with open(csv_file, 'r', encoding='utf-8') as file:
# # # #             reader = csv.reader(file)
# # # #             next(reader)  # Skip header row if it exists
            
# # # #             for row in reader:
# # # #                 # Check if the row contains exactly 2 elements
# # # #                 if len(row) == 2:
# # # #                     name, mobile_no = row
# # # #                     # Insert contact into the database
# # # #                     cursor.execute('''
# # # #                     INSERT INTO contacts (name, mobile_no) VALUES (?, ?)
# # # #                     ''', (name, mobile_no))
# # # #                 else:
# # # #                     print(f"Skipping row due to incorrect number of columns: {row}")

# # # #         # Commit changes and close the connection
# # # #         conn.commit()
# # # #         print(f"Contacts from {csv_file} have been successfully imported.")
# # # #     except UnicodeDecodeError as e:
# # # #         print(f"Error reading the CSV file: {e}")
# # # #     except Exception as e:
# # # #         print(f"An error occurred: {e}")
# # # #     finally:
# # # #         conn.close()

# # # # # Call the function to insert data from contacts.csv to jarvis.db
# # # # insert_contacts_into_db()


# # # import csv
# # # import sqlite3

# # # def insert_contacts_into_db(csv_file='contacts.csv', db_file='jarvis.db'):
# # #     # Connect to the SQLite database
# # #     conn = sqlite3.connect(db_file)
# # #     cursor = conn.cursor()

# # #     # Create the contacts table if it doesn't exist
# # #     cursor.execute(''' 
# # #     CREATE TABLE IF NOT EXISTS contact (
# # #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# # #         name TEXT NOT NULL,
# # #         mobile_no TEXT NOT NULL
# # #     )
# # #     ''')

# # #     try:
# # #         with open(csv_file, 'r', encoding='utf-8') as file:
# # #             reader = csv.reader(file)
# # #             next(reader)  # Skip header row if it exists
            
# # #             for row in reader:
# # #                 # Check if the row contains exactly 2 elements
# # #                 if len(row) == 2:
# # #                     name, mobile_no = row
# # #                     # Insert contact into the database
# # #                     cursor.execute('''
# # #                     INSERT INTO contacts (name, mobile_no) VALUES (?, ?)
# # #                     ''', (name, mobile_no))  # Tuple insertion
# # #                 else:
# # #                     print(f"Skipping row due to incorrect number of columns: {row}")

# # #         # Commit changes and close the connection
# # #         conn.commit()
# # #         print(f"Contacts from {csv_file} have been successfully imported.")
# # #     except UnicodeDecodeError as e:
# # #         print(f"Error reading the CSV file: {e}")
# # #     except Exception as e:
# # #         print(f"An error occurred: {e}")
# # #     finally:
# # #         conn.close()

# # # # Call the function to insert data from contacts.csv to jarvis.db
# # # insert_contacts_into_db()


import sqlite3

# Connect to the database
conn = sqlite3.connect('jarvis.db')
cursor = conn.cursor()

# Fetch and print all contacts
cursor.execute("SELECT * FROM Contacts")
contacts = cursor.fetchall()

for contact in contacts:
    print(contact)

conn.close()


# # import csv
# # import sqlite3

# # def insert_contacts_into_db(csv_file='contacts.csv', db_file='jarvis.db'):
# #     # Connect to the SQLite database
# #     conn = sqlite3.connect(db_file)
# #     cursor = conn.cursor()

# #     # Create the contacts table if it doesn't exist
# #     cursor.execute('''
# #     CREATE TABLE IF NOT EXISTS contacttss (
# #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         name TEXT NOT NULL,
# #         mobile_no TEXT NOT NULL
# #     )
# #     ''')

# #     desired_columns_indices = [0, 1]  # Ensure this matches actual columns in the CSV file

# #     try:
# #         with open(csv_file, 'r', encoding='utf-8') as file:
# #             reader = csv.reader(file)
# #             next(reader)  # Skip header row if it exists
            
# #             for row in reader:
# #                 if row:  # Skip empty rows
# #                     # Ensure the row has enough columns before accessing the desired columns
# #                     if len(row) > max(desired_columns_indices):  # Check if row has enough columns
# #                         # Select the required columns based on indices
# #                         selected_data = [row[i] for i in desired_columns_indices]
# #                         cursor.execute('''
# #                         INSERT INTO contacttss (name, mobile_no) VALUES (?, ?)
# #                         ''', tuple(selected_data))  # Insert tuple of selected data
# #                     else:
# #                         print(f"Skipping row due to insufficient columns: {row}")

# #         # Commit changes and close the connection
# #         conn.commit()
# #         print(f"Contacts from {csv_file} have been successfully imported.")
# #     except UnicodeDecodeError as e:
# #         print(f"Error reading the CSV file: {e}")
# #     except Exception as e:
# #         print(f"An error occurred: {e}")
# #     finally:
# #         conn.close()

# # # Call the function to insert data from contacts.csv to jarvis.db
# # insert_contacts_into_db()

# import csv
# import sqlite3

# def insert_contacts_into_db(csv_file='contacts.csv', db_file='jarvis.db'):
#     # Connect to the SQLite database
#     conn = sqlite3.connect(db_file)
#     cursor = conn.cursor()

#     # Create the contacts table if it doesn't exist
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS contacts (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         mobile_no TEXT NOT NULL
#     )
#     ''')

#     desired_columns_indices = [0, 100]  # Ensure this matches actual columns in the CSV file

#     try:
#         with open(csv_file, 'r', encoding='utf-8') as file:
#             reader = csv.reader(file)
#             next(reader)  # Skip header row if it exists
            
#             for row in reader:
#                 if row:  # Skip empty rows
#                     # Ensure the row has enough columns before accessing the desired columns
#                     if len(row) > max(desired_columns_indices):  # Check if row has enough columns
#                         # Select the required columns based on indices
#                         selected_data = [row[i] for i in desired_columns_indices]
                        
#                         # Print the selected data for debugging
#                         print(f"Selected data: {selected_data}")
                        
#                         # Insert selected data into the database
#                         cursor.execute('''
#                         INSERT INTO contacts (name, mobile_no) VALUES (?, ?)
#                         ''', tuple(selected_data))  # Insert tuple of selected data
#                     else:
#                         print(f"Skipping row due to insufficient columns: {row}")

#         # Commit changes and close the connection
#         conn.commit()
#         print(f"Contacts from {csv_file} have been successfully imported.")
#     except UnicodeDecodeError as e:
#         print(f"Error reading the CSV file: {e}")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         conn.close()

# # Call the function to insert data from contacts.csv to jarvis.db
# insert_contacts_into_db(
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    
# import csv
# import sqlite3

# def insert_contacts_into_db(csv_file='contacts.csv', db_file='jarvis.db'):
#     # Connect to the SQLite database
#     conn = sqlite3.connect(db_file)
#     cursor = conn.cursor()

#     # Create the contacts table if it doesn't exist
#     cursor.execute(''' 
#     CREATE TABLE IF NOT EXISTS contacts ( 
#         id INTEGER PRIMARY KEY AUTOINCREMENT, 
#         name TEXT NOT NULL, 
#         mobile_no TEXT NOT NULL 
#     ) 
#     ''')

#     try:
#         with open(csv_file, 'r', encoding='utf-8') as file:
#             reader = csv.reader(file)
#             next(reader)  # Skip header row if it exists
            
#             for row in reader:
#                 if row:  # Skip empty rows
#                     # Check if the row has at least two columns (name and mobile number)
#                     if len(row) > 1:
#                         # The first column (name) and the last column (mobile number)
#                         name = row[0]
#                         mobile_no = row[-1]

#                         # Print the selected data for debugging
#                         print(f"Selected data: Name = {name}, Mobile = {mobile_no}")

#                         # Insert data into the database
#                         cursor.execute('''
#                         INSERT INTO contacts (name, mobile_no) VALUES (?, ?)
#                         ''', (name, mobile_no))  # Insert as tuple (name, mobile_no)
#                     else:
#                         print(f"Skipping row due to insufficient columns: {row}")

#         # Commit changes and close the connection
#         conn.commit()
#         print(f"Contacts from {csv_file} have been successfully imported.")
#     except UnicodeDecodeError as e:
#         print(f"Error reading the CSV file: {e}")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         conn.close()

# # Call the function to insert data from contacts.csv to jarvis.db
# insert_contacts_into_db()




# import sqlite3

# def delete_table(db_file='jarvis.db', table_name='contactss'):
#     # Connect to the SQLite database
#     conn = sqlite3.connect(db_file)
#     cursor = conn.cursor()

#     try:
#         # Execute the DROP TABLE command to delete the table
#         cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
#         conn.commit()
#         print(f"The table '{table_name}' has been deleted successfully.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         conn.close()

# # Call the function to delete the 'contacts' table
# delete_table()

# conn = sqlite3.connect('jarvis.db')  # Ensure you're connecting to the correct DB file
# cursor = conn.cursor()
