from flask import Flask, request
from flask_cors import CORS
from classSlack import SlackApprovedService
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/slack/approved", methods=['POST'])
def slack_service():
    data = json.loads(request.data)
    # slack.push(added_date, idi, description)

    added_date = data.get("added_date")
    idi = data.get("id")
    description = data.get("description")
    slack.push_test(added_date, idi, description)

    return "Success"


if __name__ == '__main__':
    slack = SlackApprovedService("config.yaml")
    # slack.message("START -> slack-approved-service")
    app.run(host=slack.host, port=slack.port)
