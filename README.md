# Ticket Alert

An application to notify users via email when a certain event has tickets for at most a given price threshold.

## Explanation About Project Components

The Ticket Alert application contains four main components that interact with each other: AWS Lambda function with four attached triggers, MySQL relational database, project defined Event class, and a Google Chrome extension.

Here is an explanation of each component:

- AWS Lambda function: The function carries on four responsibilities, depenedent upon the trigger that invokes it. The Lambda's responsibilities are: insert newly given data regarding an event into the database, delete all events that have already passed from the database, select all future events, conduct an API call to check whether tickets are available subject to the threshold, and if so, notify the user by sending an email using Amazon Simple Email Service, and unsubscribe a user from the notification service by deleting it from the database. The function is found under event_notifications/lambda_function.py, which calls the functions found under event_notifications/run_queries.py.

- Lambda Triggers: As mentioned above, the Lambda function can be invoked by three different triggers, where each one contains information regarding the operation the function shall carry out. The select and delete operations are each attached to a different scheduled EventBridge event, with the select operation triggering the Lambda once per hour, and the delete doing so once per day. The insert operation happens when the Lambda is invoked via an API Gateway that is called from the Chrome extension, that will pass into the Lambda an event containing the operation and the information to be inserted into the database. The unsubscribe operation is attached to a second API Gateway that in its path parameters passes the id of the event to be deleted (encrypted), and an indication whether to unsubscribe the user from this notification only or from all notifications they are subscribed to. The URL the user click on to invoke this API is in the bottom of every email that is sent with ticket notifications.

- MySQL Relational Database: The database stores all relevant information regarding a particular event. The schema for the database can be found at event_notifications/sql/create.sql. The database is hosted on Amazon RDS, and is manipulated using the Lambda function, which calls functions in event_notifications/run_queries.py.

- Event class: The event class, defined in event_notifications/event_info.py, contains all information and operations needed for finding if an event has tickets subject to the threshold. The class allows for getting the JSON of the event through an API call, look through the JSON for tickets to check if they meet the threshold, and construct a notification to be sent in an email to a user if tickets of interest are available. Unit tests for the class are found under event_notifications/test_event_info.py.

- Google Chrome extension: The Chrome extension provides an interactive user interface for the users to interact with the application. It is written in HTML and JavaScript, and can found under chrome_extension/extension/popup.html and chrome_extension/extension/popup.js, with the required manifest.json found under chrome_extension. The extension is to be operated when the user is located in a StubHub event page (e.g. concert, soccer game), and alerts the user when they try to operate it elsewhere. The extension contains two input textboxes, one for the user's email address and one for the price threshold, as well as a submit button. When the submit button is pressed, the extension performs a POST request and calls the API Gateway that invokes the Lambda to insert information into the database, passing it the given email and price threshold, as well as the performer and city, the event date and url.

## Setup

The following is an explanation of how to set up the project for use:

- AWS Lambda function: Create a Lambda function on AWS. Do not attach it to any VPC. 
The deployment package for the function must contain the following files (all in event_notifications folder) all zipped together: event_info.py, run_queries.py, lambda_function.py. It also must contain the following dependencies as well: requests, mysql-connector-python.

- Lambda Triggers: Set up two different EventBridge events, one to run once per hour and another to run once per day. Have each of those pass an event that will allow the Lambda to identify the operation. Also create an API Gateway with a POST method and attach it to the Lambda for the insert operation. For the unsubscribe API create another API Gateway with an ANY method, and connect it to a Lambda proxy. This will allow for the Lambda to access the query path parameters.

- MySQL Database: Create a MySQL Community database on AWS RDS. Make sure that the inbound rules of the security group attached to the database allows for all traffic, so that the Lambda can connect to it. To connect via code, use the mysql-connector library (or any equivalent Python MySQL connection library). Make sure to note that database username, password, endpoint (i.e. host), port and name. Store these in enviroment variables with names matching the ones in event_notifications/run_queries.py.

- Google Chrome extension: Head into chrome://extensions. Turn on developer mode, and export the entire chrome_extension folder as a new extension by choosing the Load Unpacked button and selecting the aforementioned folder.

## Future Features

- ~~Manual unsubscription options. Users should be able to choose if they want to unsubscribe from a specific notification or from all notifications.~~

- Currency conversions. Allow users to specify the currency they would like to receive their notifications in, along with a threshold in said currency. Presently the application operates with USD only.

- ~~Subscription confirmation. Send a confirmation message to users that would confirm their subscription to notifications.~~

## Limitations:

- Subscription Confirmation: When a user subscribes to an event, they receive an email to confirm their subscription by clicking a link. Currently, the confimation email that is sent is the one that verifies an email identity in AWS SES. Due to sandbox constraints, the email is not customized but is the standard AWS email. In a production environment, this step may even be completely skipped over and the confirmation emails will be completely different.