import pandas as pd
import cassiopeia as cass

cass.set_riot_api_key("RGAPI-e22a2f61-a2fb-4553-b8b8-9216f7bff4d4")

def get_stats(player, new_df):
    

    jungle = False
    if player.individual_position.name == 'jungle':
        jungle = True

    time_5 = "05:00"
    time_10 = "10:00"
    time_15 = "15:00"

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


    p_state = player.cumulative_timeline[time_5]
    kills_5 = p_state.kills
    deaths_5 = p_state.deaths
    assists_5 = p_state.assists

    if jungle == True:
        cs_5 = p_state.neutral_minions_killed
    else:
        cs_5 = p_state.creep_score

    p_state = player.cumulative_timeline[time_10]
    kills_10 = p_state.kills
    deaths_10 = p_state.deaths
    assists_10 = p_state.assists

    if jungle == True:
        cs_10 = p_state.neutral_minions_killed
    else:
        cs_10 = p_state.creep_score

    p_state = player.cumulative_timeline[time_15]
    kills_15 = p_state.kills
    deaths_15 = p_state.deaths
    assists_15 = p_state.assists

    if jungle == True:
        cs_15 = p_state.neutral_minions_killed
    else:
        cs_15 = p_state.creep_score




    new_df['First_Bloods'] += first_blood
    new_df['Double_Kills'] += double_kill
    new_df['Triple_Kills'] += triple_kill 
    new_df['Quadra_Kills'] += quadra_kills 
    new_df['Penta_Kills'] += penta_kills 
    new_df['CS_5'] += cs_5
    new_df['Kills_5'] += kills_5
    new_df['Deaths_5'] += deaths_5
    new_df['Assists_5'] += assists_5
    new_df['CS_10'] += cs_10
    new_df['Kills_10'] += kills_10
    new_df['Deaths_10'] += deaths_10
    new_df['Assists_10'] += assists_10
    new_df['CS_15'] += kills_15
    new_df['Kills_15'] += deaths_15
    new_df['Deaths_15'] += assists_15
    new_df['Assists_15'] += cs_15
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
        
