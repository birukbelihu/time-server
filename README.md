![GitHub Repo stars](https://img.shields.io/github/stars/BirukBelihu/Cody)
![GitHub forks](https://img.shields.io/github/forks/BirukBelihu/Cody)
![GitHub issues](https://img.shields.io/github/issues/BirukBelihu/Cody)
![GitHub license](https://img.shields.io/github/license/BirukBelihu/Cody)


## Time Server

A Simple [Flask](https://flask.palletsprojects.com/) Time API to get real-time time information without any third-party API.

---

## Features

- Highly Customizable
- Get Comprehensive List Of Time Data Such As:
  - Milliseconds
  - Seconds
  - Minutes
  - Hour
  - Day
  - Month
  - Year
  - Date & Many More
- Supports 500+ World Time Zones
- Can be easily integrated with Android, Web, or any project via a simple HTTP request.

---

## Usage

TimeServer Is Live On Render

[TimeServer](https://timeserver-y2yg.onrender.com)

## Running

To get started with Time Server on your local machine, follow these steps:

## 🛠️ Prerequisites

Make sure you have the following installed:

- [Git](https://git-scm.com/)

```bash
git --version
```

- [Python](https://www.python.org/)

```bash
python --version
```

- [Docker(Only If you want to run the server in docker container)](https://www.docker.com/)

```bash
docker --version
```

Clone The Repository

```
git clone https://github.com/BirukBelihu/time-server.git
```

Go Inside The Project

```
cd time-server
```

### Set up Python virtual environment(I recommend using [uv](https://github.com/astral-sh/uv) for lightning speed)

### With uv

```bash
uv venv .venv
```

### With Python

```bash
python -m venv .venv
```

# Activate virtual environment

```bash
.venv\Scripts\activate # On Windows
```

```bash
source .venv/bin/activate # On Linux, WSL & macOS
```


Install Required Dependencies

```
pip install -r requirements.txt
```

Go Inside The Source Folder

```bash
cd src
```

Start The Time Server

```
python app.py
```

If You're Calling The API From External Clients(Android Or Web) Don't Forget To Expose The Port Using [Ngrok](https://ngrok.com).

```
ngrok http 5000
```

**N.B** Replace 5000 With Your Own PORT If You're Using Different Port Number. 

Sample Request Using [cURL](https://curl.se/)

```
curl http://IP_ADDRESS:PORT/api/v1/time/current/zone?timeZone=Africa/Addis_Ababa
```

Response

```
{
  "date": "12/09/2025",
  "dateTime": "2025-09-12T11:20:53+0300",
  "day": 12,
  "dayOfWeek": "Friday",
  "dstActive": false,
  "hour": 11,
  "milliSecond": 7,
  "minute": 20,
  "month": 9,
  "second": 53,
  "time": "11:20",
  "timeZone": "Africa/Addis_Ababa",
  "year": 2025
}
```

Get All The Available Time Zones

```
curl http://192.168.1.3:5000/api/v1/time/current/zone/availabletimeZones
```

Response

```
[
    "Africa/Abidjan",
    "Africa/Accra",
    "Africa/Addis_Ababa",
    "Africa/Algiers",
    "Africa/Asmara",
    "Africa/Asmera",
    "Africa/Bamako",
    "Africa/Bangui",
    "Africa/Banjul",
    ...
]
```

Get Server Status

```
 http://IP_ADDRESS:PORT/api/v1/status
```

Run Tests Using Pytest

```
pytest test_server.py
```

To Run TimeServer In [Docker](https://www.docker.com) Container Follow This Steps.



Build Docker Image

```
docker build -t timeserver .
```

Run The Server

```
docker run -p 5000:5000 timeserver
```

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for more details.


