from flask import Flask, request, jsonify
import datetime
import uuid

app = Flask(__name__)

# Mock database for events and alerts
events = []
alerts = {}
location_type_thresholds = {
    "highway": 4,
    "city_center": 3,
    "commercial": 2,
    "residential": 1,
}

# Helper function to check if an alert can be generated
def can_generate_alert(location_type):
    now = datetime.datetime.now()
    last_alert_time = next((a['timestamp'] for a in alerts if a['location_type'] == location_type), None)
    if last_alert_time is None or (now - last_alert_time).total_seconds() >= 300:
        return True
    return False

# Rule engine to generate alerts
def generate_alerts():
    for location_type, threshold in location_type_thresholds.items():
        unsafe_events = [e for e in events if e['location_type'] == location_type and not e['is_driving_safe']]
        if len(unsafe_events) >= threshold and can_generate_alert(location_type):
            alert_id = str(uuid.uuid4())
            alerts[alert_id] = {
                'alert_id': alert_id,
                'timestamp': datetime.datetime.now(),
                'location_type': location_type,
                'message': f"Unsafe driving detected in {location_type}"
            }

# Define the POST /event endpoint to receive driving events
@app.route('/event', methods=['POST'])
def receive_event():
    data = request.get_json()
    events.append(data)
    generate_alerts()
    return jsonify({'message': 'Event received'}), 201

# Define the GET /alert endpoint to retrieve all alerts
@app.route('/alerts', methods=['GET'])
def get_alerts():
    return jsonify(list(alerts.values()))

# Define the GET /alert/{alert_id} endpoint to retrieve an alert by ID
@app.route('/alert/<string:alert_id>', methods=['GET'])
def get_alert_by_id(alert_id):
    alert = alerts.get(alert_id)
    if alert:
        return jsonify(alert)
    return jsonify({'message': 'Alert not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
