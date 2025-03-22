# Expense Tracker Project

## Project Overview
This Expense Tracker project helps users manage and track their expenses efficiently using Python.

## DATABASE Structure 


### User Table
| Column Name    | Data Type        | Constraints                 | Description              |
|---------------|-----------------|----------------------------|--------------------------|
| user_id       | INT             | PRIMARY KEY, AUTO_INCREMENT | Unique ID for each user |
| name          | VARCHAR(100)    | NOT NULL                   | User's full name        |
| email         | VARCHAR(100)    | UNIQUE, NOT NULL           | User's email address    |
| password_hash | VARCHAR(255)    | NOT NULL                   | Hashed password         |
| time          | TIMESTAMP       | DEFAULT CURRENT_TIMESTAMP  | Account creation time   |

### Expenses Table
| Column Name  | Data Type        | Constraints                   | Description               |
|-------------|-----------------|------------------------------|---------------------------|
| expense_id  | INT             | PRIMARY KEY, AUTO_INCREMENT | Unique expense ID        |
| user_id     | INT             | FOREIGN KEY REFERENCES user(user_id) | User who made the expense |
| amount      | DECIMAL(10,2)   | NOT NULL                     | Expense amount           |
| category    | VARCHAR(50)     | NOT NULL                     | Expense category         |
| description | TEXT            | NULLABLE                     | Details of the expense   |
| time        | DATE_TIME       | NOT NULL                     | Datetime of the expense  |
