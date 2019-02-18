# User Guide 

## Getting Started 
Determining identity on the Internet is difficult. With VPNs on the rise, it's trivial for users to circumvent bans.
Idenifeye is software plug in that you can add to your application to help detect ban evansion. In this user guide we 
will be explaining how to use Identeye with your application. 

## About Identifeye
This project builds profiles on people and detect rule breaking behavior such as avoiding bans
or sharing accounts. This is done by using gathered text submitted by a user such as product reviews, or social media
comments, along with the user's IP, and other attributes. After your data set conatin a good amount of sample text 
from a user the text is analyzed, along with 
with different methods such as char n-gram analysis which identifies frequent characters used by an author. From there we
will use these analyzed text to train a classifier that can predict solely off of text if a message came from one of the banned
users with a high degree of probability. Then we would be able to identify if a banned user is using a different 
account or if people are sharing accounts.

## Input 


## Output 


## Using the Results 




