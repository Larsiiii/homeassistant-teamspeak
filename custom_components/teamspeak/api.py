"""Teamspeak 3 API Client."""
import logging
import ts3

TIMEOUT = 10


_LOGGER: logging.Logger = logging.getLogger(__package__)


class TeamspeakApiClient:
    """Teamspeak API Client."""

    def __init__(self, host: str, username: str, password: str) -> None:
        """API Client constructor."""
        self._host = host
        self._username = username
        self._password = password
        self._session = None

    def establish_connection(self, host, user, pwd):
        """Establish connection to teamspeak3 server."""
        ts3conn = None
        try:
            ts3conn = ts3.query.TS3Connection(host)
            ts3conn.login(client_login_name=user, client_login_password=pwd)
            self._session = ts3conn
        except ts3.query.TS3QueryError as err:
            _LOGGER.error(
                "Unable to connect to Teamspeak Server. %s", err.resp.error["msg"]
            )

    def terminate_connection(self):
        """Terminate connection to teamspeak3 server."""
        self._session.quit()
        self._session = None

    async def async_get_data(self) -> dict:
        """Get data from teamspeak3 server."""
        if self._session is None:
            self.establish_connection(self._host, self._username, self._password)
        try:
            # data = self.client.get_data()
            self._session.use(sid=1)
            serverinfo = self._session.serverinfo().parsed[0]
            clientlist = self._session.clientlist().parsed
            channellist = self._session.channellist().parsed
            # self.terminate_connection()
            return {
                "clients": clientlist,
                "serverinfo": {
                    "unique_identifier": serverinfo.get(
                        "virtualserver_unique_identifier"
                    ),
                    "status": serverinfo.get("virtualserver_status"),
                    "name": serverinfo.get("virtualserver_name"),
                    "platform": serverinfo.get("virtualserver_platform"),
                    "port": serverinfo.get("virtualserver_port"),
                    "version": serverinfo.get("virtualserver_version").split()[0],
                    "maxclients": serverinfo.get("virtualserver_maxclients"),
                    "reservedslots": serverinfo.get("virtualserver_reserved_slots"),
                    "clientsonline": serverinfo.get("virtualserver_clientsonline"),
                    "clientconnections": serverinfo.get(
                        "virtualserver_client_connections"
                    ),
                    "channelsonline": serverinfo.get("virtualserver_channelsonline"),
                    "created": serverinfo.get("virtualserver_created"),
                    "uptime": serverinfo.get("virtualserver_uptime"),
                },
                "channels": channellist,
            }
        except Exception as error:  # pylint: disable=broad-except
            self._session = None
            _LOGGER.error("Could not update data - %s", error)
