import json

from caldav import DAVClient
from flask import Flask


app = Flask(__name__)

with open('config.json') as configFile:
    config = json.load(configFile)
    username = config['username']
    password = config['password']
    url = config['url']
    client = DAVClient(url=url, username=username, password=password)
    calendar = client.principal().calendar()



@app.route('/')
def get_ics():
    events = calendar.events()
    events_data = map(lambda event: event.data, events)
    return '\r\n'.join(events_data)


if __name__ == '__main__':
    app.run()
