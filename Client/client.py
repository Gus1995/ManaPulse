from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/home')
def home():
    print ('Application started')

    player1_mana = {'{B}': 0, '{W}': 2,'{G}': 0,'{R}': 0,'{U}': 0}

    hand_cards = [
        {'name': 'Card 1', 'image_url': url_for('static', filename='7ed-84-mahamoti-djinn.jpg')},
        {'name': 'Card 2', 'image_url': url_for('static', filename='2ed-39-savannah-lions.jpg')},
        {'name': 'Card 3', 'image_url': url_for('static', filename='itp-54-plains.jpg')},
        {'name': 'Card 4', 'image_url': url_for('static', filename='itp-54-plains.jpg')},
    ]

    return render_template('home.html', cards=hand_cards, player1_mana=player1_mana)

if __name__ == '__main__':
    app.run(debug=True)
