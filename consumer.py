from pykafka import KafkaClient

client = KafkaClient(hosts="10.25.217.78:9095")
print(client.topics)
topic = client.topics['my.test']

consumer = topic.get_simple_consumer()
for message in consumer:
    if message is not None:
        print(message.offset, message.value)
print("done.")
