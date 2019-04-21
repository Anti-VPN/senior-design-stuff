# Final Report
## Project Description 
When running some online service, you have the problem of users attempting to hide their identity in order to avoid IP bans or log in to an account they shouldn’t. Our solution is to build a heuristics engine that can determine the connection between users and whether they’re doing anything malicious. It takes in data from the players such as their IP address and username and returns whether the user is doing anything suspicious.
Our project, Identifeye, has three main components the anonymizer, the interfacing library, and analysis program. The anonymizer takes in real world data and makes its secure and private while maintaining the ability to analyze it for connections between users. The interfacing libraries bridges the gap between the anonymizer and the analysis program. The analysis program stores the data in graphical data structures, analysis the data, and returns the confidence percentage of which users are connected. 

## User Interface Specifications 
Our project consistent of back end programs and does not have a visual user interface. The backend interface will be covered more in the user manual section.  

## Tests Plan and Results 
[Test Plan](https://github.com/Identifeye/senior-design-assignments/blob/master/Final_Report/Test%20Plan.pdf)

## User Manual 
[User Manual](https://github.com/Identifeye/senior-design-assignments/blob/master/User_documentation.md)
