
import re
from flask import Flask, render_template, request
app = Flask(__name__)

kinoko_count = 3
takenoko_count = 3

messeages = [
    "きのこおいしい！",
    "たけこのうめぇ",
]

@app.route('/')
def top():
    return render_template('index.html', **vars())

@app.route('/vote', methods=['POST'])
def answer():
    global kinoko_count, takenoko_count, messeages
    if request.form.get("item") == "kinoko":
        kinoko_count += 1
    elif request.form.get("item") == "takenoko":
        takenoko_count += 1

    messeages.append(request.form.get("message"))

    if (len(messeages) > 3):
        messeages.pop(0)

    html_messeages = ""
    for i in range(len(messeages)):
        messeage = messeages[i]
        messeage = re.sub(r'&', r'&amp;', messeage)
        messeage = re.sub(r'<', r'&lt;', messeage)
        messeage = re.sub(r'>', r'&gt;', messeage)
        messeage = re.sub(r"(\d{2,3})-\d+-\d+", r"\1-****-****", messeage)
        html_messeages += '<div class="alert {1}" role="alert"> {0} </div>'.format(
            messeage, "alert-warning ms-5" if i % 2 == 0 else "alert-success me-5"
        )

    kinoko_percent = (kinoko_count / (kinoko_count + takenoko_count)) * 100
    takenoko_percent = (takenoko_count / (kinoko_count + takenoko_count)) * 100
    return render_template('vote.html', **vars())

if __name__ == '__main__':
    app.run(debug=True)
