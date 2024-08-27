from kafka import KafkaProducer
import time
import json
from tqdm import tqdm

# KafkaProducer(bootstrap_servers=["원하는 localhost"])
producer = KafkaProducer(bootstrap_servers=['ec2-43-203-210-250.ap-northeast-2.compute.amazonaws.com:9092'],
        value_serializer = lambda x : json.dumps(x).encode('utf-8'),
        #compression_type='gzip',
        batch_size=100)
# json 형식을 읽을때는 직렬?로 읽어줘야함

start = time.time() # 시작 시간 보려고

for i in tqdm(range(10000)):
    data = {'str' : 'value' + str(i)}
    # send('지정 토픽명', value = 메시지값)
    producer.send('mammamia', value = data)
    # 종료 구문
    producer.flush()
    time.sleep(0.001)

end = time.time() # 끝나는 시간 확
print(f"DONE : {end - start}")
