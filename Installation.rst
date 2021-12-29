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


Setting Up the Environment
----------

This installation assumes you have already registered a bot with Discord. If you have not, you can start the application process `Here <https://discord.com/developers>`_.

Fist, let's install or update `Python <https://www.python.org/downloads/release/python-3100/>`_ to version 3.10 or greater.

.. code:: sh
    
    # Linux
    sudo apt install python3.10

    # macOS
    #Use above download or use Homebrew
    brew install python


Once complete, we need to make sure the certificate store is up to date. 

.. code:: sh

    # Linux
    ./Python\ 3.10/Install\ Certificates.command

    # macOS
    ./Applications/Python\ 3.10/Install\ Certificates.command


This may ask you to install `Certifi <https://pypi.org/project/certifi/>`_ which can be accomplished with:

.. code:: sh

    # Linux/macOS
    pip3 install certifi


When that's complete, we need to get `Discord.py <https://github.com/Rapptz/discord.py>`_ which can be done with python.

.. code:: sh

    # Linux/macOS
    pip3 install discord.py


We also need to grab `DotENV <https://pypi.org/project/python-dotenv/>`_ to handle our Discord authentication.

.. code:: sh

    # Linux/macOS
    pip3 install python-dotenv


Setting Up the Bot
----------

The current verion of the bot is hard-coded to run one server, called Vanilla. It is set up to run in a subdirectory of DisCraft, which you can make:

.. code:: sh

    # Linux/macOS
    mkdir -p /servers/vanilla


Should you want to edit where this is pointing, open ``DisCraft.py`` and look for:

.. code:: py

    @commands.command(brief='Start!',description='Open a new shell, start a vanilla server.')
    async def start(self, ctx):
        await ctx.send("Starting!")
        os.system("screen -dmS vanillaMC bash -c 'cd servers/vanilla; ./vanillastart.sh'")


Here, you will want to change either the subdirectory ``servers/vanilla``, or the shell ``vanillastart.sh``.
When the directory is set up, create your shell file and make it executeable:

.. code:: sh
    
    # Linux/macOS
    chmod +x ./servers/vanilla/vanillastart.sh


Personally, I prefer to use `Paper <https://papermc.io/downloads>`_ for running vanilla or lightly modded servers. Feed the Beast servers can also be run this way, just point the bot to the ``start.sh`` file or rename it to ``vanillastart.sh``.

If you need a solid startup script:

.. code:: sh

    #!/bin/bash
    cd /DisCraft/servers/vanilla/

    java -Xms4G -Xmx4G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -Dlog4j2.formatMsgNoLookups=true -jar paper_1.18.1.jar nogui


All that is left is running the bot. Navigate your shell to the bot's folder, and run ``Discraft.py``.

.. code:: sh

    # Linux/macOS
    ./discraft.py


If you get an error that the shell is not executable:

.. code:: sh
    
    # Linux/macOS
    chmod +x ./discraft.sh


Launch your bot and enjoy!


**This repository is being utilized as a learning tool, and may change heavily over time. Feel free to fork and use anything helpful to you!**

Links
------

- `Discord API <https://discord.gg/discord-api>`_
- `Discord.py <https://github.com/Rapptz/discord.py>`_
