# Database
The `initialise_or_create_database_at(path: str)` function commands the creation of an SQLite3 Databse in the specified path. Any method for databse access supported by SQLlite3 can then be applied to your work. 

See [database_access.py](/QCoDeS/src/qcodes_testing/database_access.py) for python interfacing with db.
There are also a multitude of software that can visualize SQLlite3 databases, such as the [SQLite Database viewer](https://sqlitebrowser.org/)

As I've discovered. It's cumbersome to access database elements outside of the program. Thus, make your best efforts to save and export the relevant data for your experiments during execution. 

For measurement contexts, there are datasaver objects that give immediate access to the running data, while dond returns the output data when called. 

See [transconductance.py](/QCoDeS/src/qcodes_testing/data/test.py) to see results from data taken in a qcodes sweep accessed after execution. 