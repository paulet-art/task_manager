# Task Manager Application 📋

Welcome to the Task Manager Application! This Flask-based web application allows users to efficiently manage their tasks.

## Features 🚀

- **Create Tasks**: Easily create new tasks with titles, descriptions, statuses, and due dates.
- **View Tasks**: See a list of all tasks and their details.
- **Update Tasks**: Modify existing tasks, including their titles, descriptions, statuses, and due dates.
- **Delete Tasks**: Remove tasks that are no longer needed.

## Errors and Resolutions during the project 🛠️

### Error: Failed to find Flask application or factory in module 'app'

- **Cause** 🚨: Flask cannot locate the Flask application object (app) or factory function in the specified module.
- **Resolution** ✅: Ensure that the FLASK_APP environment variable is correctly set to `app`. You can set it using:

  ```bash
  export FLASK_APP=app
  ```

### Error: ModuleNotFoundError: No module named 'config'

- **Cause** 🚨: Flask cannot locate the config module.
- **Resolution** ✅: Ensure that the `config.py` file exists in the `app` directory and contains the necessary configuration settings. Also, check the import statement in the `__init__.py` file to ensure it correctly imports the config module.

### Error: ModuleNotFoundError: No module named 'config'

- **Cause** 🚨: Flask cannot locate the config module.
- **Resolution** ✅: Ensure that the `config.py` file exists in the `app` directory and contains the necessary configuration settings. Also, check the import statement in the `__init__.py` file to ensure it correctly imports the config module.

# Learning Journey: REST API with PostgreSQL and Flask 📚

In my learning journey, I've delved into the world of building RESTful APIs using Flask, a popular Python web framework, and PostgreSQL, a powerful open-source relational database system.

## What I've Learned 🎓

### Flask

Flask provides a simple yet powerful framework for building web applications in Python. Some key concepts I've learned about Flask include:

- **Routing**: Defining routes to handle HTTP requests and specifying the corresponding view functions.
- **Request Handling**: Processing incoming requests and accessing request data such as form inputs or JSON payloads.
- **Response Generation**: Generating HTTP responses to return data or render templates.
- **Middleware**: Utilizing middleware for tasks such as error handling, authentication, and logging.
- **Extensions**: Integrating Flask extensions like Flask-SQLAlchemy and Flask-RESTful to add additional functionality.

### PostgreSQL

PostgreSQL is a robust and feature-rich relational database management system. Throughout my exploration of PostgreSQL, I've gained insights into:

- **Database Design**: Designing schemas, tables, and relationships to organize and structure data efficiently.
- **Querying**: Writing SQL queries to retrieve, insert, update, and delete data from the database.
- **Transactions**: Understanding transaction management to ensure data integrity and consistency.
- **Performance Optimization**: Implementing indexing, query optimization, and other performance tuning techniques.
- **Concurrency Control**: Handling concurrent access to the database to prevent data corruption and ensure data consistency.

## Next Steps 🚀

Armed with knowledge of Flask, PostgreSQL, and RESTful API principles, I'm excited to continue honing my skills and exploring more advanced topics such as authentication, authorization, deployment, and scaling.






