Day 3
So, i figure i now need to create a better interface. Maybe a forms type website that can accept tasks and display them?
The plan:
explore frontend today
understand how it works 
how can it be connected to my application?
On exploring these topics I think this is what i need to do:
* Learn basic flask
* Learn about html forms
* Learn about get and post
this should let me atleast add tasks to the database using html
 So i set up a virtual env and let git ignore that folder
Installed flask in the env. Why is it a good idea to create a venv -> requirements.txt
Run "pip install requirements.txt" in the terminal(within a virtualenv) to install the required dependencies.

Made a single page web app with no funcionality that can be hosted locally using flask
Have to add :
* viewing tasks 
* adding tasks using forms

Seems like a good playlist to understand basics of flask: https://www.youtube.com/playlist?list=PLB5jA40tNf3vX6Ue_ud64DDRVSryHHr1h

Hmm - jinja loops could be used to display the tasks(maybe not cuz the list would be an sql query)
I also need to remember to write an exception for invalid deletion in the last program.