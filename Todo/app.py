from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
    return render_template("index.html", tasks=tasks)

app.run(host="0.0.0.0", port=5000)
