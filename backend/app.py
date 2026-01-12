from flask import Flask, jsonify
from data_simulator import generate_sensor_data
from anomaly_detection import detect_anomaly

app = Flask(__name__)

@app.route("/data")
def get_data():
    data = generate_sensor_data()
    alert = detect_anomaly(
        data["temperature"],
        data["vibration"]
    )

    return jsonify({
        "temperature": data["temperature"],
        "vibration": data["vibration"],
        "alert": alert
    })

if __name__ == "__main__":
    app.run(debug=True)
