# Gym_management_app_Python_Project




## Setup

### Languages and Frameworks used:

Python, HTML, CSS, PostgreSQL, Flask

### Initiate the postreSQL database

To run it, cd into the `Final_Project` directory and do the following:

```bash
# Terminal
createdb gym
psql -d gym -f db/gym.sql 
```

Then you can run the `console.py` file.

```bash
python3 console.py
```

This will create two tables and populate it with multiple rows

### Validate creation in Postico

If you have Postico, you can validate that the database has been setup:

1. Connect to localhost, and navigate to localhost

2. Local host should be populated with two tables: Classes and Members

3. Inside those tables should be populated with entries into rows

### Install flask

The first thing we'll do, is download and install Flask:

```bash
# terminal

pip3 install Flask
```

### Run flask

You can run your first web application, with the following command:

```bash
# terminal

flask run
```
You should see the following:

```bash
* Serving Flask app "app.py"
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://localhost:4999/ (Press CTRL+C to quit)
```

### Open project in browser

The project should now open. 
