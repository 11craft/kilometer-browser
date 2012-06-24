Requirements
============

Linux Mint 12
-------------

Install the following apt packages:

-   git

-   python-dev

-   python-pip

-   python-pyside

Install virtualenvwrapper::

    $ sudo pip install virtualenvwrapper
    ...
    # follow further instructions to activate


Once inside virtualenv and project dir
======================================

::

    $ pip install cython
    $ pip install traits ply casuarius

Install enaml::

    $ pip install ipython
    $ git clone https://github.com/enthought/enaml
    $ cd enaml
    $ python setup.py develop

