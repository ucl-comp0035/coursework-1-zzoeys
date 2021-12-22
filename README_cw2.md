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

However, due to ethical and time restrictions, brainstorming will be used instead of focus groups. The context diagram will guide the process of brainstorming so that requirements of all users of the system can be identified. User stories are also added and refined as the design process is carried out, such as when more detail was added to the acceptance criteria after drawing the wireframe. For example, the acceptance criteria for a separate view to enlarge the data on the dashboard was added when design research was conducted to specify the wireframe for the dashboard. 

### Context diagram

<img src = diagrams/design/context_flow.png width = '1000px'>

### Requirement specification method

Data Driven Scrum (DDS) was chosen as the project methodology to guide the use of sprint planning as DDS is an agile methodology and a core principle of agile development is developing software that is user-focused. Thus, creating user stories was chosen as the method of requirement specification as they keep the product team focused on the value of their software’s features and how they address a particular need of the client (Rehkopf, 2021). User stories articulate the desired purpose of the system and provide the basis for communication and collaboration between the product team about the user’s requirements. User stories are also meant to be easily understood and revised, which is helpful for an inexperienced product team like that of this project.

### Prioritisation method

The MoSCoW prioritisation method was chosen as it complements the use of user stories and agile projects (Agile Business, 2021). Though it is simple, it provides enough detail about 'Must Have', 'Should Have', 'Could Have' and 'Won't Have this time' requirements that help project teams set and manage priorities.

The considerations made when prioritising requirements are detailed on the Trello page linked below. They are labelled with the purple label named 'Prioritisation Considerations'. 

### Documented and prioritised requirements

