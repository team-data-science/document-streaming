from kafka import KafkaConsumer

#consumer = KafkaConsumer()

# define a consumer that waits for new messages
def kafka_python_consumer():
    
    # Consumer using the topic name and setting a group id
    consumer = KafkaConsumer('ingestion-topic', group_id='mypythonconsumer',bootstrap_servers='localhost:9092',)
    for msg in consumer:
      print(msg)

print("start consuming")

# start the consumer
kafka_python_consumer()

print("done")
