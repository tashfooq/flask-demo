from flask import Flask, request, abort
from datetime import datetime, timedelta

app = Flask(__name__)

appointments = []

def round_up_to_nearest_30(timestamp):
    return timestamp + (datetime.min - timestamp) % timedelta(minutes=30)

def abort_if_same_day_appointment(timestamp, user_id, appointments, datetime_format):
    for appointment in appointments:
        if appointment["user_id"] == user_id and datetime.strptime(appointment["datetime"], datetime_format).date() == timestamp.date():
            abort(409, "User already has an appointment on this datetime")

@app.route('/')
def hello():
    return "Maven Appointment Scheduler"

@app.route('/api/appointments/<user_id>')
def getAppointments(user_id):
    global appointments
    result = []
    for appointment in appointments:
        if appointment["user_id"] == int(user_id):
            result.append(appointment)
    if not result:
        abort(404, "User does not exist")
    return {"appointments": result}

@app.route('/api/appointments', methods=['POST'])
def addAppointment():
    global appointments
    datetime_format = "%m/%d/%Y %H:%M"
    timestamp = datetime.strptime(request.json['datetime'], datetime_format) 
    timestamp = round_up_to_nearest_30(timestamp)

    abort_if_same_day_appointment(timestamp, request.json["user_id"], appointments, datetime_format)

    appointments.append({'user_id': request.json['user_id'], 'datetime': timestamp.strftime(datetime_format)})

    return {"appointments": appointments}, 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)