import docker
import redis
import socket

from flask import Flask


app = Flask(__name__)


r = redis.Redis(
    host='redis-server', 
    port=6379, 
    db=0, 
    decode_responses=True
    )
r.set("visitors", 0)


@app.route("/")
def index():
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    container = client.containers.get(socket.gethostname())
    container.stop()
    r.set("visitors", int(r.get("visitors")) + 1)
    return "No of visitors: " + r.get("visitors")


@app.route("/hello")
def hello():
    return "Hello"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
