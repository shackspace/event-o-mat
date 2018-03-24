event-o-mat
===========

.. image:: https://img.shields.io/travis/shackspace/event-o-mat.svg
   :target: https://travis-ci.org/shackspace/event-o-mat
   :alt: Continuous integration

.. image:: https://img.shields.io/codecov/c/github/shackspace/event-o-mat.svg
   :target: https://codecov.io/gh/shackspace/event-o-mat
   :alt: Coverage

event-o-mat is the shackspace event management software.

It consists of a `REST API`_ server backend written in Django_, and a single
page application frontend written in `vue.js`_.


Setup
-----

These are instructions for the development setup. If you want to run
event-o-mat in production, please refer to the ansible role instead.

To run the **server**, you'll need a Python 3.5+ virtualenv of some sort. Once
you've activated the virtualenv, execute in the ``server`` directory::

  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver

At http://localhost:8000/admin, you can now log in and create the data you want
to work with. Go to http://localhost:8000/rooms, http://localhost:8000/events
etc to see the API for yourself.

If you make changes, add or edit the appropriate tests in ``tests/`` and run
``pytest tests`` in the ``server`` directory.

To run the **frontend**, go into the ``client`` directory, and execute::

  npm install
  npm start

.. _REST API: https://en.wikipedia.org/wiki/Representational_state_transfer
.. _Django: https://www.djangoproject.com/
.. _vue.js: https://vuejs.org/
