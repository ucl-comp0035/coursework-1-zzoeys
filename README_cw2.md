# Coursework 2

## Technical information
### Repository URL
[Repository](https://github.com/ucl-comp0035/coursework-1-zzoeys.git)

### Set-up instructions

No additional requirements beyond requirements.txt.

## Requirements definition and analysis


### Requirements identification methods

Firstly, a context diagram is built to gain insight into interface requirements. This is a form of interface analysis, a BABOK elicitation technique (International Institute of Business Analysis, 2015), and it enables the understanding of the users that send and receive data to and from the system at a high-level of abstraction. 

Ideally, a focus group would also be conducted with aspiring business owners to learn about their requirements for the web application. During a focus group, participants can build on the responses of others and comment on any differing opinions. This makes focus groups useful for understanding a collective view (Kitzinger, 1995) and would allow the product team to gain an understanding of the aspiring business owners’ needs and how the proposed web application can best support these needs. 

However, due to ethical and time restrictions, brainstorming will be used instead of focus groups. The context diagram will guide the process of brainstorming so that requirements of all users of the system can be identified. User stories are also added and refined as the design process is carried out, such as when more detail was added to the acceptance criteria after drawing the wireframe. For example, the acceptance criteria for a separate view to enlarge the data on the dashboard was added as design research was conducted to specify the wireframe for the dashboard. 

### Context diagram




### Requirement specification method

Data Driven Scrum (DDS) was chosen as the project methodology to guide the use of sprint planning as DDS is an agile methodology and a core principle of agile development is developing software that is user-focused. Thus, creating user stories was chosen as the method of requirement specification as they keep the product team focused on the value of their software’s features and how they address a particular need of the client (https://www.atlassian.com/agile/project-management/user-stories). User stories articulate the desired purpose of the system and provide the basis for communication and collaboration between the product team about the user’s requirements. User stories are also meant to be easily understood and revised, which is helpful for an inexperienced product team like that of this project.

The feature of a developer being able to whitelist a user's emails so that 

### Prioritisation method

### Documented and prioritised requirements
Link to the full list of documented and prioritised requirements.

Trello was used, here. Click the labels at the top of each card to see the name of the labels.


## Design
### Structure and flow of the interface

#### User flows

#### Design Research for Application Design

A dashboard for the data visualisations was chosen to be created as it is an accessible way of visually consolidating the most relevant information for a user to view (Subotin, 2017). To improve usability, it is important for the dashboard to include filters that enable users to customize what data is displayed. It is also important for the data to be displayed in a minimized view, but with a feature that allows users to show more details in a separate view. These features were thus added as acceptance criteria in the user stories.


#### Wireframes

Lucidchart was used to create the wireframes for the web app. As the user of the web app would tend to use their laptops to access the app instead of other devices like their mobile phone, the sketch would assume the user is accessing the web app on their laptop.

![Wireframe 1. User logs in](wireframes/1_user_logs_in.png)

#### Class diagram

A class diagram was created for a high level visualisation of the model of the web application. [why create a class diagram]

A data-driven approach was chosen to identify the classes and their attributes and methods, and the relationships between the classes. This approach was chosen as it utilises analysing the user stories to draw out potential classes. Thus, when the user stories get refined throughout the development process as feedback from external stakeholders is received, it would be easier to detect how the classes would change. As a responsibility-driven approach focuses on identifying all the requirements from the start , it may not suit this project which is involves an inexperienced team so the user stories would change over time.

To create the filtering function as specified in the user stories, the Filter Pattern was chosen as the design function (Tutorials Point, 2021). It involves utilising concrete classes to implement the operations and attributes defined by the interface class. 

As it is not possible to create of class of type 'interface' in Python unlike in Java, the design pattern can still be applied by utilising different methods of creating a class with similar functions to that of an 'interface' class. 

Criteria interface and concrete classes implementing this interface to filter list of Person objects.


<from sarah>
Conceptually this makes sense. A class diagram is a model of your application. As a model of your design intent I personally think this makes sense. You are correct in that you can't create a class of type interface in Python, you have choices (you may have already read the article but if not see https://realpython.com/python-interface/). Given that I don't know which students' coursework will be moderated, I would suggest that rather than try to modify the diagram again that you write in the markdown and explain your reasons for applying this design pattern. You can also note that the diagram is modelling the interface concept (ie that you want there to be a filter method for which the actual implementation is handled by the classes that use it) even though you are aware that there is no specific interface keyword in Python.


Low coupling etc

#### Routes


| Route | View | Controller Function |
| :----- | :----- | :----- |
| /login | 1.1 | login() Checks the entered account info against the details in the database, returns an error if details are incorrect, otherwise redirects users to the main page. |
| /signup | 1.1.1 | signup() Checks the entered email against the whitelisted emails in the database, returns an error if the email is not present, otherwise store the login details in the database and redirects users to the main page. |
| /main | 1.2 | index() Renders home page. |
| /visualisation | 1.1.1 | filter() enlarge() |
| /visualisation/create_filter |  | create_filter() |
| /forum |  | delete() edit() (change you can't have more than one controller in a view)|
| /forum/create |  | submit() |
| /news |  |  |
| /settings |  | reset_password() |
| /settings/developer |  | whitelist() |


### Relational database design

#### ERD
An ERD diagram is created.

For the saved filters, instead of storing the list of boroughs and years in the filter as a list as modelled in the class diagram, first normalisation was performed. Other considerations made were to introduce a *user id* field to ensue that the primary key of each table is an integer 

SQLite, the database to be used, doesn't allow data to be stored as a date-time format and boolean, so the integer format for UNIX time

Boolean values are stored as integers 0 (false) and 1 (true) [https://www.sqlite.org/datatype3.html]

#### Data dictionary

| Key | Attribute | Data type | Constraint |
| :----- | :----- | :----- | :----- |
| PK | user_id | Integer | Not null, |
|  | username | Text | Not null |
|  | name | Text | Not null |

|  | name | Integer | 0 or 1 |

## Testing

Unit tests

### Choice of unit testing library

Pytest was chosen because it is simpler to use and unlike unittest, doesn't [require creating classes and defining the testing functions within that class]
scalable and simple tests
[https://www.pythonpool.com/python-unittest-vs-pytest/]

Accessibilty of testing using selenium axe [https://pypi.org/project/axe-selenium-python-dev/]
The code is in the file test_accessibility, however, it cannot be run as geckodriver has to be installed on Firefox [https://www.guru99.com/gecko-marionette-driver-selenium.html] When the webpage has been launched, this will be added

To ensure code quality, standard conventions for Python from PEP8, PEP257 were used

Process of checking for bugs in the project development stage
https://www.mitchlacey.com/blog/managing-bugs-in-scrum-and-agile-projects/

### Tests
test_user


### Test results
Provide evidence that the tests have been run and the results of the tests (e.g. screenshot).

### Continuous integration 
Consider using GitHub Actions (or other) to establish a continuous integration pipeline. If you do so then please provide a link to the .yml and a screenshot of the results of a workflow run.




## References

Delete this instruction text before submitting:

- Include references to any templates you have used.
- If you justify any of your choices with references then remember to also include these.
- Use any [referencing style](https://library-guides.ucl.ac.uk/referencing-plagiarism/referencing-styles) that you are
  used to using in your course.


International Institute of Business Analysis. (2015). A Guide to the Business Analysis Body of Knowledge (Babok Guide). International Institute of Business Analysis. 

Kitzinger, J., 1995. ‘Qualitative Research: Introducing focus groups’. BMJ, 311(7000), pp.299–302. Available at: <https://www.bmj.com/content/311/7000/299.short?casa_token=uJ4gtahRwrAAAAAA:2k59gth8O5qcSTJ9OTiid4f8Gu-u5oXe8svsPsgYXGLltwIUv0kjsTXThj-n-lAxUbHrtoeofWQ4> [Accessed Nov 24, 2021]. 

Subotin, S., 2017. Dashboard Design - Considerations and Best Practices. Designers. Available at: https://www.toptal.com/designers/data-visualization/dashboard-design-best-practices [Accessed December 13, 2021]. 

TutorialsPoint https://www.tutorialspoint.com/design_pattern/filter_pattern.htm 