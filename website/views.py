from flask import Blueprint, render_template, request
from LiveLobby import Lobby
import pandas as pd

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
        
        current_lobby = Lobby(top_sum=yourTopSum,top_champ=yourTopChamp,
                                jung_sum=yourJungSum,jung_champ=yourJungChamp,
                                mid_sum=yourMidSum,mid_champ=yourMidChamp,
                                bot_sum=yourBotSum,bot_champ=yourBotChamp,
                                sup_sum=yourSupSum,sup_champ=yourSupChamp,
                                e_top=theirTopChamp,e_jung=theirJungChamp,e_mid=theirMidChamp,e_bot=theirBotChamp,e_sup=theirSupChamp)
        current_lobby.to_csv("lobby.csv",index=False,mode='w',header=True)
    return render_template("home.html")
