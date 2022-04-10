from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        yourTopSum = request.form.get('Your Top Summoner')
        yourTopChamp = request.form.get('Your Top Champ')
        yourJungSum = request.form.get('Your Jung Summoner')
        yourJungChamp = request.form.get('Your Jung Champ')
        yourMidSum = request.form.get('Your Mid Summoner')
        yourMidChamp = request.form.get('Your Mid Champ')
        yourBotSum = request.form.get('Your Bot Summoner')
        yourBotChamp = request.form.get('Your Bot Champ')
        yourSupSum = request.form.get('Your Sup Summoner')
        yourSupChamp = request.form.get('Your Sup Champ')
        theirTopChamp = request.form.get('Their Top Champ')
        theirJungChamp = request.form.get('Their Jung Champ')
        theirMidChamp = request.form.get('Their Mid Champ')
        theirBotChamp = request.form.get('Their Bot Champ')
        theirSupChamp = request.form.get('Their Sup Champ')
    return render_template("home.html")