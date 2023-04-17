import threading
import asyncio

from flask import Flask, jsonify


print(f"In flask global level: {threading.current_thread().name}")
app = Flask(__name__)

@app.route("/test", methods=["GET"])
def index():
    print(f"Inside flask function: {threading.current_thread().name}")
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(hello())
    return jsonify({"result": result})

@app.route("/hhh")
async def hello():
    print(f"Inside flask function: {threading.current_thread().native_id}")
    await asyncio.sleep(5)
    return str(threading.current_thread().native_id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4567, debug=False)