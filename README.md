# Final_Project




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

connect to localhost, and navigate to localhost

![Localhost location](/images/readme_setup_images/Screenshot%202023-02-01%20at%2020.22.21.png?raw=true "Optional Title")

Local host should be populated with two tables
![Localhost location](/images/readme_setup_images/Screenshot%202023-02-01%20at%2020.27.44.png?raw=true "Optional Title")

Inside those tables should be populated with entries into rows
![Localhost location](/images/readme_setup_images/Screenshot%202023-02-01%20at%2020.28.56.png?raw=true "Optional Title")

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

The project should now open. To access the homepage go to:  ![Localhost location](/images/readme_setup_images/Screenshot%202023-02-01%20at%2022.11.04.png?raw=true "Optional Title")
