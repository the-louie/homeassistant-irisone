DOMAIN = "irisone"


async def async_setup(hass, config):
    hass.states.async_set("irisone.initilized", True)

    # Return boolean to indicate that initialization was successful.
    return True
