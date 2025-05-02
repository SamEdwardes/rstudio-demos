import os
import sqlite3

# Database file name
db_file = "sample.db"

# Remove the database file if it already exists
if os.path.exists(db_file):
    os.remove(db_file)

# Connect to the database (this will create the file if it doesn't exist)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create a table for storing employee information
cursor.execute('''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    department TEXT,
    salary REAL,
    hire_date TEXT
)
''')

# Sample data to insert
employees_data = [
    (1, 'John', 'Smith', 'john.smith@example.com', 'Engineering', 85000.00, '2022-03-15'),
    (2, 'Sarah', 'Johnson', 'sarah.j@example.com', 'Marketing', 72000.00, '2021-11-01'),
    (3, 'Michael', 'Williams', 'michael.w@example.com', 'Engineering', 92000.00, '2020-06-22'),
    (4, 'Emily', 'Brown', 'emily.b@example.com', 'Human Resources', 68000.00, '2023-01-10'),
    (5, 'David', 'Jones', 'david.j@example.com', 'Finance', 78500.00, '2022-09-05')
]

# Insert the sample data
cursor.executemany('''
INSERT INTO employees (id, first_name, last_name, email, department, salary, hire_date)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', employees_data)

# Create a second table for departments
cursor.execute('''
CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT,
    manager_id INTEGER,
    FOREIGN KEY (manager_id) REFERENCES employees (id)
)
''')

# Sample department data
departments_data = [
    (1, 'Engineering', 'Building A, Floor 2', 3),
    (2, 'Marketing', 'Building B, Floor 1', 2),
    (3, 'Human Resources', 'Building A, Floor 1', 4),
    (4, 'Finance', 'Building C, Floor 3', 5)
]

# Insert the department data
cursor.executemany('''
INSERT INTO departments (id, name, location, manager_id)
VALUES (?, ?, ?, ?)
''', departments_data)

# Commit the changes and close the connection
conn.commit()

# Verify the data was inserted correctly
print("Employees table data:")
for row in cursor.execute("SELECT * FROM employees"):
    print(row)

print("\nDepartments table data:")
for row in cursor.execute("SELECT * FROM departments"):
    print(row)

# Close the connection
conn.close()

print(f"\nDatabase '{db_file}' created successfully with sample data.")