from typing import Any, Dict


class mqttConfig:
    """[summary]
    """

    def __init__(self, **kwargs):
        """[summary]
        """
        self.mqtt_base_topic = kwargs.get("base_topic")
        self.mqtt_host = kwargs.get("mqtt_host")
        self.mqtt_port = kwargs.get("mqtt_port")
        self.mqtt_user = kwargs.get("mqtt_user")
        self.mqtt_password = kwargs.get("mqtt_password")
        self.mqtt_interval = kwargs.get("interval")

    def get_mqtt_base_topic(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.mqtt_base_topic

    def get_mqtt_host(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.mqtt_host

    def get_mqtt_port(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.mqtt_port

    def get_mqtt_user(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.mqtt_user

    def get_mqtt_password(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.mqtt_password

    def get_mqtt_interval(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.mqtt_interval


if __name__ == "__main__":
    pass
