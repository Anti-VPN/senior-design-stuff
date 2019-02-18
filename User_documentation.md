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

## Input 
Input a matrix of data with attributes like IP, text comment, and username. 

Example: 

| Username        | IP           | Text Comment  |
| ------------- |:-------------:| -----:|
| bob11      | 127.0.01 | Hi my name is Bob  |
| not_bob11    | 127.0.0.1     |   Hi my name is Bob. |
| zebra_stripes101 | 70.127.168.235      |   Hello world |


## Output 
Outputs a list of usernames that are suspected to belong to one user.

Example: 

| Username  A    | Username B          | Reason  |
| ------------- |:-------------:| -----:|
| bob11      | not_bob11 | Matching IP, Matching Text Comment  |



## Using the Results 

Due to Authorship Identification being an emerging field these results are meant to be 
used at the users discretion.




