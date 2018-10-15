import pika
import sys
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='config_settings', durable=True)

message = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
channel.basic_publish(exchange='',
                      routing_key='config_settings',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent %r" % message)
connection.close()
