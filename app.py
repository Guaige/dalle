import os, time

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = 


@app.route("/", methods=("GET", "POST"))
def index():
    
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
        """
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))
        """
        return redirect(url_for("index", result=response['data'][0]['url']))
        #return redirect(url_for("index", result=animal))
    result = request.args.get("result")
    return render_template("index.html", result=result)



def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )

host = '0.0.0.0'
port = 80
app.run(host=host, port=port, debug=True)