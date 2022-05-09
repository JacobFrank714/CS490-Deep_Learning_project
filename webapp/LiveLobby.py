import pandas as pd
import cassiopeia as cass
from ProcessPredictFunctions import ProcessLiveData, Predict

cass.set_riot_api_key("RGAPI-e22a2f61-a2fb-4553-b8b8-9216f7bff4d4")

def get_stats(player, new_df):
    # Function that gets all the needed stats for the player provided and inserts them into the dataframe
    first_blood = player.stats.first_blood_kill
    double_kill = player.stats.double_kills
    triple_kill = player.stats.triple_kills
    quadra_kills = player.stats.quadra_kills
    penta_kills = player.stats.penta_kills
    kda = player.stats.kda
    kills = player.stats.kills
    deaths = player.stats.deaths
    assists = player.stats.assists
    CS = player.stats.total_minions_killed + player.stats.neutral_minions_killed
    damage_dealt = player.stats.total_damage_dealt_to_champions
    damage_taken = player.stats.total_damage_taken
    gold_earned = player.stats.gold_earned
    turret_damage = player.stats.damage_dealt_to_turrets
    turret_kills = player.stats.turret_kills
    turret_takedowns = player.stats.turret_takedowns
    vision_wards_bought = player.stats.vision_wards_bought 
    vision_wards_placed = player.stats.vision_wards_placed 
    wards_placed = player.stats.wards_placed 
    wards_killed = player.stats.wards_killed 
    cc_score = player.stats.time_CCing_others



    new_df['First_Bloods'] += first_blood
    new_df['Double_Kills'] += double_kill
    new_df['Triple_Kills'] += triple_kill 
    new_df['Quadra_Kills'] += quadra_kills 
    new_df['Penta_Kills'] += penta_kills 
    new_df['KDA'] += kda 
    new_df['Kills'] += kills
    new_df['Deaths'] += deaths 
    new_df['Assists'] += assists 
    new_df['CS'] += CS 
    new_df['Damage_Dealt'] += damage_dealt 
    new_df['Damage_Taken'] += damage_taken 
    new_df['Gold_Earned'] += gold_earned 
    new_df['Turret_Damage'] += turret_damage 
    new_df['Turret_Kills'] += turret_kills 
    new_df['Turrt_Takedowns'] += turret_takedowns
    new_df['VisionW_Bought'] += vision_wards_bought 
    new_df['VisionW_Placed'] += vision_wards_placed 
    new_df['Wards_Placed'] += wards_placed 
    new_df['Wards_Killed'] += wards_killed 
    new_df['CC_Score'] += cc_score 
        
        
