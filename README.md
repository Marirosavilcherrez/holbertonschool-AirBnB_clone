# AirBnB clone - The console

### __Overview__
AirBnB Clone is a program inspired by the platform that every known AirBnB website, which allows users to choose the location from cities to stay, among others.
In this case, a command interpreter has been developed from where the data can be manipulated.
Through the shell, the programmer can enter different data (such as: cities,
number of rooms, length, etc) that will be added to your database.
The program is developed in Python 3, because it is a high-level program, it has a wide variety of libraries and frameworks and is easy to use.

### __How to run the project for programmers__
1.- Install Python3: https://www.python.org/downloads/ \
2.- Have a github account: https://github.com/ \
3.- Upload the repository to your Github 

### __How to use the command line__
1.- Execute the file console.py (ex./console.py)\
2.- It will appear on the screen:\
__(hbnb)__\
3.- Write help\
4.- Different options will appear to type\
5.- Press quit to exit the command line

### __How to Contribute to the Project__
We care about your comments and suggestions if you are interested in this project do not hesitate to write us
and implement future improvements

### Usage

#### Basic Usage of The Console
---
| Command    | Usage                                     | Example                                           | Functionality                       |
|------------|-------------------------------------------|---------------------------------------------------|-------------------------------------|
| `help`     | `help`                                    | `help`                                            | displays a list of the commands     |
| `create`   | `create <class>`                          | `create User`                                     | creates a new instance of a class   |
| `show`     | `show <class> <id>`                       | `show User 123-123-123`                           | shows a specific instance           |
| `destroy`  | `destroy <class> <id>`                    | `destroy User 123-123-123`                        | deletes a specific instance         |
| `all`      | `all` or `all <class>`                    | `all User`                                        | shows all instances or a class      |
| `update`   | `update <class> <id> <attribute> <value>` | `update User 123-123-123 email 'hello@hello.com'` | updates an attribute of an instance |
| `count`    | `<class>.count`                           | `User.count`                                      | counts the number of instances      |
| `quit`     | `quit`                                    | `quit`                                            | quits the console                   |

#### Advanced Command Usage of The Console
---
| Command         | Usage                                          | Example Usage                                              |
|-----------------|------------------------------------------------|------------------------------------------------------------|
| `show`          | `<class>.show(<id>)`                           | `User.show(123-123-123)`                                   |
| `destroy`       | `<class>.destroy(<id>)`                        | `User.destroy(123-123-123)`                                |
| `all`           | `<class>.all`                                  | `User.all`                                                 |
| `update`        | `<class>.update(<id>, <attribute>, <value>)`   | `User.update(123-123-123, email, 'hello@hello.com')`       |
| `update` (dict) | `<class>.update(<id>, <dictionary>)`           | `User.update(123-123-123, {'email' : 'hello@hello.com'})`  |
---
### Installation
```
git clone git@github.com:thiago9623/AirBnB_clone.git
```
---

### Example Usage

#### Interactive Mode
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
(hbnb)
(hbnb) quit
$
```
### Authors
Marirosa Vilcherrez

Silvia Cordova
