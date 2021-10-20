# caldav-to-ics-server

**Archived since Google Calendar subscription often fails. [Davx5](https://www.davx5.com/) can sync CalDAV to Android local calendar.**

Convert CalDAV to `ics` file.

You can deploy on your server so that Google Calendar can subscribe it.

## Usage

1. install Python 3 requirements.

```shell
pip install -r requirements.txt
```

2. Fill in `config.json` with your CalDAV `URL`, `username` and `password`.

```json
{
  "url": "http://caldav.example.com",
  "username": "username",
  "password": "password"
}
```

3. Run

```shell
python3 main.py
```

4. Open [http://localhost:45000/caldav.ics](http://localhost:45000/caldav.ics) in your browser.

## License

MIT
