# k_chat

## Usage
```bash
$ python src/k_chat/kafka/prod.py
# result
DONE : 0.08131051063537598
```

## Consumer
```bash
$ bin/kafka-console-consumer.sh --topic topic1 --bootstrap-server localhost:9092

{"str": "value0"}
{"str": "value1"}
{"str": "value2"}
{"str": "value3"}
{"str": "value4"}
{"str": "value5"}
{"str": "value6"}
{"str": "value7"}
{"str": "value8"}
{"str": "value9"}
```
