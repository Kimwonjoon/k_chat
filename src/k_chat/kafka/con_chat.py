from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
        'input',
        bootstrap_servers = ["ec2-13-125-118-73.ap-northeast-2.compute.amazonaws.com:9092"],
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id='chat_group',
        value_deserializer = lambda x : loads(x.decode('utf-8'))
        )
print("채팅 프로그램 - 메시지 수신")
print("메시지 대기 중 ...")

try:
    for m in consumer:
        data = m.value
        sender = data['sender']
        print(f"[{sender}] : {data['message']} (받은 시간 : {data['time']})")
except KeyboardInterrupt:
    print("채팅 종료")
finally:
    consumer.close()
