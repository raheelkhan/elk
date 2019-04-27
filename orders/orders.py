"""
Generates random orders logs for last week where order status will
be completed or rejected
"""
import logging
import logstash
import sys
import random
from datetime import datetime, timedelta

host = 'logstash'

logger = logging.getLogger('orders')
logger.setLevel(logging.INFO)
logger.addHandler(logstash.TCPLogstashHandler(host, 5959, version=1))

end_date = datetime.now()
order_status = ("completed", "rejected")

for i in range(0, 100):
    logger.info("Order processed", extra={
        "order_number": random.randint(1, 1000),
        "order_status": random.choice(order_status),
        "order_date": (end_date - timedelta(random.randint(0, 7))).strftime("%Y-%m-%d")
    })
