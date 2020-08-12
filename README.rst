.. image:: https://travis-ci.com/kbalko/flask_blog_app.svg?branch=master
   :target: https://travis-ci.com/kbalko/flask_blog_app

.. image:: https://coveralls.io/repos/github/kbalko/flask_blog_app/badge.svg?branch=master
   :target: https://coveralls.io/github/kbalko/flask_blog_app?branch=master

.. image:: https://app.statuscake.com/button/index.php?Track=QjIa1aJ2zN&Days=1000&Design=1
   :target: https://www.statuscake.com






Microblog Flask App  & CI/CD
=============================
General info
-----------------

Flask `microblog <https://microflaskapp.herokuapp.com/devops>`_ application with Continuous Integration/Continuous Deployment.


The application allows you to register users, log in, edit your profile, add content, view other users' content, observe / not observe other users, and reset your password via e-mail verified with a token.
In case of failure, the administrator receives an email with error logs. Find out more `here <https://github.com/kbalko/flask_blog_app/tree/master/docs>`_.

Apllication is integrated with:

- `TravisCI <https://travis-ci.com/github/kbalko/flask_blog_app>`_

- `Docker <https://hub.docker.com/r/kbalko/hello-world-printer>`_

- Jenkins

- `Heroku <https://microflaskapp.herokuapp.com>`_

- `Statuscake <https://www.statuscake.com>`_

- `Coveralls <https://coveralls.io/github/kbalko/flask_blog_app>`_


Linter tool:

- Flake8

Tech-stack
------------------
- Python
- Flask
- SQLAlchemy
- Bootstrap

All dependencies are store in requirements.txt and test_requirements.txt

Getting started
---------------

- preparing a virtual environment:

  ::

    # ubuntu, add to ~/.bashrc
    $ source /usr/local/bin/virtualenvwrapper.sh

    $ mkvirtualenv wsb-simple-flask-app
    $ pip install -r requirements.txt
    $ pip install -r test_requirements.txt

  or just use target from Makefile:

  ::

    # install dependencies
    $ make deps


- Run application:

  ::

    # target from Makefile:
    $ make run

    #runs the command:
    PYTHONPATH=. FLASK_APP=hello_world flask run

- Running tests:

  ::

    $ PYTHONPATH=. py.test
    $ PYTHONPATH=. py.test  --verbose -s

  or just use target from Makefile:

  ::

    $ make test
    $ make_xunit
    $ make test_complexity
    $ make test_cov


- Tests with Robot Framework and Selenium library:

  ::

    $ robot test.robot

    # without browser window
    $ robot -v BROWSER:headlessfirefox test.robot
    # target from Makefile:
    $ make robot_test

  Tests are running automatically in TravisCI  after  pushing changes on Github.

- To continue work on the project

  ::

    $ source /usr/local/bin/virtualenvwrapper.sh
    $ workon wsb-simple-flask-app

    ...
    $ deactivate
