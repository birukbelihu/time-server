from datetime import datetime
import pytz
from flask import Flask, redirect, url_for, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return redirect(url_for("get_current_time"))


@app.route("/api/v1/status")
def health():
    return jsonify({"status": "TimeServer Is Running"}), 200


@app.route("/api/v1/time/current/zone", methods=["GET"])
def get_current_time():
    time_zone = request.args.get("timeZone", "UTC")

    try:
        timezone = pytz.timezone(time_zone)
    except pytz.UnknownTimeZoneError:
        return jsonify({"error": "Unknown Time Zone Provided"}), 400

    current_time = datetime.now(timezone)

    response = {
        "year": current_time.year,
        "month": current_time.month,
        "day": current_time.day,
        "hour": current_time.hour,
        "minute": current_time.minute,
        "second": current_time.second,
        "milliSecond": current_time.microsecond // 1000,
        "dateTime": current_time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "date": current_time.strftime("%d/%m/%Y"),
        "time": current_time.strftime("%H:%M"),
        "timeZone": str(timezone),
        "dayOfWeek": current_time.strftime("%A"),
    }
    return jsonify(response)


@app.route("/api/v1/time/current/zone/availableTimeZones", methods=["GET"])
def get_available_time_zones():
    return jsonify(pytz.all_timezones)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
