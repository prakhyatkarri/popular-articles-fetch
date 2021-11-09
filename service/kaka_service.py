from kafka import KafkaProducer

from properties.app_config import AppConfig


class KafkaService:
    properties = {}
    producer = None
    kafka_client = None

    def __init__(self):
        self.properties = AppConfig().kafka_properties
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            api_version=(0, 10, 0),
            # api_version=(0, 9, 4),
            batch_size=0,
            linger_ms=10,
            request_timeout_ms = 60000
        )

    def publish(self, message):
        try:
            topic = self.properties['stage_notification_topic']
            value = bytes(str(message), encoding='utf-8')
            key = bytes(str(message['id']), encoding='utf-8')

            try:
                self.producer.send(topic=topic, value=value, key=key).get(timeout=60)
                # print(self.producer.bootstrap_connected())
                # self.producer.send('foo', b'bar')
                # self.producer.flush()
            except Exception as e:
                print(f'Exception in send: {e}')

        except Exception as e:
            print(f'Exception in publish: {e}')