Trello was used, [here](https://trello.com/b/cjogVnBl/user-stories), to document user stories. Please click the labels at the top of each card to see the name of the labels.

The user stories are also documented as a PDF file [here](user_stories/user_stories.pdf).

## Design

### Design Research for Application Design

A dashboard for the data visualisations will be created as it is an accessible way of visually consolidating the most relevant information for a user to view (Subotin, 2017). To improve usability, it is important for the dashboard to include filters that enable users to customize what data is displayed. It is also important for the data to be displayed in a minimized view, but with a feature that allows users to show more details in a separate view. These features were thus added as acceptance criteria in the user stories.

As Flask will be used to create the web app, the routes and controllers (in the form of a table), models (in the form of a class diagram) and views (in the form of wireframes) will be detailed. 

### Structure and flow of the interface

#### User flows

To get a high-level model of the basic flow of a potential business owner using the site, a user flow was created.

<img src = diagrams/design/user_flow.png width = '700px'>


#### Detailed use cases

To guide the creation of the wireframes, a detailed use case was created for the process of a user signing up to the site as it is a complicated process. The creation of a use case was guided by the acceptance criteria of the user stories, but also helped to elicit more detailed acceptance criteria. For example, the feature of a developer being able to whitelist a user's emails so that only the project's clients could sign up on the site was added while drawing up the use case.

<img src = diagrams/design/use_case.png width = '800px'>


#### Class diagram

A class diagram was created for a high level visualisation of the model of the web application. A data-driven approach was chosen to identify the classes and their attributes and methods, and the relationships between the classes. This approach was chosen as it utilises analysing the user stories to draw out potential classes. Thus, when the user stories get refined throughout the development process as feedback from external stakeholders is received, it would be easier to detect how the classes would change. As a responsibility-driven approach focuses on identifying all the requirements from the start, it may not suit this project which involves an inexperienced team so the user stories would change over time.

To create the filter method as specified in the user stories for filtering the data in the visualisations, the Filter Pattern was chosen as the design pattern (tutorialspoint, 2021). It involves utilising concrete classes to implement the operations and attributes defined by the interface class, and these classes have a realisation relationship. This way, the implementation of the filter method is handled by the classes that use it and filters can be saved as saved filters. Though Python does not have an 'interface' keyword like in Java, the design pattern can still be applied by utilising different methods of creating a class with similar functions to that of an 'interface' class (Real Python, 2021). 

Despite trying to ensure low coupling, it was necessary to have the forum_comment, forum_post and user class to all be linked to each other. These classes are dependent on each other, for example, if a user's name is changed, the forum posts and comments should reflect those changes.

The resulting class diagram is shown below:

<img src = diagrams/design/class_diagram.png width = '1000px'>

#### Wireframes

Lucidchart was used to create the wireframes for the web app. As the user of the web app would tend to use their laptops to access the app instead of other devices like their mobile phone, the sketch would assume the user is accessing the web app on their laptop.

**User or developer logs in or signs up**
<img src = wireframes/wireframe_1.png width = '1000px'>
<br>
<br>

**User saves a filter**
<img src = wireframes/wireframe_2.png width = '1000px'>
<br>
<br>

**User uses the forum**
<img src = wireframes/wireframe_3.png width = '1000px'>
<br>
<br>

**User reads a news articles**
<img src = wireframes/wireframe_4.png width = '1000px'>
<br>
<br>

**User goes to the settings page**
<img src = wireframes/wireframe_5.png width = '1000px'>
<br>
<br>


#### Routes

* Note: all routes except /login and /signup require the @login_required decorator from the flask-login plugin 

| Route | View (frame in the wireframes) | Controller Function |
| :----- | :----- | :----- |
| /login | 1.1 | login() Checks the entered account info against the details in the database, returns an error if details are incorrect, otherwise redirects users to the main page. |
| /signup | 1.1.1 | signup() Checks the entered email against the whitelisted emails in the database, returns an error if the email is not present, otherwise stores the login details in the database and redirects users to the main page. |
| /main | 1.2 and 1.2.1 | index() Renders the home page with the user's first saved visualisation. filter() Renders the visualisations according to the saved filter chosen by the user. sidebar() Shows the full names of the headers when the user hovers over the sidebar. |
| /main/enlarge | 1.2.2 | enlarge() Shows the visualisation that the user clicks on in a larger pop-up. |
| /whitelist | 1.3 | whitelist() Whitelists a user's email by adding their email to the database of whitelisted emails and refreshes the whitelist page showing the newly whitelisted email at the bottom. |
| /visualisation | 2.1 | get_dash() Calls the Dash dashboard app to render the visualisations. |
| /visualisation/enlarge | 2.1.1 | enlarge() Shows the visualisation that the user clicks on in a larger pop-up. |
| /visualisation/create_filter | 2.1.2 | create_filter() Saves the current boroughs and years selected by the user as a saved filter under the name written by the user. |
| /forum | 3.1 | create_new() Shows a pop-up where the user can write the title and body of the forum post they want to write. read() When a user clicks on a forum post, shows a pop-up with the full contents of the forum post |
| /forum/<forum_post_id> (user's post)| 3.2 | edit() When a user clicks on the 'Edit post' button on a forum post created by them, shows a pop-up where they can edit the body of their post. comment() When a user clicks on the 'Comment' button, shows a pop-up where the users can comment on the post |
| /forum/<forum_post_id>/edit (user's post)| 3.2 | save() Saves the edits made to the post. delete() Deletes the post so it can no longer be accessed and removes it from the database. |
| /forum/<forum_post_id> (other user's post)| 3.3 | comment() When a user clicks on the 'Comment' button, shows a pop-up where the users can comment on the post. |
| /forum/<forum_post_id>/comment | 3.4 | submit() When a user clicks on the 'Submit' button after writing their comment, adds the details of the comment to the database, redirects users to the post page and renders the new comment on the post page. |
| /forum/create_new | 3.5 | post() When a user clicks on the 'Post' button after writing their post, adds the details of the post to the database, redirects users to the forum page and renders the new post on the forum page. |
| /news | 4.1 | get_news() Calls the third party news API to show news articles related to business news in London. |
| /news/<article_id> | 4.1.1 | read() When the user clicks on a news article, shows a pop-up with the full contents of the article. |
| /settings | 5.1 | display_settings() Returns the user's settings page with data for that user. |


### Relational database design

#### ERD

Firstly, considerations were made to ensure that the primary key of each table is an integer, so the user_id, forum_post_id, forum_comment_id and filter_id attributes were added.

SQLite, the database to be used, doesn't allow data to be stored as a date-time data type, so the text format for ISO8601 strings is used. Boolean values are also not supported so they are stored as integers 0 (false) and 1 (true) (SQLite, 2021).

To model the database with the saved filters, instead of storing the list of boroughs and years in the saved filter as a list as modelled in the class diagram, first normalisation was performed. Storing these details as a list would mean that a table cell would have one or more values which violates the requirements for 1st Normal Form (1NF). To avoid this, two tables were created linking the filter_id of the filter to the years and borough_id's of the boroughs that are in the filter. The tables, named filter_borough and filter_year, would also solve the many-to-many relationship between saved filters, boroughs and years: one filter can have many boroughs and years and one borough/year can belong to multiple filters. The resulting ERD is below:

<img src = diagrams/ERDs/ERD_saved_filter.png width = '400px'>

In the process of second normalisation to 2nd Normal Form (2NF), the table borough_name was created as the attribute borough_name is only dependent on borough_id and not the combination of filter_id and borough_id which make up the composite primary key. It also avoids duplication of data as it prevents having to store the borough name every time a borough is linked to a filter. The resulting tables have no transitive functional dependencies, so the requirements for 3rd Normal Form (3NF) are satisfied as shown in the resulting ERD at the bottom. 

To model the databases for forum posts and forum comments, referential integrity, where each foreign key references an existing primary key in the parent table (Database.Guide, 2016), is ensured. These tables also satisfy the requirements for 1NF, 2NF and 3NF as shown below:

<img src = diagrams/ERDs/ERD_forum.png width = '400px'>

A table to store the whitelisted emails added by developers was created without any relationships with other tables. This is because the table with whitelisted emails only serves one purpose to check whether new users are authenticated by checking their emails against the list of whitelisted emails. Only once the users have signed up successfully are their details added to the user database table. As the table of whitelisted emails is still necessary to model the whole process of a user's journey while using the web app despite it having no relationships to other tables, it is still appropriate to have it.

The resulting ERD is shown below:

<img src = diagrams/ERDs/ERD.png width = '800px'>


#### Data dictionary

| Table | Column name | Key |  Data type | Constraints | Description |
| :----- | :----- | :----- | :----- | :----- | :----- |
| user | user_id | PK | Integer | Not null, auto increment | Unique identifer for users |
| user | username |  | Text | Not null | The unique username of the user which is used for logging in and is displayed on their profile |
| user | name |  | Text | Can be null (like when the user has just signed up and hasn't input their name) | User's name, can be first name, last name or full name |
| user | email  |  | Text | Not null, check with regex that the email is in a valid @ and .com format | User's email that was used to sign up | 
| user | password  |  | Text | Not null | Hashed password |
| user | is_developer  |  | Integer | Not null, 0 for False or 1 for True | Whether a user has developer permissions |
| forum_post | forum_post_id | PK | Integer | Not null, auto increment | Unique identifer for forum posts |
| forum_post | user_id | FK | Integer | Not null | The user id of the writer of the forum post |
| forum_post | title |  | Text | Not null | Title of the forum post |
| forum_post | body |  | Text | Not null | Body text of the forum post |
| forum_post | date_published |  | Text | Not null, stored as text as ISO8601 strings | Date the post was published |
| forum_comment | forum_comment_id | PK | Integer | Not null, auto increment | Unique identifer for forum comments |
| forum_comment | forum_post_id | FK | Integer | Not null | The forum post id of the post that the comment belongs to |
| forum_comment | user_id | FK | Integer | Not null | The user id of the writer of the forum comment |
| forum_comment | body |  | Text | Not null | Body text of the forum comment |
| saved_filter | filter_id | PK | Integer | Not null, auto increment | Unique identifer for saved filters |
| saved_filter | saved_filter_name |  | Text | Not null | Name given by the user for the saved filter |
| saved_filter | user_id | FK | Integer | Not null | The user id of the user that created the saved filter |
| filter_borough | filter_id | FK | Integer | Not null | The filter id of the filter that contains the borough |
| filter_borough | borough_id | FK | Integer | Not null | The borough id of the  borough that is included in the filter |
| borough_name | borough_id | PK | Integer | Not null, auto increment | Unique identifer for boroughs |
| borough_name | borough_name |  | Text | Not null | Name of the borough |
| filter_year | filter_id_year | PK | Integer | Not null, auto increment | Unique identifer for the combination of the filter id and year that is included in the filter |
| filter_year | filter_id | FK | Integer | Not null | The filter id of the filter that contains the year |
| filter_year | year |  | Integer | Not null, YYYY format | The year that is included in the filter |
| whitelisted_email | whitelist_id | PK | Integer | Not null, auto increment | Unique identifer for the whitelisted email |
| whitelisted_email | whitelist_email |  | Text | Not null, check with regex that the email is in a valid @ and .com format | User's email that has been whitelisted | 


## Testing

Though it is not necessary to cite official documentation and tutorials of python libraries, I thought it would be useful to link the relevant pages of material not covered in the course as they were heavily consulted. 

The software development team of this project team will utilise a real-time bug fixing approach where bugs are fixed as they are found. This way, the consequential damage caused by the bug can be limited and team members would be provided with a learning opportunity to write better code (Lacey, 2016). 


### Choice of unit testing library

pytest was chosen because it is simpler to use and requires less code compared to unittest (Python Pool, 2021). While unittest requires developers to create a class to contain the testing functions, pytest only requires defining the test function. 

Automated web accessibility testing using [aXe and selenium](https://pypi.org/project/axe-selenium-python/) is to be performed once the web app page is running. It cannot currently be performed because there is no url. Once the web page has a url, [geckodriver for Firefox](https://www.guru99.com/gecko-marionette-driver-selenium.html) will also be installed so that the test can run. 


### Tests

<img src = test_results/test_file_structure.png width = '600px'>


Pages in the pytest documentation were referenced to [parametrize the tests](https://docs.pytest.org/en/latest/how-to/parametrize.html), to [pass a fixture as a value in parametrized tests](https://docs.pytest.org/en/latest/example/parametrize.html#indirect-parametrization) and to apply [conditional raising in a parametrized tests](https://docs.pytest.org/en/stable/example/parametrize.html#parametrizing-conditional-raising) so that it can be tested if an error is raised when specific values are passed in a parametrized test.


The file with the code for the accessibility testing is in the tests folder for reference, but when running the test please use the commands `python -m pytest -v tests/test_user.py` and `python -m pytest --cov=user tests/test_user.py` to only run the tests and see the coverage report for the test_user file as the test_accessibility file would result in errors. 


### Test results

When running `python -m pytest -v tests/test_user.py` to get the test report:

<img src = test_results/result_test_user.png width = '800px'>

When running `python -m pytest --cov=user tests/test_user.py` to get the coverage report:

<img src = test_results/result_test_user_cov.png width = '800px'>


#### Code quality

To ensure code quality, it is important to follow standard conventions for Python, such as those from PEP8 and PEP257. This was checked with the flake8 linter through Github Actions, which found the lines of code that did not adhere to style guides.

<img src = test_results/flake8.png width = '800px'>

The (Black Python code reformatter)[https://pypi.org/project/black/] was used for to ensure that PEP8 conventions were followed in the user.py, data_preparation.py, conftest.py, test_user and test_accessibility files.

<img src = test_results/black_1.png width = '800px'>
<img src = test_results/black_2.png width = '800px'>

### Continuous integration 
GitHub Actions was used to establish a continuous integration (CI) pipeline, which is especially beneficial for a project team using agile methodologies. Using a CI pipeline increases the efficiency of the software delivery process as it aids the automation of key software development processes, such as building, testing and deploying (Subrameyer, 2021). Code can also be tested more frequently which allows developers to detect and fix issues as they arise. As a result, the timing between releases can be reduced to achieve more frequent releases. 

The Python Application workflow on Github Actions was added to the project. The link to the .yml file is [here](.github/workflows/python-app.yml) and the results of a successful workflow run are shown below:

<img src = test_results/github_actions_1.png width = '800px'>
<img src = test_results/github_actions_2.png width = '800px'>

## References

Agile Business, 2021. 10 Moscow Prioritisation - Agile Business. Agile Business Consortium. Available at: https://www.agilebusiness.org/page/ProjectFramework_10_MoSCoWPrioritisation [Accessed December 19, 2021]. 

Database.Guide, 2016. What is Referential Integrity? Database.Guide. Available at: https://database.guide/what-is-referential-integrity/ [Accessed December 15, 2021]. 

International Institute of Business Analysis. (2015). A Guide to the Business Analysis Body of Knowledge (Babok Guide). International Institute of Business Analysis. 

Kitzinger, J., 1995. ‘Qualitative Research: Introducing focus groups’. BMJ, 311(7000), pp.299–302. Available at: <https://www.bmj.com/content/311/7000/299.short?casa_token=uJ4gtahRwrAAAAAA:2k59gth8O5qcSTJ9OTiid4f8Gu-u5oXe8svsPsgYXGLltwIUv0kjsTXThj-n-lAxUbHrtoeofWQ4> [Accessed Nov 24, 2021]. 

Lacey, M., 2016. Managing Bugs in Scrum and Agile Projects. Mitch Lacey &amp; Associates, Inc. Available at: https://www.mitchlacey.com/blog/managing-bugs-in-scrum-and-agile-projects/ [Accessed December 22, 2021]. 

Python Pool, 2021. Python unittest VS pytest: Choose the best. Python Pool. Available at: https://www.pythonpool.com/python-unittest-vs-pytest/ [Accessed December 19, 2021]. 

Real Python, 2021. Implementing an interface in Python. Real Python. Available at: https://realpython.com/python-interface/ [Accessed December 19, 2021]. 

Rehkopf, M., 2021. User stories with examples and a template. Atlassian. Available at: https://www.atlassian.com/agile/project-management/user-stories [Accessed December 21, 2021]. 

SQLite, 2021. Datatypes in SQLite. Datatypes In SQLite. Available at: https://www.sqlite.org/datatype3.html [Accessed December 19, 2021]. 

Subotin, S., 2017. Dashboard Design - Considerations and Best Practices. Designers. Available at: https://www.toptal.com/designers/data-visualization/dashboard-design-best-practices [Accessed December 13, 2021]. 

Subrameyer, R., 2021. 5 benefits of implementing a CI/CD pipeline. Ranorex. Available at: https://www.ranorex.com/blog/5-benefits-ci-cd-pipeline/ [Accessed December 21, 2021]. 

tutorialspoint, 2021. Design Patterns - Filter Pattern. Available at: https://www.tutorialspoint.com/design_pattern/filter_pattern.htm [Accessed December 15, 2021]. 