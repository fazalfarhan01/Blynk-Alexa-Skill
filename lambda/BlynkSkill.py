import requests
import json
import threading
import Errors


class BlynkSkill():
    def __init__(self, json_config_file="./config.json", debug=False):
        self.DEBUG_MODE = debug

        # Load the configuration from config.json
        with open(json_config_file) as config_file:
            self.config = json.load(config_file)

        self.URL = "http://{}:{}/{}/".format(
            self.config["server_name"], self.config["server_port"], self.config["auth_token"])
        if self.DEBUG_MODE:
            print("Server URL is:\t{}".format(self.URL))

    def get(self, virtual_pin):
        self.get_URL = "{}get/{}".format(self.URL, virtual_pin)
        response = requests.get(self.get_URL)
        content = response.content.decode("utf-8")
        if (response.status_code == 400):
            Errors.raiseError(content)
        status = json.loads(content)
        if self.DEBUG_MODE:
            print("GET URL is:\t{}".format(self.get_URL))
            print("Got Value:\t{}".format(status[0]))
        return status[0]

    def update(self, virtual_pin, value):
        parameters = {
            "value":value
        }
        self.update_URL = "{}update/{}".format(self.URL, virtual_pin)
        response = requests.get(self.update_URL, parameters)
        if self.DEBUG_MODE:
            print("Update URL is:\t{}".format(response.url))
            print("Update Status is:\t{}".format(response.status_code))
        return response.status_code

    def isConnected(self):
        self.connected_URL = "{}isHardwareConnected".format(self.URL)
        response = requests.get(self.connected_URL)
        status = response.content.decode("utf-8")
        if response.status_code == 400:
            Errors.raiseError(status)
        elif status == "true":
            return True
        elif status == "false":
            return False

    def manageMapping(self, appliance, action):
        pin = self.config["appliance"][appliance]
        value = self.config["action"][action]
        return [pin, value]
        

if __name__ == "__main__":
    
    skill = BlynkSkill()

    getResponse = skill.get("V3")
    updateResponse = skill.update("V3",0)

    print(getResponse)
    print(updateResponse)
    print(skill.isConnected())