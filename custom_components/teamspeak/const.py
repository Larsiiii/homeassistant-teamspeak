"""Constants for teamspeak."""
# Base component constants
NAME = "Teamspeak 3 Server"
DOMAIN = "teamspeak"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.1.0"
MANUFACTURER = "TeamSpeak Systems, Inc"
ATTRIBUTION = f"Data from this is provided by a Teamspeak 3 Server by {MANUFACTURER}."
ISSUE_URL = "https://github.com/Larsiiii/teamspeak-homeassistant-integration/issues"

# Icons
ICON = "mdi:headset"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]


# Configuration and options
CONF_ENABLED = "enabled"
CONF_HOST = "host"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
