# Identifeye

## Members

Zak Fahey - faheyzt@mail.uc.edu

Mitchell Haas - haasm3@mail.uc.edu 

Brendan Fisher - fisherb8@mail.uc.edu 

## Faculty advisor
Raj Bhatnagar

## Abstract and Background Description
The objective of this project is to build profiles on people and detect rule breaking behavior such as avoiding bans or sharing accounts. This will be done by gathering text submitted by a user such as product reviews, or social media comments. After obtaining a good amount of sample text from a user the text will be analyzed with different methods such as char n-gram analysis which identifies frequent characters used by an author. From there we will use these analyzed text to train a classifier that can predict solely off of text if a message came from one of the banned users with a high degree of probability. Then we would be able to identify if a banned user is using a different account or if people are sharing accounts. 


## Problem statement

Determining identity on the Internet is difficult. With VPNs on the rise, it's trivial for users to circumvent bans. 

## Inadequacy of current solutions

The industry defaults to banning all VPN’s, but this can prohibit valid user from accessing content. Or an application can ban an IP, but with a VPN a user can access the application by changing there IP. 

## Background skills
We have all had coop's and networking classes along with a strong base in programming and computer science. Some of us had experience managing game servers, others are taking a data analysis courses or have experience from coops in data analysis. 

## Approach
Using Python as the programming language we intended to create an application which will interface with other applications a like on a game server, web application, forum, or social network. It well then collect and store data about users and try to create a user profile that will be able to identify the user from their actions and detect when they are breaking the rules. 

First we try out authorship identification on a cleaned up dataset of Amazon Commerce Reviews to text out methods of text analysis, and different classifying techniques. Then we can expand into taking in raw text to analysis and interfacing with outside applications. 



