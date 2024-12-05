from kafka import KafkaProducer
from json import dumps
import time
from datetime import datetime

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
    data = {'sender' : '김원준', 'message' : msg, 'time' : datetime.today().strftime("%Y-%m-%d %H:%M:%S")}
    p.send('input', value = data)
    p.flush()

print("채팅 종료")
