from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/simulate", methods=["POST"])
def simulate():
    agents = ["Alpha", "Beta", "Gamma"]
    resources = {agent: 50 for agent in agents}
    history = {agent: [50] for agent in agents}

    steps = request.json.get("steps", 10)

    for _ in range(steps):
        a, b = random.sample(agents, 2)
        delta = random.randint(-5, 5)
        resources[a] += delta
        resources[b] -= delta
        for agent in agents:
            resources[agent] = max(0, resources[agent])
            history[agent].append(resources[agent])

    return jsonify({"history": history})

if __name__ == "__main__":
    app.run(port=5000)
