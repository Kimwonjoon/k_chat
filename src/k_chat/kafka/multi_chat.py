from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads
from datetime import datetime
import threading

def produc():
    p = KafkaProducer(
        bootstrap_servers=['13.125.118.73:9092'],
        value_serializer = lambda x : dumps(x).encode('utf-8'),
        )
    print("채팅 프로그램 - 메시지 발신자")
    print("메시지를 입력하세요. (종료시 'exit' 입력)")

    while True:
        msg = input("You : ")
        if msg.lower() == "exit":
            break
        data = {'sender' : '김원준', 
            'message' : msg, 
            'time' : datetime.today().strftime("%Y-%m-%d %H:%M:%S")}    
        p.send('input', value = data)
        p.flush()

    print("채팅 종료")

def consum():
    consumer = KafkaConsumer(
        'input',
        bootstrap_servers = ["ec2-13-125-118-73.ap-northeast-2.compute.amazonaws.com:9092"],
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id='chat_group',
        value_deserializer = lambda x : loads(x.decode('utf-8')))
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
producer = threading.Thread(target=produc)
consumer = threading.Thread(target=consum)

producer.start()
consumer.start()

producer.join()
consumer.join()

