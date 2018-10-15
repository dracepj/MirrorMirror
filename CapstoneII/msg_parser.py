import json
import pika
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
local_ip_address = s.getsockname()[0]

print("Listening on: %s" % local_ip_address)

creds = pika.PlainCredentials('config_user', 'cfguser')
parms = pika.ConnectionParameters('192.168.0.107', 5672, '/', creds)
connection = pika.BlockingConnection(parms)
channel = connection.channel()

channel.queue_declare(queue='config_settings', durable=True)

def callback(ch, method, properties, body):
	print("Received payload %r" % body)
	body_str = body.decode('utf-8')
	settings = json.loads(body_str)
	print(settings)
	ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='config_settings')

channel.start_consuming()
