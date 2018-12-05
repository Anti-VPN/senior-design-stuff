# Identifeye 

1 and 2.) [Project Abstract, Team Names, Advisor Name, and Description](https://github.com/Identifeye/senior-design-assignments/blob/master/Project-Description.md) 

3.) User Stories and Design Diagrams 

* [User Stories](https://github.com/Identifeye/senior-design-assignments/blob/master/User_Stories.md)

* [Design Diagram Level 0](https://github.com/Identifeye/senior-design-assignments/blob/master/Design%20Diagrams/design_diagram_level_0.PNG)

In this diagram we are depicting the input which is all the data we have collected about a user. At first it will be analyzed text 
and as the project expands it will include the other attributes such as the user’s IP address, and friend groups as shown in the diagram. From there 
the user data will be stored and sent through our prediction model to see if they are a close match to a banned or malicious user.
Then the system will output the results with a probability prediction of if the user is likely one of the banned users or not.

* [Design Diagram Level 1](https://github.com/Identifeye/senior-design-assignments/blob/master/Design%20Diagrams/Design_Diagram_Level_1.pdf)

In this diagram the input is the same analyzed text and then we will expand to raw text and other attributes about the user. In this System 
we break down the IP address analysis, friend group analysis, and text analysis into separate entities. This is because they will all require 
different methods of analysis to compare the attributes. After the multiple types of analysis are computed they are gathered and output as a probability 
that indicates how sure the system is that the user in question matches one of the banned users. 


* [Design Diagram Level 2](https://github.com/Identifeye/senior-design-assignments/blob/master/Design%20Diagrams/design%20diagram%20level%202.pdf)

 In this diagram we show that our application is a plug in to a third party application that will be providing the same input as described in 
the first two diagrams. It details that there will be an interfacing library that is dependent on the language used in the 
third party application. The data will then be passed into our core analysis server which does the text analysis, IP address analysis, and friend 
group analysis. Which is all hooked up to an API that can send out alerts to the third party if our analysis has found a malicious user. 
In addition to these stretch goals there will be a web application that comes with our plugin library to help give the third party 
visual graphs of the banned users, and options on how to handle suspected malicious users. 

4.) [Project Tasks and Timeline](https://github.com/Identifeye/senior-design-assignments/blob/master/Milestones_Timeline_Effort_Matrix.md)

5.) [ABET Constraint Essay](https://github.com/Identifeye/senior-design-assignments/blob/master/ABET_Constraint_Essay)

6.) [Slideshow](https://github.com/Identifeye/senior-design-assignments/blob/master/Senior%20Design%20Presentation.pdf)

7.) Self-Assessment Essays 

* [Zak](https://github.com/Identifeye/senior-design-assignments/blob/master/Assignment%203/fahey.md)

* [Brendan](https://github.com/Identifeye/senior-design-assignments/blob/master/Assignment%203/FisherAssignment3.pdf)

* [Mitchell](https://github.com/Identifeye/senior-design-assignments/blob/master/Assignment%203/haas_assignment_3.md)

8.) Professional Biographies

* [Zak](https://github.com/Identifeye/senior-design-assignments/blob/master/Biographies/fahey.md)

* [Brendan](https://github.com/Identifeye/senior-design-assignments/blob/master/Biographies/BrendanFisherProfBio.md)

* [Mitchell](https://github.com/Identifeye/senior-design-assignments/blob/master/Biographies/mitchell_haas_bio.md)
