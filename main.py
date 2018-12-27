from pykafka import KafkaClient
client = KafkaClient(hosts="10.25.153.206:9095")
for k, v in client.topics.items():
    print("{}: {}".format(k, v))
