# team-mcr
Team mcr's project for the "arm Intern Innovation Challenge"

This project is a web application that visualizes schools and health facilities in Colombia. The user is able to input values for 'min' and 'max' range to show all schools that are within that range of a health facility. Clicking any marker on the map shows that point's name.

In the top right corner of the web application the user can find a language selection. To enable further collaboration between those working to help Colombia and those living in Colombia the current languages of choice are 'English' and 'Spanish'.

# running the server
To run the server, you have two choices:

1. Run the app locally using Python.
2. Run the app in a Docker container.

# running the app locally
To do this, you will need to set up a Python virtualenv. There are a number of tools available to do this. I prefer
`pipenv`, but plain old `virtualenv` will work just fine too.

Install whichever virtualenv tool you prefer, set up a virtualenv in the repo directory, and activate it. Navigate to the root of the repo then run:

`./install.sh`

This will use pip to install all Python dependencies, npm to install all JavaScript dependencies, wget to download data packages, and unzip to extract them.
NOTE: Please ensure pip, wget, and unzip are installed before running this script.

Next, we have to tell Flask where the app is by setting the `FLASK_APP` environment variable. To do this:

`export FLASK_APP=$(pwd)/mcr.py`

from the root of the repository.

Now, to launch the app, use `flask run`. By default, Flask binds to 127.0.0.1:5000 -- if you visit that in your browser,
you should see the web page.

# running the app in a docker container
To do this, make sure you have Docker installed and run the following command from the root directory of the repository:

`docker build -t flask:latest . && docker run -it -p 5000:5000 flask:latest`

This uses the repo's Dockerfile to build a new docker container and runs it, mapping port 5000 on the container to
port 5000 on the host. Again, if you visit 127.0.0.1:5000 in your browser, you should see the page.

# running tests
To run tests, make sure you are in the root directory of the project and run the following command:

`python -m unittest discover -v`
