from project.xzceb-flask_eng_fr.final_project import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_French")
def english_to_French():
    textToTranslate = request.args.get('textToTranslate')
    url.set_service_url(url)
    french_text = url.translate(text = english_text, model_id = 'en-fr').get_result()
    return "Translated text to French"


@app.route("/french_to_English")
def french_to_English():
    textToTranslate = request.args.get('textToTranslate')
     url.set_service_url(url)
    english_text = url.translate(text = french_text, model_id ='fr-en').get_result()
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
