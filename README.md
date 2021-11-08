# Appointment Scheduling API

## Set Up

### Clone the Repo

> `git clone https://github.com/tashfooq/flask-demo.git`

### Pull the Docker Image

> `docker pull tashfooq/maven-appointment:latest`

### Navigate to Repo

> `cd ~/flask-demo`

### Run Docker Image

> `docker run -p 5001:5000 tashfooq/maven-appointment`

In the web browser visit http://localhost:5001/

## How To Use

### GET Request

***The URL***

> http://127.0.0.1:5000/api/appointments/<user_id>

The user ID must be passed in or else it will throw an error. Initially there are no appointments in memory so a get request will return 404 error with a message saying user not found

### POST Request

***The URL***

> http://127.0.0.1:5000/api/appointments

The request body must have
`{
  user_id: int,
  datetime: MM/DD/YYYY HH:MM
 }`
The datetime must be passed in that exact format -> example `11/08/2021 12:00`

The time passed in will be rounded up to the nearest 30 mins -> example `12:12` becomes `12:30`
