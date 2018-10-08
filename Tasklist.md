# Tasks

## Zak

1. Use gRPC to create an interfacing library in Python to communicate between the analysis server and clients.
2. Develop the core of the analysis server in Python.
   1. Implement the interfacing library in this application to accept input.
   2. Implement the interfacing library to send alerts to the API endpoints when suspicious behavior is detected.
   3. Develop a plugin system for the detection of various anomalies.
   4. Develop a plugin system to add custom flag relationship behavior.
   5. Dockerize everything.
   6. Set up the database to store user data.
   7. Develop the algorithm to determine the similarity score between two interactions.
   8. Create a system to configure where the API endpoints are.

## Mitchell

1. Develop the web server in Node.js.
   1. Write all the API functions the client needs.
   2. Fetch data from the analysis server to send in APIs.
   3. Implement an authentication system.
2. Develop the web client in React.
   1. Create data visualization reports.
   2. Authentication support.
3. Code detection of account sharing.

## Brendan

Develop the sample application and interfacing library in one langauge:

1. Code detection of mass duplicate accounts.
2. Code detection of ban evasion.
3. Create a flag for text content.
