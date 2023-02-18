# A fastapi helloworld

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from skywalking import config, agent

config.collector_address= 'localhost:12800'
config.agent_name = 'benchmark-kafka-001'
config.protocol = 'kafka'
config.kafka_bootstrap_servers = 'localhost:9094'
# # config.logging_level = 'DEBUG'
agent.start()
app = FastAPI()


@app.get("/get")
async def root():
    return JSONResponse(content={"message": "Hello World"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, access_log=False)
