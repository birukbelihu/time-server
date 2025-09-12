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
git clone https://github.com/BirukBelihu/TimeServer.git
```

Go Inside The Project

```
cd TimeServer
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

Start The Time Server

```
python main.py
```

If You're Calling The API From External Clients(Android Or Web) Don't Forget To Expose The Port Using [Ngrok](https://ngrok.com).

```
ngrok http 5000
```

**N.B** Replace 5000 With Your Own PORT If You're Using Different Port Number. 

Sample Request Using **[cURL](https://curl.se/)**

```
curl http://IP_ADDRESS:PORT/api/v1/time/current/zone?timeZone=Africa/Addis_Ababa
```

Response

```
{
  "date": "03/04/2025",
  "dateTime": "2025-04-03T19:52:05.599935+03:00",
  "day": 3,
  "dayOfWeek": "Thursday",
  "dstActive": false,
  "hour": 19,
  "milliSeconds": 599,
  "minute": 52,
  "month": 4,
  "seconds": 5,
  "time": "19:52",
  "timeZone": "Africa/Addis_Ababa",
  "year": 2025
}
```

Get All The Available Time Zones

```
curl https://IP_ADDRESS:PORT/api/v1/time/current/zone/timeZones
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

The Rest Of The Steps Are Same

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for more details.


