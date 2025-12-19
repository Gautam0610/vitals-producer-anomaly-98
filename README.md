# vitals-producer-anomaly-98

This project generates and pushes random vitals data to a Kafka topic with occasional anomalies.

## Usage

1.  Clone the repository.
2.  Create a `.env` file with the following variables:

    ```
    OUTPUT_TOPIC=your_topic
    BOOTSTRAP_SERVERS=your_bootstrap_servers
    SASL_USERNAME=your_sasl_username
    SASL_PASSWORD=your_sasl_password
    SECURITY_PROTOCOL=SASL_SSL
    SASL_MECHANISM=PLAIN
    INTERVAL_MS=1000
    ```

3.  Run the Docker container:

    ```
    docker build -t vitals-producer .
    docker run vitals-producer
    ```