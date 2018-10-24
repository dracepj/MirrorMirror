import json
import pika
import socket
from filelock import Timeout, FileLock

class MessageParser:
	channel = None
	settings_file = "./conf/settings.json"
	
	def handle_msg(self, channel, method, header, body):
		print("Received payload %r" % body)
		body_str = body.decode('utf-8')
		settings = json.loads(body_str)
		print(settings)
		lock = FileLock(self.settings_file + ".lock", timeout=2)
		s_data = None
		channel.basic_ack(delivery_tag = method.delivery_tag)
		try:
			with lock:
				open(self.settings_file, 'w').write(body_str)
				print(s_data)
		except Timeout:
			print("failed to acquire lock")
		finally:
			lock.release()
	
	def get_local_ip(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
		return s.getsockname()[0]
	
	def on_declare_queue(self, frame):
		channel.basic_consume(self.handle_msg, queue='config_settings')
	
	def open_channel(self, connection):
		connection.channel(self.on_open_channel)
	
	def on_open_channel(self, new_channel):
		global channel
		channel = new_channel
		channel.queue_declare(callback=self.on_declare_queue, queue='config_settings', durable=True)
		channel.basic_qos(prefetch_count=1)
#		channel.basic_consume(self.callback, queue='config_settings')

	def start_listening(self):
		print("Listening on: %s" % self.ip)
		creds = pika.PlainCredentials('config', 'cfg_user')
		parms = pika.ConnectionParameters(self.ip, 5672, '/', creds)
		connection = pika.SelectConnection(parms, self.open_channel)
		try:
			connection.ioloop.start()
		except KeyboardInterrupt:
			connection.close()
			connection.ioloop.start()

	def __init__(self):
		self.ip = self.get_local_ip()

msg = MessageParser()
msg.start_listening()


