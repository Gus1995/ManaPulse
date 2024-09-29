from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/home')
def home():
    print ('Application started')

    #display hand
    hand_cards = [
        {'name': 'Card 1', 'image_url': url_for('static', filename='o90p-5-shivan-dragon.jpg')},
        {'name': 'Card 2', 'image_url': url_for('static', filename='brb-119-mountain.jpg')},
        {'name': 'Card 3', 'image_url': url_for('static', filename='ath-59-llanowar-elves.jpg')},
        {'name': 'Card 3', 'image_url': url_for('static', filename='ath-43-lightning-bolt.jpg')},
        {'name': 'Card 3', 'image_url': url_for('static', filename='5ed-240-hurloon-minotaur.jpg')}
    ]
    #display 
    battlefield_cards_creatures = []
    battlefield_cards_permanents = []
    
    return render_template('home.html', cards=hand_cards)

if __name__ == '__main__':
    app.run(debug=True)