def Lobby(side,top_sum,top_champ, jung_sum,jung_champ, mid_sum,mid_champ, bot_sum,bot_champ, sup_sum,sup_champ, e_top,e_jung,e_mid,e_bot,e_sup):

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

    top_history = cass.MatchHistory(puuid=puuid_one,continent="AMERICAS", region='NA',begin_index = 0, end_index = 20,queue=cass.Queue.ranked_solo_fives)
    jg_history = cass.MatchHistory(puuid=puuid_two,continent="AMERICAS", region='NA',begin_index = 0, end_index = 20,queue=cass.Queue.ranked_solo_fives)
    mid_history = cass.MatchHistory(puuid=puuid_three,continent="AMERICAS", region='NA',begin_index = 0, end_index = 20,queue=cass.Queue.ranked_solo_fives)
    bot_history = cass.MatchHistory(puuid=puuid_four,continent="AMERICAS", region='NA',begin_index = 0, end_index = 20,queue=cass.Queue.ranked_solo_fives)
    sup_history = cass.MatchHistory(puuid=puuid_five,continent="AMERICAS", region='NA',begin_index = 0, end_index = 20,queue=cass.Queue.ranked_solo_fives)

    new_df = pd.DataFrame()
    new_df['First_Bloods'] = [0]
    new_df['Double_Kills'] = [0]
    new_df['Triple_Kills'] = [0] 
    new_df['Quadra_Kills'] = [0] 
    new_df['Penta_Kills'] = [0] 
    new_df['CS_5'] = [0]
    new_df['Kills_5'] = [0]
    new_df['Deaths_5'] = [0]
    new_df['Assists_5'] = [0]
    new_df['CS_10'] = [0]
    new_df['Kills_10'] = [0]
    new_df['Deaths_10'] = [0]
    new_df['Assists_10'] = [0]
    new_df['CS_15'] = [0]
    new_df['Kills_15'] = [0]
    new_df['Deaths_15'] = [0]
    new_df['Assists_15'] = [0]
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
    
    stat_import['Side'] = [side]
    stat_import['Top_Current_Champ'] = [0]
    stat_import['Top_Current_Champ'] = top_champ
    stat_import['Top_games_on_role'] = [0]
    stat_import['Top_games_on_champ'] = [0]
    stat_import['Jg_Current_Champ'] = jung_champ
    stat_import['Jg_games_on_role'] = [0]
    stat_import['Jg_games_on_champ'] = [0]
    stat_import['Mid_Current_Champ'] = mid_champ  
    stat_import['Mid_games_on_role'] = [0]
    stat_import['Mid_games_on_champ'] = [0]
    stat_import['Bot_Current_Champ'] = bot_champ
    stat_import['Bot_games_on_role'] = [0]
    stat_import['Bot_games_on_champ'] = [0]
    stat_import['Sup_Current_Champ'] = sup_champ
    stat_import['Sup_games_on_role'] = [0]
    stat_import['Sup_games_on_champ'] = [0]


    stat_import['Top_Enemy_Champ'] = e_top
    stat_import['Jg_Enemy_Champ'] = e_jung
    stat_import['Mid_Enemy_Champ'] = e_mid
    stat_import['Bot_Enemy_Champ'] = e_bot
    stat_import['Sup_Enemy_Champ'] = e_sup

    try:
        for matches in top_history:
            for participants in matches.participants:
                if participants.summoner.puuid == puuid_one:    
                    if participants.individual_position.name == 'top_lane':
                        stat_import['Top_games_on_role'] += 1
                    if participants.champion.name == top_champ:
                        stat_import['Top_games_on_champ'] += 1
                    get_stats(participants, new_df)
                    break
    except:
        pass

    new_df.iloc[0:,5:] = new_df.iloc[0:,5:] / 20
    for column in new_df.columns:
        stat_import['Top_'+column] = new_df[column] 
        new_df[column] = [0] 

    try:
        for matches in jg_history:
            for participants in matches.participants:
                if participants.summoner.puuid == puuid_two:
                    if participants.individual_position.name == 'jungle':
                        stat_import['Jg_games_on_role'] += 1
                    if participants.champion.name == jung_champ:
                        stat_import['Jg_games_on_champ'] += 1
                    get_stats(participants, new_df)
                    break
    except:
        pass

    new_df.iloc[0:,5:] = new_df.iloc[0:,5:] / 20
    for column in new_df.columns:
        stat_import['Jg_'+column] = new_df[column]
        new_df[column] = [0]


    try:
        for matches in mid_history:
            for participants in matches.participants:
                if participants.summoner.puuid == puuid_three:
                    if participants.individual_position.name == 'mid_lane':
                        stat_import['Mid_games_on_role'] += 1
                    if participants.champion.name == mid_champ:
                        stat_import['Mid_games_on_champ'] += 1
                    get_stats(participants, new_df)
                    break
    except:
        pass

    new_df.iloc[0:,5:] = new_df.iloc[0:,5:] / 20
    for column in new_df.columns:
        stat_import['Mid_'+column] = new_df[column]
        new_df[column] = [0] 

    try:
        for matches in bot_history:
            for participants in matches.participants:
                if participants.summoner.puuid == puuid_four:
                    if participants.individual_position.name == 'bot_lane':
                        stat_import['Bot_games_on_role'] += 1
                    if participants.champion.name == bot_champ:
                        stat_import['Bot_games_on_champ'] += 1
                    get_stats(participants, new_df)
                    break
    except:
        pass

    new_df.iloc[0:,5:] = new_df.iloc[0:,5:] / 20
    for column in new_df.columns:
        stat_import['Bot_'+column] = new_df[column] 
        new_df[column] = [0] 

    try:
        for matches in sup_history:
            for participants in matches.participants:
                if participants.summoner.puuid == puuid_five:
                    if participants.individual_position.name == 'utility':
                        stat_import['Sup_games_on_role'] += 1
                    if participants.champion.name == sup_champ:
                        stat_import['Sup_games_on_champ'] += 1
                    get_stats(participants, new_df)
                    break
    except:
        pass

    new_df.iloc[0:,5:] = new_df.iloc[0:,5:] / 20
    for column in new_df.columns:
        stat_import['Sup_'+column] = new_df[column] 
        new_df[column] = [0] 

    return stat_import