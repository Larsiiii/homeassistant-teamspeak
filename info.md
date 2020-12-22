[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]

_Component to integrate with a [Teamspeak 3 Server instance][teamspeak3_server]._

_DISCLAIMER: This project is a private open source project and doesn't have any connection with TeamSpeak Systems, Inc._

**This component will set up the following platforms.**

Platform | Description
-- | --
`sensor` | Shows info from the configured Teamspeak 3 Server.


The following information can be found under Attributes
### Serverinfo
Attribute | Description
-- | --
`unique_identifier` | Unique identifier of the configured Teamspeak Server
`status` | Online status
`name` | Servername
`platform` | Platform the server is hosted on (e.g Windows, Linux, Mac)
`port` | Port the server listens on
`version` | Currently installed Teamspeak verison
`maxclients` | Maximum simultaneous allowed client connections
`reservedslots` | Number of reserved slots
`clientsonline` | Number of connections (includes Server query users)
`clientconnections` | Number of connected clients
`channelsonline` | Number of available channels
`created` | Unix time stamp of server creation date
`uptime` | Seconds since server start

### Clients
### Channels

{% if not installed %}
## Installation

1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Teamspeak 3 Server"
2. Enter the IP address of your Teamspeak 3 Server
3. Enter username and password for a valid Server Query Account. The credentials for the Server Query Admin Account can be found in the Teamspeak server logs after the first start:
```
------------------------------------------------------------------
               Server Query Admin Account created
         loginname= "serveradmin", password= "ZS8PRONS"
         apikey= "BADUFzEGXK60NntGmTWYGkfH6nSrM9Dh_SThG7X"
------------------------------------------------------------------
```

{% endif %}


## Configuration is done in the UI

<!---->

***

[teamspeak3_server]: https://www.teamspeak.com/en/
[hacs]: https://github.com/custom-components/hacs
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/Larsiiii/teamspeak-homeassistant-integration.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/Larsiiii/teamspeak-homeassistant-integration.svg?style=for-the-badge
[releases]: https://github.com/Larsiiii/teamspeak-homeassistant-integration/releases

