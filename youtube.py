import random
import time
import boto3

client = boto3.client('firehose')
deliveryStream = 'jouw-naam'

with open('/data/exportVideos.json') as file:
    line = file.readline()

    for line in file:
        data = line.strip()
        print(data)

        client.put_record(DeliveryStreamName=deliveryStream, Record={'Data': data})
        sleep = random.randint(50, 100) / 50
        time.sleep(sleep)
