from flask import Flask
app = Flask(__name__)
from skywalking import config, agent
import os
import logging

config.collector_address= 'localhost:12800'
config.agent_name = 'benchmark-http-001'
config.protocol = 'http'
config.kafka_bootstrap_servers = 'localhost:9094'
# # config.logging_level = 'DEBUG'
agent.start()

@app.route("/get")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8000',debug=False)