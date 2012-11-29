Build You Very First App
============



Fast Start
----------
To create you very basic application you need make few steps:

    1. Move to your `addons` folder.

    2. Then run  ``bunny-create [type] [appname]``

    3. That's it! Now you can run XBMC and check it out in you video addons. The app will be named 'fancyapp'


    **Command examples:**
.. code-block:: text

      > cd ~/Library/Application Support/XBMC/addons
      > bynny-create video fancyapp
      > cd scrip.video.funcyapp

What You Need To Know
---------------------

After ``bunny-create`` creates app folder. You will find this file structure inside:

.. code-block:: text

    funcyapp/
    bunny/
    resources/
    addon.xml
    default.py

``fancyapp/`` - is actually you application. It is where you will store you python code.

``bunny/`` - is framework code. You will usually never want to change anything inside it.

``resources/`` - is a folder where you will store you static assets (image, video files) and xml layout files. We will discus structure of this folder later.

``addon.xml`` - is whre you specefy all information about you app. Like version, email, author name and much more.

``default.py``  - is you you entry point. It is where you application begins to do stuff. You can anytime chage this file in ``addon.xml``