def Lobby(side, rank, top_sum, top_champ, jung_sum, jung_champ, mid_sum, mid_champ, bot_sum, bot_champ, sup_sum, sup_champ, e_top, e_jung, e_mid, e_bot, e_sup):
    # Initializes the dataframe with the column names with initial values of zero or the input parameters that matches
    # Getting the player id using the summoner names
    player1 = cass.Summoner(name=top_sum, region="NA")
    player2 = cass.Summoner(name=jung_sum, region="NA")
    player3 = cass.Summoner(name=mid_sum, region="NA")
    player4 = cass.Summoner(name=bot_sum, region="NA")
    player5 = cass.Summoner(name=sup_sum, region="NA")

    puuid_one = player1.puuid
    puuid_two = player2.puuid
    puuid_three = player3.puuid
    puuid_four = player4.puuid
    puuid_five = player5.puuid
    # Getting the most recent 20 games from each player's match history
    top_history = cass.MatchHistory(puuid=puuid_one,continent="AMERICAS", region='NA',begin_index = 0, end_index = 20,queue=cass.Queue.ranked_solo_fives)
    jg_history = cass.MatchHistory(puuid=puuid_two,continent="AMERICAS", region='NA',begin_index = 0, end_index = 20,queue=cass.Queue.ranked_solo_fives)
    mid_history = cass.MatchHistory(puuid=puuid_three,continent="AMERICAS", region='NA',begin_index = 0, end_index = 20,queue=cass.Queue.ranked_solo_fives)
    bot_history = cass.MatchHistory(puuid=puuid_four,continent="AMERICAS", region='NA',begin_index = 0, end_index = 20,queue=cass.Queue.ranked_solo_fives)
    sup_history = cass.MatchHistory(puuid=puuid_five,continent="AMERICAS", region='NA',begin_index = 0, end_index = 20,queue=cass.Queue.ranked_solo_fives)
    # Initialize the stats with 0
    new_df = pd.DataFrame()
    new_df['First_Bloods'] = [0]
    new_df['Double_Kills'] = [0]
    new_df['Triple_Kills'] = [0] 
    new_df['Quadra_Kills'] = [0] 
    new_df['Penta_Kills'] = [0] 
    new_df['KDA']= [0] 
    new_df['Kills']= [0]
    new_df['Deaths']= [0] 
    new_df['Assists']= [0] 
    new_df['CS']= [0] 
    new_df['Damage_Dealt'] = [0] 
    new_df['Damage_Taken'] = [0] 
    new_df['Gold_Earned']= [0] 
    new_df['Turret_Damage']= [0] 
    new_df['Turret_Kills']= [0] 
    new_df['Turrt_Takedowns']= [0]
    new_df['VisionW_Bought']= [0] 
    new_df['VisionW_Placed']= [0] 
    new_df['Wards_Placed']= [0] 
    new_df['Wards_Killed']= [0] 
    new_df['CC_Score']= [0] 
    

    stat_import = pd.DataFrame()
    stat_import['Side'] = [0]
    stat_import['Rank'] = [0]
    stat_import['Top_Current_Champ'] = [0]
    stat_import['Top_games_on_role'] = [0]
    stat_import['Top_games_on_champ'] = [0]
    stat_import['Top_Win'] = [0]
    stat_import['Top_Lose'] = [0]
    stat_import['Top_Win_2'] = [0]
    stat_import['Top_Win_5'] = [0]
    stat_import['Jg_Current_Champ'] = [0]
    stat_import['Jg_games_on_role'] = [0]
    stat_import['Jg_games_on_champ'] = [0]
    stat_import['Jg_Win'] = [0]
    stat_import['Jg_Lose'] = [0]
    stat_import['Jg_Win_2'] = [0]
    stat_import['Jg_Win_5'] = [0]
    stat_import['Mid_Current_Champ'] = [0]  
    stat_import['Mid_games_on_role'] = [0]
    stat_import['Mid_games_on_champ'] = [0]
    stat_import['Mid_Win'] = [0]
    stat_import['Mid_Lose'] = [0]
    stat_import['Mid_Win_2'] = [0]
    stat_import['Mid_Win_5'] = [0]
    stat_import['Bot_Current_Champ'] = [0]
    stat_import['Bot_games_on_role'] = [0]
    stat_import['Bot_games_on_champ'] = [0]
    stat_import['Bot_Win'] = [0]
    stat_import['Bot_Lose'] = [0]
    stat_import['Bot_Win_2'] = [0]
    stat_import['Bot_Win_5'] = [0]
    stat_import['Sup_Current_Champ'] = [0]
    stat_import['Sup_games_on_role'] = [0]
    stat_import['Sup_games_on_champ'] = [0]
    stat_import['Sup_Win'] = [0]
    stat_import['Sup_Lose'] = [0]
    stat_import['Sup_Win_2'] = [0]
    stat_import['Sup_Win_5'] = [0]

    # Input all the input parameters into the dataframe
    stat_import['Side'] = [side]
    stat_import['Rank'] = [rank]
    stat_import['Top_Current_Champ'] = top_champ
    stat_import['Jg_Current_Champ'] = jung_champ
    stat_import['Mid_Current_Champ'] = mid_champ  
    stat_import['Bot_Current_Champ'] = bot_champ
    stat_import['Sup_Current_Champ'] = sup_champ
    stat_import['Top_Enemy_Champ'] = e_top
    stat_import['Jg_Enemy_Champ'] = e_jung
    stat_import['Mid_Enemy_Champ'] = e_mid
    stat_import['Bot_Enemy_Champ'] = e_bot
    stat_import['Sup_Enemy_Champ'] = e_sup
    # Getting each player's wins and losses
    try:
        match_count = 0
        for matches in top_history:
            for participants in matches.participants:
                if participants.summoner.puuid == puuid_one:    
                    if participants.individual_position.name == 'top_lane':
                        stat_import['Top_games_on_role'] += 1
                    if participants.champion.name == stat_import.iloc[0]['Top_Current_Champ']:
                        stat_import['Top_games_on_champ'] += 1
                    if participants.stats.win.real == 1:
                        stat_import['Top_Win'] += 1
                    elif participants.stats.win.real == 0:
                        stat_import['Top_Lose'] += 1
                    if match_count < 2:
                        if participants.stats.win.real == 1:
                            stat_import['Top_Win_2'] += 1  
                    if match_count < 5:
                        if participants.stats.win.real == 1:
                            stat_import['Top_Win_5'] += 1
                    match_count += 1
                    get_stats(participants,new_df)
                    break
    except:
        pass
    new_df.iloc[0:,5:] = new_df.iloc[0:,5:] / 20
    for column in new_df.columns:
        stat_import['Top_'+column] = new_df[column] 
        new_df[column] = [0] 
    try:
        match_count = 0
        for matches in jg_history:
            for participants in matches.participants:
                if participants.summoner.puuid == puuid_two:
                    if participants.individual_position.name == 'jungle':
                        stat_import['Jg_games_on_role'] += 1
                    if participants.champion.name == stat_import.iloc[0]['Jg_Current_Champ']:
                        stat_import['Jg_games_on_champ'] += 1
                    if participants.stats.win.real == 1:
                        stat_import['Jg_Win'] += 1
                    elif participants.stats.win.real == 0:
                        stat_import['Jg_Lose'] += 1
                    if match_count < 2:
                        if participants.stats.win.real == 1:
                            stat_import['Jg_Win_2'] += 1
                    if match_count < 5:
                        if participants.stats.win.real == 1:
                            stat_import['Jg_Win_5'] += 1
                    match_count += 1
                    get_stats(participants,new_df)
                    break
    except:
        pass
    new_df.iloc[0:,5:] = new_df.iloc[0:,5:] / 20
    for column in new_df.columns:
        stat_import['Jg_'+column] = new_df[column]
        new_df[column] = [0]
    try:
        match_count = 0
        for matches in mid_history:
            for participants in matches.participants:
                if participants.summoner.puuid == puuid_three:
                    if participants.individual_position.name == 'mid_lane':
                        stat_import['Mid_games_on_role'] += 1
                    if participants.champion.name == stat_import.iloc[0]['Mid_Current_Champ']:
                        stat_import['Mid_games_on_champ'] += 1
                    if participants.stats.win.real == 1:
                        stat_import['Mid_Win'] += 1
                    elif participants.stats.win.real == 0:
                        stat_import['Mid_Lose'] += 1
                    if match_count < 2:
                        if participants.stats.win.real == 1:
                            stat_import['Mid_Win_2'] += 1
                    if match_count < 5:
                        if participants.stats.win.real == 1:
                            stat_import['Mid_Win_5'] += 1
                    match_count += 1
                    get_stats(participants,new_df)
                    break
    except:
        pass
        new_df.iloc[0:,5:] = new_df.iloc[0:,5:] / 20
    for column in new_df.columns:
        stat_import['Mid_'+column] = new_df[column]
        new_df[column] = [0] 
    try:
        match_count = 0
        for matches in bot_history:
            for participants in matches.participants:
                if participants.summoner.puuid == puuid_four:
                    if participants.individual_position.name == 'bot_lane':
                        stat_import['Bot_games_on_role'] += 1
                    if participants.champion.name == stat_import.iloc[0]['Bot_Current_Champ']:
                        stat_import['Bot_games_on_champ'] += 1
                    if participants.stats.win.real == 1:
                        stat_import['Bot_Win'] += 1
                    elif participants.stats.win.real == 0:
                        stat_import['Bot_Lose'] += 1
                    if match_count < 2:
                        if participants.stats.win.real == 1:
                            stat_import['Bot_Win_2'] += 1
                    if match_count < 5:
                        if participants.stats.win.real == 1:
                            stat_import['Bot_Win_5'] += 1
                    match_count += 1
                    get_stats(participants,new_df)
                    break
    except:
        pass
    new_df.iloc[0:,5:] = new_df.iloc[0:,5:] / 20
    for column in new_df.columns:
        stat_import['Bot_'+column] = new_df[column] 
        new_df[column] = [0] 
    try:
        match_count = 0
        for matches in sup_history:
            for participants in matches.participants:
                if participants.summoner.puuid == puuid_five:
                    if participants.individual_position.name == 'utility':
                        stat_import['Sup_games_on_role'] += 1
                    if participants.champion.name == stat_import.iloc[0]['Sup_Current_Champ']:
                        stat_import['Sup_games_on_champ'] += 1
                    if participants.stats.win.real == 1:
                        stat_import['Sup_Win'] += 1
                    elif participants.stats.win.real == 0:
                        stat_import['Sup_Lose'] += 1
                    if match_count < 2:
                        if participants.stats.win.real == 1:
                            stat_import['Sup_Win_2'] += 1
                    if match_count < 5:
                        if participants.stats.win.real == 1:
                            stat_import['Sup_Win_5'] += 1
                    match_count += 1
                    get_stats(participants,new_df)
                    break
    except:
        pass
    new_df.iloc[0:,5:] = new_df.iloc[0:,5:] / 20
    for column in new_df.columns:
        stat_import['Sup_'+column] = new_df[column] 
        new_df[column] = [0]
    # calls our predict function from the ProcessPredictFunctions file
    prediction = Predict(stat_import)
    return prediction
