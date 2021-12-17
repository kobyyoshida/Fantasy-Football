from espn_api.football import League, box_player, player
from espn_api.football import box_score
from espn_api.football.box_score import BoxScore
from espn_api.football.team import Team
from espn_api.football import matchup
from espn_api.football import pick

league = League(league_id = 2294301, year=2021)

teamBisco = league.teams[2]

# print(teamBisco.team_id)
# print(teamBisco.team_name)
# print(teamBisco.owner)
# print(teamBisco.wins,"-", teamBisco.losses)
# print("Points for: ",teamBisco.points_for)
# print("Points against: ",teamBisco.points_against)
# print(teamBisco.roster)

# box = box_player.POSITION_MAP
# print(box)
#print(box_score.BoxPlayer)
#print(teamBisco.roster[0].injuryStatus)

#for i in teamBisco.roster:
#     print(i.name, " is ", i.injuryStatus)
#print(teamBisco.roster[0].stats)


#for i in league.teams:

#print(league.teams[0].draft)
#print(teamBisco.roster[0].playerId)

print(league.draft[0].playerId)
print(league.draft[0].playerName)

#for i in league.draft:
