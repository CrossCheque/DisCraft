# DisCraft
## Discord Bot for Minecraft Server Management!
### v.0.01a ALPHA BUILD

### 1. PURPOSE
    Discord management of Minecraft servers, initially targeting: Server Uptime, Server Status, Active Users, Server Start, Server Reboot, Notifications on Reboot, Crash, Suspend.
    
### 2. SCOPE
    Initially developed for FORGE based Minecraft servers.
    Creation of DisCraft.js for server hooks.
        a. Transmit thread ID for multi-instance servers.
        b. Identify crashes.
        c. Suspend/stop server thread after X time IDLE
    Creation of DisCraft Bot.
        a. Send reboot, start and status commands.
        b. Nofiticaions for server crashes.
        c. Promote /op though discord.
            
### 3. CONFIGURATION
    
    
### 4. COMMANDS
    !op
        Sends /op command to server. Requires [username] and [serverID].
        Usage: !op [Toot'sToot] [CrossCheque]
    !players
        Lists connected users.
        Usage: !players
    !reboot
        Sends /stop command and restarts server. Requires [serverID].
        Usage: !reboot [Toot'sToot]
    !say
        Sends /say command to server. Requires [serverID].
        Usage: !say [Toot'sToot] Hello World!
    !server
        Lists [serverID] by friendly name, thread ID and status. Requires configuration of DisCraft back end.
        Usage: !list
    !start
        Sends start command to DisCraft bot. Requires [serverID].
        Usage: !start [Toot'sToot]
    !status
        Displays if server is running, connected users, and uptime. Requires [severID].
        Usage: !status [Toot'sToot]
    !stop
        Sends /stop command to server. Requires [serverID].
        Usage: !stop [Toot'sToot]
```
