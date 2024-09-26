I think i should implement sql functionalities. That way i would be able to save todo tasks.

Current Plan:
check ways to design a good database
design and make the database
connect with existing program such that program remains functional across multiple executions.

Currently the app needs to work for a single user. So i think a single "todos" table which contains all the tasks and its attributes is enough. We would have to come back to this later when we try to implement multiple users.
So, the database currently requires a table "todos" that has the following attributes:
* task_id integer
* task text
* summary text
* completed integer

I have decided to make changes to the 'status' attribute and replace it with a 'completed' attribute such that a boolean value can be used to denote its status. *Note - this is made for sqlite and thus no boolean datatype available. The data will be stored as int (0 or 1)

Update:
So the sqlite database has been implemented and works pretty well. Now i would like to add online functionality. Restful Api should be implemented. Adding CRUD functionality seems to be the logical next step.