from datetime import datetime
import pytz
from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI(
    title="TimeServer",
    description="A Simple Time API to get real-time time information without any third-party API.",
    version="1.2.0",
)


@app.get("/", include_in_schema=False)
async def home():
    return RedirectResponse(url="/api/v1/time/current/zone")


@app.get("/api/v1/status", summary="Check API health")
async def health():
    return {"status": "TimeServer is running"}


@app.get("/api/v1/time/current/zone", summary="Get current time for a timezone")
async def get_current_time(
    time_zone: str = Query("UTC", alias="timeZone", description="Timezone, e.g. 'Africa/Addis_Ababa'"),
):
    try:
        timezone = pytz.timezone(time_zone)
    except pytz.UnknownTimeZoneError:
        raise HTTPException(status_code=404, detail="Unknown Time Zone Provided")

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
        "timeZone": time_zone,
        "dayOfWeek": current_time.strftime("%A"),
    }

    return JSONResponse(content=response)


@app.get(
    "/api/v1/time/current/zone/availableTimeZones",
    summary="List all available time zones",
)
async def get_available_time_zones():
    return JSONResponse(content=pytz.all_timezones)


@app.exception_handler(404)
async def not_found(_, __):
    return JSONResponse(content={"error": "Endpoint not found"}, status_code=404)


@app.exception_handler(500)
async def server_error(_, exc):
    return JSONResponse(
        content={"error": "Internal Server Error", "details": str(exc)}, status_code=500
    )
