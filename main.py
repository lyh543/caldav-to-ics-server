import json
from icalendar import Calendar, Event

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


def merge_ics(ics_list: list):
    final_ics = Calendar.from_ical(ics_list.pop())
    for ics in ics_list:
        cal = Calendar.from_ical(ics)
        events = list(filter(lambda component: component.name == 'VEVENT', cal.walk()))
        for event in events:
            final_ics.add_component(event)
    return final_ics.to_ical()


@app.route('/caldav.ics')
def get_ics():
    ics_list = calendar.events()
    ics_data_list = list(map(lambda event: event.data, ics_list))
    return merge_ics(ics_data_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=45000)
