### create_random_clients
Creates random clients and stores them in .csv file. You can specify the number of clients to be created and the language (English or Russian). The random name, random phone number, random address, email depending on the client's name, random birth date and the random source the client known about the company will be generated. The clients' code is a fibonacci sequence.


### Motivation
This is my learning project.


### Tech/framework used 
- [tkinter](https://docs.python.org/3/library/tkinter.html "tkinter - Python interface to Tcl/Tk"). The program interacts with user by tkinter;
- [country-list](https://pypi.org/project/country-list/ "List of all countries with names and ISO 3166-1 codes in all languages and all data formats"). The app uses it to list all countries in the chosen language;
- [phonenumbers](https://pypi.org/project/phonenumbers/ "Python version of Google's common library for parsing, formatting, storing and validating international phone numbers"). Determines a calling code of the chosen country;
- [python-dateutil](https://pypi.org/project/python-dateutil/1.4/ "Extensions to the standard python 2.3+ datetime module"). Tells age given a birthdate;
- [csv](https://docs.python.org/3/library/csv.html "CSV File Reading and Writing"). Helps to write the data to the .csv file.


### How to use
1. Start the program;
2. In the opened tkinter window choose the language and hit "Choose";
3. Choose the country from the drop-down list and hit "Choose";
4. Enter the number of clients to be created and hit "OK";
5. You can now find results on the directory where the program located by the name 'random_clients.csv'.
