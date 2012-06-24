Requirements
============

Linux Mint 12
-------------

Install the following apt packages:

-   git
-   libzmq-dev
-   python-dev
-   python-pip
-   python-pyside
-   python-virtualenv

Starting from a directory of your choice,
create a "virtualenv" in which to place ``kilometer-browser``::

    $ virtualenv --system-site-packages kilometer-browser

Activate the environment to work within it::

    $ cd kilometer-browser
    $ . bin/activate

    # The prompt should now look something like this:
    (kilometer-browser) $


Once inside virtualenv
======================

Install prerequisites::

    $ pip install cython
    $ pip install casuarius ipython ply pygments pyzmq traits

Install enaml::

    $ git clone https://github.com/enthought/enaml
    $ cd enaml
    $ python setup.py develop
    $ cd ..

Install kilometer-browser::

    $ git clone https://github.com/11craft/kilometer-browser
    $ cd kilometer-browser
    $ python setup.py develop
    $ cd ..


Starting kilometer-browser
==========================

If you have your virtualenv currently active,
just run the script directly::

    $ kilometer-browser

You don't have to have it active though;
you can refer to the direct location of the script
to start it.
This is useful if you are setting up a shortcut
in a menu or on a toolbar.

For example, say you've created the virtualenv
inside a "/home/myuser/projects" directory::

    $ /home/myuser/projects/kilometer-browser/bin/kilometer-browser
