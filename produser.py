from pykafka import KafkaClient

client = KafkaClient(hosts="10.25.217.78:9095")
print(client.topics)
topic = client.topics['my.test']
with topic.get_sync_producer() as producer:
    for i in range(4000):
        producer.produce(b'test message ' + bytes(str(i), encoding='utf-8'))
print("done.")
