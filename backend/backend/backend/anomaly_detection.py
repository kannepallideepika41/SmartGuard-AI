def detect_anomaly(temperature, vibration):
    if temperature > 80 or vibration > 4.0:
        return True
    else:
        return False
