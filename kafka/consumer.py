# 消费kafka
from kafka import KafkaConsumer
from google.protobuf.json_format import MessageToJson, Parse
import chardet


def kafkaconsumer():
    print('--------------')
    consumer = KafkaConsumer('dag-row',
                             group_id='my-group',
                             auto_offset_reset='earliest',  # 从头消费，默认latest
                             bootstrap_servers=['kafka:9092'])
    for msg in consumer:
        # print('%s:%d:%d: key=%s value=%s' % (msg.topic, msg.partition,
        #                                      msg.offset, msg.key, msg.value))

        print('msg.value.type: ', type(msg.value))


if __name__ == '__main__':
    kafkaconsumer()
