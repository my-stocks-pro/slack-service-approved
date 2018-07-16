from slackclient import SlackClient
import yaml
import os
from datetime import datetime


class SlackApprovedService:
    def __init__(self, slack_conf):
        self.conf = self.read_config(slack_conf)
        self.host, self.port = self.check_env()
        self.slack_client = SlackClient(self.conf.get('token'))
        self.slack_channel = self.conf.get('channel')
        self.jpeg = "https://image.shutterstock.com/mosaic_250/0/0/{}.jpg"
        self.link = "https://www.shutterstock.com/image/{}"
        self.message = "Date: {} {}\nID: {}"

    def check_env(self):
        host = self.conf.get('host')
        hostprod = self.conf.get('hostprod')
        port = self.conf.get('port')

        prod = os.getenv("PROD")
        if prod == "1":
            return hostprod, port
        return host, port

    def push_message(self, message):
        self.slack_client.api_call(
            "chat.postMessage",
            channel=self.slack_channel,
            text=message)

    def push(self, added_date, idi, description, jpeg, link, curr_time):
        link_id = "<{}|{}>".format(link, idi)
        message = self.message.format(added_date, curr_time, link_id)
        attachments = [
            {
                "title": description,
                "image_url": jpeg
            }]
        try:
            self.slack_client.api_call(
                "chat.postMessage",
                channel=self.slack_channel,
                text=message,
                attachments=attachments)
        except Exception as err:
            return err

    @staticmethod
    def read_config(conf_path):
        with open(conf_path, 'r') as file:
            return yaml.load(file)

    def push_test(self, added_date, idi, description):
        jpeg = self.jpeg.format(idi)
        link = self.link.format(idi)
        curr_time = datetime.now().strftime("%H:%M")

        link_id = "<{}|{}>".format(link, idi)
        message = self.message.format(added_date, curr_time, link_id)
        attachments = [
            {
                "title": description,
                "image_url": jpeg
            }]
        print(self.slack_channel, message, attachments)