DisCraft.py
==========

.. image:: https://cdn.discordapp.com/attachments/924349559163990087/925759123092553798/discraft_server.png
		:target: https://discord.gg/butbuzKtea
		:alt: Discord Invite
.. image:: https://img.shields.io/badge/python-v3.10-blue
		:target: https://www.python.org/downloads/release/python-3100/
		:alt: Made with Python 3.10!

An easy to use Discord integrated bot for Minecraft server management!

**THIS REPOSITORY IS IN EARLY ALPHA!**
Current usage is very limited.

Key Features
-------------

- **Run easily on macOS or Linux systems!** 
    No libraries, managers or long lists of packages required! See `Installation.txt <https://github.com/CrossCheque/DisCraft/blob/5a2eba35f9cb444ed14a705ba6c1b046c3ec9b5b/Installation.rst>`_ for full details.
- **Runs on hosted servers!**
    Not all 3rd party hosts are compatible, requires shell access.
- **Note: This repository has not been tested on Windows systems.**


Installation
----------

**Built on Python 3.10+**
See `Installation.txt <https://github.com/CrossCheque/DisCraft/blob/5a2eba35f9cb444ed14a705ba6c1b046c3ec9b5b/Installation.rst>`_ for full details

Quick Overview:
Installation of `Discord.py` and `DotENV` are required to run:

.. code:: sh

    # Linux/macOS
    pip3 install discord.py
    pip3 install python-dotenv


Make the subdirectories:

.. code:: sh

    # Linux/macOS
    mkdir -p /servers/vanilla


Place your start file in the directory, and make it executable:

.. code:: sh
    
    # Linux/macOS
    chmod +x ./servers/vanilla/vanillastart.sh


Launch your bot and enjoy!


**This repository is being utilized as a learning tool, and may change heavily over time. Feel free to fork and use anything helpful to you!**

Links
------

- `Discord API <https://discord.gg/discord-api>`_
- `Discord.py <https://github.com/Rapptz/discord.py>`_
