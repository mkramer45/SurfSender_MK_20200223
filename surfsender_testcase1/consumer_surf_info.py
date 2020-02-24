import json
from time import sleep
import psycopg2

from kafka import KafkaConsumer

# This script servers as our consumer to the producer (producer_surfinfo.py)
# Once executed, this script will take the messages living in the topic & send them to an Aiven PostgreSQL database.

if __name__ == '__main__':
	parsed_topic_name = 'surf_data_topic'

	consumer = KafkaConsumer(parsed_topic_name, auto_offset_reset='earliest',
							 bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)
	for msg in consumer:
		message = msg.value.decode("utf-8")

		id_ = '5'


		conn = psycopg2.connect("dbname=surf_db user=admin3 password=admin323 host=localhost")
		cur = conn.cursor()
		# cur.execute("INSERT INTO surf_data (id, surf_info) VALUES (?,?)", (id_,message))
		cur.execute("INSERT INTO surf_conditions (wave_info) VALUES (%s)", (message,))
		conn.commit()
		cur.close()
		conn.close()


		print(message)

	if consumer is not None:
		consumer.close()

