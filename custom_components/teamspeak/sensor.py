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
        # return f"{DEFAULT_NAME}_{SENSOR}"
        return self.coordinator.data.get("serverinfo").get("name")

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get("serverinfo").get("status")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return self.coordinator.data
