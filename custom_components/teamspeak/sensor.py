"""Sensor platform for Teamspeak 3 Server."""
from .const import DEFAULT_NAME, DOMAIN, ICON, SENSOR
from .entity import TeamspeakEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([TeamspeakSensor(coordinator, entry)])


class TeamspeakSensor(TeamspeakEntity):
    """teamspeak Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        serverinfo = self.coordinator.data.get("serverinfo")
        if serverinfo is not None:
            return self.coordinator.data.get("serverinfo").get("name")
        else:
            return "No Connection to Server"

    @property
    def state(self):
        """Return the state of the sensor."""
        serverinfo = self.coordinator.data.get("serverinfo")
        if serverinfo is not None:
            return self.coordinator.data.get("serverinfo").get("status")
        else:
            return "No Connection to Server"

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return self.coordinator.data
