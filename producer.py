import os
import time
import random
from kafka import KafkaProducer
from dotenv import load_dotenv

load_dotenv()

output_topic = os.getenv('OUTPUT_TOPIC')
bootstrap_servers = os.getenv('BOOTSTRAP_SERVERS')
sasl_username = os.getenv('SASL_USERNAME')
sasl_password = os.getenv('SASL_PASSWORD')
security_protocol = os.getenv('SECURITY_PROTOCOL', 'SASL_SSL')
sasl_mechanism = os.getenv('SASL_MECHANISM', 'PLAIN')
interval_ms = int(os.getenv('INTERVAL_MS', '1000'))

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    security_protocol=security_protocol,
    sasl_mechanism=sasl_mechanism,
    sasl_plain_username=sasl_username,
    sasl_plain_password=sasl_password,
    api_version=(0, 11, 5)
)

def generate_vitals():
    body_temp = round(random.uniform(36.0, 38.0), 1)
    heart_rate = random.randint(60, 100)
    systolic_pressure = random.randint(110, 140)
    diastolic_pressure = random.randint(70, 90)
    breaths_per_minute = random.randint(12, 20)
    oxygen_saturation = random.randint(95, 100)
    blood_glucose = random.randint(70, 140)

    return {
        'body_temp': body_temp,
        'heart_rate': heart_rate,
        'systolic_pressure': systolic_pressure,
        'diastolic_pressure': diastolic_pressure,
        'breaths_per_minute': breaths_per_minute,
        'oxygen_saturation': oxygen_saturation,
        'blood_glucose': blood_glucose
    }

def generate_anomaly(vitals):
    vitals['heart_rate'] = random.randint(150, 220)
    vitals['breaths_per_minute'] = random.randint(30, 50)
    return vitals


while True:
    vitals = generate_vitals()
    if random.random() < 0.1:  # 10% chance of anomaly
        vitals = generate_anomaly(vitals)

    try:
        producer.send(output_topic, str(vitals).encode('utf-8'))
        print(f"Sent: {vitals}")
    except Exception as e:
        print(f"Error sending message: {e}")

    time.sleep(interval_ms / 1000)
