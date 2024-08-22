from kafka import KafkaConsumer, TopicPartition
from json import loads
import os

OFFSET_FILE = "consumer_offset.txt"
# txt 파일에 offset값 저장
def save_offset(offset):
    with open(OFFSET_FILE, 'w') as f:
        f.write(str(offset))
# 저장한 파일 읽어오기
def read_offset():
    if os.path.exists(OFFSET_FILE): # 파일이 있는 경우에만 동작!!!!
        with open(OFFSET_FILE, 'r') as f:
            return int(f.read().strip())
    return None
# 아예 위에서 읽어서 반복적이게 읽어오지 않게 하자
saved_offset = read_offset()
# KafkaConsumer("받을토픽", bootstrap_servers = ["원하는 로컬"], value_deserializer = json 받는거, consumer_timeout_ms=5000 이건 자유)
consumer = KafkaConsumer(
        #"topic1",
        bootstrap_servers = ["172.17.0.1:9092"],
        value_deserializer = lambda x : loads(x.decode('utf-8')),
        consumer_timeout_ms=5000,
        # 최근에 돌린 offset들을 가져온다.
        #auto_offset_reset="earliest" if saved_offset is None else "none",
        #auto_offset_reset="latest",
        group_id = "fbi",
        enable_auto_commit=False,
)

print('[START] Consumer')

p = TopicPartition('topic1', 0)
consumer.assign([p])
if saved_offset is not None: # 파일이 있는 경우
    consumer.seek(p, saved_offset)
else: # 파일이 없는 경우
    consumer.seek_to_beginning(p)

# 받은 메시지들 출력
for msg in consumer:
    print(f"offset={msg.offset}, value={msg.value}")
    save_offset(msg.offset + 1)

# topic='topic1', partition=0, offset=79, timestamp=1724219008710, timestamp_type=0, key=None, value={'str': 'value9'}, headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=17, serialized_header_size=-1

print('[END] Consumer')
