import os, time
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = 


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/dalle", methods=("GET", "POST"))
def dalle():

    if request.method == "POST":
        animal = request.form["animal"]
        since = time.time()
        response = openai.Image.create(
          prompt=animal,
          n=1,
          size="512x512"
        )
        print('time_gen : ', time.time() - since)
        since = time.time()
        image_url = response['data'][0]['url']
        return redirect(url_for("dalle", result=response['data'][0]['url']))
    result = request.args.get("result")
    return render_template("dalle.html", result=result)

@app.route("/codex", methods=("GET", "POST"))
def codex():
    
    if request.method == "POST":
        animal = request.form["animal"]
        since = time.time()
        response = openai.Completion.create(
          model="code-davinci-002",
          prompt=animal,
          temperature=0,
          max_tokens=4000,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )
        print('time_gen : ', time.time() - since)
        since = time.time()
        codes = response['choices'][0]['text']
        return redirect(url_for("codex", result=response['choices'][0]['text']))
    result = request.args.get("result")
    return render_template("codex.html", result=result)


@app.route("/davinci", methods=("GET", "POST"))
def davinci():
    
    if request.method == "POST":
        animal = request.form["animal"]
        since = time.time()
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt=animal,
          temperature=0,
          max_tokens=4000,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )
        print('time_gen : ', time.time() - since)
        since = time.time()
        answer = response['choices'][0]['text']
        return redirect(url_for("davinci", result=animal + response['choices'][0]['text']))
    result = request.args.get("result")
    return render_template("davinci.html", result=result)


host = '0.0.0.0'
port = 80
app.run(host=host, port=port, debug=True)
