from kafka import KafkaConsumer
from json import loads

# KafkaConsumer("받을토픽", bootstrap_servers = ["원하는 로컬"], value_deserializer = json 받는거, consumer_timeout_ms=5000 이건 자유)
consumer = KafkaConsumer("topic1",
        bootstrap_servers = ["localhost:9092"],
        value_deserializer = lambda x : loads(x.decode('utf-8')),
        consumer_timeout_ms=5000
)

print('[START] Consumer')
# 받은 메시지들 출력
for msg in consumer:
    print(msg)

print('[END] Consumer')
