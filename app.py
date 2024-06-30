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
        messeage_html = f'<div class="alert alert-warning ms-5" role="alert"> {messeage} </div>'
        html_messeages += messeage_html

    kinoko_percent = (kinoko_count / (kinoko_count + takenoko_count)) * 100
    takenoko_percent = (takenoko_count / (kinoko_count + takenoko_count)) * 100
    return render_template('vote.html', **vars())

if __name__ == '__main__':
    app.run(debug=True)
