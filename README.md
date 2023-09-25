# Enview_PRJ
# Driver Monitoring System

## Description

The Driver Monitoring System is a service that helps track and analyze driver behavior to improve road safety. It receives driving events from IoT devices installed in vehicles and generates alerts based on predefined rules.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/Enview_PRJ.git

   cd Enview_PRJ
Usage
To use the Driver Monitoring System, follow these steps:

Start the application:

2. python app.py
   Make API requests to send driving events and retrieve alerts.
   
API Endpoints
POST /event
Description: Send a driving event to the system.

Request Format: JSON

Example Request:   
{
  "timestamp": "2023-09-25T12:00:00",
  "is_driving_safe": false,
  "vehicle_id": "123",
  "location_type": "highway"
}

{
  "message": "Event received"
}
GET /alert/{alert_id}
Description: Retrieve an alert by ID.

Example Request: /alert/1

Example Response:
{
  "alert_id": 1,
  "timestamp": "2023-09-25T12:05:00",
  "location_type": "highway",
  "message": "Unsafe driving detected in highway"
}
Testing
To test the Driver Monitoring System, you can use tools like curl to send requests to the API endpoints and verify the responses.

License
This project is licensed under the MIT License. See the LICENSE file for details.
   

