# User Guide 

## Getting Started 
Determining identity on the Internet is difficult. With VPNs on the rise, it's trivial for users to circumvent bans.
Identifeye is software plug in that you can add to your application to help detect ban evasion. In this user guide we 
will be explaining how to use Identifeye with your application. 

## About Identifeye
This project builds profiles on people and detects rule breaking behavior such as avoiding bans
or sharing accounts. This is done by inputting a matrix of data with attributes like IP, text comment,
username, etc... Then the program compares IP's, usernames, and text comments of the input and outputs 
a list of usernames that are suspected to belong to one user, and why. 

## How to Use the Analysis Program 

### Input 
Input a matrix of data with the attributes ID, Account Name, Character Name, IP, UUID, IP Geolocation, Is Banned, and Activity Time.
Example: 

![Example Input Data](https://github.com/Identifeye/senior-design-assignments/blob/master/input_data.PNG "Example Input Data")



### Output 
Outputs a list of usernames that are suspected to belong to one user, and the confidence of the connections.

Example: 

![Example Output Data](https://github.com/Identifeye/senior-design-assignments/blob/master/Output_anlysis_program.PNG "Example Output Data")


### Running the Code 
First download the code and integrate it into your project. Then update the data you would like analyzed and run the program. 

[Analysis Program](https://github.com/Identifeye/senior-design-assignments/blob/master/anlaysis.py)

### Using the Results 

Once you have obtained the results a staff member can set which confidence threshold, they would like to review at, and the take appropriate action to accounts that are confidently run by the person.




