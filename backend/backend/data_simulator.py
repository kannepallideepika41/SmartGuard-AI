import random
import time

def generate_sensor_data():
    temperature = random.randint(20, 100)
    vibration = round(random.uniform(0.1, 5.0), 2)

    return {
        "temperature": temperature,
        "vibration": vibration
    }

if __name__ == "__main__":
    while True:
        data = generate_sensor_data()
        print(data)
        time.sleep(2)
