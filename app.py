from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Voting options and icons
options = {
    'cat': 'icons/cat.png',
    'dog': 'icons/dog.png',
    'bird': 'icons/bird.png'
}

# Simple in-memory vote counter
votes = {key: 0 for key in options}

@app.route('/')
def vote_page():
    return render_template('vote.html', options=options)

@app.route('/vote/<option>')
def cast_vote(option):
    if option in votes:
        votes[option] += 1
        return redirect(url_for('results', selected=option))
    return "Invalid option", 404

@app.route('/results')
def results():
    selected = request.args.get('selected')
    return render_template('results.html', votes=votes, options=options, selected=selected)



if __name__ == '__main__':
    app.run(debug=True)