# TicketAlert

An application to notify users when a certain event has tickets for less than or equal to a given price threshold.

## Explanation About Project Components

The Ticket Alert application contains four main components that interact with each other: AWS Lambda function, MySQL relational database, project defined Event class, and a Google Chrome extension.

Here is an explanation of each component:

- AWS Lambda function: The function carries on three responsibilities, depenedent upon the trigger that invokes it. The Lambda's responsibilities are: insert newly given data regarding an event into the database, delete all events that have already passed, and select all future events, conduct an API call to check whether tickets are available (subject to the threshold), and if so, notify the user by sending an email using Amazon Simple Email Service. The function is found under requests_notify/lambda_function.py, which calls the functions found under requests_notify/run_queries.py.

- MySQL Relational Database: The database stores all relavant information regarding a particular event. The schema for the database can be found at requests_notify/sql/create.sql. The database is hosted on Amazon RDS, and is manipulated using the Lambda function, which calls functions in requests_notify/run_queries.py.

- Event class: The event class, defined in requests_notify/event_info.py, contains all information and operations needed for finding if an event has tickets subject to the threshold. The class allows for getting the JSON of the event through an API call, look through the JSON for tickets to check if they meet the threshold, and construct a notification to be sent in an email to a user if tickets of interest are available. Unit tests for the class are found under requests_notify/test_event_info.py.

- Google Chrome extension: TODO

## Setup

The following is an explanation of how to set up the project for use:

- AWS Lambda function: Create a Lambda function on AWS. Do not attach it to any VPC. 
The deployment package for the function must contain the following files (all in requests_notify folder) all zipped together: event_info.py, run_queries.py, lambda_function.py. It also must contain the following dependencies as well: requests, mysql-connector-python.

- MySQL Database: Create a MySQL Community database on AWS RDS. Make sure that the inbound rules of the security group attached to the database allows for all traffic, so that the Lambda can connect to it. To connect via code, use the mysql-connector library (or any equivalent Python MySQL connection library). Make sure to note that database username, password, endpoint (i.e. host), port and name.

- Google Chrome extension: TODO