from flask import Flask, render_template, request, redirect, url_for, session
from telestrations import Telestrations
from waitress import serve


app = Flask(__name__)
app.secret_key='development_key_69420hthtuhtuhtuhtu'

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/generate')
def generate_image():
    prompt = request.args.get('prompt','')
    T = Telestrations(styles=["Simple line drawing"])
    img_url = T.get_image_url_from_prompt(prompt)
    session['img_url'] = img_url
    img_url = session.get('img_url', None)

    return render_template(
        'gptelestrations.html',
        prompt = prompt,
        img_url = img_url)
    


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)

