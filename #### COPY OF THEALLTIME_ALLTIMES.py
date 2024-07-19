"""

Welcome on in! This is my first actual solo data analysis project.

Updates per day I worked on it:

5/10/2024: Initialized project, outlined goals of project, planned 
the process of the project and established table of contents, read in 
the data. 
(1.5 hours)

5/12/2024: Began experimenting with merging procedures on all of the 
datasets, not much success. 
(2 hours)

5/16/2024: Attempted merging procedures until it was deemed that
merging this early would be very difficult and not be of much help, 
studyed up on each dataset and determined how each one works and which
datasets would be compatable with one another in regards to merging,
studied the MLB divisions, briefly studied MLB stats and players to help
determine which stats might be helpful in determining the best players,
noted down the Nationals players I wanted to add post-2015, created lists
of each of the teams that each of the 30 remaining MLB franchises used to
be in order to, on a later date, create 30 giant tables containing only
the records of each specific MLB franchise.
(5.5 hours)

5/26/2024: Spent time planning on how to combine team data despite the
differences in format of the tables and the players' multiple stints in a
year connundrum. Separated all star, batting, post batting, pitching, post
pitching, fielding, and post fielding single-season data into 30 different
tables, one for each franchise. 
(3.5 hours)

5/28/2024: Theorized and developed a way where I could set the
players' main position over their career the as the main position in a
copied dataframe. This makes it easier to decide all of the best starters
for each of the 30 MLB teams and will likely make merging easier. 
(1 hour)

5/30/2024: Finished the task of 5/28 and set all 30 teams players' main 
positions as their only position (in a copied dataframe), fixed a couple of
bugs and bug tested to make sure that players did not have Nan as their
main position. 
(1 hour)

6/3/2024: Figured out how to add enough points columns to each team
statistical dataset, researched historic batting data in order to help solidify
my criteria, crafted my batting criteria for points in both the regular
season and postseason, and implemented the metric for the batting tables for
every team. 
(2 hours)

6/6/2024: Theorized the best statistics to be used for my fielding metrics, 
crafted my fielding and post fielding data metrics, began the pitching metrics.
(2 hours)

6/7/2024: Found a way to group sum total points and make a dataset with
individual player id and total number of accumulated points, which would be
subsequently used for merging with the final players dataset of each team, 
where the final players dataset is just the first instance of an observation
with that player ID for that team. Finished the pitching table and postseason
pitching table.
(1.67 hours)

6/8/2024: Finished the all star table, created a new column for each of the 7
main tables called combined_total_sum that consists of every single point a
player has gotten over the course of their career. Fixed bug stating that
baopp in postseason pitching was an object and not a float, so I made each
baopp numeric. 
(2.33 hours)

6/11/2024: Made the rest of the important postseason pitching columns
numeric so that points can be added correctly, got rid of some redundant code,
made new dataframes to hold only the unique point sums and player id, initiated
the merging process of all the points, positions, player_ids, and full names.
(1.5 hours)

6/17/2024: Figured out tournament seeding, developed and modified a function
to get scores and winner from a sample playoff game, learned about how
vscode and shell scripts operate, inched along on the everything merge.
(1.25 hours)

6/18/2024: Completed the entire everything merge for every single team,
learned about players that probably should and shouldn't be on the list and 
why, pondered over ways to make the point distribution more balanced across
eras, eliminated redundant code and organized my code a bit better.
(3.75 hours)

6/20/2024: Figured out a basic way to return more pitchers and outfielders,
but I did not save the code, although it should be easy to reproduce. Spent
most of today adding the player awards data into the mix because it should
help balance out the point distribution. Created the point criteria for the
award data and spent lots of time attmepting the merging and sorting out bugs.
(2.5 hours)

6/28/2024: FINALLY figured out the silly little bug not letting me correctly
calculate the points for awards, I was merging by too many different columns.
Changed some more of the point delegation system in order to reduce 
recency bias, added 2 additional outfielders and 4 additional pitchers to
the final player lineups for each team.
(2.75 hours)

7/7/2024: Added Triple Crowns to possible awards to win, filled out entire
active roster with best overall remaining players to make each team have
26 players, the amount that an MLB active roster has. Reworked the
point stats even more so that they would be even more even. Found an
alternative way to filter out the players that don't belong to the
specified teams by eliminating creating an empty dataframe and reducing
the unnecessary options in my filter function. Added comments to
improve readability and to help make sure I understand what the
code is actually doing.
(3.25 hours)

Total Days Worked: 16
Total Hours Worked: 37.5














NEXT MISSION: Seed each team and then apply my tourney game function to 
every single team in order to complete the tourney

If time:
- Change all outfielders positions to OF (just changing all of the CFs and LFs)
- Format the project better, get rid of the unneeded print statements and 
start all the explanations and comments for each section
- Add additional Nationals Players so that we actually have a chance (Only add
the ones that you think are better than the current list ones and make
realistic point additions so the team isn't too stacked)









Table of Contents:

1a: Purpose of project

1bi: Mission
1bii: Objectives
1biii: Side Quests

2a: Description of dataset
2b: Descriptions of tables used
2c: Descriptions of important variables considered

3a: Reading in the required data
3b: Filtering out the unusable data
3c: Sorting of the data
    - Assigning every possible team_id to its associated franchise


4b: 


"""







"""
1a

Purpose: Get further aquainted with Python, VSCode, SQL, and large datasets
with lots and lots of variables and observations. This may not be a long
project, but I hope it will still be one where I grow a lot and near double
my programming knowledge. There will be 1 main project mission and 5 
objectives, and smaller side quests will likely be added accordingly 
if I find there is something cool that I can implement.






1bi

Mission: Formulate the best all-time rosters for every single current MLB
team. Use statistics from a pleathora of tables in order to back your
claim.

1bii

Objective 1: Use SQL and query data from at minimum 10 different baseball
tables in order to come up with the best possible team over the course of
all of baseball

Objective 2: Create a(n) function(s) to establish one or more metrics in
order to compare how good one all time team is to another

Objective 3: Create sub-teams per different era. Compare all the eras and
determine the best era for each team. The eras will be: 1871-1900 (Infancy
era), 1901-1920 (Dead Ball era), 1921-1942 (Live Ball era), 1943-1961
(Integration era), 1962-1977 (Expansion era), 1978-1994 (Free Agent era), 
1995-2004 (Steriod era), and 2005-2015 (Contemporary Era).

Objective 4: In some way, implement one additional language to aid in
accomplishing at least one of the objectives and/or side quests.
Preferably in a way where it is necessary to use this language and
would me much harder to implement in Python or in SQL.

Objective 5: Create a gigantic 30-team tournament at the end, seeded
based on whatever metric(s) I used to compare them. Set up wild card series
(best of 3), some best of 5 series, and some best of 7 series with some
variation due to chance in order to crown the ultimate champion across
all of baseball ever. Make tournament in the style of 15 seeds in AL on
one side and 15 sides NL on the other side.

1biii

Side Quest 1: Go in further depth with the Nationals/Expos lineup,
use some super obscure stats and see how different the lineup is compared
to the original. Add the important players that were added 
to the lineup after 2015 (Juan Soto, for example). For players like him,
Scherzer, and Strasburg, add in all necessary stats from
each year in order for the Nationals to be even somewhat competitive
in the final massive tournament.




Second stint means you got traded midway through the season

Cool thing about this list is that the best players for every team only
includes the years they played for that team
"""













"""
2a

2b

2c

"""


















### IMPORTANT NOTE, COPY ALL THE TABLES FROM INSIDE THE FOLDER THAT
### YOU WILL BE USING AND PASTE THEM OUTSIDE, THAT WILL BE HOW
### YOU ARE ABLE TO READ IN THE DATA

# 3a

# Importing necessary packages
import pandas as pd
import numpy as np




### Reading in 11 different datasets with info I need in order to pick
### the best teams
batting_data = pd.read_csv("batting.csv")
batting_data.fillna(0, inplace = True)
batting_post_data = pd.read_csv("batting_postseason.csv")
batting_post_data.fillna(0, inplace = True)


fielding_infield_data = pd.read_csv("fielding.csv")
fielding_infield_data.fillna(0, inplace = True)
fielding_outfield_data = pd.read_csv("fielding_outfield.csv")
fielding_outfield_data.fillna(0, inplace = True)
fielding_post_data = pd.read_csv("fielding_postseason.csv")
fielding_post_data.fillna(0, inplace = True)

pitching_data = pd.read_csv("pitching.csv")
pitching_data.fillna(0, inplace = True)
pitching_post_data = pd.read_csv("pitching_postseason.csv")
pitching_post_data.fillna(0, inplace = True)


all_star_data = pd.read_csv("all_star.csv")
all_star_data.fillna(0, inplace = True)
player_awards_data = pd.read_csv("player_award.csv")
player_awards_data.fillna(0, inplace = True)
player_data = pd.read_csv("player.csv")
player_data.fillna(0, inplace = True)

team_data = pd.read_csv("team.csv")
team_data.fillna(0, inplace = True)








# Defining each of the teams for each franchise


## American League






### AL East
orioles_teams = ["MLA", "SLA", "BAL"]
red_sox_teams = ["BOS"]
yankees_teams = ["BLA", "NYA"]
rays_teams = ["TBA"]
blue_jays_teams = ["TOR"]

### AL Central
white_sox_teams = ["CHA"]
guardians_teams = ["CLE"]
tigers_teams = ["DET"]
royals_teams = ["KCA"]
twins_teams = ["WS1", "MIN"]

### AL West
astros_teams = ["HOU"]
angels_teams = ["LAA", "CAL", "ANA"]
athletics_teams = ["PHA", "KC1", "OAK"]
mariners_teams = ["SEA"]
rangers_teams = ["WS2", "TEX"]



## National League



### NL East
braves_teams = ["BSN", "ML1", "ATL"]
marlins_teams = ["FLO", "MIA"]
mets_teams = ["NYN"]
phillies_teams = ["PHI"]
nationals_teams = ["MON", "WAS"]

### NL Central
cubs_teams = ["CHN"]
reds_teams = ["CN2", "CIN"]
brewers_teams = ["SE1", "ML4", "MIL"]
pirates_teams = ["PT1", "PIT"]
cardinals_teams = ["SL4", "SLN"]

### NL West
diamondbacks_teams = ["ARI"]
rockies_teams = ["COL"]
dodgers_teams = ["BR3", "BRO", "LAN"]
padres_teams = ["SDN"]
giants_teams = ["NY1", "SFN"]





"""



##### IMPORTANT ######

The order for which I will be determining the best teams:

- Make a copy of each of the datasets, add a new column for each and name
it points_batting or something distinctive, and have it be initialized at 0





- Assign conditions to reward points for good baseball attributes for
each table


- MAKE 30 NEW DATASETS SOMEHOW





- I want to, in each of the 30 team datasets, have the player ID,
player name, team, position, each of the point totals per category, and
the total number of points earned.







"""
















# Batting per team (each single season batting observation for a single franchise)




"""


The code in this code chunk is the greatly reduced code that basically does everything that I need it to do: Creates a list of each of the team names from the
past per franchise, defines a function where the batting_data dataframe gets filtered down into only containing the full observations of franchises where the
team_id is contained in the list of team_ids for that franchise, and then the new dataframe is created. Since the old code works and I am not pressed for space
or for efficiency at the current moment, I am going to keep what I have as my working code but keep this template here in case I decide to simplify the code
and make it much more efficient and readable.





test_orioles_teams = ["MLA"]



def special_append(team_ids):
    return batting_data[batting_data["team_id"].isin(team_ids)]

orioles_batting3 = special_append(test_orioles_teams)
print(orioles_batting3.tail())

"""



# Creating new dataframes for each team (redundant, but required when I concatenate this dataframe and the filtered one for my function)

orioles_batting = pd.DataFrame(columns = batting_data.columns)
red_sox_batting = pd.DataFrame(columns = batting_data.columns)
yankees_batting = pd.DataFrame(columns = batting_data.columns)
rays_batting = pd.DataFrame(columns = batting_data.columns)
blue_jays_batting = pd.DataFrame(columns = batting_data.columns)

white_sox_batting = pd.DataFrame(columns = batting_data.columns)
guardians_batting = pd.DataFrame(columns = batting_data.columns)
tigers_batting = pd.DataFrame(columns = batting_data.columns)
royals_batting = pd.DataFrame(columns = batting_data.columns)
twins_batting = pd.DataFrame(columns = batting_data.columns)

astros_batting = pd.DataFrame(columns = batting_data.columns)
angels_batting = pd.DataFrame(columns = batting_data.columns)
athletics_batting = pd.DataFrame(columns = batting_data.columns)
mariners_batting = pd.DataFrame(columns = batting_data.columns)
rangers_batting = pd.DataFrame(columns = batting_data.columns)



braves_batting = pd.DataFrame(columns = batting_data.columns)
marlins_batting = pd.DataFrame(columns = batting_data.columns)
mets_batting = pd.DataFrame(columns = batting_data.columns)
nationals_batting = pd.DataFrame(columns = batting_data.columns)
phillies_batting = pd.DataFrame(columns = batting_data.columns)

cubs_batting = pd.DataFrame(columns = batting_data.columns)
reds_batting = pd.DataFrame(columns = batting_data.columns)
brewers_batting = pd.DataFrame(columns = batting_data.columns)
pirates_batting = pd.DataFrame(columns = batting_data.columns)
cardinals_batting = pd.DataFrame(columns = batting_data.columns)

diamondbacks_batting = pd.DataFrame(columns = batting_data.columns)
rockies_batting = pd.DataFrame(columns = batting_data.columns)
dodgers_batting = pd.DataFrame(columns = batting_data.columns)
padres_batting = pd.DataFrame(columns = batting_data.columns)
giants_batting = pd.DataFrame(columns = batting_data.columns)


# Defining a functino where I take in a list of team ids and an existing empty team batting dataframe
# Filters out all observations that do not have any of the specified team_ids
# Returns a concatenation of the filtered dataframe and the empty dataframe (basically copying and pasting the filtered dataframe)


def append_specified_team_ids_batting(team_ids, target_df):
    filtered_df = batting_data[batting_data["team_id"].isin(team_ids)]
    return pd.concat([target_df, filtered_df], ignore_index = True)




# Applying the function to each of the individual teams. All of the regular_season batting stats of only players who played for the specified franchises are kept.

orioles_batting = append_specified_team_ids_batting(orioles_teams, orioles_batting)
red_sox_batting = append_specified_team_ids_batting(red_sox_teams, red_sox_batting)
yankees_batting = append_specified_team_ids_batting(yankees_teams, yankees_batting)
rays_batting = append_specified_team_ids_batting(rays_teams, rays_batting)
blue_jays_batting = append_specified_team_ids_batting(blue_jays_teams, blue_jays_batting)

white_sox_batting = append_specified_team_ids_batting(white_sox_teams, white_sox_batting)
guardians_batting = append_specified_team_ids_batting(guardians_teams, guardians_batting)
tigers_batting = append_specified_team_ids_batting(tigers_teams, tigers_batting)
royals_batting = append_specified_team_ids_batting(royals_teams, royals_batting)
twins_batting = append_specified_team_ids_batting(twins_teams, twins_batting)

astros_batting = append_specified_team_ids_batting(astros_teams, astros_batting)
angels_batting = append_specified_team_ids_batting(angels_teams, angels_batting)
athletics_batting = append_specified_team_ids_batting(athletics_teams, athletics_batting)
mariners_batting = append_specified_team_ids_batting(mariners_teams, mariners_batting)
rangers_batting = append_specified_team_ids_batting(rangers_teams, rangers_batting)




braves_batting = append_specified_team_ids_batting(braves_teams, braves_batting)
marlins_batting = append_specified_team_ids_batting(marlins_teams, marlins_batting)
mets_batting = append_specified_team_ids_batting(mets_teams, mets_batting)
nationals_batting = append_specified_team_ids_batting(nationals_teams, nationals_batting)
phillies_batting = append_specified_team_ids_batting(phillies_teams, phillies_batting)

cubs_batting = append_specified_team_ids_batting(cubs_teams, cubs_batting)
reds_batting = append_specified_team_ids_batting(reds_teams, reds_batting)
brewers_batting = append_specified_team_ids_batting(brewers_teams, brewers_batting)
pirates_batting = append_specified_team_ids_batting(pirates_teams, pirates_batting)
cardinals_batting = append_specified_team_ids_batting(cardinals_teams, cardinals_batting)

diamondbacks_batting = append_specified_team_ids_batting(diamondbacks_teams, diamondbacks_batting)
rockies_batting = append_specified_team_ids_batting(rockies_teams, rockies_batting)
dodgers_batting = append_specified_team_ids_batting(dodgers_teams, dodgers_batting)
padres_batting = append_specified_team_ids_batting(padres_teams, padres_batting)
giants_batting = append_specified_team_ids_batting(giants_teams, giants_batting)



# Defining points for each of the regular season batting stats.
# First, a number of point category columns are created based on how many I want
# Second, in each batting dataset, I look to see if an observation satisfies each of the if statements. If they do, they get points assigned to the point categories
# I then get the sum of the points per that given season called Sum_Total_Points
# Lastly, I get the sum of the career number of points, the column called Combined_Total_Points

for i in range(1, 9):
    orioles_batting[f"Point_Category_{i}"] = 0

for index, row in orioles_batting.iterrows():
    if row["h"] >= 160:
        red_sox_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        orioles_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        orioles_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        orioles_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        orioles_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        orioles_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        orioles_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        orioles_batting.at[index, 'Point_Category_8'] = 1
    
orioles_batting["Sum_Total_Points"] = orioles_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
orioles_batting["Combined_Total_Points"] = orioles_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 9):
    red_sox_batting[f"Point_Category_{i}"] = 0

for index, row in red_sox_batting.iterrows():
    if row["h"] >= 160:
        red_sox_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        red_sox_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        red_sox_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        red_sox_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        red_sox_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        red_sox_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        red_sox_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        red_sox_batting.at[index, 'Point_Category_8'] = 1
    
red_sox_batting["Sum_Total_Points"] = red_sox_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
red_sox_batting["Combined_Total_Points"] = red_sox_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    yankees_batting[f"Point_Category_{i}"] = 0

for index, row in yankees_batting.iterrows():
    if row["h"] >= 160:
        yankees_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        yankees_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        yankees_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        yankees_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        yankees_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        yankees_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        yankees_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        yankees_batting.at[index, 'Point_Category_8'] = 1
    
yankees_batting["Sum_Total_Points"] = yankees_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
yankees_batting["Combined_Total_Points"] = yankees_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    rays_batting[f"Point_Category_{i}"] = 0

for index, row in rays_batting.iterrows():
    if row["h"] >= 160:
        rays_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        rays_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        rays_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        rays_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        rays_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        rays_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        rays_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        rays_batting.at[index, 'Point_Category_8'] = 1
    
rays_batting["Sum_Total_Points"] = rays_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
rays_batting["Combined_Total_Points"] = rays_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    blue_jays_batting[f"Point_Category_{i}"] = 0

for index, row in blue_jays_batting.iterrows():
    if row["h"] >= 160:
        blue_jays_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        blue_jays_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        blue_jays_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        blue_jays_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        blue_jays_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        blue_jays_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        blue_jays_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        blue_jays_batting.at[index, 'Point_Category_8'] = 1
    
blue_jays_batting["Sum_Total_Points"] = blue_jays_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
blue_jays_batting["Combined_Total_Points"] = blue_jays_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')









for i in range(1, 9):
    white_sox_batting[f"Point_Category_{i}"] = 0

for index, row in white_sox_batting.iterrows():
    if row["h"] >= 160:
        white_sox_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        white_sox_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        white_sox_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        white_sox_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        white_sox_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        white_sox_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        white_sox_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        white_sox_batting.at[index, 'Point_Category_8'] = 1
    
white_sox_batting["Sum_Total_Points"] = white_sox_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
white_sox_batting["Combined_Total_Points"] = white_sox_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    guardians_batting[f"Point_Category_{i}"] = 0

for index, row in guardians_batting.iterrows():
    if row["h"] >= 160:
        guardians_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        guardians_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        guardians_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        guardians_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        guardians_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        guardians_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        guardians_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        guardians_batting.at[index, 'Point_Category_8'] = 1
    
guardians_batting["Sum_Total_Points"] = guardians_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
guardians_batting["Combined_Total_Points"] = guardians_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    tigers_batting[f"Point_Category_{i}"] = 0

for index, row in tigers_batting.iterrows():
    if row["h"] >= 160:
        tigers_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        tigers_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        tigers_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        tigers_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        tigers_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        tigers_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        tigers_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        tigers_batting.at[index, 'Point_Category_8'] = 1
    
tigers_batting["Sum_Total_Points"] = tigers_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
tigers_batting["Combined_Total_Points"] = tigers_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    royals_batting[f"Point_Category_{i}"] = 0

for index, row in royals_batting.iterrows():
    if row["h"] >= 160:
        royals_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        royals_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        royals_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        royals_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        royals_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        royals_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        royals_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        royals_batting.at[index, 'Point_Category_8'] = 1
    
royals_batting["Sum_Total_Points"] = royals_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
royals_batting["Combined_Total_Points"] = royals_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    twins_batting[f"Point_Category_{i}"] = 0

for index, row in twins_batting.iterrows():
    if row["h"] >= 160:
        twins_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        twins_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        twins_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        twins_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        twins_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        twins_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        twins_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        twins_batting.at[index, 'Point_Category_8'] = 1
    
twins_batting["Sum_Total_Points"] = twins_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
twins_batting["Combined_Total_Points"] = twins_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')









for i in range(1, 9):
    astros_batting[f"Point_Category_{i}"] = 0

for index, row in astros_batting.iterrows():
    if row["h"] >= 160:
        astros_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        astros_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        astros_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        astros_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        astros_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        astros_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        astros_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        astros_batting.at[index, 'Point_Category_8'] = 1
    
astros_batting["Sum_Total_Points"] = astros_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
astros_batting["Combined_Total_Points"] = astros_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    angels_batting[f"Point_Category_{i}"] = 0

for index, row in angels_batting.iterrows():
    if row["h"] >= 160:
        angels_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        angels_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        angels_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        angels_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        angels_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        angels_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        angels_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        angels_batting.at[index, 'Point_Category_8'] = 1
    
angels_batting["Sum_Total_Points"] = angels_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
angels_batting["Combined_Total_Points"] = angels_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    athletics_batting[f"Point_Category_{i}"] = 0

for index, row in athletics_batting.iterrows():
    if row["h"] >= 160:
        athletics_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        athletics_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        athletics_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        athletics_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        athletics_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        athletics_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        athletics_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        athletics_batting.at[index, 'Point_Category_8'] = 1
    
athletics_batting["Sum_Total_Points"] = athletics_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
athletics_batting["Combined_Total_Points"] = athletics_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    mariners_batting[f"Point_Category_{i}"] = 0

for index, row in mariners_batting.iterrows():
    if row["h"] >= 160:
        mariners_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        mariners_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        mariners_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        mariners_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        mariners_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        mariners_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        mariners_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        mariners_batting.at[index, 'Point_Category_8'] = 1
    
mariners_batting["Sum_Total_Points"] = mariners_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
mariners_batting["Combined_Total_Points"] = mariners_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    rangers_batting[f"Point_Category_{i}"] = 0

for index, row in rangers_batting.iterrows():
    if row["h"] >= 160:
        rangers_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        rangers_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        rangers_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        rangers_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        rangers_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        rangers_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        rangers_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        rangers_batting.at[index, 'Point_Category_8'] = 1
    
rangers_batting["Sum_Total_Points"] = rangers_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
rangers_batting["Combined_Total_Points"] = rangers_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')












for i in range(1, 9):
    braves_batting[f"Point_Category_{i}"] = 0

for index, row in braves_batting.iterrows():
    if row["h"] >= 160:
        braves_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        braves_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        braves_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        braves_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        braves_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        braves_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        braves_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        braves_batting.at[index, 'Point_Category_8'] = 1
    
braves_batting["Sum_Total_Points"] = braves_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
braves_batting["Combined_Total_Points"] = braves_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    marlins_batting[f"Point_Category_{i}"] = 0

for index, row in marlins_batting.iterrows():
    if row["h"] >= 160:
        marlins_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        marlins_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        marlins_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        marlins_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        marlins_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        marlins_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        marlins_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        marlins_batting.at[index, 'Point_Category_8'] = 1
    
marlins_batting["Sum_Total_Points"] = marlins_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
marlins_batting["Combined_Total_Points"] = marlins_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    mets_batting[f"Point_Category_{i}"] = 0

for index, row in mets_batting.iterrows():
    if row["h"] >= 160:
        mets_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        mets_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        mets_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        mets_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        mets_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        mets_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        mets_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        mets_batting.at[index, 'Point_Category_8'] = 1
    
mets_batting["Sum_Total_Points"] = mets_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
mets_batting["Combined_Total_Points"] = mets_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    nationals_batting[f"Point_Category_{i}"] = 0

for index, row in nationals_batting.iterrows():
    if row["h"] >= 160:
        nationals_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        nationals_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        nationals_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        nationals_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        nationals_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        nationals_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        nationals_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        nationals_batting.at[index, 'Point_Category_8'] = 1
    
nationals_batting["Sum_Total_Points"] = nationals_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
nationals_batting["Combined_Total_Points"] = nationals_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    phillies_batting[f"Point_Category_{i}"] = 0

for index, row in phillies_batting.iterrows():
    if row["h"] >= 160:
        phillies_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        phillies_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        phillies_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        phillies_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        phillies_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        phillies_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        phillies_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        phillies_batting.at[index, 'Point_Category_8'] = 1
    
phillies_batting["Sum_Total_Points"] = phillies_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
phillies_batting["Combined_Total_Points"] = phillies_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')









for i in range(1, 9):
    cubs_batting[f"Point_Category_{i}"] = 0

for index, row in cubs_batting.iterrows():
    if row["h"] >= 160:
        cubs_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        cubs_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        cubs_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        cubs_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        cubs_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        cubs_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        cubs_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        cubs_batting.at[index, 'Point_Category_8'] = 1
    
cubs_batting["Sum_Total_Points"] = cubs_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
cubs_batting["Combined_Total_Points"] = cubs_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    reds_batting[f"Point_Category_{i}"] = 0

for index, row in reds_batting.iterrows():
    if row["h"] >= 160:
        reds_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        reds_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        reds_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        reds_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        reds_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        reds_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        reds_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        reds_batting.at[index, 'Point_Category_8'] = 1
    
reds_batting["Sum_Total_Points"] = reds_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
reds_batting["Combined_Total_Points"] = reds_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    brewers_batting[f"Point_Category_{i}"] = 0

for index, row in brewers_batting.iterrows():
    if row["h"] >= 160:
        brewers_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        brewers_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        brewers_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        brewers_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        brewers_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        brewers_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        brewers_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        brewers_batting.at[index, 'Point_Category_8'] = 1
    
brewers_batting["Sum_Total_Points"] = brewers_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
brewers_batting["Combined_Total_Points"] = brewers_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    pirates_batting[f"Point_Category_{i}"] = 0

for index, row in pirates_batting.iterrows():
    if row["h"] >= 160:
        pirates_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        pirates_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        pirates_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        pirates_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        pirates_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        pirates_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        pirates_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        pirates_batting.at[index, 'Point_Category_8'] = 1
    
pirates_batting["Sum_Total_Points"] = pirates_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
pirates_batting["Combined_Total_Points"] = pirates_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    cardinals_batting[f"Point_Category_{i}"] = 0

for index, row in cardinals_batting.iterrows():
    if row["h"] >= 160:
        cardinals_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        cardinals_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        cardinals_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        cardinals_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        cardinals_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        cardinals_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        cardinals_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        cardinals_batting.at[index, 'Point_Category_8'] = 1
    
cardinals_batting["Sum_Total_Points"] = cardinals_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
cardinals_batting["Combined_Total_Points"] = cardinals_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')









for i in range(1, 9):
    diamondbacks_batting[f"Point_Category_{i}"] = 0

for index, row in diamondbacks_batting.iterrows():
    if row["h"] >= 160:
        diamondbacks_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        diamondbacks_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        diamondbacks_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        diamondbacks_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        diamondbacks_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        diamondbacks_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        diamondbacks_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        diamondbacks_batting.at[index, 'Point_Category_8'] = 1
    
diamondbacks_batting["Sum_Total_Points"] = diamondbacks_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
diamondbacks_batting["Combined_Total_Points"] = diamondbacks_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    rockies_batting[f"Point_Category_{i}"] = 0

for index, row in rockies_batting.iterrows():
    if row["h"] >= 160:
        rockies_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        rockies_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        rockies_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        rockies_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        rockies_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        rockies_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        rockies_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        rockies_batting.at[index, 'Point_Category_8'] = 1
    
rockies_batting["Sum_Total_Points"] = rockies_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
rockies_batting["Combined_Total_Points"] = rockies_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    dodgers_batting[f"Point_Category_{i}"] = 0

for index, row in dodgers_batting.iterrows():
    if row["h"] >= 160:
        dodgers_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        dodgers_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        dodgers_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        dodgers_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        dodgers_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        dodgers_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        dodgers_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        dodgers_batting.at[index, 'Point_Category_8'] = 1
    
dodgers_batting["Sum_Total_Points"] = dodgers_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
dodgers_batting["Combined_Total_Points"] = dodgers_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    padres_batting[f"Point_Category_{i}"] = 0

for index, row in padres_batting.iterrows():
    if row["h"] >= 160:
        padres_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        padres_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        padres_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        padres_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        padres_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        padres_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        padres_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        padres_batting.at[index, 'Point_Category_8'] = 1
    
padres_batting["Sum_Total_Points"] = padres_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
padres_batting["Combined_Total_Points"] = padres_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    giants_batting[f"Point_Category_{i}"] = 0

for index, row in giants_batting.iterrows():
    if row["h"] >= 160:
        giants_batting.at[index, "Point_Category_1"] = 2
    if row["double"] >= 35:
        giants_batting.at[index, "Point_Category_2"] = 1
    if row["triple"] >= 10:
        giants_batting.at[index, "Point_Category_3"] = 1
    if row["g"] >= 150:
        giants_batting.at[index, "Point_Category_4"] = 1
    if row["hr"] >= 30:
        giants_batting.at[index, "Point_Category_5"] = 1
    if row["rbi"] >= 115:
        giants_batting.at[index, "Point_Category_6"] = 1
    if row["sb"] >= 40:
        giants_batting.at[index, "Point_Category_7"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        giants_batting.at[index, 'Point_Category_8'] = 1
    
giants_batting["Sum_Total_Points"] = giants_batting[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
giants_batting["Combined_Total_Points"] = giants_batting.groupby("player_id")["Sum_Total_Points"].transform('sum')













# Post batting per team

# Creating new dataframes for each team (redundant, but required when I concatenate this dataframe and the filtered one for my function)


orioles_batting_post = pd.DataFrame(columns = batting_post_data.columns)
red_sox_batting_post = pd.DataFrame(columns = batting_post_data.columns)
yankees_batting_post = pd.DataFrame(columns = batting_post_data.columns)
rays_batting_post = pd.DataFrame(columns = batting_post_data.columns)
blue_jays_batting_post = pd.DataFrame(columns = batting_post_data.columns)

white_sox_batting_post = pd.DataFrame(columns = batting_post_data.columns)
guardians_batting_post = pd.DataFrame(columns = batting_post_data.columns)
tigers_batting_post = pd.DataFrame(columns = batting_post_data.columns)
royals_batting_post = pd.DataFrame(columns = batting_post_data.columns)
twins_batting_post = pd.DataFrame(columns = batting_post_data.columns)

astros_batting_post = pd.DataFrame(columns = batting_post_data.columns)
angels_batting_post = pd.DataFrame(columns = batting_post_data.columns)
athletics_batting_post = pd.DataFrame(columns = batting_post_data.columns)
mariners_batting_post = pd.DataFrame(columns = batting_post_data.columns)
rangers_batting_post = pd.DataFrame(columns = batting_post_data.columns)



braves_batting_post = pd.DataFrame(columns = batting_post_data.columns)
marlins_batting_post = pd.DataFrame(columns = batting_post_data.columns)
mets_batting_post = pd.DataFrame(columns = batting_post_data.columns)
nationals_batting_post = pd.DataFrame(columns = batting_post_data.columns)
phillies_batting_post = pd.DataFrame(columns = batting_post_data.columns)

cubs_batting_post = pd.DataFrame(columns = batting_post_data.columns)
reds_batting_post = pd.DataFrame(columns = batting_post_data.columns)
brewers_batting_post = pd.DataFrame(columns = batting_post_data.columns)
pirates_batting_post = pd.DataFrame(columns = batting_post_data.columns)
cardinals_batting_post = pd.DataFrame(columns = batting_post_data.columns)

diamondbacks_batting_post = pd.DataFrame(columns = batting_post_data.columns)
rockies_batting_post = pd.DataFrame(columns = batting_post_data.columns)
dodgers_batting_post = pd.DataFrame(columns = batting_post_data.columns)
padres_batting_post = pd.DataFrame(columns = batting_post_data.columns)
giants_batting_post = pd.DataFrame(columns = batting_post_data.columns)


# Defining a functino where I take in a list of team ids and an existing empty team batting post dataframe
# Filters out all observations that do not have any of the specified team_ids
# Returns a concatenation of the filtered dataframe and the empty dataframe (basically copying and pasting the filtered dataframe)

def append_specified_team_ids_batting_post(team_ids, target_df):
    filtered_df = batting_post_data[batting_post_data["team_id"].isin(team_ids)]
    return pd.concat([target_df, filtered_df], ignore_index = True)




orioles_batting_post = append_specified_team_ids_batting_post(orioles_teams, orioles_batting_post)
red_sox_batting_post = append_specified_team_ids_batting_post(red_sox_teams, red_sox_batting_post)
yankees_batting_post = append_specified_team_ids_batting_post(yankees_teams, yankees_batting_post)
rays_batting_post = append_specified_team_ids_batting_post(rays_teams, rays_batting_post)
blue_jays_batting_post = append_specified_team_ids_batting_post(blue_jays_teams, blue_jays_batting_post)

white_sox_batting_post = append_specified_team_ids_batting_post(white_sox_teams, white_sox_batting_post)
guardians_batting_post = append_specified_team_ids_batting_post(guardians_teams, guardians_batting_post)
tigers_batting_post = append_specified_team_ids_batting_post(tigers_teams, tigers_batting_post)
royals_batting_post = append_specified_team_ids_batting_post(royals_teams, royals_batting_post)
twins_batting_post = append_specified_team_ids_batting_post(twins_teams, twins_batting_post)

astros_batting_post = append_specified_team_ids_batting_post(astros_teams, astros_batting_post)
angels_batting_post = append_specified_team_ids_batting_post(angels_teams, angels_batting_post)
athletics_batting_post = append_specified_team_ids_batting_post(athletics_teams, athletics_batting_post)
mariners_batting_post = append_specified_team_ids_batting_post(mariners_teams, mariners_batting_post)
rangers_batting_post = append_specified_team_ids_batting_post(rangers_teams, rangers_batting_post)




braves_batting_post = append_specified_team_ids_batting_post(braves_teams, braves_batting_post)
marlins_batting_post = append_specified_team_ids_batting_post(marlins_teams, marlins_batting_post)
mets_batting_post = append_specified_team_ids_batting_post(mets_teams, mets_batting_post)
nationals_batting_post = append_specified_team_ids_batting_post(nationals_teams, nationals_batting_post)
phillies_batting_post = append_specified_team_ids_batting_post(phillies_teams, phillies_batting_post)

cubs_batting_post = append_specified_team_ids_batting_post(cubs_teams, cubs_batting_post)
reds_batting_post = append_specified_team_ids_batting_post(reds_teams, reds_batting_post)
brewers_batting_post = append_specified_team_ids_batting_post(brewers_teams, brewers_batting_post)
pirates_batting_post = append_specified_team_ids_batting_post(pirates_teams, pirates_batting_post)
cardinals_batting_post = append_specified_team_ids_batting_post(cardinals_teams, cardinals_batting_post)

diamondbacks_batting_post = append_specified_team_ids_batting_post(diamondbacks_teams, diamondbacks_batting_post)
rockies_batting_post = append_specified_team_ids_batting_post(rockies_teams, rockies_batting_post)
dodgers_batting_post = append_specified_team_ids_batting_post(dodgers_teams, dodgers_batting_post)
padres_batting_post = append_specified_team_ids_batting_post(padres_teams, padres_batting_post)
giants_batting_post = append_specified_team_ids_batting_post(giants_teams, giants_batting_post)



# Defining points for each of the post season batting stats.
# First, a number of point category columns are created based on how many I want
# Second, in each batting dataset, I look to see if an observation satisfies each of the if statements. If they do, they get points assigned to the point categories
# I then get the sum of the points per that given season called Sum_Total_Points
# Lastly, I get the sum of the career number of points, the column called Combined_Total_Points

for i in range(1, 8):
    orioles_batting_post[f"Point_Category_{i}"] = 0

for index, row in orioles_batting_post.iterrows():
    if row["h"] >= 6:
        orioles_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        orioles_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        orioles_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        orioles_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        orioles_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        orioles_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        orioles_batting_post.at[index, 'Point_Category_7'] = 0.5

orioles_batting_post["Sum_Total_Points"] = orioles_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
orioles_batting_post["Combined_Total_Points"] = orioles_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    red_sox_batting_post[f"Point_Category_{i}"] = 0

for index, row in red_sox_batting_post.iterrows():
    if row["h"] >= 6:
        red_sox_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        red_sox_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        red_sox_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        red_sox_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        red_sox_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        red_sox_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        red_sox_batting_post.at[index, 'Point_Category_7'] = 0.5

red_sox_batting_post["Sum_Total_Points"] = red_sox_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
red_sox_batting_post["Combined_Total_Points"] = red_sox_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    yankees_batting_post[f"Point_Category_{i}"] = 0

for index, row in yankees_batting_post.iterrows():
    if row["h"] >= 6:
        yankees_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        yankees_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        yankees_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        yankees_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        yankees_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        yankees_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        yankees_batting_post.at[index, 'Point_Category_7'] = 0.5

yankees_batting_post["Sum_Total_Points"] = yankees_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
yankees_batting_post["Combined_Total_Points"] = yankees_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    rays_batting_post[f"Point_Category_{i}"] = 0

for index, row in rays_batting_post.iterrows():
    if row["h"] >= 6:
        rays_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        rays_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        rays_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        rays_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        rays_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        rays_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        rays_batting_post.at[index, 'Point_Category_7'] = 0.5

rays_batting_post["Sum_Total_Points"] = rays_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
rays_batting_post["Combined_Total_Points"] = rays_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    blue_jays_batting_post[f"Point_Category_{i}"] = 0

for index, row in blue_jays_batting_post.iterrows():
    if row["h"] >= 6:
        blue_jays_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        blue_jays_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        blue_jays_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        blue_jays_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        blue_jays_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        blue_jays_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        blue_jays_batting_post.at[index, 'Point_Category_7'] = 0.5

blue_jays_batting_post["Sum_Total_Points"] = blue_jays_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
blue_jays_batting_post["Combined_Total_Points"] = blue_jays_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')








for i in range(1, 8):
    white_sox_batting_post[f"Point_Category_{i}"] = 0

for index, row in white_sox_batting_post.iterrows():
    if row["h"] >= 6:
        white_sox_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        white_sox_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        white_sox_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        white_sox_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        white_sox_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        white_sox_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        white_sox_batting_post.at[index, 'Point_Category_7'] = 0.5

white_sox_batting_post["Sum_Total_Points"] = white_sox_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
white_sox_batting_post["Combined_Total_Points"] = white_sox_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    guardians_batting_post[f"Point_Category_{i}"] = 0

for index, row in guardians_batting_post.iterrows():
    if row["h"] >= 6:
        guardians_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        guardians_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        guardians_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        guardians_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        guardians_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        guardians_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        guardians_batting_post.at[index, 'Point_Category_7'] = 0.5

guardians_batting_post["Sum_Total_Points"] = guardians_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
guardians_batting_post["Combined_Total_Points"] = guardians_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    tigers_batting_post[f"Point_Category_{i}"] = 0

for index, row in tigers_batting_post.iterrows():
    if row["h"] >= 6:
        tigers_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        tigers_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        tigers_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        tigers_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        tigers_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        tigers_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        tigers_batting_post.at[index, 'Point_Category_7'] = 0.5

tigers_batting_post["Sum_Total_Points"] = tigers_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
tigers_batting_post["Combined_Total_Points"] = tigers_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    royals_batting_post[f"Point_Category_{i}"] = 0

for index, row in royals_batting_post.iterrows():
    if row["h"] >= 6:
        royals_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        royals_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        royals_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        royals_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        royals_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        royals_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        royals_batting_post.at[index, 'Point_Category_7'] = 0.5

royals_batting_post["Sum_Total_Points"] = royals_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
royals_batting_post["Combined_Total_Points"] = royals_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    twins_batting_post[f"Point_Category_{i}"] = 0

for index, row in twins_batting_post.iterrows():
    if row["h"] >= 6:
        twins_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        twins_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        twins_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        twins_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        twins_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        twins_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        twins_batting_post.at[index, 'Point_Category_7'] = 0.5

twins_batting_post["Sum_Total_Points"] = twins_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
twins_batting_post["Combined_Total_Points"] = twins_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')








for i in range(1, 8):
    astros_batting_post[f"Point_Category_{i}"] = 0

for index, row in astros_batting_post.iterrows():
    if row["h"] >= 6:
        astros_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        astros_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        astros_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        astros_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        astros_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        astros_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        astros_batting_post.at[index, 'Point_Category_7'] = 0.5

astros_batting_post["Sum_Total_Points"] = astros_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
astros_batting_post["Combined_Total_Points"] = astros_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    angels_batting_post[f"Point_Category_{i}"] = 0

for index, row in angels_batting_post.iterrows():
    if row["h"] >= 6:
        angels_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        angels_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        angels_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        angels_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        angels_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        angels_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        angels_batting_post.at[index, 'Point_Category_7'] = 0.5

angels_batting_post["Sum_Total_Points"] = angels_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
angels_batting_post["Combined_Total_Points"] = angels_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    athletics_batting_post[f"Point_Category_{i}"] = 0

for index, row in athletics_batting_post.iterrows():
    if row["h"] >= 6:
        athletics_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        athletics_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        athletics_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        athletics_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        athletics_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        athletics_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        athletics_batting_post.at[index, 'Point_Category_7'] = 0.5

athletics_batting_post["Sum_Total_Points"] = athletics_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
athletics_batting_post["Combined_Total_Points"] = athletics_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    mariners_batting_post[f"Point_Category_{i}"] = 0

for index, row in mariners_batting_post.iterrows():
    if row["h"] >= 6:
        mariners_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        mariners_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        mariners_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        mariners_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        mariners_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        mariners_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        mariners_batting_post.at[index, 'Point_Category_7'] = 0.5

mariners_batting_post["Sum_Total_Points"] = mariners_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
mariners_batting_post["Combined_Total_Points"] = mariners_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    rangers_batting_post[f"Point_Category_{i}"] = 0

for index, row in rangers_batting_post.iterrows():
    if row["h"] >= 6:
        rangers_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        rangers_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        rangers_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        rangers_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        rangers_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        rangers_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        rangers_batting_post.at[index, 'Point_Category_7'] = 0.5

rangers_batting_post["Sum_Total_Points"] = rangers_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
rangers_batting_post["Combined_Total_Points"] = rangers_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')












for i in range(1, 8):
    braves_batting_post[f"Point_Category_{i}"] = 0

for index, row in braves_batting_post.iterrows():
    if row["h"] >= 6:
        braves_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        braves_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        braves_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        braves_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        braves_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        braves_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        braves_batting_post.at[index, 'Point_Category_7'] = 0.5

braves_batting_post["Sum_Total_Points"] = braves_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
braves_batting_post["Combined_Total_Points"] = braves_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    marlins_batting_post[f"Point_Category_{i}"] = 0

for index, row in marlins_batting_post.iterrows():
    if row["h"] >= 6:
        marlins_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        marlins_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        marlins_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        marlins_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        marlins_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        marlins_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        marlins_batting_post.at[index, 'Point_Category_7'] = 0.5

marlins_batting_post["Sum_Total_Points"] = marlins_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
marlins_batting_post["Combined_Total_Points"] = marlins_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    mets_batting_post[f"Point_Category_{i}"] = 0

for index, row in mets_batting_post.iterrows():
    if row["h"] >= 6:
        mets_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        mets_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        mets_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        mets_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        mets_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        mets_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        mets_batting_post.at[index, 'Point_Category_7'] = 0.5

mets_batting_post["Sum_Total_Points"] = mets_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
mets_batting_post["Combined_Total_Points"] = mets_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    nationals_batting_post[f"Point_Category_{i}"] = 0

for index, row in nationals_batting_post.iterrows():
    if row["h"] >= 6:
        nationals_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        nationals_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        nationals_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        nationals_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        nationals_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        nationals_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        nationals_batting_post.at[index, 'Point_Category_7'] = 0.5

nationals_batting_post["Sum_Total_Points"] = nationals_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
nationals_batting_post["Combined_Total_Points"] = nationals_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    phillies_batting_post[f"Point_Category_{i}"] = 0

for index, row in phillies_batting_post.iterrows():
    if row["h"] >= 6:
        phillies_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        phillies_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        phillies_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        phillies_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        phillies_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        phillies_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        phillies_batting_post.at[index, 'Point_Category_7'] = 0.5

phillies_batting_post["Sum_Total_Points"] = phillies_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
phillies_batting_post["Combined_Total_Points"] = phillies_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')








for i in range(1, 8):
    cubs_batting_post[f"Point_Category_{i}"] = 0

for index, row in cubs_batting_post.iterrows():
    if row["h"] >= 6:
        cubs_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        cubs_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        cubs_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        cubs_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        cubs_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        cubs_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        cubs_batting_post.at[index, 'Point_Category_7'] = 0.5

cubs_batting_post["Sum_Total_Points"] = cubs_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
cubs_batting_post["Combined_Total_Points"] = cubs_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    reds_batting_post[f"Point_Category_{i}"] = 0

for index, row in reds_batting_post.iterrows():
    if row["h"] >= 6:
        reds_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        reds_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        reds_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        reds_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        reds_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        reds_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        reds_batting_post.at[index, 'Point_Category_7'] = 0.5

reds_batting_post["Sum_Total_Points"] = reds_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
reds_batting_post["Combined_Total_Points"] = reds_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    brewers_batting_post[f"Point_Category_{i}"] = 0

for index, row in brewers_batting_post.iterrows():
    if row["h"] >= 6:
        brewers_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        brewers_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        brewers_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        brewers_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        brewers_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        brewers_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        brewers_batting_post.at[index, 'Point_Category_7'] = 0.5

brewers_batting_post["Sum_Total_Points"] = brewers_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
brewers_batting_post["Combined_Total_Points"] = brewers_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    pirates_batting_post[f"Point_Category_{i}"] = 0

for index, row in pirates_batting_post.iterrows():
    if row["h"] >= 6:
        pirates_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        pirates_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        pirates_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        pirates_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        pirates_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        pirates_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        pirates_batting_post.at[index, 'Point_Category_7'] = 0.5

pirates_batting_post["Sum_Total_Points"] = pirates_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
pirates_batting_post["Combined_Total_Points"] = pirates_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    cardinals_batting_post[f"Point_Category_{i}"] = 0

for index, row in cardinals_batting_post.iterrows():
    if row["h"] >= 6:
        cardinals_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        cardinals_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        cardinals_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        cardinals_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        cardinals_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        cardinals_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        cardinals_batting_post.at[index, 'Point_Category_7'] = 0.5

cardinals_batting_post["Sum_Total_Points"] = cardinals_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
cardinals_batting_post["Combined_Total_Points"] = cardinals_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')








for i in range(1, 8):
    diamondbacks_batting_post[f"Point_Category_{i}"] = 0

for index, row in diamondbacks_batting_post.iterrows():
    if row["h"] >= 6:
        diamondbacks_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        diamondbacks_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        diamondbacks_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        diamondbacks_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        diamondbacks_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        diamondbacks_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        diamondbacks_batting_post.at[index, 'Point_Category_7'] = 0.5

diamondbacks_batting_post["Sum_Total_Points"] = diamondbacks_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
diamondbacks_batting_post["Combined_Total_Points"] = diamondbacks_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    rockies_batting_post[f"Point_Category_{i}"] = 0

for index, row in rockies_batting_post.iterrows():
    if row["h"] >= 6:
        rockies_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        rockies_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        rockies_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        rockies_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        rockies_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        rockies_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        rockies_batting_post.at[index, 'Point_Category_7'] = 0.5

rockies_batting_post["Sum_Total_Points"] = rockies_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
rockies_batting_post["Combined_Total_Points"] = rockies_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    dodgers_batting_post[f"Point_Category_{i}"] = 0

for index, row in dodgers_batting_post.iterrows():
    if row["h"] >= 6:
        dodgers_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        dodgers_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        dodgers_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        dodgers_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        dodgers_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        dodgers_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        dodgers_batting_post.at[index, 'Point_Category_7'] = 0.5

dodgers_batting_post["Sum_Total_Points"] = dodgers_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
dodgers_batting_post["Combined_Total_Points"] = dodgers_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    padres_batting_post[f"Point_Category_{i}"] = 0

for index, row in padres_batting_post.iterrows():
    if row["h"] >= 6:
        padres_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        padres_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        padres_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        padres_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        padres_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        padres_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        padres_batting_post.at[index, 'Point_Category_7'] = 0.5

padres_batting_post["Sum_Total_Points"] = padres_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
padres_batting_post["Combined_Total_Points"] = padres_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 8):
    giants_batting_post[f"Point_Category_{i}"] = 0

for index, row in giants_batting_post.iterrows():
    if row["h"] >= 6:
        giants_batting_post.at[index, "Point_Category_1"] = 1
    if row["double"] >= 2:
        giants_batting_post.at[index, "Point_Category_2"] = 0.5
    if row["r"] >= 5:
        giants_batting_post.at[index, "Point_Category_3"] = 1
    if row["hr"] >= 2:
        giants_batting_post.at[index, "Point_Category_4"] = 1
    if row["rbi"] >= 7:
        giants_batting_post.at[index, "Point_Category_5"] = 1
    if row["sb"] >= 2:
        giants_batting_post.at[index, "Point_Category_6"] = 0.5

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.750:
        giants_batting_post.at[index, 'Point_Category_7'] = 0.5

giants_batting_post["Sum_Total_Points"] = giants_batting_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
giants_batting_post["Combined_Total_Points"] = giants_batting_post.groupby("player_id")["Sum_Total_Points"].transform('sum')








# Infielding per team (each single season batting observation for a single franchise)

# Creating new dataframes for each team (redundant, but required when I concatenate this dataframe and the filtered one for my function)


orioles_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
red_sox_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
yankees_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
rays_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
blue_jays_infielding = pd.DataFrame(columns = fielding_infield_data.columns)

white_sox_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
guardians_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
tigers_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
royals_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
twins_infielding = pd.DataFrame(columns = fielding_infield_data.columns)

astros_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
angels_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
athletics_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
mariners_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
rangers_infielding = pd.DataFrame(columns = fielding_infield_data.columns)



braves_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
marlins_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
mets_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
nationals_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
phillies_infielding = pd.DataFrame(columns = fielding_infield_data.columns)

cubs_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
reds_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
brewers_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
pirates_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
cardinals_infielding = pd.DataFrame(columns = fielding_infield_data.columns)

diamondbacks_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
rockies_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
dodgers_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
padres_infielding = pd.DataFrame(columns = fielding_infield_data.columns)
giants_infielding = pd.DataFrame(columns = fielding_infield_data.columns)


# Defining a functino where I take in a list of team ids and an existing empty team infielding dataframe
# Filters out all observations that do not have any of the specified team_ids
# Returns a concatenation of the filtered dataframe and the empty dataframe (basically copying and pasting the filtered dataframe)

def append_specified_team_ids_infielding(team_ids, target_df):
    filtered_df = fielding_infield_data[fielding_infield_data["team_id"].isin(team_ids)]
    return pd.concat([target_df, filtered_df], ignore_index = True)



orioles_infielding = append_specified_team_ids_infielding(orioles_teams, orioles_infielding)
red_sox_infielding = append_specified_team_ids_infielding(red_sox_teams, red_sox_infielding)
yankees_infielding = append_specified_team_ids_infielding(yankees_teams, yankees_infielding)
rays_infielding = append_specified_team_ids_infielding(rays_teams, rays_infielding)
blue_jays_infielding = append_specified_team_ids_infielding(blue_jays_teams, blue_jays_infielding)

white_sox_infielding = append_specified_team_ids_infielding(white_sox_teams, white_sox_infielding)
guardians_infielding = append_specified_team_ids_infielding(guardians_teams, guardians_infielding)
tigers_infielding = append_specified_team_ids_infielding(tigers_teams, tigers_infielding)
royals_infielding = append_specified_team_ids_infielding(royals_teams, royals_infielding)
twins_infielding = append_specified_team_ids_infielding(twins_teams, twins_infielding)

astros_infielding = append_specified_team_ids_infielding(astros_teams, astros_infielding)
angels_infielding = append_specified_team_ids_infielding(angels_teams, angels_infielding)
athletics_infielding = append_specified_team_ids_infielding(athletics_teams, athletics_infielding)
mariners_infielding = append_specified_team_ids_infielding(mariners_teams, mariners_infielding)
rangers_infielding = append_specified_team_ids_infielding(rangers_teams, rangers_infielding)




braves_infielding = append_specified_team_ids_infielding(braves_teams, braves_infielding)
marlins_infielding = append_specified_team_ids_infielding(marlins_teams, marlins_infielding)
mets_infielding = append_specified_team_ids_infielding(mets_teams, mets_infielding)
nationals_infielding = append_specified_team_ids_infielding(nationals_teams, nationals_infielding)
phillies_infielding = append_specified_team_ids_infielding(phillies_teams, phillies_infielding)

cubs_infielding = append_specified_team_ids_infielding(cubs_teams, cubs_infielding)
reds_infielding = append_specified_team_ids_infielding(reds_teams, reds_infielding)
brewers_infielding = append_specified_team_ids_infielding(brewers_teams, brewers_infielding)
pirates_infielding = append_specified_team_ids_infielding(pirates_teams, pirates_infielding)
cardinals_infielding = append_specified_team_ids_infielding(cardinals_teams, cardinals_infielding)

diamondbacks_infielding = append_specified_team_ids_infielding(diamondbacks_teams, diamondbacks_infielding)
rockies_infielding = append_specified_team_ids_infielding(rockies_teams, rockies_infielding)
dodgers_infielding = append_specified_team_ids_infielding(dodgers_teams, dodgers_infielding)
padres_infielding = append_specified_team_ids_infielding(padres_teams, padres_infielding)
giants_infielding = append_specified_team_ids_infielding(giants_teams, giants_infielding)





# Defining points for each of the regular season infielding stats.
# First, a number of point category columns are created based on how many I want
# Second, in each batting dataset, I look to see if an observation satisfies each of the if statements. If they do, they get points assigned to the point categories
# I then get the sum of the points per that given season called Sum_Total_Points
# Lastly, I get the sum of the career number of points, the column called Combined_Total_Points

for i in range(1, 9):
    orioles_infielding[f"Point_Category_{i}"] = 0

for index, row in orioles_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            orioles_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            orioles_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            orioles_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            orioles_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            orioles_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            orioles_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            orioles_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            orioles_infielding.at[index, 'Point_Category_8'] = 1
    
orioles_infielding["Sum_Total_Points"] = orioles_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
orioles_infielding["Combined_Total_Points"] = orioles_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    red_sox_infielding[f"Point_Category_{i}"] = 0

for index, row in red_sox_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            red_sox_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            red_sox_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            red_sox_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            red_sox_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            red_sox_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            red_sox_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            red_sox_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            red_sox_infielding.at[index, 'Point_Category_8'] = 1
    
red_sox_infielding["Sum_Total_Points"] = red_sox_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
red_sox_infielding["Combined_Total_Points"] = red_sox_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    yankees_infielding[f"Point_Category_{i}"] = 0

for index, row in yankees_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            yankees_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            yankees_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            yankees_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            yankees_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            yankees_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            yankees_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            yankees_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            yankees_infielding.at[index, 'Point_Category_8'] = 1
    
yankees_infielding["Sum_Total_Points"] = yankees_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
yankees_infielding["Combined_Total_Points"] = yankees_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    rays_infielding[f"Point_Category_{i}"] = 0

for index, row in rays_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            rays_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            rays_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            rays_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            rays_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            rays_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            rays_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            rays_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            rays_infielding.at[index, 'Point_Category_8'] = 1
    
rays_infielding["Sum_Total_Points"] = rays_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
rays_infielding["Combined_Total_Points"] = rays_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    blue_jays_infielding[f"Point_Category_{i}"] = 0

for index, row in blue_jays_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            blue_jays_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            blue_jays_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            blue_jays_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            blue_jays_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            blue_jays_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            blue_jays_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            blue_jays_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            blue_jays_infielding.at[index, 'Point_Category_8'] = 1
    
blue_jays_infielding["Sum_Total_Points"] = blue_jays_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
blue_jays_infielding["Combined_Total_Points"] = blue_jays_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')








for i in range(1, 9):
    white_sox_infielding[f"Point_Category_{i}"] = 0

for index, row in white_sox_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            white_sox_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            white_sox_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            white_sox_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            white_sox_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            white_sox_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            white_sox_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            white_sox_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            white_sox_infielding.at[index, 'Point_Category_8'] = 1
    
white_sox_infielding["Sum_Total_Points"] = white_sox_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
white_sox_infielding["Combined_Total_Points"] = white_sox_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    guardians_infielding[f"Point_Category_{i}"] = 0

for index, row in guardians_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            guardians_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            guardians_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            guardians_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            guardians_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            guardians_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            guardians_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            guardians_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            guardians_infielding.at[index, 'Point_Category_8'] = 1
    
guardians_infielding["Sum_Total_Points"] = guardians_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
guardians_infielding["Combined_Total_Points"] = guardians_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    tigers_infielding[f"Point_Category_{i}"] = 0

for index, row in tigers_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            tigers_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            tigers_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            tigers_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            tigers_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            tigers_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            tigers_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            tigers_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            tigers_infielding.at[index, 'Point_Category_8'] = 1
    
tigers_infielding["Sum_Total_Points"] = tigers_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
tigers_infielding["Combined_Total_Points"] = tigers_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    royals_infielding[f"Point_Category_{i}"] = 0

for index, row in royals_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            royals_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            royals_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            royals_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            royals_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            royals_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            royals_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            royals_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            royals_infielding.at[index, 'Point_Category_8'] = 1
    
royals_infielding["Sum_Total_Points"] = royals_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
royals_infielding["Combined_Total_Points"] = royals_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    twins_infielding[f"Point_Category_{i}"] = 0

for index, row in twins_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            twins_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            twins_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            twins_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            twins_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            twins_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            twins_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            twins_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            twins_infielding.at[index, 'Point_Category_8'] = 1
    
twins_infielding["Sum_Total_Points"] = twins_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
twins_infielding["Combined_Total_Points"] = twins_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')









for i in range(1, 9):
    astros_infielding[f"Point_Category_{i}"] = 0

for index, row in astros_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            astros_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            astros_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            astros_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            astros_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            astros_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            astros_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            astros_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            astros_infielding.at[index, 'Point_Category_8'] = 1
    
astros_infielding["Sum_Total_Points"] = astros_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
astros_infielding["Combined_Total_Points"] = astros_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    angels_infielding[f"Point_Category_{i}"] = 0

for index, row in angels_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            angels_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            angels_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            angels_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            angels_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            angels_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            angels_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            angels_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            angels_infielding.at[index, 'Point_Category_8'] = 1
    
angels_infielding["Sum_Total_Points"] = angels_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
angels_infielding["Combined_Total_Points"] = angels_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    athletics_infielding[f"Point_Category_{i}"] = 0

for index, row in athletics_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            athletics_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            athletics_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            athletics_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            athletics_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            athletics_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            athletics_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            athletics_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            athletics_infielding.at[index, 'Point_Category_8'] = 1
    
athletics_infielding["Sum_Total_Points"] = athletics_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
athletics_infielding["Combined_Total_Points"] = athletics_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    mariners_infielding[f"Point_Category_{i}"] = 0

for index, row in mariners_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            mariners_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            mariners_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            mariners_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            mariners_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            mariners_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            mariners_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            mariners_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            mariners_infielding.at[index, 'Point_Category_8'] = 1
    
mariners_infielding["Sum_Total_Points"] = mariners_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
mariners_infielding["Combined_Total_Points"] = mariners_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    rangers_infielding[f"Point_Category_{i}"] = 0

for index, row in rangers_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            rangers_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            rangers_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            rangers_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            rangers_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            rangers_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            rangers_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            rangers_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            rangers_infielding.at[index, 'Point_Category_8'] = 1
    
rangers_infielding["Sum_Total_Points"] = rangers_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
rangers_infielding["Combined_Total_Points"] = rangers_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')












for i in range(1, 9):
    braves_infielding[f"Point_Category_{i}"] = 0

for index, row in braves_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            braves_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            braves_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            braves_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            braves_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            braves_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            braves_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            braves_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            braves_infielding.at[index, 'Point_Category_8'] = 1
    
braves_infielding["Sum_Total_Points"] = braves_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
braves_infielding["Combined_Total_Points"] = braves_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    marlins_infielding[f"Point_Category_{i}"] = 0

for index, row in marlins_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            marlins_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            marlins_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            marlins_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            marlins_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            marlins_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            marlins_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            marlins_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            marlins_infielding.at[index, 'Point_Category_8'] = 1
    
marlins_infielding["Sum_Total_Points"] = marlins_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
marlins_infielding["Combined_Total_Points"] = marlins_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    mets_infielding[f"Point_Category_{i}"] = 0

for index, row in mets_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            mets_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            mets_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            mets_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            mets_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            mets_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            mets_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            mets_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            mets_infielding.at[index, 'Point_Category_8'] = 1
    
mets_infielding["Sum_Total_Points"] = mets_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
mets_infielding["Combined_Total_Points"] = mets_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    nationals_infielding[f"Point_Category_{i}"] = 0

for index, row in nationals_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            nationals_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            nationals_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            nationals_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            nationals_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            nationals_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            nationals_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            nationals_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            nationals_infielding.at[index, 'Point_Category_8'] = 1
    
nationals_infielding["Sum_Total_Points"] = nationals_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
nationals_infielding["Combined_Total_Points"] = nationals_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 9):
    phillies_infielding[f"Point_Category_{i}"] = 0

for index, row in phillies_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            phillies_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            phillies_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            phillies_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            phillies_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            phillies_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            phillies_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            phillies_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            phillies_infielding.at[index, 'Point_Category_8'] = 1
    
phillies_infielding["Sum_Total_Points"] = phillies_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
phillies_infielding["Combined_Total_Points"] = phillies_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')






for i in range(1, 9):
    cubs_infielding[f"Point_Category_{i}"] = 0

for index, row in cubs_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            cubs_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            cubs_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            cubs_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            cubs_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            cubs_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            cubs_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            cubs_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            cubs_infielding.at[index, 'Point_Category_8'] = 1
    
cubs_infielding["Sum_Total_Points"] = cubs_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
cubs_infielding["Combined_Total_Points"] = cubs_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 9):
    reds_infielding[f"Point_Category_{i}"] = 0

for index, row in reds_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            reds_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            reds_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            reds_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            reds_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            reds_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            reds_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            reds_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            reds_infielding.at[index, 'Point_Category_8'] = 1
    
reds_infielding["Sum_Total_Points"] = reds_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
reds_infielding["Combined_Total_Points"] = reds_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 9):
    brewers_infielding[f"Point_Category_{i}"] = 0

for index, row in brewers_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            brewers_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            brewers_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            brewers_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            brewers_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            brewers_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            brewers_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            brewers_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            brewers_infielding.at[index, 'Point_Category_8'] = 1
    
brewers_infielding["Sum_Total_Points"] = brewers_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
brewers_infielding["Combined_Total_Points"] = brewers_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 9):
    pirates_infielding[f"Point_Category_{i}"] = 0

for index, row in pirates_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            pirates_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            pirates_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            pirates_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            pirates_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            pirates_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            pirates_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            pirates_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            pirates_infielding.at[index, 'Point_Category_8'] = 1
    
pirates_infielding["Sum_Total_Points"] = pirates_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
pirates_infielding["Combined_Total_Points"] = pirates_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 9):
    cardinals_infielding[f"Point_Category_{i}"] = 0

for index, row in cardinals_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            cardinals_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            cardinals_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            cardinals_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            cardinals_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            cardinals_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            cardinals_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            cardinals_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            cardinals_infielding.at[index, 'Point_Category_8'] = 1
    
cardinals_infielding["Sum_Total_Points"] = cardinals_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
cardinals_infielding["Combined_Total_Points"] = cardinals_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')






for i in range(1, 9):
    diamondbacks_infielding[f"Point_Category_{i}"] = 0

for index, row in diamondbacks_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            diamondbacks_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            diamondbacks_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            diamondbacks_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            diamondbacks_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            diamondbacks_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            diamondbacks_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            diamondbacks_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            diamondbacks_infielding.at[index, 'Point_Category_8'] = 1
    
diamondbacks_infielding["Sum_Total_Points"] = diamondbacks_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
diamondbacks_infielding["Combined_Total_Points"] = diamondbacks_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 9):
    rockies_infielding[f"Point_Category_{i}"] = 0

for index, row in rockies_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            rockies_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            rockies_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            rockies_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            rockies_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            rockies_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            rockies_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            rockies_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            rockies_infielding.at[index, 'Point_Category_8'] = 1
    
rockies_infielding["Sum_Total_Points"] = rockies_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
rockies_infielding["Combined_Total_Points"] = rockies_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 9):
    dodgers_infielding[f"Point_Category_{i}"] = 0

for index, row in dodgers_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            dodgers_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            dodgers_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            dodgers_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            dodgers_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            dodgers_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            dodgers_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            dodgers_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            dodgers_infielding.at[index, 'Point_Category_8'] = 1
    
dodgers_infielding["Sum_Total_Points"] = dodgers_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
dodgers_infielding["Combined_Total_Points"] = dodgers_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 9):
    padres_infielding[f"Point_Category_{i}"] = 0

for index, row in padres_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            padres_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            padres_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            padres_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            padres_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            padres_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            padres_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            padres_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            padres_infielding.at[index, 'Point_Category_8'] = 1
    
padres_infielding["Sum_Total_Points"] = padres_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
padres_infielding["Combined_Total_Points"] = padres_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 9):
    giants_infielding[f"Point_Category_{i}"] = 0

for index, row in giants_infielding.iterrows():
    if row["g"] >= 81:
        if row["po"] >= 1000:
            giants_infielding.at[index, "Point_Category_1"] = 1
        if row["po"] >= 1400:
            giants_infielding.at[index, "Point_Category_2"] = 1
        if row["a"] >= 500:
            giants_infielding.at[index, "Point_Category_3"] = 1
        if row["a"] >= 400:
            giants_infielding.at[index, "Point_Category_4"] = 1
        if row["e"] <= 13:
            giants_infielding.at[index, "Point_Category_5"] = 1
        if row["e"] <= 8:
            giants_infielding.at[index, "Point_Category_6"] = 1
        if row["dp"] >= 110:
            giants_infielding.at[index, "Point_Category_7"] = 1
        if row["cs"] >= 40:
            giants_infielding.at[index, 'Point_Category_8'] = 1
    
giants_infielding["Sum_Total_Points"] = giants_infielding[[f"Point_Category_{i}" for i in range(1, 9)]].sum(axis=1)
giants_infielding["Combined_Total_Points"] = giants_infielding.groupby("player_id")["Sum_Total_Points"].transform('sum')









# Post fielding per team

# Creating new dataframes for each team (redundant, but required when I concatenate this dataframe and the filtered one for my function)


orioles_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
red_sox_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
yankees_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
rays_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
blue_jays_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)

white_sox_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
guardians_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
tigers_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
royals_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
twins_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)

astros_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
angels_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
athletics_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
mariners_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
rangers_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)



braves_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
marlins_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
mets_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
nationals_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
phillies_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)

cubs_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
reds_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
brewers_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
pirates_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
cardinals_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)

diamondbacks_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
rockies_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
dodgers_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
padres_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)
giants_fielding_post = pd.DataFrame(columns = fielding_post_data.columns)


# Defining a functino where I take in a list of team ids and an existing empty team infielding post dataframe
# Filters out all observations that do not have any of the specified team_ids
# Returns a concatenation of the filtered dataframe and the empty dataframe (basically copying and pasting the filtered dataframe)

def append_specified_team_ids_fielding_post(team_ids, target_df):
    filtered_df = fielding_post_data[fielding_post_data["team_id"].isin(team_ids)]
    return pd.concat([target_df, filtered_df], ignore_index = True)




orioles_fielding_post = append_specified_team_ids_fielding_post(orioles_teams, orioles_fielding_post)
red_sox_fielding_post = append_specified_team_ids_fielding_post(red_sox_teams, red_sox_fielding_post)
yankees_fielding_post = append_specified_team_ids_fielding_post(yankees_teams, yankees_fielding_post)
rays_fielding_post = append_specified_team_ids_fielding_post(rays_teams, rays_fielding_post)
blue_jays_fielding_post = append_specified_team_ids_fielding_post(blue_jays_teams, blue_jays_fielding_post)

white_sox_fielding_post = append_specified_team_ids_fielding_post(white_sox_teams, white_sox_fielding_post)
guardians_fielding_post = append_specified_team_ids_fielding_post(guardians_teams, guardians_fielding_post)
tigers_fielding_post = append_specified_team_ids_fielding_post(tigers_teams, tigers_fielding_post)
royals_fielding_post = append_specified_team_ids_fielding_post(royals_teams, royals_fielding_post)
twins_fielding_post = append_specified_team_ids_fielding_post(twins_teams, twins_fielding_post)

astros_fielding_post = append_specified_team_ids_fielding_post(astros_teams, astros_fielding_post)
angels_fielding_post = append_specified_team_ids_fielding_post(angels_teams, angels_fielding_post)
athletics_fielding_post = append_specified_team_ids_fielding_post(athletics_teams, athletics_fielding_post)
mariners_fielding_post = append_specified_team_ids_fielding_post(mariners_teams, mariners_fielding_post)
rangers_fielding_post = append_specified_team_ids_fielding_post(rangers_teams, rangers_fielding_post)




braves_fielding_post = append_specified_team_ids_fielding_post(braves_teams, braves_fielding_post)
marlins_fielding_post = append_specified_team_ids_fielding_post(marlins_teams, marlins_fielding_post)
mets_fielding_post = append_specified_team_ids_fielding_post(mets_teams, mets_fielding_post)
nationals_fielding_post = append_specified_team_ids_fielding_post(nationals_teams, nationals_fielding_post)
phillies_fielding_post = append_specified_team_ids_fielding_post(phillies_teams, phillies_fielding_post)

cubs_fielding_post = append_specified_team_ids_fielding_post(cubs_teams, cubs_fielding_post)
reds_fielding_post = append_specified_team_ids_fielding_post(reds_teams, reds_fielding_post)
brewers_fielding_post = append_specified_team_ids_fielding_post(brewers_teams, brewers_fielding_post)
pirates_fielding_post = append_specified_team_ids_fielding_post(pirates_teams, pirates_fielding_post)
cardinals_fielding_post = append_specified_team_ids_fielding_post(cardinals_teams, cardinals_fielding_post)

diamondbacks_fielding_post = append_specified_team_ids_fielding_post(diamondbacks_teams, diamondbacks_fielding_post)
rockies_fielding_post = append_specified_team_ids_fielding_post(rockies_teams, rockies_fielding_post)
dodgers_fielding_post = append_specified_team_ids_fielding_post(dodgers_teams, dodgers_fielding_post)
padres_fielding_post = append_specified_team_ids_fielding_post(padres_teams, padres_fielding_post)
giants_fielding_post = append_specified_team_ids_fielding_post(giants_teams, giants_fielding_post)









# Defining points for each of the post season infielding stats.
# First, a number of point category columns are created based on how many I want
# Second, in each batting dataset, I look to see if an observation satisfies each of the if statements. If they do, they get points assigned to the point categories
# I then get the sum of the points per that given season called Sum_Total_Points
# Lastly, I get the sum of the career number of points, the column called Combined_Total_Points

for i in range(1, 8):
    orioles_fielding_post[f"Point_Category_{i}"] = 0

for index, row in orioles_fielding_post.iterrows():
    if row["po"] >= 25:
        orioles_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        orioles_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        orioles_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        orioles_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        orioles_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        orioles_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        orioles_fielding_post.at[index, "Point_Category_7"] = 4
    
orioles_fielding_post["Sum_Total_Points"] = orioles_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
orioles_fielding_post["Combined_Total_Points"] = orioles_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    red_sox_fielding_post[f"Point_Category_{i}"] = 0

for index, row in red_sox_fielding_post.iterrows():
    if row["po"] >= 25:
        red_sox_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        red_sox_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        red_sox_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        red_sox_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        red_sox_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        red_sox_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        red_sox_fielding_post.at[index, "Point_Category_7"] = 4
    
red_sox_fielding_post["Sum_Total_Points"] = red_sox_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
red_sox_fielding_post["Combined_Total_Points"] = red_sox_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    yankees_fielding_post[f"Point_Category_{i}"] = 0

for index, row in yankees_fielding_post.iterrows():
    if row["po"] >= 25:
        yankees_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        yankees_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        yankees_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        yankees_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        yankees_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        yankees_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        yankees_fielding_post.at[index, "Point_Category_7"] = 4
    
yankees_fielding_post["Sum_Total_Points"] = yankees_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
yankees_fielding_post["Combined_Total_Points"] = yankees_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    rays_fielding_post[f"Point_Category_{i}"] = 0

for index, row in rays_fielding_post.iterrows():
    if row["po"] >= 25:
        rays_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        rays_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        rays_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        rays_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        rays_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        rays_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        rays_fielding_post.at[index, "Point_Category_7"] = 4
    
rays_fielding_post["Sum_Total_Points"] = rays_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
rays_fielding_post["Combined_Total_Points"] = rays_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    blue_jays_fielding_post[f"Point_Category_{i}"] = 0

for index, row in blue_jays_fielding_post.iterrows():
    if row["po"] >= 25:
        blue_jays_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        blue_jays_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        blue_jays_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        blue_jays_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        blue_jays_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        blue_jays_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        blue_jays_fielding_post.at[index, "Point_Category_7"] = 4
    
blue_jays_fielding_post["Sum_Total_Points"] = blue_jays_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
blue_jays_fielding_post["Combined_Total_Points"] = blue_jays_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')









for i in range(1, 8):
    white_sox_fielding_post[f"Point_Category_{i}"] = 0

for index, row in white_sox_fielding_post.iterrows():
    if row["po"] >= 25:
        white_sox_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        white_sox_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        white_sox_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        white_sox_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        white_sox_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        white_sox_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        white_sox_fielding_post.at[index, "Point_Category_7"] = 4
    
white_sox_fielding_post["Sum_Total_Points"] = white_sox_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
white_sox_fielding_post["Combined_Total_Points"] = white_sox_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    guardians_fielding_post[f"Point_Category_{i}"] = 0

for index, row in guardians_fielding_post.iterrows():
    if row["po"] >= 25:
        guardians_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        guardians_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        guardians_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        guardians_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        guardians_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        guardians_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        guardians_fielding_post.at[index, "Point_Category_7"] = 4
    
guardians_fielding_post["Sum_Total_Points"] = guardians_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
guardians_fielding_post["Combined_Total_Points"] = guardians_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    tigers_fielding_post[f"Point_Category_{i}"] = 0

for index, row in tigers_fielding_post.iterrows():
    if row["po"] >= 25:
        tigers_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        tigers_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        tigers_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        tigers_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        tigers_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        tigers_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        tigers_fielding_post.at[index, "Point_Category_7"] = 4
    
tigers_fielding_post["Sum_Total_Points"] = tigers_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
tigers_fielding_post["Combined_Total_Points"] = tigers_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    royals_fielding_post[f"Point_Category_{i}"] = 0

for index, row in royals_fielding_post.iterrows():
    if row["po"] >= 25:
        royals_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        royals_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        royals_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        royals_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        royals_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        royals_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        royals_fielding_post.at[index, "Point_Category_7"] = 4
    
royals_fielding_post["Sum_Total_Points"] = royals_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
royals_fielding_post["Combined_Total_Points"] = royals_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    twins_fielding_post[f"Point_Category_{i}"] = 0

for index, row in twins_fielding_post.iterrows():
    if row["po"] >= 25:
        twins_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        twins_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        twins_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        twins_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        twins_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        twins_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        twins_fielding_post.at[index, "Point_Category_7"] = 4
    
twins_fielding_post["Sum_Total_Points"] = twins_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
twins_fielding_post["Combined_Total_Points"] = twins_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')







for i in range(1, 8):
    astros_fielding_post[f"Point_Category_{i}"] = 0

for index, row in astros_fielding_post.iterrows():
    if row["po"] >= 25:
        astros_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        astros_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        astros_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        astros_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        astros_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        astros_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        astros_fielding_post.at[index, "Point_Category_7"] = 4
    
astros_fielding_post["Sum_Total_Points"] = astros_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
astros_fielding_post["Combined_Total_Points"] = astros_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    angels_fielding_post[f"Point_Category_{i}"] = 0

for index, row in angels_fielding_post.iterrows():
    if row["po"] >= 25:
        angels_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        angels_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        angels_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        angels_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        angels_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        angels_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        angels_fielding_post.at[index, "Point_Category_7"] = 4
    
angels_fielding_post["Sum_Total_Points"] = angels_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
angels_fielding_post["Combined_Total_Points"] = angels_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    athletics_fielding_post[f"Point_Category_{i}"] = 0

for index, row in athletics_fielding_post.iterrows():
    if row["po"] >= 25:
        athletics_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        athletics_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        athletics_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        athletics_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        athletics_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        athletics_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        athletics_fielding_post.at[index, "Point_Category_7"] = 4
    
athletics_fielding_post["Sum_Total_Points"] = athletics_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
athletics_fielding_post["Combined_Total_Points"] = athletics_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    mariners_fielding_post[f"Point_Category_{i}"] = 0

for index, row in mariners_fielding_post.iterrows():
    if row["po"] >= 25:
        mariners_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        mariners_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        mariners_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        mariners_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        mariners_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        mariners_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        mariners_fielding_post.at[index, "Point_Category_7"] = 4
    
mariners_fielding_post["Sum_Total_Points"] = mariners_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
mariners_fielding_post["Combined_Total_Points"] = mariners_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    rangers_fielding_post[f"Point_Category_{i}"] = 0

for index, row in rangers_fielding_post.iterrows():
    if row["po"] >= 25:
        rangers_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        rangers_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        rangers_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        rangers_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        rangers_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        rangers_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        rangers_fielding_post.at[index, "Point_Category_7"] = 4
    
rangers_fielding_post["Sum_Total_Points"] = rangers_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
rangers_fielding_post["Combined_Total_Points"] = rangers_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')








for i in range(1, 8):
    braves_fielding_post[f"Point_Category_{i}"] = 0

for index, row in braves_fielding_post.iterrows():
    if row["po"] >= 25:
        braves_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        braves_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        braves_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        braves_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        braves_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        braves_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        braves_fielding_post.at[index, "Point_Category_7"] = 4
    
braves_fielding_post["Sum_Total_Points"] = braves_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
braves_fielding_post["Combined_Total_Points"] = braves_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    marlins_fielding_post[f"Point_Category_{i}"] = 0

for index, row in marlins_fielding_post.iterrows():
    if row["po"] >= 25:
        marlins_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        marlins_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        marlins_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        marlins_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        marlins_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        marlins_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        marlins_fielding_post.at[index, "Point_Category_7"] = 4
    
marlins_fielding_post["Sum_Total_Points"] = marlins_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
marlins_fielding_post["Combined_Total_Points"] = marlins_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    mets_fielding_post[f"Point_Category_{i}"] = 0

for index, row in mets_fielding_post.iterrows():
    if row["po"] >= 25:
        mets_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        mets_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        mets_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        mets_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        mets_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        mets_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        mets_fielding_post.at[index, "Point_Category_7"] = 4
    
mets_fielding_post["Sum_Total_Points"] = mets_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
mets_fielding_post["Combined_Total_Points"] = mets_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    nationals_fielding_post[f"Point_Category_{i}"] = 0

for index, row in nationals_fielding_post.iterrows():
    if row["po"] >= 25:
        nationals_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        nationals_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        nationals_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        nationals_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        nationals_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        nationals_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        nationals_fielding_post.at[index, "Point_Category_7"] = 4
    
nationals_fielding_post["Sum_Total_Points"] = nationals_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
nationals_fielding_post["Combined_Total_Points"] = nationals_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    phillies_fielding_post[f"Point_Category_{i}"] = 0

for index, row in phillies_fielding_post.iterrows():
    if row["po"] >= 25:
        phillies_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        phillies_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        phillies_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        phillies_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        phillies_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        phillies_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        phillies_fielding_post.at[index, "Point_Category_7"] = 4
    
phillies_fielding_post["Sum_Total_Points"] = phillies_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
phillies_fielding_post["Combined_Total_Points"] = phillies_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')









for i in range(1, 8):
    cubs_fielding_post[f"Point_Category_{i}"] = 0

for index, row in cubs_fielding_post.iterrows():
    if row["po"] >= 25:
        cubs_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        cubs_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        cubs_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        cubs_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        cubs_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        cubs_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        cubs_fielding_post.at[index, "Point_Category_7"] = 4
    
cubs_fielding_post["Sum_Total_Points"] = cubs_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
cubs_fielding_post["Combined_Total_Points"] = cubs_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    reds_fielding_post[f"Point_Category_{i}"] = 0

for index, row in reds_fielding_post.iterrows():
    if row["po"] >= 25:
        reds_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        reds_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        reds_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        reds_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        reds_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        reds_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        reds_fielding_post.at[index, "Point_Category_7"] = 4
    
reds_fielding_post["Sum_Total_Points"] = reds_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
reds_fielding_post["Combined_Total_Points"] = reds_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    brewers_fielding_post[f"Point_Category_{i}"] = 0

for index, row in brewers_fielding_post.iterrows():
    if row["po"] >= 25:
        brewers_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        brewers_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        brewers_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        brewers_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        brewers_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        brewers_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        brewers_fielding_post.at[index, "Point_Category_7"] = 4
    
brewers_fielding_post["Sum_Total_Points"] = brewers_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
brewers_fielding_post["Combined_Total_Points"] = brewers_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    pirates_fielding_post[f"Point_Category_{i}"] = 0

for index, row in pirates_fielding_post.iterrows():
    if row["po"] >= 25:
        pirates_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        pirates_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        pirates_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        pirates_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        pirates_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        pirates_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        pirates_fielding_post.at[index, "Point_Category_7"] = 4
    
pirates_fielding_post["Sum_Total_Points"] = pirates_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
pirates_fielding_post["Combined_Total_Points"] = pirates_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    cardinals_fielding_post[f"Point_Category_{i}"] = 0

for index, row in cardinals_fielding_post.iterrows():
    if row["po"] >= 25:
        cardinals_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        cardinals_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        cardinals_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        cardinals_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        cardinals_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        cardinals_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        cardinals_fielding_post.at[index, "Point_Category_7"] = 4
    
cardinals_fielding_post["Sum_Total_Points"] = cardinals_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
cardinals_fielding_post["Combined_Total_Points"] = cardinals_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')









for i in range(1, 8):
    diamondbacks_fielding_post[f"Point_Category_{i}"] = 0

for index, row in diamondbacks_fielding_post.iterrows():
    if row["po"] >= 25:
        diamondbacks_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        diamondbacks_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        diamondbacks_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        diamondbacks_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        diamondbacks_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        diamondbacks_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        diamondbacks_fielding_post.at[index, "Point_Category_7"] = 4
    
diamondbacks_fielding_post["Sum_Total_Points"] = diamondbacks_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
diamondbacks_fielding_post["Combined_Total_Points"] = diamondbacks_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    rockies_fielding_post[f"Point_Category_{i}"] = 0

for index, row in rockies_fielding_post.iterrows():
    if row["po"] >= 25:
        rockies_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        rockies_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        rockies_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        rockies_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        rockies_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        rockies_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        rockies_fielding_post.at[index, "Point_Category_7"] = 4
    
rockies_fielding_post["Sum_Total_Points"] = rockies_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
rockies_fielding_post["Combined_Total_Points"] = rockies_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    dodgers_fielding_post[f"Point_Category_{i}"] = 0

for index, row in dodgers_fielding_post.iterrows():
    if row["po"] >= 25:
        dodgers_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        dodgers_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        dodgers_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        dodgers_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        dodgers_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        dodgers_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        dodgers_fielding_post.at[index, "Point_Category_7"] = 4
    
dodgers_fielding_post["Sum_Total_Points"] = dodgers_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
dodgers_fielding_post["Combined_Total_Points"] = dodgers_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    padres_fielding_post[f"Point_Category_{i}"] = 0

for index, row in padres_fielding_post.iterrows():
    if row["po"] >= 25:
        padres_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        padres_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        padres_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        padres_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        padres_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        padres_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        padres_fielding_post.at[index, "Point_Category_7"] = 4

    
padres_fielding_post["Sum_Total_Points"] = padres_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
padres_fielding_post["Combined_Total_Points"] = padres_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    giants_fielding_post[f"Point_Category_{i}"] = 0

for index, row in giants_fielding_post.iterrows():
    if row["po"] >= 25:
        giants_fielding_post.at[index, "Point_Category_1"] = 0.5
    if row["po"] >= 40:
        giants_fielding_post.at[index, "Point_Category_2"] = 0.5
    if row["a"] >= 15:
        giants_fielding_post.at[index, "Point_Category_3"] = 0.5
    if row["e"] <= 1:
        giants_fielding_post.at[index, "Point_Category_4"] = 0.5
    if row["round"] == "ALCS":
        giants_fielding_post.at[index, "Point_Category_5"] = 0.5
    if row["round"] == "NLCS":
        giants_fielding_post.at[index, "Point_Category_6"] = 0.5
    if row["round"] == "WS":
        giants_fielding_post.at[index, "Point_Category_7"] = 4
    
giants_fielding_post["Sum_Total_Points"] = giants_fielding_post[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
giants_fielding_post["Combined_Total_Points"] = giants_fielding_post.groupby("player_id")["Sum_Total_Points"].transform('sum')













# Pitching team data

# Creating new dataframes for each team (redundant, but required when I concatenate this dataframe and the filtered one for my function)



orioles_pitching = pd.DataFrame(columns = pitching_data.columns)
red_sox_pitching = pd.DataFrame(columns = pitching_data.columns)
yankees_pitching = pd.DataFrame(columns = pitching_data.columns)
rays_pitching = pd.DataFrame(columns = pitching_data.columns)
blue_jays_pitching = pd.DataFrame(columns = pitching_data.columns)

white_sox_pitching = pd.DataFrame(columns = pitching_data.columns)
guardians_pitching = pd.DataFrame(columns = pitching_data.columns)
tigers_pitching = pd.DataFrame(columns = pitching_data.columns)
royals_pitching = pd.DataFrame(columns = pitching_data.columns)
twins_pitching = pd.DataFrame(columns = pitching_data.columns)

astros_pitching = pd.DataFrame(columns = pitching_data.columns)
angels_pitching = pd.DataFrame(columns = pitching_data.columns)
athletics_pitching = pd.DataFrame(columns = pitching_data.columns)
mariners_pitching = pd.DataFrame(columns = pitching_data.columns)
rangers_pitching = pd.DataFrame(columns = pitching_data.columns)



braves_pitching = pd.DataFrame(columns = pitching_data.columns)
marlins_pitching = pd.DataFrame(columns = pitching_data.columns)
mets_pitching = pd.DataFrame(columns = pitching_data.columns)
nationals_pitching = pd.DataFrame(columns = pitching_data.columns)
phillies_pitching = pd.DataFrame(columns = pitching_data.columns)

cubs_pitching = pd.DataFrame(columns = pitching_data.columns)
reds_pitching = pd.DataFrame(columns = pitching_data.columns)
brewers_pitching = pd.DataFrame(columns = pitching_data.columns)
pirates_pitching = pd.DataFrame(columns = pitching_data.columns)
cardinals_pitching = pd.DataFrame(columns = pitching_data.columns)

diamondbacks_pitching = pd.DataFrame(columns = pitching_data.columns)
rockies_pitching = pd.DataFrame(columns = pitching_data.columns)
dodgers_pitching = pd.DataFrame(columns = pitching_data.columns)
padres_pitching = pd.DataFrame(columns = pitching_data.columns)
giants_pitching = pd.DataFrame(columns = pitching_data.columns)


# Defining a functino where I take in a list of team ids and an existing empty team pitching dataframe
# Filters out all observations that do not have any of the specified team_ids
# Returns a concatenation of the filtered dataframe and the empty dataframe (basically copying and pasting the filtered dataframe)

def append_specified_team_ids_pitching(team_ids, target_df):
    filtered_df = pitching_data[pitching_data["team_id"].isin(team_ids)]
    return pd.concat([target_df, filtered_df], ignore_index = True)



orioles_pitching = append_specified_team_ids_pitching(orioles_teams, orioles_pitching)
red_sox_pitching = append_specified_team_ids_pitching(red_sox_teams, red_sox_pitching)
yankees_pitching = append_specified_team_ids_pitching(yankees_teams, yankees_pitching)
rays_pitching = append_specified_team_ids_pitching(rays_teams, rays_pitching)
blue_jays_pitching = append_specified_team_ids_pitching(blue_jays_teams, blue_jays_pitching)

white_sox_pitching = append_specified_team_ids_pitching(white_sox_teams, white_sox_pitching)
guardians_pitching = append_specified_team_ids_pitching(guardians_teams, guardians_pitching)
tigers_pitching = append_specified_team_ids_pitching(tigers_teams, tigers_pitching)
royals_pitching = append_specified_team_ids_pitching(royals_teams, royals_pitching)
twins_pitching = append_specified_team_ids_pitching(twins_teams, twins_pitching)

astros_pitching = append_specified_team_ids_pitching(astros_teams, astros_pitching)
angels_pitching = append_specified_team_ids_pitching(angels_teams, angels_pitching)
athletics_pitching = append_specified_team_ids_pitching(athletics_teams, athletics_pitching)
mariners_pitching = append_specified_team_ids_pitching(mariners_teams, mariners_pitching)
rangers_pitching = append_specified_team_ids_pitching(rangers_teams, rangers_pitching)




braves_pitching = append_specified_team_ids_pitching(braves_teams, braves_pitching)
marlins_pitching = append_specified_team_ids_pitching(marlins_teams, marlins_pitching)
mets_pitching = append_specified_team_ids_pitching(mets_teams, mets_pitching)
nationals_pitching = append_specified_team_ids_pitching(nationals_teams, nationals_pitching)
phillies_pitching = append_specified_team_ids_pitching(phillies_teams, phillies_pitching)

cubs_pitching = append_specified_team_ids_pitching(cubs_teams, cubs_pitching)
reds_pitching = append_specified_team_ids_pitching(reds_teams, reds_pitching)
brewers_pitching = append_specified_team_ids_pitching(brewers_teams, brewers_pitching)
pirates_pitching = append_specified_team_ids_pitching(pirates_teams, pirates_pitching)
cardinals_pitching = append_specified_team_ids_pitching(cardinals_teams, cardinals_pitching)

diamondbacks_pitching = append_specified_team_ids_pitching(diamondbacks_teams, diamondbacks_pitching)
rockies_pitching = append_specified_team_ids_pitching(rockies_teams, rockies_pitching)
dodgers_pitching = append_specified_team_ids_pitching(dodgers_teams, dodgers_pitching)
padres_pitching = append_specified_team_ids_pitching(padres_teams, padres_pitching)
giants_pitching = append_specified_team_ids_pitching(giants_teams, giants_pitching)




# Defining points for each of the regular season pitching stats.
# First, a number of point category columns are created based on how many I want
# Second, in each batting dataset, I look to see if an observation satisfies each of the if statements. If they do, they get points assigned to the point categories
# I then get the sum of the points per that given season called Sum_Total_Points
# Lastly, I get the sum of the career number of points, the column called Combined_Total_Points

for i in range(1, 8):
    orioles_pitching[f"Point_Category_{i}"] = 0

for index, row in orioles_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            orioles_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            orioles_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            orioles_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            orioles_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            orioles_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            orioles_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            orioles_pitching.at[index, 'Point_Category_7'] = 1
        
orioles_pitching["Sum_Total_Points"] = orioles_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
orioles_pitching["Combined_Total_Points"] = orioles_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    red_sox_pitching[f"Point_Category_{i}"] = 0

for index, row in red_sox_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            red_sox_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            red_sox_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            red_sox_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            red_sox_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            red_sox_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            red_sox_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            red_sox_pitching.at[index, 'Point_Category_7'] = 1
        
red_sox_pitching["Sum_Total_Points"] = red_sox_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
red_sox_pitching["Combined_Total_Points"] = red_sox_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    yankees_pitching[f"Point_Category_{i}"] = 0

for index, row in yankees_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            yankees_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            yankees_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            yankees_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            yankees_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            yankees_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            yankees_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            yankees_pitching.at[index, 'Point_Category_7'] = 1
        
yankees_pitching["Sum_Total_Points"] = yankees_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
yankees_pitching["Combined_Total_Points"] = yankees_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    rays_pitching[f"Point_Category_{i}"] = 0

for index, row in rays_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            rays_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            rays_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            rays_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            rays_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            rays_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            rays_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            rays_pitching.at[index, 'Point_Category_7'] = 1
        
rays_pitching["Sum_Total_Points"] = rays_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
rays_pitching["Combined_Total_Points"] = rays_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    blue_jays_pitching[f"Point_Category_{i}"] = 0

for index, row in blue_jays_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            blue_jays_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            blue_jays_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            blue_jays_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            blue_jays_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            blue_jays_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            blue_jays_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            blue_jays_pitching.at[index, 'Point_Category_7'] = 1
        
blue_jays_pitching["Sum_Total_Points"] = blue_jays_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
blue_jays_pitching["Combined_Total_Points"] = blue_jays_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')







for i in range(1, 8):
    white_sox_pitching[f"Point_Category_{i}"] = 0

for index, row in white_sox_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            white_sox_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            white_sox_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            white_sox_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            white_sox_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            white_sox_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            white_sox_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            white_sox_pitching.at[index, 'Point_Category_7'] = 1
        
white_sox_pitching["Sum_Total_Points"] = white_sox_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
white_sox_pitching["Combined_Total_Points"] = white_sox_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    guardians_pitching[f"Point_Category_{i}"] = 0

for index, row in guardians_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            guardians_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            guardians_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            guardians_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            guardians_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            guardians_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            guardians_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            guardians_pitching.at[index, 'Point_Category_7'] = 1
        
guardians_pitching["Sum_Total_Points"] = guardians_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
guardians_pitching["Combined_Total_Points"] = guardians_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    tigers_pitching[f"Point_Category_{i}"] = 0

for index, row in tigers_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            tigers_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            tigers_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            tigers_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            tigers_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            tigers_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            tigers_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            tigers_pitching.at[index, 'Point_Category_7'] = 1
        
tigers_pitching["Sum_Total_Points"] = tigers_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
tigers_pitching["Combined_Total_Points"] = tigers_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    royals_pitching[f"Point_Category_{i}"] = 0

for index, row in royals_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            royals_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            royals_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            royals_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            royals_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            royals_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            royals_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            royals_pitching.at[index, 'Point_Category_7'] = 1
        
royals_pitching["Sum_Total_Points"] = royals_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
royals_pitching["Combined_Total_Points"] = royals_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    twins_pitching[f"Point_Category_{i}"] = 0

for index, row in twins_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            twins_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            twins_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            twins_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            twins_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            twins_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            twins_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            twins_pitching.at[index, 'Point_Category_7'] = 1
        
twins_pitching["Sum_Total_Points"] = twins_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
twins_pitching["Combined_Total_Points"] = twins_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')







for i in range(1, 8):
    astros_pitching[f"Point_Category_{i}"] = 0

for index, row in astros_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            astros_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            astros_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            astros_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            astros_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            astros_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            astros_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            astros_pitching.at[index, 'Point_Category_7'] = 1
        
astros_pitching["Sum_Total_Points"] = astros_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
astros_pitching["Combined_Total_Points"] = astros_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    angels_pitching[f"Point_Category_{i}"] = 0

for index, row in angels_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            angels_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            angels_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            angels_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            angels_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            angels_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            angels_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            angels_pitching.at[index, 'Point_Category_7'] = 1
        
angels_pitching["Sum_Total_Points"] = angels_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
angels_pitching["Combined_Total_Points"] = angels_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    athletics_pitching[f"Point_Category_{i}"] = 0

for index, row in athletics_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            athletics_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            athletics_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            athletics_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            athletics_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            athletics_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            athletics_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            athletics_pitching.at[index, 'Point_Category_7'] = 1
        
athletics_pitching["Sum_Total_Points"] = athletics_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
athletics_pitching["Combined_Total_Points"] = athletics_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    mariners_pitching[f"Point_Category_{i}"] = 0

for index, row in mariners_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            mariners_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            mariners_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            mariners_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            mariners_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            mariners_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            mariners_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            mariners_pitching.at[index, 'Point_Category_7'] = 1
        
mariners_pitching["Sum_Total_Points"] = mariners_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
mariners_pitching["Combined_Total_Points"] = mariners_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    rangers_pitching[f"Point_Category_{i}"] = 0

for index, row in rangers_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            rangers_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            rangers_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            rangers_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            rangers_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            rangers_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            rangers_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            rangers_pitching.at[index, 'Point_Category_7'] = 1
        
rangers_pitching["Sum_Total_Points"] = rangers_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
rangers_pitching["Combined_Total_Points"] = rangers_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')













for i in range(1, 8):
    braves_pitching[f"Point_Category_{i}"] = 0

for index, row in braves_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            braves_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            braves_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            braves_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            braves_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            braves_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            braves_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            braves_pitching.at[index, 'Point_Category_7'] = 1
        
braves_pitching["Sum_Total_Points"] = braves_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
braves_pitching["Combined_Total_Points"] = braves_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    marlins_pitching[f"Point_Category_{i}"] = 0

for index, row in marlins_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            marlins_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            marlins_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            marlins_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            marlins_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            marlins_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            marlins_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            marlins_pitching.at[index, 'Point_Category_7'] = 1
        
marlins_pitching["Sum_Total_Points"] = marlins_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
marlins_pitching["Combined_Total_Points"] = marlins_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    mets_pitching[f"Point_Category_{i}"] = 0

for index, row in mets_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            mets_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            mets_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            mets_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            mets_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            mets_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            mets_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            mets_pitching.at[index, 'Point_Category_7'] = 1
        
mets_pitching["Sum_Total_Points"] = mets_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
mets_pitching["Combined_Total_Points"] = mets_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    nationals_pitching[f"Point_Category_{i}"] = 0

for index, row in nationals_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            nationals_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            nationals_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            nationals_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            nationals_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            nationals_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            nationals_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            nationals_pitching.at[index, 'Point_Category_7'] = 1
        
nationals_pitching["Sum_Total_Points"] = nationals_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
nationals_pitching["Combined_Total_Points"] = nationals_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    phillies_pitching[f"Point_Category_{i}"] = 0

for index, row in phillies_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            phillies_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            phillies_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            phillies_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            phillies_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            phillies_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            phillies_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            phillies_pitching.at[index, 'Point_Category_7'] = 1
        
phillies_pitching["Sum_Total_Points"] = phillies_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
phillies_pitching["Combined_Total_Points"] = phillies_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')







for i in range(1, 8):
    cubs_pitching[f"Point_Category_{i}"] = 0

for index, row in cubs_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            cubs_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            cubs_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            cubs_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            cubs_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            cubs_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            cubs_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            cubs_pitching.at[index, 'Point_Category_7'] = 1
        
cubs_pitching["Sum_Total_Points"] = cubs_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
cubs_pitching["Combined_Total_Points"] = cubs_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    reds_pitching[f"Point_Category_{i}"] = 0

for index, row in reds_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            reds_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            reds_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            reds_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            reds_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            reds_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            reds_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            reds_pitching.at[index, 'Point_Category_7'] = 1
        
reds_pitching["Sum_Total_Points"] = reds_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
reds_pitching["Combined_Total_Points"] = reds_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    brewers_pitching[f"Point_Category_{i}"] = 0

for index, row in brewers_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            brewers_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            brewers_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            brewers_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            brewers_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            brewers_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            brewers_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            brewers_pitching.at[index, 'Point_Category_7'] = 1
        
brewers_pitching["Sum_Total_Points"] = brewers_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
brewers_pitching["Combined_Total_Points"] = brewers_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    pirates_pitching[f"Point_Category_{i}"] = 0

for index, row in pirates_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            pirates_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            pirates_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            pirates_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            pirates_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            pirates_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            pirates_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            pirates_pitching.at[index, 'Point_Category_7'] = 1
        
pirates_pitching["Sum_Total_Points"] = pirates_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
pirates_pitching["Combined_Total_Points"] = pirates_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    cardinals_pitching[f"Point_Category_{i}"] = 0

for index, row in cardinals_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            cardinals_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            cardinals_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            cardinals_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            cardinals_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            cardinals_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            cardinals_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            cardinals_pitching.at[index, 'Point_Category_7'] = 1
        
cardinals_pitching["Sum_Total_Points"] = cardinals_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
cardinals_pitching["Combined_Total_Points"] = cardinals_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')










for i in range(1, 8):
    diamondbacks_pitching[f"Point_Category_{i}"] = 0

for index, row in diamondbacks_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            diamondbacks_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            diamondbacks_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            diamondbacks_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            diamondbacks_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            diamondbacks_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            diamondbacks_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            diamondbacks_pitching.at[index, 'Point_Category_7'] = 1
        
diamondbacks_pitching["Sum_Total_Points"] = diamondbacks_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
diamondbacks_pitching["Combined_Total_Points"] = diamondbacks_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    rockies_pitching[f"Point_Category_{i}"] = 0

for index, row in rockies_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            rockies_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            rockies_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            rockies_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            rockies_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            rockies_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            rockies_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            rockies_pitching.at[index, 'Point_Category_7'] = 1
        
rockies_pitching["Sum_Total_Points"] = rockies_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
rockies_pitching["Combined_Total_Points"] = rockies_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    dodgers_pitching[f"Point_Category_{i}"] = 0

for index, row in dodgers_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            dodgers_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            dodgers_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            dodgers_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            dodgers_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            dodgers_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            dodgers_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            dodgers_pitching.at[index, 'Point_Category_7'] = 1
        
dodgers_pitching["Sum_Total_Points"] = dodgers_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
dodgers_pitching["Combined_Total_Points"] = dodgers_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    padres_pitching[f"Point_Category_{i}"] = 0

for index, row in padres_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            padres_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            padres_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            padres_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            padres_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            padres_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            padres_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            padres_pitching.at[index, 'Point_Category_7'] = 1
        
padres_pitching["Sum_Total_Points"] = padres_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
padres_pitching["Combined_Total_Points"] = padres_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 8):
    giants_pitching[f"Point_Category_{i}"] = 0

for index, row in giants_pitching.iterrows():
    if row["g"] >= 20:
        if row["w"] >= 15:
            giants_pitching.at[index, "Point_Category_1"] = 1
        if row["l"] <= 4:
            giants_pitching.at[index, "Point_Category_2"] = 1
        if row["sho"] >= 2:
            giants_pitching.at[index, "Point_Category_3"] = 1
        if row["sv"] >= 40:
            giants_pitching.at[index, "Point_Category_4"] = 1
        if row["baopp"] <= 0.23:
            giants_pitching.at[index, "Point_Category_5"] = 2
        if row["era"] <= 2.4:
            giants_pitching.at[index, "Point_Category_6"] = 1

        strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
        if strikeout_to_walk_ratio < 0.250:
            giants_pitching.at[index, 'Point_Category_7'] = 1
        
giants_pitching["Sum_Total_Points"] = giants_pitching[[f"Point_Category_{i}" for i in range(1, 8)]].sum(axis=1)
giants_pitching["Combined_Total_Points"] = giants_pitching.groupby("player_id")["Sum_Total_Points"].transform('sum')













# Pitching postseason team data

# Creating new dataframes for each team (redundant, but required when I concatenate this dataframe and the filtered one for my function)


orioles_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
red_sox_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
yankees_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
rays_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
blue_jays_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)

white_sox_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
guardians_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
tigers_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
royals_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
twins_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)

astros_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
angels_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
athletics_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
mariners_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
rangers_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)



braves_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
marlins_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
mets_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
nationals_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
phillies_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)

cubs_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
reds_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
brewers_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
pirates_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
cardinals_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)

diamondbacks_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
rockies_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
dodgers_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
padres_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)
giants_pitching_post = pd.DataFrame(columns = pitching_post_data.columns)


# Defining a functino where I take in a list of team ids and an existing empty team pitching post dataframe
# Filters out all observations that do not have any of the specified team_ids
# Returns a concatenation of the filtered dataframe and the empty dataframe (basically copying and pasting the filtered dataframe)

def append_specified_team_ids_pitching_post(team_ids, target_df):
    filtered_df = pitching_post_data[pitching_post_data["team_id"].isin(team_ids)]
    return pd.concat([target_df, filtered_df], ignore_index = True)




orioles_pitching_post = append_specified_team_ids_pitching_post(orioles_teams, orioles_pitching_post)
orioles_pitching_post['baopp'] = pd.to_numeric(orioles_pitching_post['baopp'], errors='coerce')
orioles_pitching_post['w'] = pd.to_numeric(orioles_pitching_post['w'], errors = 'coerce')
orioles_pitching_post['sho'] = pd.to_numeric(orioles_pitching_post['sho'], errors = 'coerce')
orioles_pitching_post['sv'] = pd.to_numeric(orioles_pitching_post['sv'], errors = 'coerce')
orioles_pitching_post['so'] = pd.to_numeric(orioles_pitching_post['so'], errors = 'coerce')
orioles_pitching_post['bb'] = pd.to_numeric(orioles_pitching_post['bb'], errors = 'coerce')

red_sox_pitching_post = append_specified_team_ids_pitching_post(red_sox_teams, red_sox_pitching_post)
red_sox_pitching_post['baopp'] = pd.to_numeric(red_sox_pitching_post['baopp'], errors='coerce')
red_sox_pitching_post['w'] = pd.to_numeric(red_sox_pitching_post['w'], errors = 'coerce')
red_sox_pitching_post['sho'] = pd.to_numeric(red_sox_pitching_post['sho'], errors = 'coerce')
red_sox_pitching_post['sv'] = pd.to_numeric(red_sox_pitching_post['sv'], errors = 'coerce')
red_sox_pitching_post['so'] = pd.to_numeric(red_sox_pitching_post['so'], errors = 'coerce')
red_sox_pitching_post['bb'] = pd.to_numeric(red_sox_pitching_post['bb'], errors = 'coerce')

yankees_pitching_post = append_specified_team_ids_pitching_post(yankees_teams, yankees_pitching_post)
yankees_pitching_post['baopp'] = pd.to_numeric(yankees_pitching_post['baopp'], errors='coerce')
yankees_pitching_post['w'] = pd.to_numeric(yankees_pitching_post['w'], errors = 'coerce')
yankees_pitching_post['sho'] = pd.to_numeric(yankees_pitching_post['sho'], errors = 'coerce')
yankees_pitching_post['sv'] = pd.to_numeric(yankees_pitching_post['sv'], errors = 'coerce')
yankees_pitching_post['so'] = pd.to_numeric(yankees_pitching_post['so'], errors = 'coerce')
yankees_pitching_post['bb'] = pd.to_numeric(yankees_pitching_post['bb'], errors = 'coerce')

rays_pitching_post = append_specified_team_ids_pitching_post(rays_teams, rays_pitching_post)
rays_pitching_post['baopp'] = pd.to_numeric(rays_pitching_post['baopp'], errors='coerce')
rays_pitching_post['w'] = pd.to_numeric(rays_pitching_post['w'], errors = 'coerce')
rays_pitching_post['sho'] = pd.to_numeric(rays_pitching_post['sho'], errors = 'coerce')
rays_pitching_post['sv'] = pd.to_numeric(rays_pitching_post['sv'], errors = 'coerce')
rays_pitching_post['so'] = pd.to_numeric(rays_pitching_post['so'], errors = 'coerce')
rays_pitching_post['bb'] = pd.to_numeric(rays_pitching_post['bb'], errors = 'coerce')

blue_jays_pitching_post = append_specified_team_ids_pitching_post(blue_jays_teams, blue_jays_pitching_post)
blue_jays_pitching_post['baopp'] = pd.to_numeric(blue_jays_pitching_post['baopp'], errors='coerce')
blue_jays_pitching_post['w'] = pd.to_numeric(blue_jays_pitching_post['w'], errors = 'coerce')
blue_jays_pitching_post['sho'] = pd.to_numeric(blue_jays_pitching_post['sho'], errors = 'coerce')
blue_jays_pitching_post['sv'] = pd.to_numeric(blue_jays_pitching_post['sv'], errors = 'coerce')
blue_jays_pitching_post['so'] = pd.to_numeric(blue_jays_pitching_post['so'], errors = 'coerce')
blue_jays_pitching_post['bb'] = pd.to_numeric(blue_jays_pitching_post['bb'], errors = 'coerce')



white_sox_pitching_post = append_specified_team_ids_pitching_post(white_sox_teams, white_sox_pitching_post)
white_sox_pitching_post['baopp'] = pd.to_numeric(white_sox_pitching_post['baopp'], errors='coerce')
white_sox_pitching_post['w'] = pd.to_numeric(white_sox_pitching_post['w'], errors = 'coerce')
white_sox_pitching_post['sho'] = pd.to_numeric(white_sox_pitching_post['sho'], errors = 'coerce')
white_sox_pitching_post['sv'] = pd.to_numeric(white_sox_pitching_post['sv'], errors = 'coerce')
white_sox_pitching_post['so'] = pd.to_numeric(white_sox_pitching_post['so'], errors = 'coerce')
white_sox_pitching_post['bb'] = pd.to_numeric(white_sox_pitching_post['bb'], errors = 'coerce')

guardians_pitching_post = append_specified_team_ids_pitching_post(guardians_teams, guardians_pitching_post)
guardians_pitching_post['baopp'] = pd.to_numeric(guardians_pitching_post['baopp'], errors='coerce')
guardians_pitching_post['w'] = pd.to_numeric(guardians_pitching_post['w'], errors = 'coerce')
guardians_pitching_post['sho'] = pd.to_numeric(guardians_pitching_post['sho'], errors = 'coerce')
guardians_pitching_post['sv'] = pd.to_numeric(guardians_pitching_post['sv'], errors = 'coerce')
guardians_pitching_post['so'] = pd.to_numeric(guardians_pitching_post['so'], errors = 'coerce')
guardians_pitching_post['bb'] = pd.to_numeric(guardians_pitching_post['bb'], errors = 'coerce')

tigers_pitching_post = append_specified_team_ids_pitching_post(tigers_teams, tigers_pitching_post)
tigers_pitching_post['baopp'] = pd.to_numeric(tigers_pitching_post['baopp'], errors='coerce')
tigers_pitching_post['w'] = pd.to_numeric(tigers_pitching_post['w'], errors = 'coerce')
tigers_pitching_post['sho'] = pd.to_numeric(tigers_pitching_post['sho'], errors = 'coerce')
tigers_pitching_post['sv'] = pd.to_numeric(tigers_pitching_post['sv'], errors = 'coerce')
tigers_pitching_post['so'] = pd.to_numeric(tigers_pitching_post['so'], errors = 'coerce')
tigers_pitching_post['bb'] = pd.to_numeric(tigers_pitching_post['bb'], errors = 'coerce')

royals_pitching_post = append_specified_team_ids_pitching_post(royals_teams, royals_pitching_post)
royals_pitching_post['baopp'] = pd.to_numeric(royals_pitching_post['baopp'], errors='coerce')
royals_pitching_post['w'] = pd.to_numeric(royals_pitching_post['w'], errors = 'coerce')
royals_pitching_post['sho'] = pd.to_numeric(royals_pitching_post['sho'], errors = 'coerce')
royals_pitching_post['sv'] = pd.to_numeric(royals_pitching_post['sv'], errors = 'coerce')
royals_pitching_post['so'] = pd.to_numeric(royals_pitching_post['so'], errors = 'coerce')
royals_pitching_post['bb'] = pd.to_numeric(royals_pitching_post['bb'], errors = 'coerce')

twins_pitching_post = append_specified_team_ids_pitching_post(twins_teams, twins_pitching_post)
twins_pitching_post['baopp'] = pd.to_numeric(twins_pitching_post['baopp'], errors='coerce')
twins_pitching_post['w'] = pd.to_numeric(twins_pitching_post['w'], errors = 'coerce')
twins_pitching_post['sho'] = pd.to_numeric(twins_pitching_post['sho'], errors = 'coerce')
twins_pitching_post['sv'] = pd.to_numeric(twins_pitching_post['sv'], errors = 'coerce')
twins_pitching_post['so'] = pd.to_numeric(twins_pitching_post['so'], errors = 'coerce')
twins_pitching_post['bb'] = pd.to_numeric(twins_pitching_post['bb'], errors = 'coerce')



astros_pitching_post = append_specified_team_ids_pitching_post(astros_teams, astros_pitching_post)
astros_pitching_post['baopp'] = pd.to_numeric(astros_pitching_post['baopp'], errors='coerce')
astros_pitching_post['w'] = pd.to_numeric(astros_pitching_post['w'], errors = 'coerce')
astros_pitching_post['sho'] = pd.to_numeric(astros_pitching_post['sho'], errors = 'coerce')
astros_pitching_post['sv'] = pd.to_numeric(astros_pitching_post['sv'], errors = 'coerce')
astros_pitching_post['so'] = pd.to_numeric(astros_pitching_post['so'], errors = 'coerce')
astros_pitching_post['bb'] = pd.to_numeric(astros_pitching_post['bb'], errors = 'coerce')

angels_pitching_post = append_specified_team_ids_pitching_post(angels_teams, angels_pitching_post)
angels_pitching_post['baopp'] = pd.to_numeric(angels_pitching_post['baopp'], errors='coerce')
angels_pitching_post['w'] = pd.to_numeric(angels_pitching_post['w'], errors = 'coerce')
angels_pitching_post['sho'] = pd.to_numeric(angels_pitching_post['sho'], errors = 'coerce')
angels_pitching_post['sv'] = pd.to_numeric(angels_pitching_post['sv'], errors = 'coerce')
angels_pitching_post['so'] = pd.to_numeric(angels_pitching_post['so'], errors = 'coerce')
angels_pitching_post['bb'] = pd.to_numeric(angels_pitching_post['bb'], errors = 'coerce')

athletics_pitching_post = append_specified_team_ids_pitching_post(athletics_teams, athletics_pitching_post)
athletics_pitching_post['baopp'] = pd.to_numeric(athletics_pitching_post['baopp'], errors='coerce')
athletics_pitching_post['w'] = pd.to_numeric(athletics_pitching_post['w'], errors = 'coerce')
athletics_pitching_post['sho'] = pd.to_numeric(athletics_pitching_post['sho'], errors = 'coerce')
athletics_pitching_post['sv'] = pd.to_numeric(athletics_pitching_post['sv'], errors = 'coerce')
athletics_pitching_post['so'] = pd.to_numeric(athletics_pitching_post['so'], errors = 'coerce')
athletics_pitching_post['bb'] = pd.to_numeric(athletics_pitching_post['bb'], errors = 'coerce')

mariners_pitching_post = append_specified_team_ids_pitching_post(mariners_teams, mariners_pitching_post)
mariners_pitching_post['baopp'] = pd.to_numeric(mariners_pitching_post['baopp'], errors='coerce')
mariners_pitching_post['w'] = pd.to_numeric(mariners_pitching_post['w'], errors = 'coerce')
mariners_pitching_post['sho'] = pd.to_numeric(mariners_pitching_post['sho'], errors = 'coerce')
mariners_pitching_post['sv'] = pd.to_numeric(mariners_pitching_post['sv'], errors = 'coerce')
mariners_pitching_post['so'] = pd.to_numeric(mariners_pitching_post['so'], errors = 'coerce')
mariners_pitching_post['bb'] = pd.to_numeric(mariners_pitching_post['bb'], errors = 'coerce')

rangers_pitching_post = append_specified_team_ids_pitching_post(rangers_teams, rangers_pitching_post)
rangers_pitching_post['baopp'] = pd.to_numeric(rangers_pitching_post['baopp'], errors='coerce')
rangers_pitching_post['w'] = pd.to_numeric(rangers_pitching_post['w'], errors = 'coerce')
rangers_pitching_post['sho'] = pd.to_numeric(rangers_pitching_post['sho'], errors = 'coerce')
rangers_pitching_post['sv'] = pd.to_numeric(rangers_pitching_post['sv'], errors = 'coerce')
rangers_pitching_post['so'] = pd.to_numeric(rangers_pitching_post['so'], errors = 'coerce')
rangers_pitching_post['bb'] = pd.to_numeric(rangers_pitching_post['bb'], errors = 'coerce')






braves_pitching_post = append_specified_team_ids_pitching_post(braves_teams, braves_pitching_post)
braves_pitching_post['baopp'] = pd.to_numeric(braves_pitching_post['baopp'], errors='coerce')
braves_pitching_post['w'] = pd.to_numeric(braves_pitching_post['w'], errors = 'coerce')
braves_pitching_post['sho'] = pd.to_numeric(braves_pitching_post['sho'], errors = 'coerce')
braves_pitching_post['sv'] = pd.to_numeric(braves_pitching_post['sv'], errors = 'coerce')
braves_pitching_post['so'] = pd.to_numeric(braves_pitching_post['so'], errors = 'coerce')
braves_pitching_post['bb'] = pd.to_numeric(braves_pitching_post['bb'], errors = 'coerce')

marlins_pitching_post = append_specified_team_ids_pitching_post(marlins_teams, marlins_pitching_post)
marlins_pitching_post['baopp'] = pd.to_numeric(marlins_pitching_post['baopp'], errors='coerce')
marlins_pitching_post['w'] = pd.to_numeric(marlins_pitching_post['w'], errors = 'coerce')
marlins_pitching_post['sho'] = pd.to_numeric(marlins_pitching_post['sho'], errors = 'coerce')
marlins_pitching_post['sv'] = pd.to_numeric(marlins_pitching_post['sv'], errors = 'coerce')
marlins_pitching_post['so'] = pd.to_numeric(marlins_pitching_post['so'], errors = 'coerce')
marlins_pitching_post['bb'] = pd.to_numeric(marlins_pitching_post['bb'], errors = 'coerce')

mets_pitching_post = append_specified_team_ids_pitching_post(mets_teams, mets_pitching_post)
mets_pitching_post['baopp'] = pd.to_numeric(mets_pitching_post['baopp'], errors='coerce')
mets_pitching_post['w'] = pd.to_numeric(mets_pitching_post['w'], errors = 'coerce')
mets_pitching_post['sho'] = pd.to_numeric(mets_pitching_post['sho'], errors = 'coerce')
mets_pitching_post['sv'] = pd.to_numeric(mets_pitching_post['sv'], errors = 'coerce')
mets_pitching_post['so'] = pd.to_numeric(mets_pitching_post['so'], errors = 'coerce')
mets_pitching_post['bb'] = pd.to_numeric(mets_pitching_post['bb'], errors = 'coerce')

nationals_pitching_post = append_specified_team_ids_pitching_post(nationals_teams, nationals_pitching_post)
nationals_pitching_post['baopp'] = pd.to_numeric(nationals_pitching_post['baopp'], errors='coerce')
nationals_pitching_post['w'] = pd.to_numeric(nationals_pitching_post['w'], errors = 'coerce')
nationals_pitching_post['sho'] = pd.to_numeric(nationals_pitching_post['sho'], errors = 'coerce')
nationals_pitching_post['sv'] = pd.to_numeric(nationals_pitching_post['sv'], errors = 'coerce')
nationals_pitching_post['so'] = pd.to_numeric(nationals_pitching_post['so'], errors = 'coerce')
nationals_pitching_post['bb'] = pd.to_numeric(nationals_pitching_post['bb'], errors = 'coerce')

phillies_pitching_post = append_specified_team_ids_pitching_post(phillies_teams, phillies_pitching_post)
phillies_pitching_post['baopp'] = pd.to_numeric(phillies_pitching_post['baopp'], errors='coerce')
phillies_pitching_post['w'] = pd.to_numeric(phillies_pitching_post['w'], errors = 'coerce')
phillies_pitching_post['sho'] = pd.to_numeric(phillies_pitching_post['sho'], errors = 'coerce')
phillies_pitching_post['sv'] = pd.to_numeric(phillies_pitching_post['sv'], errors = 'coerce')
phillies_pitching_post['so'] = pd.to_numeric(phillies_pitching_post['so'], errors = 'coerce')
phillies_pitching_post['bb'] = pd.to_numeric(phillies_pitching_post['bb'], errors = 'coerce')



cubs_pitching_post = append_specified_team_ids_pitching_post(cubs_teams, cubs_pitching_post)
cubs_pitching_post['baopp'] = pd.to_numeric(cubs_pitching_post['baopp'], errors='coerce')
cubs_pitching_post['w'] = pd.to_numeric(cubs_pitching_post['w'], errors = 'coerce')
cubs_pitching_post['sho'] = pd.to_numeric(cubs_pitching_post['sho'], errors = 'coerce')
cubs_pitching_post['sv'] = pd.to_numeric(cubs_pitching_post['sv'], errors = 'coerce')
cubs_pitching_post['so'] = pd.to_numeric(cubs_pitching_post['so'], errors = 'coerce')
cubs_pitching_post['bb'] = pd.to_numeric(cubs_pitching_post['bb'], errors = 'coerce')

reds_pitching_post = append_specified_team_ids_pitching_post(reds_teams, reds_pitching_post)
reds_pitching_post['baopp'] = pd.to_numeric(reds_pitching_post['baopp'], errors='coerce')
reds_pitching_post['w'] = pd.to_numeric(reds_pitching_post['w'], errors = 'coerce')
reds_pitching_post['sho'] = pd.to_numeric(reds_pitching_post['sho'], errors = 'coerce')
reds_pitching_post['sv'] = pd.to_numeric(reds_pitching_post['sv'], errors = 'coerce')
reds_pitching_post['so'] = pd.to_numeric(reds_pitching_post['so'], errors = 'coerce')
reds_pitching_post['bb'] = pd.to_numeric(reds_pitching_post['bb'], errors = 'coerce')

brewers_pitching_post = append_specified_team_ids_pitching_post(brewers_teams, brewers_pitching_post)
brewers_pitching_post['baopp'] = pd.to_numeric(brewers_pitching_post['baopp'], errors='coerce')
brewers_pitching_post['w'] = pd.to_numeric(brewers_pitching_post['w'], errors = 'coerce')
brewers_pitching_post['sho'] = pd.to_numeric(brewers_pitching_post['sho'], errors = 'coerce')
brewers_pitching_post['sv'] = pd.to_numeric(brewers_pitching_post['sv'], errors = 'coerce')
brewers_pitching_post['so'] = pd.to_numeric(brewers_pitching_post['so'], errors = 'coerce')
brewers_pitching_post['bb'] = pd.to_numeric(brewers_pitching_post['bb'], errors = 'coerce')

pirates_pitching_post = append_specified_team_ids_pitching_post(pirates_teams, pirates_pitching_post)
pirates_pitching_post['baopp'] = pd.to_numeric(pirates_pitching_post['baopp'], errors='coerce')
pirates_pitching_post['w'] = pd.to_numeric(pirates_pitching_post['w'], errors = 'coerce')
pirates_pitching_post['sho'] = pd.to_numeric(pirates_pitching_post['sho'], errors = 'coerce')
pirates_pitching_post['sv'] = pd.to_numeric(pirates_pitching_post['sv'], errors = 'coerce')
pirates_pitching_post['so'] = pd.to_numeric(pirates_pitching_post['so'], errors = 'coerce')
pirates_pitching_post['bb'] = pd.to_numeric(pirates_pitching_post['bb'], errors = 'coerce')

cardinals_pitching_post = append_specified_team_ids_pitching_post(cardinals_teams, cardinals_pitching_post)
cardinals_pitching_post['baopp'] = pd.to_numeric(cardinals_pitching_post['baopp'], errors='coerce')
cardinals_pitching_post['w'] = pd.to_numeric(cardinals_pitching_post['w'], errors = 'coerce')
cardinals_pitching_post['sho'] = pd.to_numeric(cardinals_pitching_post['sho'], errors = 'coerce')
cardinals_pitching_post['sv'] = pd.to_numeric(cardinals_pitching_post['sv'], errors = 'coerce')
cardinals_pitching_post['so'] = pd.to_numeric(cardinals_pitching_post['so'], errors = 'coerce')
cardinals_pitching_post['bb'] = pd.to_numeric(cardinals_pitching_post['bb'], errors = 'coerce')



diamondbacks_pitching_post = append_specified_team_ids_pitching_post(diamondbacks_teams, diamondbacks_pitching_post)
diamondbacks_pitching_post['baopp'] = pd.to_numeric(diamondbacks_pitching_post['baopp'], errors='coerce')
diamondbacks_pitching_post['w'] = pd.to_numeric(diamondbacks_pitching_post['w'], errors = 'coerce')
diamondbacks_pitching_post['sho'] = pd.to_numeric(diamondbacks_pitching_post['sho'], errors = 'coerce')
diamondbacks_pitching_post['sv'] = pd.to_numeric(diamondbacks_pitching_post['sv'], errors = 'coerce')
diamondbacks_pitching_post['so'] = pd.to_numeric(diamondbacks_pitching_post['so'], errors = 'coerce')
diamondbacks_pitching_post['bb'] = pd.to_numeric(diamondbacks_pitching_post['bb'], errors = 'coerce')

rockies_pitching_post = append_specified_team_ids_pitching_post(rockies_teams, rockies_pitching_post)
rockies_pitching_post['baopp'] = pd.to_numeric(rockies_pitching_post['baopp'], errors='coerce')
rockies_pitching_post['w'] = pd.to_numeric(rockies_pitching_post['w'], errors = 'coerce')
rockies_pitching_post['sho'] = pd.to_numeric(rockies_pitching_post['sho'], errors = 'coerce')
rockies_pitching_post['sv'] = pd.to_numeric(rockies_pitching_post['sv'], errors = 'coerce')
rockies_pitching_post['so'] = pd.to_numeric(rockies_pitching_post['so'], errors = 'coerce')
rockies_pitching_post['bb'] = pd.to_numeric(rockies_pitching_post['bb'], errors = 'coerce')

dodgers_pitching_post = append_specified_team_ids_pitching_post(dodgers_teams, dodgers_pitching_post)
dodgers_pitching_post['baopp'] = pd.to_numeric(dodgers_pitching_post['baopp'], errors='coerce')
dodgers_pitching_post['w'] = pd.to_numeric(dodgers_pitching_post['w'], errors = 'coerce')
dodgers_pitching_post['sho'] = pd.to_numeric(dodgers_pitching_post['sho'], errors = 'coerce')
dodgers_pitching_post['sv'] = pd.to_numeric(dodgers_pitching_post['sv'], errors = 'coerce')
dodgers_pitching_post['so'] = pd.to_numeric(dodgers_pitching_post['so'], errors = 'coerce')
dodgers_pitching_post['bb'] = pd.to_numeric(dodgers_pitching_post['bb'], errors = 'coerce')

padres_pitching_post = append_specified_team_ids_pitching_post(padres_teams, padres_pitching_post)
padres_pitching_post['baopp'] = pd.to_numeric(padres_pitching_post['baopp'], errors='coerce')
padres_pitching_post['w'] = pd.to_numeric(padres_pitching_post['w'], errors = 'coerce')
padres_pitching_post['sho'] = pd.to_numeric(padres_pitching_post['sho'], errors = 'coerce')
padres_pitching_post['sv'] = pd.to_numeric(padres_pitching_post['sv'], errors = 'coerce')
padres_pitching_post['so'] = pd.to_numeric(padres_pitching_post['so'], errors = 'coerce')
padres_pitching_post['bb'] = pd.to_numeric(padres_pitching_post['bb'], errors = 'coerce')

giants_pitching_post = append_specified_team_ids_pitching_post(giants_teams, giants_pitching_post)
giants_pitching_post['baopp'] = pd.to_numeric(giants_pitching_post['baopp'], errors='coerce')
giants_pitching_post['w'] = pd.to_numeric(giants_pitching_post['w'], errors = 'coerce')
giants_pitching_post['sho'] = pd.to_numeric(giants_pitching_post['sho'], errors = 'coerce')
giants_pitching_post['sv'] = pd.to_numeric(giants_pitching_post['sv'], errors = 'coerce')
giants_pitching_post['so'] = pd.to_numeric(giants_pitching_post['so'], errors = 'coerce')
giants_pitching_post['bb'] = pd.to_numeric(giants_pitching_post['bb'], errors = 'coerce')





# Defining points for each of the post season pitching stats.
# First, a number of point category columns are created based on how many I want
# Second, in each batting dataset, I look to see if an observation satisfies each of the if statements. If they do, they get points assigned to the point categories
# I then get the sum of the points per that given season called Sum_Total_Points
# Lastly, I get the sum of the career number of points, the column called Combined_Total_Points

for i in range(1, 10):
    orioles_pitching_post[f"Point_Category_{i}"] = 0

for index, row in orioles_pitching_post.iterrows():
    if row["w"] >= 2:
        orioles_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        orioles_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        orioles_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        orioles_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        orioles_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            orioles_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        orioles_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        orioles_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        orioles_pitching_post.at[index, "Point_Category_9"] = 4
    
orioles_pitching_post["Sum_Total_Points"] = orioles_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
orioles_pitching_post["Combined_Total_Points"] = orioles_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    red_sox_pitching_post[f"Point_Category_{i}"] = 0

for index, row in red_sox_pitching_post.iterrows():
    if row["w"] >= 2:
        red_sox_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        red_sox_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        red_sox_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        red_sox_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        red_sox_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            red_sox_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        red_sox_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        red_sox_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        red_sox_pitching_post.at[index, "Point_Category_9"] = 4
    
red_sox_pitching_post["Sum_Total_Points"] = red_sox_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
red_sox_pitching_post["Combined_Total_Points"] = red_sox_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    yankees_pitching_post[f"Point_Category_{i}"] = 0

for index, row in yankees_pitching_post.iterrows():
    if row["w"] >= 2:
        yankees_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        yankees_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        yankees_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        yankees_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        yankees_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            yankees_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        yankees_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        yankees_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        yankees_pitching_post.at[index, "Point_Category_9"] = 4
    
yankees_pitching_post["Sum_Total_Points"] = yankees_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
yankees_pitching_post["Combined_Total_Points"] = yankees_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    rays_pitching_post[f"Point_Category_{i}"] = 0

for index, row in rays_pitching_post.iterrows():
    if row["w"] >= 2:
        rays_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        rays_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        rays_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        rays_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        rays_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            rays_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        rays_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        rays_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        rays_pitching_post.at[index, "Point_Category_9"] = 4
    
rays_pitching_post["Sum_Total_Points"] = rays_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
rays_pitching_post["Combined_Total_Points"] = rays_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    blue_jays_pitching_post[f"Point_Category_{i}"] = 0

for index, row in blue_jays_pitching_post.iterrows():
    if row["w"] >= 2:
        blue_jays_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        blue_jays_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        blue_jays_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        blue_jays_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        blue_jays_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            blue_jays_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        blue_jays_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        blue_jays_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        blue_jays_pitching_post.at[index, "Point_Category_9"] = 4
    
blue_jays_pitching_post["Sum_Total_Points"] = blue_jays_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
blue_jays_pitching_post["Combined_Total_Points"] = blue_jays_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')







for i in range(1, 10):
    white_sox_pitching_post[f"Point_Category_{i}"] = 0

for index, row in white_sox_pitching_post.iterrows():
    if row["w"] >= 2:
        white_sox_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        white_sox_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        white_sox_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        white_sox_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        white_sox_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            white_sox_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        white_sox_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        white_sox_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        white_sox_pitching_post.at[index, "Point_Category_9"] = 4
    
white_sox_pitching_post["Sum_Total_Points"] = white_sox_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
white_sox_pitching_post["Combined_Total_Points"] = white_sox_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    guardians_pitching_post[f"Point_Category_{i}"] = 0

for index, row in guardians_pitching_post.iterrows():
    if row["w"] >= 2:
        guardians_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        guardians_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        guardians_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        guardians_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        guardians_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            guardians_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        guardians_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        guardians_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        guardians_pitching_post.at[index, "Point_Category_9"] = 4
    
guardians_pitching_post["Sum_Total_Points"] = guardians_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
guardians_pitching_post["Combined_Total_Points"] = guardians_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    tigers_pitching_post[f"Point_Category_{i}"] = 0

for index, row in tigers_pitching_post.iterrows():
    if row["w"] >= 2:
        tigers_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        tigers_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        tigers_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        tigers_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        tigers_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            tigers_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        tigers_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        tigers_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        tigers_pitching_post.at[index, "Point_Category_9"] = 4
    
tigers_pitching_post["Sum_Total_Points"] = tigers_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
tigers_pitching_post["Combined_Total_Points"] = tigers_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    royals_pitching_post[f"Point_Category_{i}"] = 0

for index, row in royals_pitching_post.iterrows():
    if row["w"] >= 2:
        royals_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        royals_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        royals_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        royals_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        royals_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            royals_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        royals_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        royals_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        royals_pitching_post.at[index, "Point_Category_9"] = 4
    
royals_pitching_post["Sum_Total_Points"] = royals_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
royals_pitching_post["Combined_Total_Points"] = royals_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    twins_pitching_post[f"Point_Category_{i}"] = 0

for index, row in twins_pitching_post.iterrows():
    if row["w"] >= 2:
        twins_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        twins_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        twins_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        twins_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        twins_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            twins_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        twins_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        twins_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        twins_pitching_post.at[index, "Point_Category_9"] = 4
    
twins_pitching_post["Sum_Total_Points"] = twins_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
twins_pitching_post["Combined_Total_Points"] = twins_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')







for i in range(1, 10):
    astros_pitching_post[f"Point_Category_{i}"] = 0

for index, row in astros_pitching_post.iterrows():
    if row["w"] >= 2:
        astros_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        astros_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        astros_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        astros_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        astros_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            astros_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        astros_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        astros_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        astros_pitching_post.at[index, "Point_Category_9"] = 4
    
astros_pitching_post["Sum_Total_Points"] = astros_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
astros_pitching_post["Combined_Total_Points"] = astros_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    angels_pitching_post[f"Point_Category_{i}"] = 0

for index, row in angels_pitching_post.iterrows():
    if row["w"] >= 2:
        angels_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        angels_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        angels_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        angels_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        angels_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            angels_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        angels_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        angels_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        angels_pitching_post.at[index, "Point_Category_9"] = 4
    
angels_pitching_post["Sum_Total_Points"] = angels_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
angels_pitching_post["Combined_Total_Points"] = angels_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    athletics_pitching_post[f"Point_Category_{i}"] = 0

for index, row in athletics_pitching_post.iterrows():
    if row["w"] >= 2:
        athletics_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        athletics_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        athletics_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        athletics_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        athletics_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            athletics_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        athletics_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        athletics_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        athletics_pitching_post.at[index, "Point_Category_9"] = 4
    
athletics_pitching_post["Sum_Total_Points"] = athletics_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
athletics_pitching_post["Combined_Total_Points"] = athletics_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    mariners_pitching_post[f"Point_Category_{i}"] = 0

for index, row in mariners_pitching_post.iterrows():
    if row["w"] >= 2:
        mariners_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        mariners_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        mariners_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        mariners_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        mariners_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            mariners_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        mariners_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        mariners_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        mariners_pitching_post.at[index, "Point_Category_9"] = 4
    
mariners_pitching_post["Sum_Total_Points"] = mariners_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
mariners_pitching_post["Combined_Total_Points"] = mariners_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    rangers_pitching_post[f"Point_Category_{i}"] = 0

for index, row in rangers_pitching_post.iterrows():
    if row["w"] >= 2:
        rangers_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        rangers_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        rangers_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        rangers_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        rangers_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            rangers_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        rangers_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        rangers_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        rangers_pitching_post.at[index, "Point_Category_9"] = 4
    
rangers_pitching_post["Sum_Total_Points"] = rangers_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
rangers_pitching_post["Combined_Total_Points"] = rangers_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')








for i in range(1, 10):
    braves_pitching_post[f"Point_Category_{i}"] = 0

for index, row in braves_pitching_post.iterrows():
    if row["w"] >= 2:
        braves_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        braves_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        braves_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        braves_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        braves_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            braves_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        braves_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        braves_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        braves_pitching_post.at[index, "Point_Category_9"] = 4
    
braves_pitching_post["Sum_Total_Points"] = braves_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
braves_pitching_post["Combined_Total_Points"] = braves_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    marlins_pitching_post[f"Point_Category_{i}"] = 0

for index, row in marlins_pitching_post.iterrows():
    if row["w"] >= 2:
        marlins_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        marlins_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        marlins_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        marlins_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        marlins_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            marlins_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        marlins_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        marlins_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        marlins_pitching_post.at[index, "Point_Category_9"] = 4

marlins_pitching_post["Sum_Total_Points"] = marlins_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
marlins_pitching_post["Combined_Total_Points"] = marlins_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    mets_pitching_post[f"Point_Category_{i}"] = 0

for index, row in mets_pitching_post.iterrows():
    if row["w"] >= 2:
        mets_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        mets_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        mets_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        mets_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        mets_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            mets_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        mets_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        mets_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        mets_pitching_post.at[index, "Point_Category_9"] = 4
    
mets_pitching_post["Sum_Total_Points"] = mets_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
mets_pitching_post["Combined_Total_Points"] = mets_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    nationals_pitching_post[f"Point_Category_{i}"] = 0

for index, row in nationals_pitching_post.iterrows():
    if row["w"] >= 2:
        nationals_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        nationals_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        nationals_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        nationals_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        nationals_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            nationals_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        nationals_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        nationals_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        nationals_pitching_post.at[index, "Point_Category_9"] = 4
    
nationals_pitching_post["Sum_Total_Points"] = nationals_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
nationals_pitching_post["Combined_Total_Points"] = nationals_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    phillies_pitching_post[f"Point_Category_{i}"] = 0

for index, row in phillies_pitching_post.iterrows():
    if row["w"] >= 2:
        phillies_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        phillies_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        phillies_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        phillies_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        phillies_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            phillies_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        phillies_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        phillies_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        phillies_pitching_post.at[index, "Point_Category_9"] = 4
    
phillies_pitching_post["Sum_Total_Points"] = phillies_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
phillies_pitching_post["Combined_Total_Points"] = phillies_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')






for i in range(1, 10):
    cubs_pitching_post[f"Point_Category_{i}"] = 0

for index, row in cubs_pitching_post.iterrows():
    if row["w"] >= 2:
        cubs_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        cubs_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        cubs_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        cubs_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        cubs_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            cubs_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        cubs_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        cubs_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        cubs_pitching_post.at[index, "Point_Category_9"] = 4
    
cubs_pitching_post["Sum_Total_Points"] = cubs_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
cubs_pitching_post["Combined_Total_Points"] = cubs_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    reds_pitching_post[f"Point_Category_{i}"] = 0

for index, row in reds_pitching_post.iterrows():
    if row["w"] >= 2:
        reds_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        reds_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        reds_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        reds_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        reds_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            reds_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        reds_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        reds_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        reds_pitching_post.at[index, "Point_Category_9"] = 4
    
reds_pitching_post["Sum_Total_Points"] = reds_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
reds_pitching_post["Combined_Total_Points"] = reds_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    brewers_pitching_post[f"Point_Category_{i}"] = 0

for index, row in brewers_pitching_post.iterrows():
    if row["w"] >= 2:
        brewers_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        brewers_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        brewers_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        brewers_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        brewers_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            brewers_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        brewers_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        brewers_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        brewers_pitching_post.at[index, "Point_Category_9"] = 4
    
brewers_pitching_post["Sum_Total_Points"] = brewers_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
brewers_pitching_post["Combined_Total_Points"] = brewers_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    pirates_pitching_post[f"Point_Category_{i}"] = 0

for index, row in pirates_pitching_post.iterrows():
    if row["w"] >= 2:
        pirates_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        pirates_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        pirates_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        pirates_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        pirates_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            pirates_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        pirates_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        pirates_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        pirates_pitching_post.at[index, "Point_Category_9"] = 4
    
pirates_pitching_post["Sum_Total_Points"] = pirates_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
pirates_pitching_post["Combined_Total_Points"] = pirates_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    cardinals_pitching_post[f"Point_Category_{i}"] = 0

for index, row in cardinals_pitching_post.iterrows():
    if row["w"] >= 2:
        cardinals_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        cardinals_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        cardinals_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        cardinals_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        cardinals_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            cardinals_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        cardinals_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        cardinals_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        cardinals_pitching_post.at[index, "Point_Category_9"] = 4
    
cardinals_pitching_post["Sum_Total_Points"] = cardinals_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
cardinals_pitching_post["Combined_Total_Points"] = cardinals_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')







for i in range(1, 10):
    diamondbacks_pitching_post[f"Point_Category_{i}"] = 0

for index, row in diamondbacks_pitching_post.iterrows():
    if row["w"] >= 2:
        diamondbacks_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        diamondbacks_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        diamondbacks_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        diamondbacks_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        diamondbacks_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            diamondbacks_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        diamondbacks_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        diamondbacks_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        diamondbacks_pitching_post.at[index, "Point_Category_9"] = 4
    
diamondbacks_pitching_post["Sum_Total_Points"] = diamondbacks_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
diamondbacks_pitching_post["Combined_Total_Points"] = diamondbacks_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    rockies_pitching_post[f"Point_Category_{i}"] = 0

for index, row in rockies_pitching_post.iterrows():
    if row["w"] >= 2:
        rockies_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        rockies_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        rockies_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        rockies_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        rockies_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            rockies_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        rockies_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        rockies_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        rockies_pitching_post.at[index, "Point_Category_9"] = 4
    
rockies_pitching_post["Sum_Total_Points"] = rockies_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
rockies_pitching_post["Combined_Total_Points"] = rockies_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    dodgers_pitching_post[f"Point_Category_{i}"] = 0

for index, row in dodgers_pitching_post.iterrows():
    if row["w"] >= 2:
        dodgers_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        dodgers_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        dodgers_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        dodgers_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        dodgers_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            dodgers_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        dodgers_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        dodgers_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        dodgers_pitching_post.at[index, "Point_Category_9"] = 4
    
dodgers_pitching_post["Sum_Total_Points"] = dodgers_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
dodgers_pitching_post["Combined_Total_Points"] = dodgers_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    padres_pitching_post[f"Point_Category_{i}"] = 0

for index, row in padres_pitching_post.iterrows():
    if row["w"] >= 2:
        padres_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        padres_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        padres_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        padres_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        padres_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            padres_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        padres_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        padres_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        padres_pitching_post.at[index, "Point_Category_9"] = 4
    
padres_pitching_post["Sum_Total_Points"] = padres_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
padres_pitching_post["Combined_Total_Points"] = padres_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    giants_pitching_post[f"Point_Category_{i}"] = 0

for index, row in giants_pitching_post.iterrows():
    if row["w"] >= 2:
        giants_pitching.at[index, "Point_Category_1"] = 1
    if row["sho"] >= 1:
        giants_pitching.at[index, "Point_Category_2"] = 1
    if row["sv"] >= 2:
        giants_pitching.at[index, "Point_Category_3"] = 1
    if row["baopp"] <= 0.23:
        giants_pitching.at[index, "Point_Category_4"] = 2
    if row["era"] <= 2.4:
        giants_pitching.at[index, "Point_Category_5"] = 1

    strikeout_to_walk_ratio = row['so'] / row['bb'] if row['bb'] != 0 else 0
    if strikeout_to_walk_ratio < 0.250:
            giants_pitching.at[index, 'Point_Category_6'] = 1

    if row["round"] == "ALCS":
        giants_pitching_post.at[index, "Point_Category_7"] = 0.5
    if row["round"] == "NLCS":
        giants_pitching_post.at[index, "Point_Category_8"] = 0.5
    if row["round"] == "WS":
        giants_pitching_post.at[index, "Point_Category_9"] = 4
    
giants_pitching_post["Sum_Total_Points"] = giants_pitching_post[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
giants_pitching_post["Combined_Total_Points"] = giants_pitching_post.groupby("player_id")["Sum_Total_Points"].transform('sum')





# All star data per team

# Creating new dataframes for each team (redundant, but required when I concatenate this dataframe and the filtered one for my function)


orioles_all_star = pd.DataFrame(columns = all_star_data.columns)
red_sox_all_star = pd.DataFrame(columns = all_star_data.columns)
yankees_all_star = pd.DataFrame(columns = all_star_data.columns)
rays_all_star = pd.DataFrame(columns = all_star_data.columns)
blue_jays_all_star = pd.DataFrame(columns = all_star_data.columns)

white_sox_all_star = pd.DataFrame(columns = all_star_data.columns)
guardians_all_star = pd.DataFrame(columns = all_star_data.columns)
tigers_all_star = pd.DataFrame(columns = all_star_data.columns)
royals_all_star = pd.DataFrame(columns = all_star_data.columns)
twins_all_star = pd.DataFrame(columns = all_star_data.columns)

astros_all_star = pd.DataFrame(columns = all_star_data.columns)
angels_all_star = pd.DataFrame(columns = all_star_data.columns)
athletics_all_star = pd.DataFrame(columns = all_star_data.columns)
mariners_all_star = pd.DataFrame(columns = all_star_data.columns)
rangers_all_star = pd.DataFrame(columns = all_star_data.columns)



braves_all_star = pd.DataFrame(columns = all_star_data.columns)
marlins_all_star = pd.DataFrame(columns = all_star_data.columns)
mets_all_star = pd.DataFrame(columns = all_star_data.columns)
nationals_all_star = pd.DataFrame(columns = all_star_data.columns)
phillies_all_star = pd.DataFrame(columns = all_star_data.columns)

cubs_all_star = pd.DataFrame(columns = all_star_data.columns)
reds_all_star = pd.DataFrame(columns = all_star_data.columns)
brewers_all_star = pd.DataFrame(columns = all_star_data.columns)
pirates_all_star = pd.DataFrame(columns = all_star_data.columns)
cardinals_all_star = pd.DataFrame(columns = all_star_data.columns)

diamondbacks_all_star = pd.DataFrame(columns = all_star_data.columns)
rockies_all_star = pd.DataFrame(columns = all_star_data.columns)
dodgers_all_star = pd.DataFrame(columns = all_star_data.columns)
padres_all_star = pd.DataFrame(columns = all_star_data.columns)
giants_all_star = pd.DataFrame(columns = all_star_data.columns)


# Defining a functino where I take in a list of team ids and an existing empty team all star dataframe
# Filters out all observations that do not have any of the specified team_ids
# Returns a concatenation of the filtered dataframe and the empty dataframe (basically copying and pasting the filtered dataframe)

def append_specified_team_ids_all_star(team_ids, target_df):
    filtered_df = all_star_data[all_star_data["team_id"].isin(team_ids)]
    return pd.concat([target_df, filtered_df], ignore_index = True)



orioles_all_star = append_specified_team_ids_all_star(orioles_teams, orioles_all_star)
red_sox_all_star = append_specified_team_ids_all_star(red_sox_teams, red_sox_all_star)
yankees_all_star = append_specified_team_ids_all_star(yankees_teams, yankees_all_star)
rays_all_star = append_specified_team_ids_all_star(rays_teams, rays_all_star)
blue_jays_all_star = append_specified_team_ids_all_star(blue_jays_teams, blue_jays_all_star)

white_sox_all_star = append_specified_team_ids_all_star(white_sox_teams, white_sox_all_star)
guardians_all_star = append_specified_team_ids_all_star(guardians_teams, guardians_all_star)
tigers_all_star = append_specified_team_ids_all_star(tigers_teams, tigers_all_star)
royals_all_star = append_specified_team_ids_all_star(royals_teams, royals_all_star)
twins_all_star = append_specified_team_ids_all_star(twins_teams, twins_all_star)

astros_all_star = append_specified_team_ids_all_star(astros_teams, astros_all_star)
angels_all_star = append_specified_team_ids_all_star(angels_teams, angels_all_star)
athletics_all_star = append_specified_team_ids_all_star(athletics_teams, athletics_all_star)
mariners_all_star = append_specified_team_ids_all_star(mariners_teams, mariners_all_star)
rangers_all_star = append_specified_team_ids_all_star(rangers_teams, rangers_all_star)




braves_all_star = append_specified_team_ids_all_star(braves_teams, braves_all_star)
marlins_all_star = append_specified_team_ids_all_star(marlins_teams, marlins_all_star)
mets_all_star = append_specified_team_ids_all_star(mets_teams, mets_all_star)
nationals_all_star = append_specified_team_ids_all_star(nationals_teams, nationals_all_star)
phillies_all_star = append_specified_team_ids_all_star(phillies_teams, phillies_all_star)

cubs_all_star = append_specified_team_ids_all_star(cubs_teams, cubs_all_star)
reds_all_star = append_specified_team_ids_all_star(reds_teams, reds_all_star)
brewers_all_star = append_specified_team_ids_all_star(brewers_teams, brewers_all_star)
pirates_all_star = append_specified_team_ids_all_star(pirates_teams, pirates_all_star)
cardinals_all_star = append_specified_team_ids_all_star(cardinals_teams, cardinals_all_star)

diamondbacks_all_star = append_specified_team_ids_all_star(diamondbacks_teams, diamondbacks_all_star)
rockies_all_star = append_specified_team_ids_all_star(rockies_teams, rockies_all_star)
dodgers_all_star = append_specified_team_ids_all_star(dodgers_teams, dodgers_all_star)
padres_all_star = append_specified_team_ids_all_star(padres_teams, padres_all_star)
giants_all_star = append_specified_team_ids_all_star(giants_teams, giants_all_star)




# Defining points for each of the all star stats.
# First, a number of point category columns are created based on how many I want
# Second, in each batting dataset, I look to see if an observation satisfies each of the if statements. If they do, they get points assigned to the point categories
# I then get the sum of the points per that given season called Sum_Total_Points
# Lastly, I get the sum of the career number of points, the column called Combined_Total_Points

for i in range(1, 2):
    orioles_all_star[f"Point_Category_{i}"] = 0

for index, row in orioles_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        orioles_all_star.at[index, "Point_Category_1"] = 3

orioles_all_star["Sum_Total_Points"] = orioles_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
orioles_all_star["Combined_Total_Points"] = orioles_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 2):
    red_sox_all_star[f"Point_Category_{i}"] = 0

for index, row in red_sox_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        red_sox_all_star.at[index, "Point_Category_1"] = 3

red_sox_all_star["Sum_Total_Points"] = red_sox_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
red_sox_all_star["Combined_Total_Points"] = red_sox_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    yankees_all_star[f"Point_Category_{i}"] = 0

for index, row in yankees_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        yankees_all_star.at[index, "Point_Category_1"] = 3

yankees_all_star["Sum_Total_Points"] = yankees_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
yankees_all_star["Combined_Total_Points"] = yankees_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    rays_all_star[f"Point_Category_{i}"] = 0

for index, row in rays_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        rays_all_star.at[index, "Point_Category_1"] = 3

rays_all_star["Sum_Total_Points"] = rays_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
rays_all_star["Combined_Total_Points"] = rays_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    blue_jays_all_star[f"Point_Category_{i}"] = 0

for index, row in blue_jays_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        blue_jays_all_star.at[index, "Point_Category_1"] = 3

blue_jays_all_star["Sum_Total_Points"] = blue_jays_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
blue_jays_all_star["Combined_Total_Points"] = blue_jays_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')








for i in range(1, 2):
    white_sox_all_star[f"Point_Category_{i}"] = 0

for index, row in white_sox_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        white_sox_all_star.at[index, "Point_Category_1"] = 3

white_sox_all_star["Sum_Total_Points"] = white_sox_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
white_sox_all_star["Combined_Total_Points"] = white_sox_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    guardians_all_star[f"Point_Category_{i}"] = 0

for index, row in guardians_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        guardians_all_star.at[index, "Point_Category_1"] = 3

guardians_all_star["Sum_Total_Points"] = guardians_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
guardians_all_star["Combined_Total_Points"] = guardians_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    tigers_all_star[f"Point_Category_{i}"] = 0

for index, row in tigers_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        tigers_all_star.at[index, "Point_Category_1"] = 3

tigers_all_star["Sum_Total_Points"] = tigers_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
tigers_all_star["Combined_Total_Points"] = tigers_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    royals_all_star[f"Point_Category_{i}"] = 0

for index, row in royals_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        royals_all_star.at[index, "Point_Category_1"] = 3

royals_all_star["Sum_Total_Points"] = royals_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
royals_all_star["Combined_Total_Points"] = royals_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    twins_all_star[f"Point_Category_{i}"] = 0

for index, row in twins_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        twins_all_star.at[index, "Point_Category_1"] = 3

twins_all_star["Sum_Total_Points"] = twins_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
twins_all_star["Combined_Total_Points"] = twins_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')








for i in range(1, 2):
    astros_all_star[f"Point_Category_{i}"] = 0

for index, row in astros_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        astros_all_star.at[index, "Point_Category_1"] = 3

astros_all_star["Sum_Total_Points"] = astros_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
astros_all_star["Combined_Total_Points"] = astros_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    angels_all_star[f"Point_Category_{i}"] = 0

for index, row in angels_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        angels_all_star.at[index, "Point_Category_1"] = 3

angels_all_star["Sum_Total_Points"] = angels_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
angels_all_star["Combined_Total_Points"] = angels_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    athletics_all_star[f"Point_Category_{i}"] = 0

for index, row in athletics_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        athletics_all_star.at[index, "Point_Category_1"] = 3

athletics_all_star["Sum_Total_Points"] = athletics_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
athletics_all_star["Combined_Total_Points"] = athletics_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    mariners_all_star[f"Point_Category_{i}"] = 0

for index, row in mariners_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        mariners_all_star.at[index, "Point_Category_1"] = 3

mariners_all_star["Sum_Total_Points"] = mariners_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
mariners_all_star["Combined_Total_Points"] = mariners_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    rangers_all_star[f"Point_Category_{i}"] = 0

for index, row in rangers_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        rangers_all_star.at[index, "Point_Category_1"] = 3

rangers_all_star["Sum_Total_Points"] = rangers_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
rangers_all_star["Combined_Total_Points"] = rangers_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')












for i in range(1, 2):
    braves_all_star[f"Point_Category_{i}"] = 0

for index, row in braves_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        braves_all_star.at[index, "Point_Category_1"] = 3

braves_all_star["Sum_Total_Points"] = braves_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
braves_all_star["Combined_Total_Points"] = braves_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    marlins_all_star[f"Point_Category_{i}"] = 0

for index, row in marlins_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        marlins_all_star.at[index, "Point_Category_1"] = 3

marlins_all_star["Sum_Total_Points"] = marlins_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
marlins_all_star["Combined_Total_Points"] = marlins_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 2):
    mets_all_star[f"Point_Category_{i}"] = 0

for index, row in mets_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        mets_all_star.at[index, "Point_Category_1"] = 3

mets_all_star["Sum_Total_Points"] = mets_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
mets_all_star["Combined_Total_Points"] = mets_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    nationals_all_star[f"Point_Category_{i}"] = 0

for index, row in nationals_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        nationals_all_star.at[index, "Point_Category_1"] = 3

nationals_all_star["Sum_Total_Points"] = nationals_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
nationals_all_star["Combined_Total_Points"] = nationals_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    phillies_all_star[f"Point_Category_{i}"] = 0

for index, row in phillies_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        phillies_all_star.at[index, "Point_Category_1"] = 3

phillies_all_star["Sum_Total_Points"] = phillies_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
phillies_all_star["Combined_Total_Points"] = phillies_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')








for i in range(1, 2):
    cubs_all_star[f"Point_Category_{i}"] = 0

for index, row in cubs_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        cubs_all_star.at[index, "Point_Category_1"] = 3

cubs_all_star["Sum_Total_Points"] = cubs_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
cubs_all_star["Combined_Total_Points"] = cubs_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    reds_all_star[f"Point_Category_{i}"] = 0

for index, row in reds_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        reds_all_star.at[index, "Point_Category_1"] = 3

reds_all_star["Sum_Total_Points"] = reds_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
reds_all_star["Combined_Total_Points"] = reds_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    brewers_all_star[f"Point_Category_{i}"] = 0

for index, row in brewers_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        brewers_all_star.at[index, "Point_Category_1"] = 3

brewers_all_star["Sum_Total_Points"] = brewers_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
brewers_all_star["Combined_Total_Points"] = brewers_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    pirates_all_star[f"Point_Category_{i}"] = 0

for index, row in pirates_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        pirates_all_star.at[index, "Point_Category_1"] = 3

pirates_all_star["Sum_Total_Points"] = pirates_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
pirates_all_star["Combined_Total_Points"] = pirates_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    cardinals_all_star[f"Point_Category_{i}"] = 0

for index, row in cardinals_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        cardinals_all_star.at[index, "Point_Category_1"] = 3

cardinals_all_star["Sum_Total_Points"] = cardinals_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
cardinals_all_star["Combined_Total_Points"] = cardinals_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')






for i in range(1, 2):
    diamondbacks_all_star[f"Point_Category_{i}"] = 0

for index, row in diamondbacks_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        diamondbacks_all_star.at[index, "Point_Category_1"] = 3

diamondbacks_all_star["Sum_Total_Points"] = diamondbacks_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
diamondbacks_all_star["Combined_Total_Points"] = diamondbacks_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    rockies_all_star[f"Point_Category_{i}"] = 0

for index, row in rockies_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        rockies_all_star.at[index, "Point_Category_1"] = 3

rockies_all_star["Sum_Total_Points"] = rockies_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
rockies_all_star["Combined_Total_Points"] = rockies_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    dodgers_all_star[f"Point_Category_{i}"] = 0

for index, row in dodgers_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        dodgers_all_star.at[index, "Point_Category_1"] = 3

dodgers_all_star["Sum_Total_Points"] = dodgers_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
dodgers_all_star["Combined_Total_Points"] = dodgers_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    padres_all_star[f"Point_Category_{i}"] = 0

for index, row in padres_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        padres_all_star.at[index, "Point_Category_1"] = 3

padres_all_star["Sum_Total_Points"] = padres_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
padres_all_star["Combined_Total_Points"] = padres_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')



for i in range(1, 2):
    giants_all_star[f"Point_Category_{i}"] = 0

for index, row in giants_all_star.iterrows():
    if row["league_id"] in ["NL", "AL"]:
        giants_all_star.at[index, "Point_Category_1"] = 3

giants_all_star["Sum_Total_Points"] = giants_all_star[[f"Point_Category_{i}" for i in range(1, 2)]].sum(axis=1)
giants_all_star["Combined_Total_Points"] = giants_all_star.groupby("player_id")["Sum_Total_Points"].transform('sum')




# Player awards data manipulation per team

# Creating new dataframes for each team (redundant, but required when I concatenate this dataframe and the filtered one for my function)


orioles_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
red_sox_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
yankees_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
rays_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
blue_jays_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)

white_sox_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
guardians_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
tigers_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
royals_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
twins_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)

astros_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
angels_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
athletics_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
mariners_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
rangers_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)



braves_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
marlins_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
mets_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
nationals_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
phillies_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)

cubs_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
reds_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
brewers_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
pirates_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
cardinals_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)

diamondbacks_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
rockies_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
dodgers_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
padres_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)
giants_player_awards = pd.DataFrame(player_awards_data, columns = player_awards_data.columns)




# Defining points for each of the player award stats
# First, a number of point category columns are created based on how many I want
# Second, in each batting dataset, I look to see if an observation satisfies each of the if statements. If they do, they get points assigned to the point categories
# I then get the sum of the points per that given season called Sum_Total_Points
# Lastly, I get the sum of the career number of points, the column called Combined_Total_Points

for i in range(1, 10):
    orioles_player_awards[f"Point_Category_{i}"] = 0

for index, row in orioles_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        orioles_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        orioles_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        orioles_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        orioles_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        orioles_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        orioles_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        orioles_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        orioles_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        orioles_player_awards.at[index, "Point_Category_9"] = 12


orioles_player_awards["Sum_Total_Points"] = orioles_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
orioles_player_awards["Combined_Total_Points"] = orioles_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    red_sox_player_awards[f"Point_Category_{i}"] = 0

for index, row in red_sox_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        red_sox_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        red_sox_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        red_sox_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        red_sox_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        red_sox_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        red_sox_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        red_sox_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        red_sox_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        red_sox_player_awards.at[index, "Point_Category_9"] = 12


red_sox_player_awards["Sum_Total_Points"] = red_sox_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
red_sox_player_awards["Combined_Total_Points"] = red_sox_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')

for i in range(1, 10):
    yankees_player_awards[f"Point_Category_{i}"] = 0

for index, row in yankees_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        yankees_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        yankees_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        yankees_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        yankees_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        yankees_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        yankees_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        yankees_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        yankees_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        yankees_player_awards.at[index, "Point_Category_9"] = 12


yankees_player_awards["Sum_Total_Points"] = yankees_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
yankees_player_awards["Combined_Total_Points"] = yankees_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')

for i in range(1, 10):
    rays_player_awards[f"Point_Category_{i}"] = 0

for index, row in rays_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        rays_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        rays_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        rays_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        rays_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        rays_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        rays_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        rays_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        rays_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        rays_player_awards.at[index, "Point_Category_9"] = 12

rays_player_awards["Sum_Total_Points"] = rays_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
rays_player_awards["Combined_Total_Points"] = rays_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')

for i in range(1, 10):
    blue_jays_player_awards[f"Point_Category_{i}"] = 0

for index, row in blue_jays_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        blue_jays_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        blue_jays_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        blue_jays_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        blue_jays_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        blue_jays_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        blue_jays_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        blue_jays_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        blue_jays_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        blue_jays_player_awards.at[index, "Point_Category_9"] = 12

blue_jays_player_awards["Sum_Total_Points"] = blue_jays_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
blue_jays_player_awards["Combined_Total_Points"] = blue_jays_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')






for i in range(1, 10):
    white_sox_player_awards[f"Point_Category_{i}"] = 0

for index, row in white_sox_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        white_sox_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        white_sox_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        white_sox_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        white_sox_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        white_sox_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        white_sox_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        white_sox_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        white_sox_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        white_sox_player_awards.at[index, "Point_Category_9"] = 12

white_sox_player_awards["Sum_Total_Points"] = white_sox_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
white_sox_player_awards["Combined_Total_Points"] = white_sox_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    guardians_player_awards[f"Point_Category_{i}"] = 0

for index, row in guardians_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        guardians_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        guardians_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        guardians_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        guardians_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        guardians_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        guardians_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        guardians_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        guardians_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        guardians_player_awards.at[index, "Point_Category_9"] = 12

guardians_player_awards["Sum_Total_Points"] = guardians_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
guardians_player_awards["Combined_Total_Points"] = guardians_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')

for i in range(1, 10):
    tigers_player_awards[f"Point_Category_{i}"] = 0

for index, row in tigers_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        tigers_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        tigers_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        tigers_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        tigers_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        tigers_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        tigers_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        tigers_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        tigers_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        tigers_player_awards.at[index, "Point_Category_9"] = 12

tigers_player_awards["Sum_Total_Points"] = tigers_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
tigers_player_awards["Combined_Total_Points"] = tigers_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')

for i in range(1, 10):
    royals_player_awards[f"Point_Category_{i}"] = 0

for index, row in royals_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        royals_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        royals_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        royals_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        royals_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        royals_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        royals_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        royals_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        royals_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        royals_player_awards.at[index, "Point_Category_9"] = 12

royals_player_awards["Sum_Total_Points"] = royals_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
royals_player_awards["Combined_Total_Points"] = royals_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')

for i in range(1, 10):
    twins_player_awards[f"Point_Category_{i}"] = 0

for index, row in twins_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        twins_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        twins_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        twins_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        twins_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        twins_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        twins_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        twins_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        twins_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        twins_player_awards.at[index, "Point_Category_9"] = 12

twins_player_awards["Sum_Total_Points"] = twins_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
twins_player_awards["Combined_Total_Points"] = twins_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')






for i in range(1, 10):
    astros_player_awards[f"Point_Category_{i}"] = 0

for index, row in astros_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        astros_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        astros_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        astros_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        astros_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        astros_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        astros_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        astros_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        astros_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        astros_player_awards.at[index, "Point_Category_9"] = 12

astros_player_awards["Sum_Total_Points"] = astros_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
astros_player_awards["Combined_Total_Points"] = astros_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    angels_player_awards[f"Point_Category_{i}"] = 0

for index, row in angels_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        angels_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        angels_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        angels_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        angels_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        angels_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        angels_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        angels_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        angels_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        angels_player_awards.at[index, "Point_Category_9"] = 12

angels_player_awards["Sum_Total_Points"] = angels_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
angels_player_awards["Combined_Total_Points"] = angels_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')

for i in range(1, 10):
    athletics_player_awards[f"Point_Category_{i}"] = 0

for index, row in athletics_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        athletics_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        athletics_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        athletics_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        athletics_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        athletics_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        athletics_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        athletics_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        athletics_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        athletics_player_awards.at[index, "Point_Category_9"] = 12

athletics_player_awards["Sum_Total_Points"] = athletics_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
athletics_player_awards["Combined_Total_Points"] = athletics_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')

for i in range(1, 10):
    mariners_player_awards[f"Point_Category_{i}"] = 0

for index, row in mariners_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        mariners_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        mariners_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        mariners_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        mariners_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        mariners_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        mariners_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        mariners_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        mariners_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        mariners_player_awards.at[index, "Point_Category_9"] = 12

mariners_player_awards["Sum_Total_Points"] = mariners_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
mariners_player_awards["Combined_Total_Points"] = mariners_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')

for i in range(1, 10):
    rangers_player_awards[f"Point_Category_{i}"] = 0

for index, row in rangers_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        rangers_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        rangers_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        rangers_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        rangers_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        rangers_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        rangers_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        rangers_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        rangers_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        rangers_player_awards.at[index, "Point_Category_9"] = 12

rangers_player_awards["Sum_Total_Points"] = rangers_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
rangers_player_awards["Combined_Total_Points"] = rangers_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')












for i in range(1, 10):
    braves_player_awards[f"Point_Category_{i}"] = 0

for index, row in braves_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        braves_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        braves_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        braves_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        braves_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        braves_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        braves_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        braves_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        braves_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        braves_player_awards.at[index, "Point_Category_9"] = 12

braves_player_awards["Sum_Total_Points"] = braves_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
braves_player_awards["Combined_Total_Points"] = braves_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    marlins_player_awards[f"Point_Category_{i}"] = 0

for index, row in marlins_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        marlins_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        marlins_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        marlins_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        marlins_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        marlins_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        marlins_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        marlins_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        marlins_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        marlins_player_awards.at[index, "Point_Category_9"] = 12

marlins_player_awards["Sum_Total_Points"] = marlins_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
marlins_player_awards["Combined_Total_Points"] = marlins_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')

for i in range(1, 10):
    mets_player_awards[f"Point_Category_{i}"] = 0

for index, row in mets_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        mets_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        mets_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        mets_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        mets_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        mets_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        mets_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        mets_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        mets_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        mets_player_awards.at[index, "Point_Category_9"] = 12

mets_player_awards["Sum_Total_Points"] = mets_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
mets_player_awards["Combined_Total_Points"] = mets_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')

for i in range(1, 10):
    nationals_player_awards[f"Point_Category_{i}"] = 0

for index, row in nationals_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        nationals_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        nationals_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        nationals_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        nationals_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        nationals_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        nationals_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        nationals_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        nationals_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        nationals_player_awards.at[index, "Point_Category_9"] = 12

nationals_player_awards["Sum_Total_Points"] = nationals_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
nationals_player_awards["Combined_Total_Points"] = nationals_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')

for i in range(1, 10):
    phillies_player_awards[f"Point_Category_{i}"] = 0

for index, row in phillies_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        phillies_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        phillies_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        phillies_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        phillies_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        phillies_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        phillies_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        phillies_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        phillies_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        phillies_player_awards.at[index, "Point_Category_9"] = 12

phillies_player_awards["Sum_Total_Points"] = phillies_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
phillies_player_awards["Combined_Total_Points"] = phillies_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')







for i in range(1, 10):
    cubs_player_awards[f"Point_Category_{i}"] = 0

for index, row in cubs_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        cubs_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        cubs_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        cubs_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        cubs_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        cubs_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        cubs_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        cubs_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        cubs_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        cubs_player_awards.at[index, "Point_Category_9"] = 12

cubs_player_awards["Sum_Total_Points"] = cubs_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
cubs_player_awards["Combined_Total_Points"] = cubs_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    reds_player_awards[f"Point_Category_{i}"] = 0

for index, row in reds_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        reds_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        reds_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        reds_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        reds_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        reds_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        reds_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        reds_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        reds_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        reds_player_awards.at[index, "Point_Category_9"] = 12

reds_player_awards["Sum_Total_Points"] = reds_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
reds_player_awards["Combined_Total_Points"] = reds_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')

for i in range(1, 10):
    brewers_player_awards[f"Point_Category_{i}"] = 0

for index, row in brewers_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        brewers_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        brewers_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        brewers_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        brewers_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        brewers_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        brewers_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        brewers_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        brewers_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        brewers_player_awards.at[index, "Point_Category_9"] = 12

brewers_player_awards["Sum_Total_Points"] = brewers_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
brewers_player_awards["Combined_Total_Points"] = brewers_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')

for i in range(1, 10):
    pirates_player_awards[f"Point_Category_{i}"] = 0

for index, row in pirates_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        pirates_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        pirates_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        pirates_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        pirates_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        pirates_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        pirates_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        pirates_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        pirates_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        pirates_player_awards.at[index, "Point_Category_9"] = 12

pirates_player_awards["Sum_Total_Points"] = pirates_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
pirates_player_awards["Combined_Total_Points"] = pirates_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')

for i in range(1, 10):
    cardinals_player_awards[f"Point_Category_{i}"] = 0

for index, row in cardinals_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        cardinals_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        cardinals_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        cardinals_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        cardinals_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        cardinals_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        cardinals_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        cardinals_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        cardinals_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        cardinals_player_awards.at[index, "Point_Category_9"] = 12

cardinals_player_awards["Sum_Total_Points"] = cardinals_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
cardinals_player_awards["Combined_Total_Points"] = cardinals_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')







for i in range(1, 10):
    diamondbacks_player_awards[f"Point_Category_{i}"] = 0

for index, row in diamondbacks_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        diamondbacks_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        diamondbacks_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        diamondbacks_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        diamondbacks_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        diamondbacks_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        diamondbacks_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        diamondbacks_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        diamondbacks_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        diamondbacks_player_awards.at[index, "Point_Category_9"] = 12

diamondbacks_player_awards["Sum_Total_Points"] = diamondbacks_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
diamondbacks_player_awards["Combined_Total_Points"] = diamondbacks_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')


for i in range(1, 10):
    rockies_player_awards[f"Point_Category_{i}"] = 0

for index, row in rockies_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        rockies_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        rockies_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        rockies_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        rockies_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        rockies_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        rockies_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        rockies_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        rockies_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        rockies_player_awards.at[index, "Point_Category_9"] = 12

rockies_player_awards["Sum_Total_Points"] = rockies_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
rockies_player_awards["Combined_Total_Points"] = rockies_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')

for i in range(1, 10):
    dodgers_player_awards[f"Point_Category_{i}"] = 0

for index, row in dodgers_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        dodgers_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        dodgers_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        dodgers_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        dodgers_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        dodgers_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        dodgers_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        dodgers_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        dodgers_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        dodgers_player_awards.at[index, "Point_Category_9"] = 12

dodgers_player_awards["Sum_Total_Points"] = dodgers_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
dodgers_player_awards["Combined_Total_Points"] = dodgers_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')

for i in range(1, 10):
    padres_player_awards[f"Point_Category_{i}"] = 0

for index, row in padres_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        padres_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        padres_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        padres_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        padres_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        padres_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        padres_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        padres_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        padres_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        padres_player_awards.at[index, "Point_Category_9"] = 12

padres_player_awards["Sum_Total_Points"] = padres_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
padres_player_awards["Combined_Total_Points"] = padres_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')

for i in range(1, 10):
    giants_player_awards[f"Point_Category_{i}"] = 0

for index, row in giants_player_awards.iterrows():
    if row["award_id"] == "Gold Glove":
        giants_player_awards.at[index, "Point_Category_1"] = 3
    if row["award_id"] == "Silver Slugger":
        giants_player_awards.at[index, "Point_Category_2"] = 3
    if row["award_id"] == "Most Valuable Player":
        giants_player_awards.at[index, "Point_Category_3"] = 8
    if row["award_id"] == "World Series MVP":
        giants_player_awards.at[index, "Point_Category_4"] = 8
    if row["award_id"] == "TSN Fireman of the Year":
        giants_player_awards.at[index, "Point_Category_5"] = 1
    if row["award_id"] == "TSN Reliever of the Year":
        giants_player_awards.at[index, "Point_Category_6"] = 1
    if row["award_id"] == "Cy Young Award":
        giants_player_awards.at[index, "Point_Category_7"] = 4
    if row["award_id"] == "Pitching Triple Crown":
        giants_player_awards.at[index, "Point_Category_8"] = 12
    if row["award_id"] == "Triple Crown":
        giants_player_awards.at[index, "Point_Category_9"] = 12

giants_player_awards["Sum_Total_Points"] = giants_player_awards[[f"Point_Category_{i}" for i in range(1, 10)]].sum(axis=1)
giants_player_awards["Combined_Total_Points"] = giants_player_awards.groupby("player_id")["Sum_Total_Points"].transform('sum')










# CALCULATING BEST POSITIONS FOR PLAYERS THROUGH FILTERING

### Taking the regular season fielding data and getting the most common
### positions that a player has played, for the sole purpose of designating
### players final positions and nothing else


# I might just put all infielding data manipulation together, so this for 
# now is just copied from above



# Making copies of each of the datasets to preserve the integrity of
# the originals

orioles_positions_infield_copy = orioles_infielding.copy()
red_sox_positions_infield_copy = red_sox_infielding.copy() 
yankees_positions_infield_copy = yankees_infielding.copy() 
rays_positions_infield_copy = rays_infielding.copy()
blue_jays_positions_infield_copy = blue_jays_infielding.copy()

white_sox_positions_infield_copy = white_sox_infielding.copy()
guardians_positions_infield_copy = guardians_infielding.copy()
tigers_positions_infield_copy = tigers_infielding.copy()
royals_positions_infield_copy = royals_infielding.copy()
twins_positions_infield_copy = twins_infielding.copy()

astros_positions_infield_copy = astros_infielding.copy()
angels_positions_infield_copy = angels_infielding.copy()
athletics_positions_infield_copy = athletics_infielding.copy()
mariners_positions_infield_copy = mariners_infielding.copy()
rangers_positions_infield_copy = rangers_infielding.copy()



braves_positions_infield_copy = braves_infielding.copy()
marlins_positions_infield_copy = marlins_infielding.copy()
mets_positions_infield_copy = mets_infielding.copy()
nationals_positions_infield_copy = nationals_infielding.copy()
phillies_positions_infield_copy = phillies_infielding.copy()

cubs_positions_infield_copy = cubs_infielding.copy()
reds_positions_infield_copy = reds_infielding.copy()
brewers_positions_infield_copy = brewers_infielding.copy()
pirates_positions_infield_copy = pirates_infielding.copy()
cardinals_positions_infield_copy = cardinals_infielding.copy()

diamondbacks_positions_infield_copy = diamondbacks_infielding.copy()
rockies_positions_infield_copy = rockies_infielding.copy()
dodgers_positions_infield_copy = dodgers_infielding.copy()
padres_positions_infield_copy = padres_infielding.copy()
giants_positions_infield_copy = giants_infielding.copy()




# Function that returns the most common out of all positions a player has
# played in their career

def get_most_common_position(group):
    return group["pos"].mode()[0]







# Applying funciton and instructing the copied dataset to only include in the pos variable the main position the player played over their career
# Merging the most common position dataframe and the copied infield dataset, renaming pos to be the most common position, and getting rid of the Most_Common_Position var

most_common_positions_orioles = orioles_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_orioles.columns = ["player_id", "Most_Common_Position"]
orioles_positions_infield_copy = orioles_positions_infield_copy.merge(most_common_positions_orioles, on="player_id", how="left")
orioles_positions_infield_copy["pos"] = orioles_positions_infield_copy["Most_Common_Position"]
orioles_positions_infield_copy = orioles_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_red_sox = red_sox_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_red_sox.columns = ["player_id", "Most_Common_Position"]
red_sox_positions_infield_copy = red_sox_positions_infield_copy.merge(most_common_positions_red_sox, on="player_id", how="left")
red_sox_positions_infield_copy["pos"] = red_sox_positions_infield_copy["Most_Common_Position"]
red_sox_positions_infield_copy = red_sox_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_yankees = yankees_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_yankees.columns = ["player_id", "Most_Common_Position"]
yankees_positions_infield_copy = yankees_positions_infield_copy.merge(most_common_positions_yankees, on="player_id", how="left")
yankees_positions_infield_copy["pos"] = yankees_positions_infield_copy["Most_Common_Position"]
yankees_positions_infield_copy = yankees_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_rays = rays_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_rays.columns = ["player_id", "Most_Common_Position"]
rays_positions_infield_copy = rays_positions_infield_copy.merge(most_common_positions_rays, on="player_id", how="left")
rays_positions_infield_copy["pos"] = rays_positions_infield_copy["Most_Common_Position"]
rays_positions_infield_copy = rays_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_blue_jays = blue_jays_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_blue_jays.columns = ["player_id", "Most_Common_Position"]
blue_jays_positions_infield_copy = blue_jays_positions_infield_copy.merge(most_common_positions_blue_jays, on="player_id", how="left")
blue_jays_positions_infield_copy["pos"] = blue_jays_positions_infield_copy["Most_Common_Position"]
blue_jays_positions_infield_copy = blue_jays_positions_infield_copy.drop(columns = ["Most_Common_Position"])



most_common_positions_white_sox = white_sox_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_white_sox.columns = ["player_id", "Most_Common_Position"]
white_sox_positions_infield_copy = white_sox_positions_infield_copy.merge(most_common_positions_white_sox, on="player_id", how="left")
white_sox_positions_infield_copy["pos"] = white_sox_positions_infield_copy["Most_Common_Position"]
white_sox_positions_infield_copy = white_sox_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_guardians = guardians_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_guardians.columns = ["player_id", "Most_Common_Position"]
guardians_positions_infield_copy = guardians_positions_infield_copy.merge(most_common_positions_guardians, on="player_id", how="left")
guardians_positions_infield_copy["pos"] = guardians_positions_infield_copy["Most_Common_Position"]
guardians_positions_infield_copy = guardians_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_tigers = tigers_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_tigers.columns = ["player_id", "Most_Common_Position"]
tigers_positions_infield_copy = tigers_positions_infield_copy.merge(most_common_positions_tigers, on="player_id", how="left")
tigers_positions_infield_copy["pos"] = tigers_positions_infield_copy["Most_Common_Position"]
tigers_positions_infield_copy = tigers_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_royals = royals_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_royals.columns = ["player_id", "Most_Common_Position"]
royals_positions_infield_copy = royals_positions_infield_copy.merge(most_common_positions_royals, on="player_id", how="left")
royals_positions_infield_copy["pos"] = royals_positions_infield_copy["Most_Common_Position"]
royals_positions_infield_copy = royals_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_twins = twins_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_twins.columns = ["player_id", "Most_Common_Position"]
twins_positions_infield_copy = twins_positions_infield_copy.merge(most_common_positions_twins, on="player_id", how="left")
twins_positions_infield_copy["pos"] = twins_positions_infield_copy["Most_Common_Position"]
twins_positions_infield_copy = twins_positions_infield_copy.drop(columns = ["Most_Common_Position"])



most_common_positions_astros = astros_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_astros.columns = ["player_id", "Most_Common_Position"]
astros_positions_infield_copy = astros_positions_infield_copy.merge(most_common_positions_astros, on="player_id", how="left")
astros_positions_infield_copy["pos"] = astros_positions_infield_copy["Most_Common_Position"]
astros_positions_infield_copy = astros_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_angels = angels_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_angels.columns = ["player_id", "Most_Common_Position"]
angels_positions_infield_copy = angels_positions_infield_copy.merge(most_common_positions_angels, on="player_id", how="left")
angels_positions_infield_copy["pos"] = angels_positions_infield_copy["Most_Common_Position"]
angels_positions_infield_copy = angels_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_athletics = athletics_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_athletics.columns = ["player_id", "Most_Common_Position"]
athletics_positions_infield_copy = athletics_positions_infield_copy.merge(most_common_positions_athletics, on="player_id", how="left")
athletics_positions_infield_copy["pos"] = athletics_positions_infield_copy["Most_Common_Position"]
athletics_positions_infield_copy = athletics_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_mariners = mariners_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_mariners.columns = ["player_id", "Most_Common_Position"]
mariners_positions_infield_copy = mariners_positions_infield_copy.merge(most_common_positions_mariners, on="player_id", how="left")
mariners_positions_infield_copy["pos"] = mariners_positions_infield_copy["Most_Common_Position"]
mariners_positions_infield_copy = mariners_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_rangers = rangers_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_rangers.columns = ["player_id", "Most_Common_Position"]
rangers_positions_infield_copy = rangers_positions_infield_copy.merge(most_common_positions_rangers, on="player_id", how="left")
rangers_positions_infield_copy["pos"] = rangers_positions_infield_copy["Most_Common_Position"]
rangers_positions_infield_copy = rangers_positions_infield_copy.drop(columns = ["Most_Common_Position"])



most_common_positions_braves = braves_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_braves.columns = ["player_id", "Most_Common_Position"]
braves_positions_infield_copy = braves_positions_infield_copy.merge(most_common_positions_braves, on="player_id", how="left")
braves_positions_infield_copy["pos"] = braves_positions_infield_copy["Most_Common_Position"]
braves_positions_infield_copy = braves_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_marlins = marlins_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_marlins.columns = ["player_id", "Most_Common_Position"]
marlins_positions_infield_copy = marlins_positions_infield_copy.merge(most_common_positions_marlins, on="player_id", how="left")
marlins_positions_infield_copy["pos"] = marlins_positions_infield_copy["Most_Common_Position"]
marlins_positions_infield_copy = marlins_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_mets = mets_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_mets.columns = ["player_id", "Most_Common_Position"]
mets_positions_infield_copy = mets_positions_infield_copy.merge(most_common_positions_mets, on="player_id", how="left")
mets_positions_infield_copy["pos"] = mets_positions_infield_copy["Most_Common_Position"]
mets_positions_infield_copy = mets_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_nationals = nationals_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_nationals.columns = ["player_id", "Most_Common_Position"]
nationals_positions_infield_copy = nationals_positions_infield_copy.merge(most_common_positions_nationals, on="player_id", how="left")
nationals_positions_infield_copy["pos"] = nationals_positions_infield_copy["Most_Common_Position"]
nationals_positions_infield_copy = nationals_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_phillies = phillies_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_phillies.columns = ["player_id", "Most_Common_Position"]
phillies_positions_infield_copy = phillies_positions_infield_copy.merge(most_common_positions_phillies, on="player_id", how="left")
phillies_positions_infield_copy["pos"] = phillies_positions_infield_copy["Most_Common_Position"]
phillies_positions_infield_copy = phillies_positions_infield_copy.drop(columns = ["Most_Common_Position"])




most_common_positions_cubs = cubs_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_cubs.columns = ["player_id", "Most_Common_Position"]
cubs_positions_infield_copy = cubs_positions_infield_copy.merge(most_common_positions_cubs, on="player_id", how="left")
cubs_positions_infield_copy["pos"] = cubs_positions_infield_copy["Most_Common_Position"]
cubs_positions_infield_copy = cubs_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_reds = reds_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_reds.columns = ["player_id", "Most_Common_Position"]
reds_positions_infield_copy = reds_positions_infield_copy.merge(most_common_positions_reds, on="player_id", how="left")
reds_positions_infield_copy["pos"] = reds_positions_infield_copy["Most_Common_Position"]
reds_positions_infield_copy = reds_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_brewers = brewers_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_brewers.columns = ["player_id", "Most_Common_Position"]
brewers_positions_infield_copy = brewers_positions_infield_copy.merge(most_common_positions_brewers, on="player_id", how="left")
brewers_positions_infield_copy["pos"] = brewers_positions_infield_copy["Most_Common_Position"]
brewers_positions_infield_copy = brewers_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_pirates = pirates_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_pirates.columns = ["player_id", "Most_Common_Position"]
pirates_positions_infield_copy = pirates_positions_infield_copy.merge(most_common_positions_pirates, on="player_id", how="left")
pirates_positions_infield_copy["pos"] = pirates_positions_infield_copy["Most_Common_Position"]
pirates_positions_infield_copy = pirates_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_cardinals = cardinals_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_cardinals.columns = ["player_id", "Most_Common_Position"]
cardinals_positions_infield_copy = cardinals_positions_infield_copy.merge(most_common_positions_cardinals, on="player_id", how="left")
cardinals_positions_infield_copy["pos"] = cardinals_positions_infield_copy["Most_Common_Position"]
cardinals_positions_infield_copy = cardinals_positions_infield_copy.drop(columns = ["Most_Common_Position"])



most_common_positions_diamondbacks = diamondbacks_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_diamondbacks.columns = ["player_id", "Most_Common_Position"]
diamondbacks_positions_infield_copy = diamondbacks_positions_infield_copy.merge(most_common_positions_diamondbacks, on="player_id", how="left")
diamondbacks_positions_infield_copy["pos"] = diamondbacks_positions_infield_copy["Most_Common_Position"]
diamondbacks_positions_infield_copy = diamondbacks_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_rockies = rockies_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_rockies.columns = ["player_id", "Most_Common_Position"]
rockies_positions_infield_copy = rockies_positions_infield_copy.merge(most_common_positions_rockies, on="player_id", how="left")
rockies_positions_infield_copy["pos"] = rockies_positions_infield_copy["Most_Common_Position"]
rockies_positions_infield_copy = rockies_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_dodgers = dodgers_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_dodgers.columns = ["player_id", "Most_Common_Position"]
dodgers_positions_infield_copy = dodgers_positions_infield_copy.merge(most_common_positions_dodgers, on="player_id", how="left")
dodgers_positions_infield_copy["pos"] = dodgers_positions_infield_copy["Most_Common_Position"]
dodgers_positions_infield_copy = dodgers_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_padres = padres_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_padres.columns = ["player_id", "Most_Common_Position"]
padres_positions_infield_copy = padres_positions_infield_copy.merge(most_common_positions_padres, on="player_id", how="left")
padres_positions_infield_copy["pos"] = padres_positions_infield_copy["Most_Common_Position"]
padres_positions_infield_copy = padres_positions_infield_copy.drop(columns = ["Most_Common_Position"])

most_common_positions_giants = giants_positions_infield_copy.groupby("player_id").apply(get_most_common_position).reset_index()
most_common_positions_giants.columns = ["player_id", "Most_Common_Position"]
giants_positions_infield_copy = giants_positions_infield_copy.merge(most_common_positions_giants, on="player_id", how="left")
giants_positions_infield_copy["pos"] = giants_positions_infield_copy["Most_Common_Position"]
giants_positions_infield_copy = giants_positions_infield_copy.drop(columns = ["Most_Common_Position"])









# Gathering the unique values
# By gathering the unique values, I only have the first observation of each player. I am doing this since it makes me able to merge everything since there'd only be one of each player id
# I created the Combined_Total_Points so that a player can be merged everywhere and still retain their lifetime points
# The observations with the highest lifetime points will inevitably survive the future sorting


# Batting unique values (dropping duplicate IDs)

orioles_batting_unique_id = orioles_batting.drop_duplicates(subset = "player_id", keep = "first")
red_sox_batting_unique_id = red_sox_batting.drop_duplicates(subset = "player_id", keep = "first")
yankees_batting_unique_id = yankees_batting.drop_duplicates(subset = "player_id", keep = "first")
rays_batting_unique_id = rays_batting.drop_duplicates(subset = "player_id", keep = "first")
blue_jays_batting_unique_id = blue_jays_batting.drop_duplicates(subset = "player_id", keep = "first")

white_sox_batting_unique_id = white_sox_batting.drop_duplicates(subset = "player_id", keep = "first")
guardians_batting_unique_id = guardians_batting.drop_duplicates(subset = "player_id", keep = "first")
tigers_batting_unique_id = tigers_batting.drop_duplicates(subset = "player_id", keep = "first")
royals_batting_unique_id = royals_batting.drop_duplicates(subset = "player_id", keep = "first")
twins_batting_unique_id = twins_batting.drop_duplicates(subset = "player_id", keep = "first")

astros_batting_unique_id = astros_batting.drop_duplicates(subset = "player_id", keep = "first")
angels_batting_unique_id = angels_batting.drop_duplicates(subset = "player_id", keep = "first")
athletics_batting_unique_id = athletics_batting.drop_duplicates(subset = "player_id", keep = "first")
mariners_batting_unique_id = mariners_batting.drop_duplicates(subset = "player_id", keep = "first")
rangers_batting_unique_id = rangers_batting.drop_duplicates(subset = "player_id", keep = "first")






braves_batting_unique_id = braves_batting.drop_duplicates(subset = "player_id", keep = "first")
marlins_batting_unique_id = marlins_batting.drop_duplicates(subset = "player_id", keep = "first")
mets_batting_unique_id = mets_batting.drop_duplicates(subset = "player_id", keep = "first")
nationals_batting_unique_id = nationals_batting.drop_duplicates(subset = "player_id", keep = "first")
phillies_batting_unique_id = phillies_batting.drop_duplicates(subset = "player_id", keep = "first")

cubs_batting_unique_id = cubs_batting.drop_duplicates(subset = "player_id", keep = "first")
reds_batting_unique_id = reds_batting.drop_duplicates(subset = "player_id", keep = "first")
brewers_batting_unique_id = brewers_batting.drop_duplicates(subset = "player_id", keep = "first")
pirates_batting_unique_id = pirates_batting.drop_duplicates(subset = "player_id", keep = "first")
cardinals_batting_unique_id = cardinals_batting.drop_duplicates(subset = "player_id", keep = "first")

diamondbacks_batting_unique_id = diamondbacks_batting.drop_duplicates(subset = "player_id", keep = "first")
rockies_batting_unique_id = rockies_batting.drop_duplicates(subset = "player_id", keep = "first")
dodgers_batting_unique_id = dodgers_batting.drop_duplicates(subset = "player_id", keep = "first")
padres_batting_unique_id = padres_batting.drop_duplicates(subset = "player_id", keep = "first")
giants_batting_unique_id = giants_batting.drop_duplicates(subset = "player_id", keep = "first")




# Post-season batting unique IDs

orioles_batting_post_unique_id = orioles_batting_post.drop_duplicates(subset = "player_id", keep = "first")
red_sox_batting_post_unique_id = red_sox_batting_post.drop_duplicates(subset = "player_id", keep = "first")
yankees_batting_post_unique_id = yankees_batting_post.drop_duplicates(subset = "player_id", keep = "first")
rays_batting_post_unique_id = rays_batting_post.drop_duplicates(subset = "player_id", keep = "first")
blue_jays_batting_post_unique_id = blue_jays_batting_post.drop_duplicates(subset = "player_id", keep = "first")

white_sox_batting_post_unique_id = white_sox_batting_post.drop_duplicates(subset = "player_id", keep = "first")
guardians_batting_post_unique_id = guardians_batting_post.drop_duplicates(subset = "player_id", keep = "first")
tigers_batting_post_unique_id = tigers_batting_post.drop_duplicates(subset = "player_id", keep = "first")
royals_batting_post_unique_id = royals_batting_post.drop_duplicates(subset = "player_id", keep = "first")
twins_batting_post_unique_id = twins_batting_post.drop_duplicates(subset = "player_id", keep = "first")

astros_batting_post_unique_id = astros_batting_post.drop_duplicates(subset = "player_id", keep = "first")
angels_batting_post_unique_id = angels_batting_post.drop_duplicates(subset = "player_id", keep = "first")
athletics_batting_post_unique_id = athletics_batting_post.drop_duplicates(subset = "player_id", keep = "first")
mariners_batting_post_unique_id = mariners_batting_post.drop_duplicates(subset = "player_id", keep = "first")
rangers_batting_post_unique_id = rangers_batting_post.drop_duplicates(subset = "player_id", keep = "first")






braves_batting_post_unique_id = braves_batting_post.drop_duplicates(subset = "player_id", keep = "first")
marlins_batting_post_unique_id = marlins_batting_post.drop_duplicates(subset = "player_id", keep = "first")
mets_batting_post_unique_id = mets_batting_post.drop_duplicates(subset = "player_id", keep = "first")
nationals_batting_post_unique_id = nationals_batting_post.drop_duplicates(subset = "player_id", keep = "first")
phillies_batting_post_unique_id = phillies_batting_post.drop_duplicates(subset = "player_id", keep = "first")

cubs_batting_post_unique_id = cubs_batting_post.drop_duplicates(subset = "player_id", keep = "first")
reds_batting_post_unique_id = reds_batting_post.drop_duplicates(subset = "player_id", keep = "first")
brewers_batting_post_unique_id = brewers_batting_post.drop_duplicates(subset = "player_id", keep = "first")
pirates_batting_post_unique_id = pirates_batting_post.drop_duplicates(subset = "player_id", keep = "first")
cardinals_batting_post_unique_id = cardinals_batting_post.drop_duplicates(subset = "player_id", keep = "first")

diamondbacks_batting_post_unique_id = diamondbacks_batting_post.drop_duplicates(subset = "player_id", keep = "first")
rockies_batting_post_unique_id = rockies_batting_post.drop_duplicates(subset = "player_id", keep = "first")
dodgers_batting_post_unique_id = dodgers_batting_post.drop_duplicates(subset = "player_id", keep = "first")
padres_batting_post_unique_id = padres_batting_post.drop_duplicates(subset = "player_id", keep = "first")
giants_batting_post_unique_id = giants_batting_post.drop_duplicates(subset = "player_id", keep = "first")













# Fielding unique values


orioles_infielding_unique_id = orioles_infielding.drop_duplicates(subset = "player_id", keep = "first")
red_sox_infielding_unique_id = red_sox_infielding.drop_duplicates(subset = "player_id", keep = "first")
yankees_infielding_unique_id = yankees_infielding.drop_duplicates(subset = "player_id", keep = "first")
rays_infielding_unique_id = rays_infielding.drop_duplicates(subset = "player_id", keep = "first")
blue_jays_infielding_unique_id = blue_jays_infielding.drop_duplicates(subset = "player_id", keep = "first")

white_sox_infielding_unique_id = white_sox_infielding.drop_duplicates(subset = "player_id", keep = "first")
guardians_infielding_unique_id = guardians_infielding.drop_duplicates(subset = "player_id", keep = "first")
tigers_infielding_unique_id = tigers_infielding.drop_duplicates(subset = "player_id", keep = "first")
royals_infielding_unique_id = royals_infielding.drop_duplicates(subset = "player_id", keep = "first")
twins_infielding_unique_id = twins_infielding.drop_duplicates(subset = "player_id", keep = "first")

astros_infielding_unique_id = astros_infielding.drop_duplicates(subset = "player_id", keep = "first")
angels_infielding_unique_id = angels_infielding.drop_duplicates(subset = "player_id", keep = "first")
athletics_infielding_unique_id = athletics_infielding.drop_duplicates(subset = "player_id", keep = "first")
mariners_infielding_unique_id = mariners_infielding.drop_duplicates(subset = "player_id", keep = "first")
rangers_infielding_unique_id = rangers_infielding.drop_duplicates(subset = "player_id", keep = "first")






braves_infielding_unique_id = braves_infielding.drop_duplicates(subset = "player_id", keep = "first")
marlins_infielding_unique_id = marlins_infielding.drop_duplicates(subset = "player_id", keep = "first")
mets_infielding_unique_id = mets_infielding.drop_duplicates(subset = "player_id", keep = "first")
nationals_infielding_unique_id = nationals_infielding.drop_duplicates(subset = "player_id", keep = "first")
phillies_infielding_unique_id = phillies_infielding.drop_duplicates(subset = "player_id", keep = "first")

cubs_infielding_unique_id = cubs_infielding.drop_duplicates(subset = "player_id", keep = "first")
reds_infielding_unique_id = reds_infielding.drop_duplicates(subset = "player_id", keep = "first")
brewers_infielding_unique_id = brewers_infielding.drop_duplicates(subset = "player_id", keep = "first")
pirates_infielding_unique_id = pirates_infielding.drop_duplicates(subset = "player_id", keep = "first")
cardinals_infielding_unique_id = cardinals_infielding.drop_duplicates(subset = "player_id", keep = "first")

diamondbacks_infielding_unique_id = diamondbacks_infielding.drop_duplicates(subset = "player_id", keep = "first")
rockies_infielding_unique_id = rockies_infielding.drop_duplicates(subset = "player_id", keep = "first")
dodgers_infielding_unique_id = dodgers_infielding.drop_duplicates(subset = "player_id", keep = "first")
padres_infielding_unique_id = padres_infielding.drop_duplicates(subset = "player_id", keep = "first")
giants_infielding_unique_id = giants_infielding.drop_duplicates(subset = "player_id", keep = "first")











# Post-season fielding unique values

orioles_fielding_post_unique_id = orioles_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
red_sox_fielding_post_unique_id = red_sox_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
yankees_fielding_post_unique_id = yankees_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
rays_fielding_post_unique_id = rays_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
blue_jays_fielding_post_unique_id = blue_jays_fielding_post.drop_duplicates(subset = "player_id", keep = "first")

white_sox_fielding_post_unique_id = white_sox_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
guardians_fielding_post_unique_id = guardians_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
tigers_fielding_post_unique_id = tigers_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
royals_fielding_post_unique_id = royals_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
twins_fielding_post_unique_id = twins_fielding_post.drop_duplicates(subset = "player_id", keep = "first")

astros_fielding_post_unique_id = astros_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
angels_fielding_post_unique_id = angels_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
athletics_fielding_post_unique_id = athletics_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
mariners_fielding_post_unique_id = mariners_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
rangers_fielding_post_unique_id = rangers_fielding_post.drop_duplicates(subset = "player_id", keep = "first")






braves_fielding_post_unique_id = braves_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
marlins_fielding_post_unique_id = marlins_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
mets_fielding_post_unique_id = mets_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
nationals_fielding_post_unique_id = nationals_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
phillies_fielding_post_unique_id = phillies_fielding_post.drop_duplicates(subset = "player_id", keep = "first")

cubs_fielding_post_unique_id = cubs_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
reds_fielding_post_unique_id = reds_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
brewers_fielding_post_unique_id = brewers_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
pirates_fielding_post_unique_id = pirates_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
cardinals_fielding_post_unique_id = cardinals_fielding_post.drop_duplicates(subset = "player_id", keep = "first")

diamondbacks_fielding_post_unique_id = diamondbacks_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
rockies_fielding_post_unique_id = rockies_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
dodgers_fielding_post_unique_id = dodgers_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
padres_fielding_post_unique_id = padres_fielding_post.drop_duplicates(subset = "player_id", keep = "first")
giants_fielding_post_unique_id = giants_fielding_post.drop_duplicates(subset = "player_id", keep = "first")









# Pitching unique values


orioles_pitching_unique_id = orioles_pitching.drop_duplicates(subset = "player_id", keep = "first")
red_sox_pitching_unique_id = red_sox_pitching.drop_duplicates(subset = "player_id", keep = "first")
yankees_pitching_unique_id = yankees_pitching.drop_duplicates(subset = "player_id", keep = "first")
rays_pitching_unique_id = rays_pitching.drop_duplicates(subset = "player_id", keep = "first")
blue_jays_pitching_unique_id = blue_jays_pitching.drop_duplicates(subset = "player_id", keep = "first")

white_sox_pitching_unique_id = white_sox_pitching.drop_duplicates(subset = "player_id", keep = "first")
guardians_pitching_unique_id = guardians_pitching.drop_duplicates(subset = "player_id", keep = "first")
tigers_pitching_unique_id = tigers_pitching.drop_duplicates(subset = "player_id", keep = "first")
royals_pitching_unique_id = royals_pitching.drop_duplicates(subset = "player_id", keep = "first")
twins_pitching_unique_id = twins_pitching.drop_duplicates(subset = "player_id", keep = "first")

astros_pitching_unique_id = astros_pitching.drop_duplicates(subset = "player_id", keep = "first")
angels_pitching_unique_id = angels_pitching.drop_duplicates(subset = "player_id", keep = "first")
athletics_pitching_unique_id = athletics_pitching.drop_duplicates(subset = "player_id", keep = "first")
mariners_pitching_unique_id = mariners_pitching.drop_duplicates(subset = "player_id", keep = "first")
rangers_pitching_unique_id = rangers_pitching.drop_duplicates(subset = "player_id", keep = "first")






braves_pitching_unique_id = braves_pitching.drop_duplicates(subset = "player_id", keep = "first")
marlins_pitching_unique_id = marlins_pitching.drop_duplicates(subset = "player_id", keep = "first")
mets_pitching_unique_id = mets_pitching.drop_duplicates(subset = "player_id", keep = "first")
nationals_pitching_unique_id = nationals_pitching.drop_duplicates(subset = "player_id", keep = "first")
phillies_pitching_unique_id = phillies_pitching.drop_duplicates(subset = "player_id", keep = "first")

cubs_pitching_unique_id = cubs_pitching.drop_duplicates(subset = "player_id", keep = "first")
reds_pitching_unique_id = reds_pitching.drop_duplicates(subset = "player_id", keep = "first")
brewers_pitching_unique_id = brewers_pitching.drop_duplicates(subset = "player_id", keep = "first")
pirates_pitching_unique_id = pirates_pitching.drop_duplicates(subset = "player_id", keep = "first")
cardinals_pitching_unique_id = cardinals_pitching.drop_duplicates(subset = "player_id", keep = "first")

diamondbacks_pitching_unique_id = diamondbacks_pitching.drop_duplicates(subset = "player_id", keep = "first")
rockies_pitching_unique_id = rockies_pitching.drop_duplicates(subset = "player_id", keep = "first")
dodgers_pitching_unique_id = dodgers_pitching.drop_duplicates(subset = "player_id", keep = "first")
padres_pitching_unique_id = padres_pitching.drop_duplicates(subset = "player_id", keep = "first")
giants_pitching_unique_id = giants_pitching.drop_duplicates(subset = "player_id", keep = "first")








# Post-season pitching values


orioles_pitching_post_unique_id = orioles_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
red_sox_pitching_post_unique_id = red_sox_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
yankees_pitching_post_unique_id = yankees_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
rays_pitching_post_unique_id = rays_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
blue_jays_pitching_post_unique_id = blue_jays_pitching_post.drop_duplicates(subset = "player_id", keep = "first")

white_sox_pitching_post_unique_id = white_sox_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
guardians_pitching_post_unique_id = guardians_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
tigers_pitching_post_unique_id = tigers_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
royals_pitching_post_unique_id = royals_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
twins_pitching_post_unique_id = twins_pitching_post.drop_duplicates(subset = "player_id", keep = "first")

astros_pitching_post_unique_id = astros_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
angels_pitching_post_unique_id = angels_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
athletics_pitching_post_unique_id = athletics_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
mariners_pitching_post_unique_id = mariners_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
rangers_pitching_post_unique_id = rangers_pitching_post.drop_duplicates(subset = "player_id", keep = "first")






braves_pitching_post_unique_id = braves_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
marlins_pitching_post_unique_id = marlins_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
mets_pitching_post_unique_id = mets_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
nationals_pitching_post_unique_id = nationals_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
phillies_pitching_post_unique_id = phillies_pitching_post.drop_duplicates(subset = "player_id", keep = "first")

cubs_pitching_post_unique_id = cubs_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
reds_pitching_post_unique_id = reds_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
brewers_pitching_post_unique_id = brewers_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
pirates_pitching_post_unique_id = pirates_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
cardinals_pitching_post_unique_id = cardinals_pitching_post.drop_duplicates(subset = "player_id", keep = "first")

diamondbacks_pitching_post_unique_id = diamondbacks_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
rockies_pitching_post_unique_id = rockies_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
dodgers_pitching_post_unique_id = dodgers_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
padres_pitching_post_unique_id = padres_pitching_post.drop_duplicates(subset = "player_id", keep = "first")
giants_pitching_post_unique_id = giants_pitching_post.drop_duplicates(subset = "player_id", keep = "first")










# all-star unique values


orioles_all_star_unique_id = orioles_all_star.drop_duplicates(subset = "player_id", keep = "first")
red_sox_all_star_unique_id = red_sox_all_star.drop_duplicates(subset = "player_id", keep = "first")
yankees_all_star_unique_id = yankees_all_star.drop_duplicates(subset = "player_id", keep = "first")
rays_all_star_unique_id = rays_all_star.drop_duplicates(subset = "player_id", keep = "first")
blue_jays_all_star_unique_id = blue_jays_all_star.drop_duplicates(subset = "player_id", keep = "first")

white_sox_all_star_unique_id = white_sox_all_star.drop_duplicates(subset = "player_id", keep = "first")
guardians_all_star_unique_id = guardians_all_star.drop_duplicates(subset = "player_id", keep = "first")
tigers_all_star_unique_id = tigers_all_star.drop_duplicates(subset = "player_id", keep = "first")
royals_all_star_unique_id = royals_all_star.drop_duplicates(subset = "player_id", keep = "first")
twins_all_star_unique_id = twins_all_star.drop_duplicates(subset = "player_id", keep = "first")

astros_all_star_unique_id = astros_all_star.drop_duplicates(subset = "player_id", keep = "first")
angels_all_star_unique_id = angels_all_star.drop_duplicates(subset = "player_id", keep = "first")
athletics_all_star_unique_id = athletics_all_star.drop_duplicates(subset = "player_id", keep = "first")
mariners_all_star_unique_id = mariners_all_star.drop_duplicates(subset = "player_id", keep = "first")
rangers_all_star_unique_id = rangers_all_star.drop_duplicates(subset = "player_id", keep = "first")






braves_all_star_unique_id = braves_all_star.drop_duplicates(subset = "player_id", keep = "first")
marlins_all_star_unique_id = marlins_all_star.drop_duplicates(subset = "player_id", keep = "first")
mets_all_star_unique_id = mets_all_star.drop_duplicates(subset = "player_id", keep = "first")
nationals_all_star_unique_id = nationals_all_star.drop_duplicates(subset = "player_id", keep = "first")
phillies_all_star_unique_id = phillies_all_star.drop_duplicates(subset = "player_id", keep = "first")

cubs_all_star_unique_id = cubs_all_star.drop_duplicates(subset = "player_id", keep = "first")
reds_all_star_unique_id = reds_all_star.drop_duplicates(subset = "player_id", keep = "first")
brewers_all_star_unique_id = brewers_all_star.drop_duplicates(subset = "player_id", keep = "first")
pirates_all_star_unique_id = pirates_all_star.drop_duplicates(subset = "player_id", keep = "first")
cardinals_all_star_unique_id = cardinals_all_star.drop_duplicates(subset = "player_id", keep = "first")

diamondbacks_all_star_unique_id = diamondbacks_all_star.drop_duplicates(subset = "player_id", keep = "first")
rockies_all_star_unique_id = rockies_all_star.drop_duplicates(subset = "player_id", keep = "first")
dodgers_all_star_unique_id = dodgers_all_star.drop_duplicates(subset = "player_id", keep = "first")
padres_all_star_unique_id = padres_all_star.drop_duplicates(subset = "player_id", keep = "first")
giants_all_star_unique_id = giants_all_star.drop_duplicates(subset = "player_id", keep = "first")



# Player awards unique ids

orioles_player_awards_unique_id = orioles_player_awards.drop_duplicates(subset = "player_id", keep = "first")
red_sox_player_awards_unique_id = red_sox_player_awards.drop_duplicates(subset = "player_id", keep = "first")
yankees_player_awards_unique_id = yankees_player_awards.drop_duplicates(subset = "player_id", keep = "first")
rays_player_awards_unique_id = rays_player_awards.drop_duplicates(subset = "player_id", keep = "first")
blue_jays_player_awards_unique_id = blue_jays_player_awards.drop_duplicates(subset = "player_id", keep = "first")

white_sox_player_awards_unique_id = white_sox_player_awards.drop_duplicates(subset = "player_id", keep = "first")
guardians_player_awards_unique_id = guardians_player_awards.drop_duplicates(subset = "player_id", keep = "first")
tigers_player_awards_unique_id = tigers_player_awards.drop_duplicates(subset = "player_id", keep = "first")
royals_player_awards_unique_id = royals_player_awards.drop_duplicates(subset = "player_id", keep = "first")
twins_player_awards_unique_id = twins_player_awards.drop_duplicates(subset = "player_id", keep = "first")

astros_player_awards_unique_id = astros_player_awards.drop_duplicates(subset = "player_id", keep = "first")
angels_player_awards_unique_id = angels_player_awards.drop_duplicates(subset = "player_id", keep = "first")
athletics_player_awards_unique_id = athletics_player_awards.drop_duplicates(subset = "player_id", keep = "first")
mariners_player_awards_unique_id = mariners_player_awards.drop_duplicates(subset = "player_id", keep = "first")
rangers_player_awards_unique_id = rangers_player_awards.drop_duplicates(subset = "player_id", keep = "first")






braves_player_awards_unique_id = braves_player_awards.drop_duplicates(subset = "player_id", keep = "first")
marlins_player_awards_unique_id = marlins_player_awards.drop_duplicates(subset = "player_id", keep = "first")
mets_player_awards_unique_id = mets_player_awards.drop_duplicates(subset = "player_id", keep = "first")
nationals_player_awards_unique_id = nationals_player_awards.drop_duplicates(subset = "player_id", keep = "first")
phillies_player_awards_unique_id = phillies_player_awards.drop_duplicates(subset = "player_id", keep = "first")

cubs_player_awards_unique_id = cubs_player_awards.drop_duplicates(subset = "player_id", keep = "first")
reds_player_awards_unique_id = reds_player_awards.drop_duplicates(subset = "player_id", keep = "first")
brewers_player_awards_unique_id = brewers_player_awards.drop_duplicates(subset = "player_id", keep = "first")
pirates_player_awards_unique_id = pirates_player_awards.drop_duplicates(subset = "player_id", keep = "first")
cardinals_player_awards_unique_id = cardinals_player_awards.drop_duplicates(subset = "player_id", keep = "first")

diamondbacks_player_awards_unique_id = diamondbacks_player_awards.drop_duplicates(subset = "player_id", keep = "first")
rockies_player_awards_unique_id = rockies_player_awards.drop_duplicates(subset = "player_id", keep = "first")
dodgers_player_awards_unique_id = dodgers_player_awards.drop_duplicates(subset = "player_id", keep = "first")
padres_player_awards_unique_id = padres_player_awards.drop_duplicates(subset = "player_id", keep = "first")
giants_player_awards_unique_id = giants_player_awards.drop_duplicates(subset = "player_id", keep = "first")







# Fielding positions unique values


orioles_positions_infield_copy_unique_id = orioles_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
red_sox_positions_infield_copy_unique_id = red_sox_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
yankees_positions_infield_copy_unique_id = yankees_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
rays_positions_infield_copy_unique_id = rays_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
blue_jays_positions_infield_copy_unique_id = blue_jays_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")

white_sox_positions_infield_copy_unique_id = white_sox_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
guardians_positions_infield_copy_unique_id = guardians_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
tigers_positions_infield_copy_unique_id = tigers_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
royals_positions_infield_copy_unique_id = royals_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
twins_positions_infield_copy_unique_id = twins_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")

astros_positions_infield_copy_unique_id = astros_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
angels_positions_infield_copy_unique_id = angels_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
athletics_positions_infield_copy_unique_id = athletics_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
mariners_positions_infield_copy_unique_id = mariners_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
rangers_positions_infield_copy_unique_id = rangers_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")






braves_positions_infield_copy_unique_id = braves_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
marlins_positions_infield_copy_unique_id = marlins_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
mets_positions_infield_copy_unique_id = mets_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
nationals_positions_infield_copy_unique_id = nationals_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
phillies_positions_infield_copy_unique_id = phillies_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")

cubs_positions_infield_copy_unique_id = cubs_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
reds_positions_infield_copy_unique_id = reds_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
brewers_positions_infield_copy_unique_id = brewers_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
pirates_positions_infield_copy_unique_id = pirates_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
cardinals_positions_infield_copy_unique_id = cardinals_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")

diamondbacks_positions_infield_copy_unique_id = diamondbacks_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
rockies_positions_infield_copy_unique_id = rockies_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
dodgers_positions_infield_copy_unique_id = dodgers_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
padres_positions_infield_copy_unique_id = padres_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")
giants_positions_infield_copy_unique_id = giants_positions_infield_copy.drop_duplicates(subset = "player_id", keep = "first")









# Merging EVERYTHING MUAHAHAHAHHAHAHAHHA

orioles_batting_selected_columns = orioles_batting_unique_id[["player_id", "Combined_Total_Points"]]
orioles_batting_post_selected_columns = orioles_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
orioles_infielding_selected_columns = orioles_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
orioles_fielding_post_selected_columns = orioles_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
orioles_pitching_selected_columns = orioles_pitching_unique_id[["player_id", "Combined_Total_Points"]]
orioles_pitching_post_selected_columns = orioles_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
orioles_all_star_selected_columns = orioles_all_star_unique_id[["player_id", "Combined_Total_Points"]]
orioles_player_awards_selected_columns = orioles_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
orioles_positions_infield_copy_selected_columns = orioles_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
orioles_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]

red_sox_batting_selected_columns = red_sox_batting_unique_id[["player_id", "Combined_Total_Points"]]
red_sox_batting_post_selected_columns = red_sox_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
red_sox_infielding_selected_columns = red_sox_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
red_sox_fielding_post_selected_columns = red_sox_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
red_sox_pitching_selected_columns = red_sox_pitching_unique_id[["player_id", "Combined_Total_Points"]]
red_sox_pitching_post_selected_columns = red_sox_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
red_sox_all_star_selected_columns = red_sox_all_star_unique_id[["player_id", "Combined_Total_Points"]]
red_sox_player_awards_selected_columns = red_sox_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
red_sox_positions_infield_copy_selected_columns = red_sox_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
red_sox_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]

yankees_batting_selected_columns = yankees_batting_unique_id[["player_id", "Combined_Total_Points"]]
yankees_batting_post_selected_columns = yankees_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
yankees_infielding_selected_columns = yankees_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
yankees_fielding_post_selected_columns = yankees_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
yankees_pitching_selected_columns = yankees_pitching_unique_id[["player_id", "Combined_Total_Points"]]
yankees_pitching_post_selected_columns = yankees_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
yankees_all_star_selected_columns = yankees_all_star_unique_id[["player_id", "Combined_Total_Points"]]
yankees_player_awards_selected_columns = yankees_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
yankees_positions_infield_copy_selected_columns = yankees_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
yankees_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]

rays_batting_selected_columns = rays_batting_unique_id[["player_id", "Combined_Total_Points"]]
rays_batting_post_selected_columns = rays_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
rays_infielding_selected_columns = rays_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
rays_fielding_post_selected_columns = rays_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
rays_pitching_selected_columns = rays_pitching_unique_id[["player_id", "Combined_Total_Points"]]
rays_pitching_post_selected_columns = rays_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
rays_all_star_selected_columns = rays_all_star_unique_id[["player_id", "Combined_Total_Points"]]
rays_player_awards_selected_columns = rays_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
rays_positions_infield_copy_selected_columns = rays_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
rays_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]

blue_jays_batting_selected_columns = blue_jays_batting_unique_id[["player_id", "Combined_Total_Points"]]
blue_jays_batting_post_selected_columns = blue_jays_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
blue_jays_infielding_selected_columns = blue_jays_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
blue_jays_fielding_post_selected_columns = blue_jays_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
blue_jays_pitching_selected_columns = blue_jays_pitching_unique_id[["player_id", "Combined_Total_Points"]]
blue_jays_pitching_post_selected_columns = blue_jays_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
blue_jays_all_star_selected_columns = blue_jays_all_star_unique_id[["player_id", "Combined_Total_Points"]]
blue_jays_player_awards_selected_columns = blue_jays_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
blue_jays_positions_infield_copy_selected_columns = blue_jays_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
blue_jays_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]




white_sox_batting_selected_columns = white_sox_batting_unique_id[["player_id", "Combined_Total_Points"]]
white_sox_batting_post_selected_columns = white_sox_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
white_sox_infielding_selected_columns = white_sox_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
white_sox_fielding_post_selected_columns = white_sox_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
white_sox_pitching_selected_columns = white_sox_pitching_unique_id[["player_id", "Combined_Total_Points"]]
white_sox_pitching_post_selected_columns = white_sox_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
white_sox_all_star_selected_columns = white_sox_all_star_unique_id[["player_id", "Combined_Total_Points"]]
white_sox_player_awards_selected_columns = white_sox_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
white_sox_positions_infield_copy_selected_columns = white_sox_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
white_sox_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


guardians_batting_selected_columns = guardians_batting_unique_id[["player_id", "Combined_Total_Points"]]
guardians_batting_post_selected_columns = guardians_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
guardians_infielding_selected_columns = guardians_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
guardians_fielding_post_selected_columns = guardians_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
guardians_pitching_selected_columns = guardians_pitching_unique_id[["player_id", "Combined_Total_Points"]]
guardians_pitching_post_selected_columns = guardians_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
guardians_all_star_selected_columns = guardians_all_star_unique_id[["player_id", "Combined_Total_Points"]]
guardians_player_awards_selected_columns = guardians_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
guardians_positions_infield_copy_selected_columns = guardians_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
guardians_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


tigers_batting_selected_columns = tigers_batting_unique_id[["player_id", "Combined_Total_Points"]]
tigers_batting_post_selected_columns = tigers_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
tigers_infielding_selected_columns = tigers_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
tigers_fielding_post_selected_columns = tigers_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
tigers_pitching_selected_columns = tigers_pitching_unique_id[["player_id", "Combined_Total_Points"]]
tigers_pitching_post_selected_columns = tigers_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
tigers_all_star_selected_columns = tigers_all_star_unique_id[["player_id", "Combined_Total_Points"]]
tigers_player_awards_selected_columns = tigers_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
tigers_positions_infield_copy_selected_columns = tigers_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
tigers_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


royals_batting_selected_columns = royals_batting_unique_id[["player_id", "Combined_Total_Points"]]
royals_batting_post_selected_columns = royals_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
royals_infielding_selected_columns = royals_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
royals_fielding_post_selected_columns = royals_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
royals_pitching_selected_columns = royals_pitching_unique_id[["player_id", "Combined_Total_Points"]]
royals_pitching_post_selected_columns = royals_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
royals_all_star_selected_columns = royals_all_star_unique_id[["player_id", "Combined_Total_Points"]]
royals_player_awards_selected_columns = royals_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
royals_positions_infield_copy_selected_columns = royals_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
royals_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


twins_batting_selected_columns = twins_batting_unique_id[["player_id", "Combined_Total_Points"]]
twins_batting_post_selected_columns = twins_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
twins_infielding_selected_columns = twins_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
twins_fielding_post_selected_columns = twins_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
twins_pitching_selected_columns = twins_pitching_unique_id[["player_id", "Combined_Total_Points"]]
twins_pitching_post_selected_columns = twins_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
twins_all_star_selected_columns = twins_all_star_unique_id[["player_id", "Combined_Total_Points"]]
twins_player_awards_selected_columns = twins_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
twins_positions_infield_copy_selected_columns = twins_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
twins_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]







astros_batting_selected_columns = astros_batting_unique_id[["player_id", "Combined_Total_Points"]]
astros_batting_post_selected_columns = astros_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
astros_infielding_selected_columns = astros_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
astros_fielding_post_selected_columns = astros_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
astros_pitching_selected_columns = astros_pitching_unique_id[["player_id", "Combined_Total_Points"]]
astros_pitching_post_selected_columns = astros_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
astros_all_star_selected_columns = astros_all_star_unique_id[["player_id", "Combined_Total_Points"]]
astros_player_awards_selected_columns = astros_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
astros_positions_infield_copy_selected_columns = astros_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
astros_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


angels_batting_selected_columns = angels_batting_unique_id[["player_id", "Combined_Total_Points"]]
angels_batting_post_selected_columns = angels_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
angels_infielding_selected_columns = angels_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
angels_fielding_post_selected_columns = angels_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
angels_pitching_selected_columns = angels_pitching_unique_id[["player_id", "Combined_Total_Points"]]
angels_pitching_post_selected_columns = angels_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
angels_all_star_selected_columns = angels_all_star_unique_id[["player_id", "Combined_Total_Points"]]
angels_player_awards_selected_columns = angels_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
angels_positions_infield_copy_selected_columns = angels_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
angels_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


athletics_batting_selected_columns = athletics_batting_unique_id[["player_id", "Combined_Total_Points"]]
athletics_batting_post_selected_columns = athletics_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
athletics_infielding_selected_columns = athletics_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
athletics_fielding_post_selected_columns = athletics_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
athletics_pitching_selected_columns = athletics_pitching_unique_id[["player_id", "Combined_Total_Points"]]
athletics_pitching_post_selected_columns = athletics_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
athletics_all_star_selected_columns = athletics_all_star_unique_id[["player_id", "Combined_Total_Points"]]
athletics_player_awards_selected_columns = athletics_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
athletics_positions_infield_copy_selected_columns = athletics_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
athletics_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


mariners_batting_selected_columns = mariners_batting_unique_id[["player_id", "Combined_Total_Points"]]
mariners_batting_post_selected_columns = mariners_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
mariners_infielding_selected_columns = mariners_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
mariners_fielding_post_selected_columns = mariners_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
mariners_pitching_selected_columns = mariners_pitching_unique_id[["player_id", "Combined_Total_Points"]]
mariners_pitching_post_selected_columns = mariners_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
mariners_all_star_selected_columns = mariners_all_star_unique_id[["player_id", "Combined_Total_Points"]]
mariners_player_awards_selected_columns = mariners_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
mariners_positions_infield_copy_selected_columns = mariners_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
mariners_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


rangers_batting_selected_columns = rangers_batting_unique_id[["player_id", "Combined_Total_Points"]]
rangers_batting_post_selected_columns = rangers_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
rangers_infielding_selected_columns = rangers_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
rangers_fielding_post_selected_columns = rangers_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
rangers_pitching_selected_columns = rangers_pitching_unique_id[["player_id", "Combined_Total_Points"]]
rangers_pitching_post_selected_columns = rangers_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
rangers_all_star_selected_columns = rangers_all_star_unique_id[["player_id", "Combined_Total_Points"]]
rangers_player_awards_selected_columns = rangers_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
rangers_positions_infield_copy_selected_columns = rangers_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
rangers_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]















braves_batting_selected_columns = braves_batting_unique_id[["player_id", "Combined_Total_Points"]]
braves_batting_post_selected_columns = braves_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
braves_infielding_selected_columns = braves_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
braves_fielding_post_selected_columns = braves_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
braves_pitching_selected_columns = braves_pitching_unique_id[["player_id", "Combined_Total_Points"]]
braves_pitching_post_selected_columns = braves_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
braves_all_star_selected_columns = braves_all_star_unique_id[["player_id", "Combined_Total_Points"]]
braves_player_awards_selected_columns = braves_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
braves_positions_infield_copy_selected_columns = braves_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
braves_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


marlins_batting_selected_columns = marlins_batting_unique_id[["player_id", "Combined_Total_Points"]]
marlins_batting_post_selected_columns = marlins_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
marlins_infielding_selected_columns = marlins_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
marlins_fielding_post_selected_columns = marlins_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
marlins_pitching_selected_columns = marlins_pitching_unique_id[["player_id", "Combined_Total_Points"]]
marlins_pitching_post_selected_columns = marlins_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
marlins_all_star_selected_columns = marlins_all_star_unique_id[["player_id", "Combined_Total_Points"]]
marlins_player_awards_selected_columns = marlins_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
marlins_positions_infield_copy_selected_columns = marlins_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
marlins_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


mets_batting_selected_columns = mets_batting_unique_id[["player_id", "Combined_Total_Points"]]
mets_batting_post_selected_columns = mets_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
mets_infielding_selected_columns = mets_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
mets_fielding_post_selected_columns = mets_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
mets_pitching_selected_columns = mets_pitching_unique_id[["player_id", "Combined_Total_Points"]]
mets_pitching_post_selected_columns = mets_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
mets_all_star_selected_columns = mets_all_star_unique_id[["player_id", "Combined_Total_Points"]]
mets_player_awards_selected_columns = mets_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
mets_positions_infield_copy_selected_columns = mets_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
mets_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


nationals_batting_selected_columns = nationals_batting_unique_id[["player_id", "Combined_Total_Points"]]
nationals_batting_post_selected_columns = nationals_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
nationals_infielding_selected_columns = nationals_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
nationals_fielding_post_selected_columns = nationals_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
nationals_pitching_selected_columns = nationals_pitching_unique_id[["player_id", "Combined_Total_Points"]]
nationals_pitching_post_selected_columns = nationals_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
nationals_all_star_selected_columns = nationals_all_star_unique_id[["player_id", "Combined_Total_Points"]]
nationals_player_awards_selected_columns = nationals_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
nationals_positions_infield_copy_selected_columns = nationals_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
nationals_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


phillies_batting_selected_columns = phillies_batting_unique_id[["player_id", "Combined_Total_Points"]]
phillies_batting_post_selected_columns = phillies_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
phillies_infielding_selected_columns = phillies_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
phillies_fielding_post_selected_columns = phillies_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
phillies_pitching_selected_columns = phillies_pitching_unique_id[["player_id", "Combined_Total_Points"]]
phillies_pitching_post_selected_columns = phillies_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
phillies_all_star_selected_columns = phillies_all_star_unique_id[["player_id", "Combined_Total_Points"]]
phillies_player_awards_selected_columns = phillies_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
phillies_positions_infield_copy_selected_columns = phillies_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
phillies_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]









cubs_batting_selected_columns = cubs_batting_unique_id[["player_id", "Combined_Total_Points"]]
cubs_batting_post_selected_columns = cubs_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
cubs_infielding_selected_columns = cubs_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
cubs_fielding_post_selected_columns = cubs_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
cubs_pitching_selected_columns = cubs_pitching_unique_id[["player_id", "Combined_Total_Points"]]
cubs_pitching_post_selected_columns = cubs_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
cubs_all_star_selected_columns = cubs_all_star_unique_id[["player_id", "Combined_Total_Points"]]
cubs_player_awards_selected_columns = cubs_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
cubs_positions_infield_copy_selected_columns = cubs_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
cubs_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


reds_batting_selected_columns = reds_batting_unique_id[["player_id", "Combined_Total_Points"]]
reds_batting_post_selected_columns = reds_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
reds_infielding_selected_columns = reds_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
reds_fielding_post_selected_columns = reds_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
reds_pitching_selected_columns = reds_pitching_unique_id[["player_id", "Combined_Total_Points"]]
reds_pitching_post_selected_columns = reds_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
reds_all_star_selected_columns = reds_all_star_unique_id[["player_id", "Combined_Total_Points"]]
reds_player_awards_selected_columns = reds_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
reds_positions_infield_copy_selected_columns = reds_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
reds_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


brewers_batting_selected_columns = brewers_batting_unique_id[["player_id", "Combined_Total_Points"]]
brewers_batting_post_selected_columns = brewers_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
brewers_infielding_selected_columns = brewers_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
brewers_fielding_post_selected_columns = brewers_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
brewers_pitching_selected_columns = brewers_pitching_unique_id[["player_id", "Combined_Total_Points"]]
brewers_pitching_post_selected_columns = brewers_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
brewers_all_star_selected_columns = brewers_all_star_unique_id[["player_id", "Combined_Total_Points"]]
brewers_player_awards_selected_columns = brewers_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
brewers_positions_infield_copy_selected_columns = brewers_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
brewers_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


pirates_batting_selected_columns = pirates_batting_unique_id[["player_id", "Combined_Total_Points"]]
pirates_batting_post_selected_columns = pirates_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
pirates_infielding_selected_columns = pirates_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
pirates_fielding_post_selected_columns = pirates_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
pirates_pitching_selected_columns = pirates_pitching_unique_id[["player_id", "Combined_Total_Points"]]
pirates_pitching_post_selected_columns = pirates_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
pirates_all_star_selected_columns = pirates_all_star_unique_id[["player_id", "Combined_Total_Points"]]
pirates_player_awards_selected_columns = pirates_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
pirates_positions_infield_copy_selected_columns = pirates_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
pirates_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


cardinals_batting_selected_columns = cardinals_batting_unique_id[["player_id", "Combined_Total_Points"]]
cardinals_batting_post_selected_columns = cardinals_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
cardinals_infielding_selected_columns = cardinals_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
cardinals_fielding_post_selected_columns = cardinals_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
cardinals_pitching_selected_columns = cardinals_pitching_unique_id[["player_id", "Combined_Total_Points"]]
cardinals_pitching_post_selected_columns = cardinals_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
cardinals_all_star_selected_columns = cardinals_all_star_unique_id[["player_id", "Combined_Total_Points"]]
cardinals_player_awards_selected_columns = cardinals_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
cardinals_positions_infield_copy_selected_columns = cardinals_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
cardinals_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]









diamondbacks_batting_selected_columns = diamondbacks_batting_unique_id[["player_id", "Combined_Total_Points"]]
diamondbacks_batting_post_selected_columns = diamondbacks_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
diamondbacks_infielding_selected_columns = diamondbacks_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
diamondbacks_fielding_post_selected_columns = diamondbacks_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
diamondbacks_pitching_selected_columns = diamondbacks_pitching_unique_id[["player_id", "Combined_Total_Points"]]
diamondbacks_pitching_post_selected_columns = diamondbacks_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
diamondbacks_all_star_selected_columns = diamondbacks_all_star_unique_id[["player_id", "Combined_Total_Points"]]
diamondbacks_player_awards_selected_columns = diamondbacks_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
diamondbacks_positions_infield_copy_selected_columns = diamondbacks_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
diamondbacks_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


rockies_batting_selected_columns = rockies_batting_unique_id[["player_id", "Combined_Total_Points"]]
rockies_batting_post_selected_columns = rockies_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
rockies_infielding_selected_columns = rockies_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
rockies_fielding_post_selected_columns = rockies_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
rockies_pitching_selected_columns = rockies_pitching_unique_id[["player_id", "Combined_Total_Points"]]
rockies_pitching_post_selected_columns = rockies_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
rockies_all_star_selected_columns = rockies_all_star_unique_id[["player_id", "Combined_Total_Points"]]
rockies_player_awards_selected_columns = rockies_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
rockies_positions_infield_copy_selected_columns = rockies_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
rockies_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


dodgers_batting_selected_columns = dodgers_batting_unique_id[["player_id", "Combined_Total_Points"]]
dodgers_batting_post_selected_columns = dodgers_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
dodgers_infielding_selected_columns = dodgers_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
dodgers_fielding_post_selected_columns = dodgers_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
dodgers_pitching_selected_columns = dodgers_pitching_unique_id[["player_id", "Combined_Total_Points"]]
dodgers_pitching_post_selected_columns = dodgers_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
dodgers_all_star_selected_columns = dodgers_all_star_unique_id[["player_id", "Combined_Total_Points"]]
dodgers_player_awards_selected_columns = dodgers_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
dodgers_positions_infield_copy_selected_columns = dodgers_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
dodgers_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


padres_batting_selected_columns = padres_batting_unique_id[["player_id", "Combined_Total_Points"]]
padres_batting_post_selected_columns = padres_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
padres_infielding_selected_columns = padres_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
padres_fielding_post_selected_columns = padres_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
padres_pitching_selected_columns = padres_pitching_unique_id[["player_id", "Combined_Total_Points"]]
padres_pitching_post_selected_columns = padres_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
padres_all_star_selected_columns = padres_all_star_unique_id[["player_id", "Combined_Total_Points"]]
padres_player_awards_selected_columns = padres_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
padres_positions_infield_copy_selected_columns = padres_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
padres_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]


giants_batting_selected_columns = giants_batting_unique_id[["player_id", "Combined_Total_Points"]]
giants_batting_post_selected_columns = giants_batting_post_unique_id[["player_id", "Combined_Total_Points"]]
giants_infielding_selected_columns = giants_infielding_unique_id[["player_id", "Combined_Total_Points", "year"]]
giants_fielding_post_selected_columns = giants_fielding_post_unique_id[["player_id", "Combined_Total_Points"]]
giants_pitching_selected_columns = giants_pitching_unique_id[["player_id", "Combined_Total_Points"]]
giants_pitching_post_selected_columns = giants_pitching_post_unique_id[["player_id", "Combined_Total_Points"]]
giants_all_star_selected_columns = giants_all_star_unique_id[["player_id", "Combined_Total_Points"]]
giants_player_awards_selected_columns = giants_player_awards_unique_id[["player_id", "Combined_Total_Points"]]
giants_positions_infield_copy_selected_columns = giants_positions_infield_copy_unique_id[["player_id", "pos", "year"]]
giants_player_data_selected_columns = player_data[["player_id", "name_last", "name_first"]]




# impossible to merge onto player information since it does not have team data,
# merge with fielding data since it has posiitons

pd.set_option('display.max_columns', None)  # Display all columns


orioles_positions_player_merge = pd.merge(orioles_positions_infield_copy_selected_columns, orioles_player_data_selected_columns, on = "player_id", how = "left")
orioles_positions_player_batting_merge = pd.merge(orioles_positions_player_merge, orioles_batting_selected_columns, on = "player_id", how = "left")
orioles_positions_player_batting_batpost_merge = pd.merge(orioles_positions_player_batting_merge, orioles_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
orioles_positions_player_batting_batpost_infielding_merge = pd.merge(orioles_positions_player_batting_batpost_merge, orioles_infielding_selected_columns, on = "player_id", how = "left")
orioles_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(orioles_positions_player_batting_batpost_infielding_merge, orioles_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
orioles_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(orioles_positions_player_batting_batpost_infielding_fieldpost_merge, orioles_pitching_selected_columns, on = "player_id", how = "left")
orioles_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(orioles_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, orioles_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
orioles_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(orioles_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, orioles_all_star_selected_columns, on = "player_id", how = "left")
orioles_everything = pd.merge(orioles_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, orioles_player_awards_selected_columns, on = ["player_id"], how = "left", suffixes = ("_all_stars", "_player_awards"))
orioles_everything.fillna(0, inplace=True)
orioles_everything["Every_Single_Player_Point"] = orioles_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
orioles_max_rows_per_position = orioles_everything.loc[orioles_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
orioles_max_rows_per_position = orioles_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
orioles_everything['Every_Single_Player_Point'] = pd.to_numeric(orioles_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
orioles_of_top5 = orioles_everything[orioles_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
orioles_p_top5 = orioles_everything[orioles_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([orioles_of_top5, orioles_p_top5])

# Drop duplicates based on 'player_id' within orioles_max_rows_per_position
orioles_max_rows_per_position = pd.concat([orioles_max_rows_per_position, top5_combined])
orioles_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = orioles_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = orioles_everything[~orioles_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with orioles_max_rows_per_position
orioles_max_rows_per_position = pd.concat([orioles_max_rows_per_position, top10_remaining_players])

# Reset the index
orioles_max_rows_per_position = orioles_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
orioles_max_rows_per_position['pos'] = orioles_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
baltimore_orioles = orioles_max_rows_per_position['Every_Single_Player_Point'].sum()







red_sox_positions_player_merge = pd.merge(red_sox_positions_infield_copy_selected_columns, red_sox_player_data_selected_columns, on = "player_id", how = "left")
red_sox_positions_player_batting_merge = pd.merge(red_sox_positions_player_merge, red_sox_batting_selected_columns, on = "player_id", how = "left")
red_sox_positions_player_batting_batpost_merge = pd.merge(red_sox_positions_player_batting_merge, red_sox_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
red_sox_positions_player_batting_batpost_infielding_merge = pd.merge(red_sox_positions_player_batting_batpost_merge, red_sox_infielding_selected_columns, on = "player_id", how = "left")
red_sox_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(red_sox_positions_player_batting_batpost_infielding_merge, red_sox_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
red_sox_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(red_sox_positions_player_batting_batpost_infielding_fieldpost_merge, red_sox_pitching_selected_columns, on = "player_id", how = "left")
red_sox_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(red_sox_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, red_sox_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
red_sox_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(red_sox_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, red_sox_all_star_selected_columns, on = "player_id", how = "left")
red_sox_everything = pd.merge(red_sox_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, red_sox_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
red_sox_everything.fillna(0, inplace=True)
red_sox_everything["Every_Single_Player_Point"] = red_sox_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
red_sox_max_rows_per_position = red_sox_everything.loc[red_sox_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
red_sox_max_rows_per_position = red_sox_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
red_sox_everything['Every_Single_Player_Point'] = pd.to_numeric(red_sox_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
red_sox_of_top5 = red_sox_everything[red_sox_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
red_sox_p_top5 = red_sox_everything[red_sox_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([red_sox_of_top5, red_sox_p_top5])

# Drop duplicates based on 'player_id' within red_sox_max_rows_per_position
red_sox_max_rows_per_position = pd.concat([red_sox_max_rows_per_position, top5_combined])
red_sox_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = red_sox_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = red_sox_everything[~red_sox_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with red_sox_max_rows_per_position
red_sox_max_rows_per_position = pd.concat([red_sox_max_rows_per_position, top10_remaining_players])

# Reset the index
red_sox_max_rows_per_position = red_sox_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
red_sox_max_rows_per_position['pos'] = red_sox_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
boston_red_sox = red_sox_max_rows_per_position['Every_Single_Player_Point'].sum()


yankees_positions_player_merge = pd.merge(yankees_positions_infield_copy_selected_columns, yankees_player_data_selected_columns, on = "player_id", how = "left")
yankees_positions_player_batting_merge = pd.merge(yankees_positions_player_merge, yankees_batting_selected_columns, on = "player_id", how = "left")
yankees_positions_player_batting_batpost_merge = pd.merge(yankees_positions_player_batting_merge, yankees_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
yankees_positions_player_batting_batpost_infielding_merge = pd.merge(yankees_positions_player_batting_batpost_merge, yankees_infielding_selected_columns, on = "player_id", how = "left")
yankees_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(yankees_positions_player_batting_batpost_infielding_merge, yankees_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
yankees_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(yankees_positions_player_batting_batpost_infielding_fieldpost_merge, yankees_pitching_selected_columns, on = "player_id", how = "left")
yankees_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(yankees_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, yankees_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
yankees_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(yankees_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, yankees_all_star_selected_columns, on = "player_id", how = "left")
yankees_everything = pd.merge(yankees_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, yankees_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
yankees_everything.fillna(0, inplace=True)
yankees_everything["Every_Single_Player_Point"] = yankees_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
yankees_max_rows_per_position = yankees_everything.loc[yankees_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
yankees_max_rows_per_position = yankees_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
yankees_everything['Every_Single_Player_Point'] = pd.to_numeric(yankees_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
yankees_of_top5 = yankees_everything[yankees_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
yankees_p_top5 = yankees_everything[yankees_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([yankees_of_top5, yankees_p_top5])

# Drop duplicates based on 'player_id' within yankees_max_rows_per_position
yankees_max_rows_per_position = pd.concat([yankees_max_rows_per_position, top5_combined])
yankees_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = yankees_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = yankees_everything[~yankees_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with yankees_max_rows_per_position
yankees_max_rows_per_position = pd.concat([yankees_max_rows_per_position, top10_remaining_players])

# Reset the index
yankees_max_rows_per_position = yankees_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
yankees_max_rows_per_position['pos'] = yankees_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
new_york_yankees = yankees_max_rows_per_position['Every_Single_Player_Point'].sum()


rays_positions_player_merge = pd.merge(rays_positions_infield_copy_selected_columns, rays_player_data_selected_columns, on = "player_id", how = "left")
rays_positions_player_batting_merge = pd.merge(rays_positions_player_merge, rays_batting_selected_columns, on = "player_id", how = "left")
rays_positions_player_batting_batpost_merge = pd.merge(rays_positions_player_batting_merge, rays_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
rays_positions_player_batting_batpost_infielding_merge = pd.merge(rays_positions_player_batting_batpost_merge, rays_infielding_selected_columns, on = "player_id", how = "left")
rays_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(rays_positions_player_batting_batpost_infielding_merge, rays_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
rays_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(rays_positions_player_batting_batpost_infielding_fieldpost_merge, rays_pitching_selected_columns, on = "player_id", how = "left")
rays_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(rays_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, rays_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
rays_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(rays_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, rays_all_star_selected_columns, on = "player_id", how = "left")
rays_everything = pd.merge(rays_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, rays_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
rays_everything.fillna(0, inplace=True)
rays_everything["Every_Single_Player_Point"] = rays_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
rays_max_rows_per_position = rays_everything.loc[rays_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
rays_max_rows_per_position = rays_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
rays_everything['Every_Single_Player_Point'] = pd.to_numeric(rays_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
rays_of_top5 = rays_everything[rays_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
rays_p_top5 = rays_everything[rays_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([rays_of_top5, rays_p_top5])

# Drop duplicates based on 'player_id' within rays_max_rows_per_position
rays_max_rows_per_position = pd.concat([rays_max_rows_per_position, top5_combined])
rays_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = rays_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = rays_everything[~rays_everything['player_id'].isin(already_added_players)]

# Get the top 2 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 2 players with rays_max_rows_per_position
rays_max_rows_per_position = pd.concat([rays_max_rows_per_position, top10_remaining_players])

# Reset the index
rays_max_rows_per_position = rays_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
rays_max_rows_per_position['pos'] = rays_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
tampa_bay_rays = rays_max_rows_per_position['Every_Single_Player_Point'].sum()


blue_jays_positions_player_merge = pd.merge(blue_jays_positions_infield_copy_selected_columns, blue_jays_player_data_selected_columns, on = "player_id", how = "left")
blue_jays_positions_player_batting_merge = pd.merge(blue_jays_positions_player_merge, blue_jays_batting_selected_columns, on = "player_id", how = "left")
blue_jays_positions_player_batting_batpost_merge = pd.merge(blue_jays_positions_player_batting_merge, blue_jays_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
blue_jays_positions_player_batting_batpost_infielding_merge = pd.merge(blue_jays_positions_player_batting_batpost_merge, blue_jays_infielding_selected_columns, on = "player_id", how = "left")
blue_jays_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(blue_jays_positions_player_batting_batpost_infielding_merge, blue_jays_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
blue_jays_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(blue_jays_positions_player_batting_batpost_infielding_fieldpost_merge, blue_jays_pitching_selected_columns, on = "player_id", how = "left")
blue_jays_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(blue_jays_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, blue_jays_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
blue_jays_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(blue_jays_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, blue_jays_all_star_selected_columns, on = "player_id", how = "left")
blue_jays_everything = pd.merge(blue_jays_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, blue_jays_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
blue_jays_everything.fillna(0, inplace=True)
blue_jays_everything["Every_Single_Player_Point"] = blue_jays_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
blue_jays_max_rows_per_position = blue_jays_everything.loc[blue_jays_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
blue_jays_max_rows_per_position = blue_jays_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
blue_jays_everything['Every_Single_Player_Point'] = pd.to_numeric(blue_jays_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
blue_jays_of_top5 = blue_jays_everything[blue_jays_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
blue_jays_p_top5 = blue_jays_everything[blue_jays_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([blue_jays_of_top5, blue_jays_p_top5])

# Drop duplicates based on 'player_id' within blue_jays_max_rows_per_position
blue_jays_max_rows_per_position = pd.concat([blue_jays_max_rows_per_position, top5_combined])
blue_jays_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = blue_jays_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = blue_jays_everything[~blue_jays_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with blue_jays_max_rows_per_position
blue_jays_max_rows_per_position = pd.concat([blue_jays_max_rows_per_position, top10_remaining_players])

# Reset the index
blue_jays_max_rows_per_position = blue_jays_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
blue_jays_max_rows_per_position['pos'] = blue_jays_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
toronto_blue_jays = blue_jays_max_rows_per_position['Every_Single_Player_Point'].sum()






white_sox_positions_player_merge = pd.merge(white_sox_positions_infield_copy_selected_columns, white_sox_player_data_selected_columns, on = "player_id", how = "left")
white_sox_positions_player_batting_merge = pd.merge(white_sox_positions_player_merge, white_sox_batting_selected_columns, on = "player_id", how = "left")
white_sox_positions_player_batting_batpost_merge = pd.merge(white_sox_positions_player_batting_merge, white_sox_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
white_sox_positions_player_batting_batpost_infielding_merge = pd.merge(white_sox_positions_player_batting_batpost_merge, white_sox_infielding_selected_columns, on = "player_id", how = "left")
white_sox_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(white_sox_positions_player_batting_batpost_infielding_merge, white_sox_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
white_sox_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(white_sox_positions_player_batting_batpost_infielding_fieldpost_merge, white_sox_pitching_selected_columns, on = "player_id", how = "left")
white_sox_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(white_sox_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, white_sox_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
white_sox_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(white_sox_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, white_sox_all_star_selected_columns, on = "player_id", how = "left")
white_sox_everything = pd.merge(white_sox_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, white_sox_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
white_sox_everything.fillna(0, inplace=True)
white_sox_everything["Every_Single_Player_Point"] = white_sox_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
white_sox_max_rows_per_position = white_sox_everything.loc[white_sox_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
white_sox_max_rows_per_position = white_sox_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
white_sox_everything['Every_Single_Player_Point'] = pd.to_numeric(white_sox_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
white_sox_of_top5 = white_sox_everything[white_sox_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
white_sox_p_top5 = white_sox_everything[white_sox_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([white_sox_of_top5, white_sox_p_top5])

# Drop duplicates based on 'player_id' within white_sox_max_rows_per_position
white_sox_max_rows_per_position = pd.concat([white_sox_max_rows_per_position, top5_combined])
white_sox_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = white_sox_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = white_sox_everything[~white_sox_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with white_sox_max_rows_per_position
white_sox_max_rows_per_position = pd.concat([white_sox_max_rows_per_position, top10_remaining_players])

# Reset the index
white_sox_max_rows_per_position = white_sox_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
white_sox_max_rows_per_position['pos'] = white_sox_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
chicago_white_sox = white_sox_max_rows_per_position['Every_Single_Player_Point'].sum()


guardians_positions_player_merge = pd.merge(guardians_positions_infield_copy_selected_columns, guardians_player_data_selected_columns, on = "player_id", how = "left")
guardians_positions_player_batting_merge = pd.merge(guardians_positions_player_merge, guardians_batting_selected_columns, on = "player_id", how = "left")
guardians_positions_player_batting_batpost_merge = pd.merge(guardians_positions_player_batting_merge, guardians_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
guardians_positions_player_batting_batpost_infielding_merge = pd.merge(guardians_positions_player_batting_batpost_merge, guardians_infielding_selected_columns, on = "player_id", how = "left")
guardians_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(guardians_positions_player_batting_batpost_infielding_merge, guardians_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
guardians_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(guardians_positions_player_batting_batpost_infielding_fieldpost_merge, guardians_pitching_selected_columns, on = "player_id", how = "left")
guardians_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(guardians_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, guardians_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
guardians_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(guardians_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, guardians_all_star_selected_columns, on = "player_id", how = "left")
guardians_everything = pd.merge(guardians_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, guardians_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
guardians_everything.fillna(0, inplace=True)
guardians_everything["Every_Single_Player_Point"] = guardians_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
guardians_max_rows_per_position = guardians_everything.loc[guardians_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
guardians_max_rows_per_position = guardians_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
guardians_everything['Every_Single_Player_Point'] = pd.to_numeric(guardians_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
guardians_of_top5 = guardians_everything[guardians_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
guardians_p_top5 = guardians_everything[guardians_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([guardians_of_top5, guardians_p_top5])

# Drop duplicates based on 'player_id' within guardians_max_rows_per_position
guardians_max_rows_per_position = pd.concat([guardians_max_rows_per_position, top5_combined])
guardians_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = guardians_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = guardians_everything[~guardians_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with guardians_max_rows_per_position
guardians_max_rows_per_position = pd.concat([guardians_max_rows_per_position, top10_remaining_players])

# Reset the index
guardians_max_rows_per_position = guardians_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
guardians_max_rows_per_position['pos'] = guardians_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
cleveland_guardians = guardians_max_rows_per_position['Every_Single_Player_Point'].sum()


tigers_positions_player_merge = pd.merge(tigers_positions_infield_copy_selected_columns, tigers_player_data_selected_columns, on = "player_id", how = "left")
tigers_positions_player_batting_merge = pd.merge(tigers_positions_player_merge, tigers_batting_selected_columns, on = "player_id", how = "left")
tigers_positions_player_batting_batpost_merge = pd.merge(tigers_positions_player_batting_merge, tigers_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
tigers_positions_player_batting_batpost_infielding_merge = pd.merge(tigers_positions_player_batting_batpost_merge, tigers_infielding_selected_columns, on = "player_id", how = "left")
tigers_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(tigers_positions_player_batting_batpost_infielding_merge, tigers_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
tigers_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(tigers_positions_player_batting_batpost_infielding_fieldpost_merge, tigers_pitching_selected_columns, on = "player_id", how = "left")
tigers_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(tigers_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, tigers_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
tigers_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(tigers_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, tigers_all_star_selected_columns, on = "player_id", how = "left")
tigers_everything = pd.merge(tigers_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, tigers_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
tigers_everything.fillna(0, inplace=True)
tigers_everything["Every_Single_Player_Point"] = tigers_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
tigers_max_rows_per_position = tigers_everything.loc[tigers_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
tigers_max_rows_per_position = tigers_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
tigers_everything['Every_Single_Player_Point'] = pd.to_numeric(tigers_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
tigers_of_top5 = tigers_everything[tigers_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
tigers_p_top5 = tigers_everything[tigers_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([tigers_of_top5, tigers_p_top5])

# Drop duplicates based on 'player_id' within tigers_max_rows_per_position
tigers_max_rows_per_position = pd.concat([tigers_max_rows_per_position, top5_combined])
tigers_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = tigers_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = tigers_everything[~tigers_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with tigers_max_rows_per_position
tigers_max_rows_per_position = pd.concat([tigers_max_rows_per_position, top10_remaining_players])

# Reset the index
tigers_max_rows_per_position = tigers_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
tigers_max_rows_per_position['pos'] = tigers_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
detroit_tigers = tigers_max_rows_per_position['Every_Single_Player_Point'].sum()


royals_positions_player_merge = pd.merge(royals_positions_infield_copy_selected_columns, royals_player_data_selected_columns, on = "player_id", how = "left")
royals_positions_player_batting_merge = pd.merge(royals_positions_player_merge, royals_batting_selected_columns, on = "player_id", how = "left")
royals_positions_player_batting_batpost_merge = pd.merge(royals_positions_player_batting_merge, royals_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
royals_positions_player_batting_batpost_infielding_merge = pd.merge(royals_positions_player_batting_batpost_merge, royals_infielding_selected_columns, on = "player_id", how = "left")
royals_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(royals_positions_player_batting_batpost_infielding_merge, royals_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
royals_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(royals_positions_player_batting_batpost_infielding_fieldpost_merge, royals_pitching_selected_columns, on = "player_id", how = "left")
royals_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(royals_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, royals_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
royals_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(royals_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, royals_all_star_selected_columns, on = "player_id", how = "left")
royals_everything = pd.merge(royals_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, royals_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
royals_everything.fillna(0, inplace=True)
royals_everything["Every_Single_Player_Point"] = royals_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
royals_max_rows_per_position = royals_everything.loc[royals_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
royals_max_rows_per_position = royals_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
royals_everything['Every_Single_Player_Point'] = pd.to_numeric(royals_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
royals_of_top5 = royals_everything[royals_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
royals_p_top5 = royals_everything[royals_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([royals_of_top5, royals_p_top5])

# Drop duplicates based on 'player_id' within royals_max_rows_per_position
royals_max_rows_per_position = pd.concat([royals_max_rows_per_position, top5_combined])
royals_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = royals_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = royals_everything[~royals_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with royals_max_rows_per_position
royals_max_rows_per_position = pd.concat([royals_max_rows_per_position, top10_remaining_players])

# Reset the index
royals_max_rows_per_position = royals_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
royals_max_rows_per_position['pos'] = royals_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
kansas_city_royals = royals_max_rows_per_position['Every_Single_Player_Point'].sum()


twins_positions_player_merge = pd.merge(twins_positions_infield_copy_selected_columns, twins_player_data_selected_columns, on = "player_id", how = "left")
twins_positions_player_batting_merge = pd.merge(twins_positions_player_merge, twins_batting_selected_columns, on = "player_id", how = "left")
twins_positions_player_batting_batpost_merge = pd.merge(twins_positions_player_batting_merge, twins_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
twins_positions_player_batting_batpost_infielding_merge = pd.merge(twins_positions_player_batting_batpost_merge, twins_infielding_selected_columns, on = "player_id", how = "left")
twins_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(twins_positions_player_batting_batpost_infielding_merge, twins_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
twins_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(twins_positions_player_batting_batpost_infielding_fieldpost_merge, twins_pitching_selected_columns, on = "player_id", how = "left")
twins_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(twins_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, twins_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
twins_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(twins_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, twins_all_star_selected_columns, on = "player_id", how = "left")
twins_everything = pd.merge(twins_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, twins_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
twins_everything.fillna(0, inplace=True)
twins_everything["Every_Single_Player_Point"] = twins_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
twins_max_rows_per_position = twins_everything.loc[twins_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
twins_max_rows_per_position = twins_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
twins_everything['Every_Single_Player_Point'] = pd.to_numeric(twins_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
twins_of_top5 = twins_everything[twins_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
twins_p_top5 = twins_everything[twins_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([twins_of_top5, twins_p_top5])

# Drop duplicates based on 'player_id' within twins_max_rows_per_position
twins_max_rows_per_position = pd.concat([twins_max_rows_per_position, top5_combined])
twins_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = twins_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = twins_everything[~twins_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with twins_max_rows_per_position
twins_max_rows_per_position = pd.concat([twins_max_rows_per_position, top10_remaining_players])

# Reset the index
twins_max_rows_per_position = twins_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
twins_max_rows_per_position['pos'] = twins_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
minnesota_twins = twins_max_rows_per_position['Every_Single_Player_Point'].sum()







astros_positions_player_merge = pd.merge(astros_positions_infield_copy_selected_columns, astros_player_data_selected_columns, on = "player_id", how = "left")
astros_positions_player_batting_merge = pd.merge(astros_positions_player_merge, astros_batting_selected_columns, on = "player_id", how = "left")
astros_positions_player_batting_batpost_merge = pd.merge(astros_positions_player_batting_merge, astros_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
astros_positions_player_batting_batpost_infielding_merge = pd.merge(astros_positions_player_batting_batpost_merge, astros_infielding_selected_columns, on = "player_id", how = "left")
astros_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(astros_positions_player_batting_batpost_infielding_merge, astros_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
astros_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(astros_positions_player_batting_batpost_infielding_fieldpost_merge, astros_pitching_selected_columns, on = "player_id", how = "left")
astros_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(astros_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, astros_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
astros_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(astros_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, astros_all_star_selected_columns, on = "player_id", how = "left")
astros_everything = pd.merge(astros_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, astros_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
astros_everything.fillna(0, inplace=True)
astros_everything["Every_Single_Player_Point"] = astros_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
astros_max_rows_per_position = astros_everything.loc[astros_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
astros_max_rows_per_position = astros_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
astros_everything['Every_Single_Player_Point'] = pd.to_numeric(astros_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
astros_of_top5 = astros_everything[astros_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
astros_p_top5 = astros_everything[astros_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([astros_of_top5, astros_p_top5])

# Drop duplicates based on 'player_id' within astros_max_rows_per_position
astros_max_rows_per_position = pd.concat([astros_max_rows_per_position, top5_combined])
astros_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = astros_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = astros_everything[~astros_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with astros_max_rows_per_position
astros_max_rows_per_position = pd.concat([astros_max_rows_per_position, top10_remaining_players])

# Reset the index
astros_max_rows_per_position = astros_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
astros_max_rows_per_position['pos'] = astros_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
houston_astros = astros_max_rows_per_position['Every_Single_Player_Point'].sum()


angels_positions_player_merge = pd.merge(angels_positions_infield_copy_selected_columns, angels_player_data_selected_columns, on = "player_id", how = "left")
angels_positions_player_batting_merge = pd.merge(angels_positions_player_merge, angels_batting_selected_columns, on = "player_id", how = "left")
angels_positions_player_batting_batpost_merge = pd.merge(angels_positions_player_batting_merge, angels_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
angels_positions_player_batting_batpost_infielding_merge = pd.merge(angels_positions_player_batting_batpost_merge, angels_infielding_selected_columns, on = "player_id", how = "left")
angels_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(angels_positions_player_batting_batpost_infielding_merge, angels_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
angels_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(angels_positions_player_batting_batpost_infielding_fieldpost_merge, angels_pitching_selected_columns, on = "player_id", how = "left")
angels_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(angels_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, angels_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
angels_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(angels_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, angels_all_star_selected_columns, on = "player_id", how = "left")
angels_everything = pd.merge(angels_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, angels_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
angels_everything.fillna(0, inplace=True)
angels_everything["Every_Single_Player_Point"] = angels_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
angels_max_rows_per_position = angels_everything.loc[angels_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
angels_max_rows_per_position = angels_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
angels_everything['Every_Single_Player_Point'] = pd.to_numeric(angels_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
angels_of_top5 = angels_everything[angels_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
angels_p_top5 = angels_everything[angels_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([angels_of_top5, angels_p_top5])

# Drop duplicates based on 'player_id' within angels_max_rows_per_position
angels_max_rows_per_position = pd.concat([angels_max_rows_per_position, top5_combined])
angels_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = angels_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = angels_everything[~angels_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with angels_max_rows_per_position
angels_max_rows_per_position = pd.concat([angels_max_rows_per_position, top10_remaining_players])

# Reset the index
angels_max_rows_per_position = angels_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
angels_max_rows_per_position['pos'] = angels_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
los_angeles_angels = angels_max_rows_per_position['Every_Single_Player_Point'].sum()


athletics_positions_player_merge = pd.merge(athletics_positions_infield_copy_selected_columns, athletics_player_data_selected_columns, on = "player_id", how = "left")
athletics_positions_player_batting_merge = pd.merge(athletics_positions_player_merge, athletics_batting_selected_columns, on = "player_id", how = "left")
athletics_positions_player_batting_batpost_merge = pd.merge(athletics_positions_player_batting_merge, athletics_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
athletics_positions_player_batting_batpost_infielding_merge = pd.merge(athletics_positions_player_batting_batpost_merge, athletics_infielding_selected_columns, on = "player_id", how = "left")
athletics_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(athletics_positions_player_batting_batpost_infielding_merge, athletics_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
athletics_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(athletics_positions_player_batting_batpost_infielding_fieldpost_merge, athletics_pitching_selected_columns, on = "player_id", how = "left")
athletics_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(athletics_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, athletics_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
athletics_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(athletics_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, athletics_all_star_selected_columns, on = "player_id", how = "left")
athletics_everything = pd.merge(athletics_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, athletics_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
athletics_everything.fillna(0, inplace=True)
athletics_everything["Every_Single_Player_Point"] = athletics_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
athletics_max_rows_per_position = athletics_everything.loc[athletics_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
athletics_max_rows_per_position = athletics_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
athletics_everything['Every_Single_Player_Point'] = pd.to_numeric(athletics_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
athletics_of_top5 = athletics_everything[athletics_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
athletics_p_top5 = athletics_everything[athletics_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([athletics_of_top5, athletics_p_top5])

# Drop duplicates based on 'player_id' within athletics_max_rows_per_position
athletics_max_rows_per_position = pd.concat([athletics_max_rows_per_position, top5_combined])
athletics_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = athletics_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = athletics_everything[~athletics_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with athletics_max_rows_per_position
athletics_max_rows_per_position = pd.concat([athletics_max_rows_per_position, top10_remaining_players])

# Reset the index
athletics_max_rows_per_position = athletics_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
athletics_max_rows_per_position['pos'] = athletics_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
oakland_athletics = athletics_max_rows_per_position['Every_Single_Player_Point'].sum()


mariners_positions_player_merge = pd.merge(mariners_positions_infield_copy_selected_columns, mariners_player_data_selected_columns, on = "player_id", how = "left")
mariners_positions_player_batting_merge = pd.merge(mariners_positions_player_merge, mariners_batting_selected_columns, on = "player_id", how = "left")
mariners_positions_player_batting_batpost_merge = pd.merge(mariners_positions_player_batting_merge, mariners_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
mariners_positions_player_batting_batpost_infielding_merge = pd.merge(mariners_positions_player_batting_batpost_merge, mariners_infielding_selected_columns, on = "player_id", how = "left")
mariners_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(mariners_positions_player_batting_batpost_infielding_merge, mariners_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
mariners_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(mariners_positions_player_batting_batpost_infielding_fieldpost_merge, mariners_pitching_selected_columns, on = "player_id", how = "left")
mariners_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(mariners_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, mariners_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
mariners_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(mariners_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, mariners_all_star_selected_columns, on = "player_id", how = "left")
mariners_everything = pd.merge(mariners_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, mariners_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
mariners_everything.fillna(0, inplace=True)
mariners_everything["Every_Single_Player_Point"] = mariners_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
mariners_max_rows_per_position = mariners_everything.loc[mariners_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
mariners_max_rows_per_position = mariners_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
mariners_everything['Every_Single_Player_Point'] = pd.to_numeric(mariners_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
mariners_of_top5 = mariners_everything[mariners_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
mariners_p_top5 = mariners_everything[mariners_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([mariners_of_top5, mariners_p_top5])

# Drop duplicates based on 'player_id' within mariners_max_rows_per_position
mariners_max_rows_per_position = pd.concat([mariners_max_rows_per_position, top5_combined])
mariners_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = mariners_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = mariners_everything[~mariners_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with mariners_max_rows_per_position
mariners_max_rows_per_position = pd.concat([mariners_max_rows_per_position, top10_remaining_players])

# Reset the index
mariners_max_rows_per_position = mariners_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
mariners_max_rows_per_position['pos'] = mariners_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
seattle_mariners = mariners_max_rows_per_position['Every_Single_Player_Point'].sum()


rangers_positions_player_merge = pd.merge(rangers_positions_infield_copy_selected_columns, rangers_player_data_selected_columns, on = "player_id", how = "left")
rangers_positions_player_batting_merge = pd.merge(rangers_positions_player_merge, rangers_batting_selected_columns, on = "player_id", how = "left")
rangers_positions_player_batting_batpost_merge = pd.merge(rangers_positions_player_batting_merge, rangers_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
rangers_positions_player_batting_batpost_infielding_merge = pd.merge(rangers_positions_player_batting_batpost_merge, rangers_infielding_selected_columns, on = "player_id", how = "left")
rangers_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(rangers_positions_player_batting_batpost_infielding_merge, rangers_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
rangers_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(rangers_positions_player_batting_batpost_infielding_fieldpost_merge, rangers_pitching_selected_columns, on = "player_id", how = "left")
rangers_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(rangers_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, rangers_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
rangers_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(rangers_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, rangers_all_star_selected_columns, on = "player_id", how = "left")
rangers_everything = pd.merge(rangers_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, rangers_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
rangers_everything.fillna(0, inplace=True)
rangers_everything["Every_Single_Player_Point"] = rangers_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
rangers_max_rows_per_position = rangers_everything.loc[rangers_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
rangers_max_rows_per_position = rangers_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
rangers_everything['Every_Single_Player_Point'] = pd.to_numeric(rangers_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
rangers_of_top5 = rangers_everything[rangers_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
rangers_p_top5 = rangers_everything[rangers_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([rangers_of_top5, rangers_p_top5])

# Drop duplicates based on 'player_id' within rangers_max_rows_per_position
rangers_max_rows_per_position = pd.concat([rangers_max_rows_per_position, top5_combined])
rangers_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = rangers_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = rangers_everything[~rangers_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with rangers_max_rows_per_position
rangers_max_rows_per_position = pd.concat([rangers_max_rows_per_position, top10_remaining_players])

# Reset the index
rangers_max_rows_per_position = rangers_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
rangers_max_rows_per_position['pos'] = rangers_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
texas_rangers = rangers_max_rows_per_position['Every_Single_Player_Point'].sum()










braves_positions_player_merge = pd.merge(braves_positions_infield_copy_selected_columns, braves_player_data_selected_columns, on = "player_id", how = "left")
braves_positions_player_batting_merge = pd.merge(braves_positions_player_merge, braves_batting_selected_columns, on = "player_id", how = "left")
braves_positions_player_batting_batpost_merge = pd.merge(braves_positions_player_batting_merge, braves_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
braves_positions_player_batting_batpost_infielding_merge = pd.merge(braves_positions_player_batting_batpost_merge, braves_infielding_selected_columns, on = "player_id", how = "left")
braves_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(braves_positions_player_batting_batpost_infielding_merge, braves_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
braves_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(braves_positions_player_batting_batpost_infielding_fieldpost_merge, braves_pitching_selected_columns, on = "player_id", how = "left")
braves_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(braves_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, braves_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
braves_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(braves_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, braves_all_star_selected_columns, on = "player_id", how = "left")
braves_everything = pd.merge(braves_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, braves_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
braves_everything.fillna(0, inplace=True)
braves_everything["Every_Single_Player_Point"] = braves_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
braves_max_rows_per_position = braves_everything.loc[braves_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
braves_max_rows_per_position = braves_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
braves_everything['Every_Single_Player_Point'] = pd.to_numeric(braves_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
braves_of_top5 = braves_everything[braves_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
braves_p_top5 = braves_everything[braves_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([braves_of_top5, braves_p_top5])

# Drop duplicates based on 'player_id' within braves_max_rows_per_position
braves_max_rows_per_position = pd.concat([braves_max_rows_per_position, top5_combined])
braves_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = braves_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = braves_everything[~braves_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with braves_max_rows_per_position
braves_max_rows_per_position = pd.concat([braves_max_rows_per_position, top10_remaining_players])

# Reset the index
braves_max_rows_per_position = braves_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
braves_max_rows_per_position['pos'] = braves_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
atlanta_braves = braves_max_rows_per_position['Every_Single_Player_Point'].sum()


marlins_positions_player_merge = pd.merge(marlins_positions_infield_copy_selected_columns, marlins_player_data_selected_columns, on = "player_id", how = "left")
marlins_positions_player_batting_merge = pd.merge(marlins_positions_player_merge, marlins_batting_selected_columns, on = "player_id", how = "left")
marlins_positions_player_batting_batpost_merge = pd.merge(marlins_positions_player_batting_merge, marlins_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
marlins_positions_player_batting_batpost_infielding_merge = pd.merge(marlins_positions_player_batting_batpost_merge, marlins_infielding_selected_columns, on = "player_id", how = "left")
marlins_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(marlins_positions_player_batting_batpost_infielding_merge, marlins_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
marlins_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(marlins_positions_player_batting_batpost_infielding_fieldpost_merge, marlins_pitching_selected_columns, on = "player_id", how = "left")
marlins_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(marlins_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, marlins_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
marlins_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(marlins_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, marlins_all_star_selected_columns, on = "player_id", how = "left")
marlins_everything = pd.merge(marlins_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, marlins_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
marlins_everything.fillna(0, inplace=True)
marlins_everything["Every_Single_Player_Point"] = marlins_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
marlins_max_rows_per_position = marlins_everything.loc[marlins_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
marlins_max_rows_per_position = marlins_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
marlins_everything['Every_Single_Player_Point'] = pd.to_numeric(marlins_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
marlins_of_top5 = marlins_everything[marlins_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
marlins_p_top5 = marlins_everything[marlins_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([marlins_of_top5, marlins_p_top5])

# Drop duplicates based on 'player_id' within marlins_max_rows_per_position
marlins_max_rows_per_position = pd.concat([marlins_max_rows_per_position, top5_combined])
marlins_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = marlins_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = marlins_everything[~marlins_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with marlins_max_rows_per_position
marlins_max_rows_per_position = pd.concat([marlins_max_rows_per_position, top10_remaining_players])

# Reset the index
marlins_max_rows_per_position = marlins_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
marlins_max_rows_per_position['pos'] = marlins_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
miami_marlins = marlins_max_rows_per_position['Every_Single_Player_Point'].sum()


mets_positions_player_merge = pd.merge(mets_positions_infield_copy_selected_columns, mets_player_data_selected_columns, on = "player_id", how = "left")
mets_positions_player_batting_merge = pd.merge(mets_positions_player_merge, mets_batting_selected_columns, on = "player_id", how = "left")
mets_positions_player_batting_batpost_merge = pd.merge(mets_positions_player_batting_merge, mets_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
mets_positions_player_batting_batpost_infielding_merge = pd.merge(mets_positions_player_batting_batpost_merge, mets_infielding_selected_columns, on = "player_id", how = "left")
mets_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(mets_positions_player_batting_batpost_infielding_merge, mets_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
mets_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(mets_positions_player_batting_batpost_infielding_fieldpost_merge, mets_pitching_selected_columns, on = "player_id", how = "left")
mets_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(mets_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, mets_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
mets_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(mets_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, mets_all_star_selected_columns, on = "player_id", how = "left")
mets_everything = pd.merge(mets_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, mets_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
mets_everything.fillna(0, inplace=True)
mets_everything["Every_Single_Player_Point"] = mets_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
mets_max_rows_per_position = mets_everything.loc[mets_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
mets_max_rows_per_position = mets_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
mets_everything['Every_Single_Player_Point'] = pd.to_numeric(mets_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
mets_of_top5 = mets_everything[mets_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
mets_p_top5 = mets_everything[mets_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([mets_of_top5, mets_p_top5])

# Drop duplicates based on 'player_id' within mets_max_rows_per_position
mets_max_rows_per_position = pd.concat([mets_max_rows_per_position, top5_combined])
mets_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = mets_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = mets_everything[~mets_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with mets_max_rows_per_position
mets_max_rows_per_position = pd.concat([mets_max_rows_per_position, top10_remaining_players])

# Reset the index
mets_max_rows_per_position = mets_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
mets_max_rows_per_position['pos'] = mets_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
new_york_mets = mets_max_rows_per_position['Every_Single_Player_Point'].sum()


nationals_positions_player_merge = pd.merge(nationals_positions_infield_copy_selected_columns, nationals_player_data_selected_columns, on = "player_id", how = "left")
nationals_positions_player_batting_merge = pd.merge(nationals_positions_player_merge, nationals_batting_selected_columns, on = "player_id", how = "left")
nationals_positions_player_batting_batpost_merge = pd.merge(nationals_positions_player_batting_merge, nationals_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
nationals_positions_player_batting_batpost_infielding_merge = pd.merge(nationals_positions_player_batting_batpost_merge, nationals_infielding_selected_columns, on = "player_id", how = "left")
nationals_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(nationals_positions_player_batting_batpost_infielding_merge, nationals_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
nationals_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(nationals_positions_player_batting_batpost_infielding_fieldpost_merge, nationals_pitching_selected_columns, on = "player_id", how = "left")
nationals_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(nationals_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, nationals_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
nationals_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(nationals_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, nationals_all_star_selected_columns, on = "player_id", how = "left")
nationals_everything = pd.merge(nationals_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, nationals_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
nationals_everything.fillna(0, inplace=True)
nationals_everything["Every_Single_Player_Point"] = nationals_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
nationals_max_rows_per_position = nationals_everything.loc[nationals_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
nationals_max_rows_per_position = nationals_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
nationals_everything['Every_Single_Player_Point'] = pd.to_numeric(nationals_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
nationals_of_top5 = nationals_everything[nationals_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
nationals_p_top5 = nationals_everything[nationals_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([nationals_of_top5, nationals_p_top5])

# Drop duplicates based on 'player_id' within nationals_max_rows_per_position
nationals_max_rows_per_position = pd.concat([nationals_max_rows_per_position, top5_combined])
nationals_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = nationals_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = nationals_everything[~nationals_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with nationals_max_rows_per_position
nationals_max_rows_per_position = pd.concat([nationals_max_rows_per_position, top10_remaining_players])

# Reset the index
nationals_max_rows_per_position = nationals_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
nationals_max_rows_per_position['pos'] = nationals_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
washington_nationals = nationals_max_rows_per_position['Every_Single_Player_Point'].sum()


phillies_positions_player_merge = pd.merge(phillies_positions_infield_copy_selected_columns, phillies_player_data_selected_columns, on = "player_id", how = "left")
phillies_positions_player_batting_merge = pd.merge(phillies_positions_player_merge, phillies_batting_selected_columns, on = "player_id", how = "left")
phillies_positions_player_batting_batpost_merge = pd.merge(phillies_positions_player_batting_merge, phillies_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
phillies_positions_player_batting_batpost_infielding_merge = pd.merge(phillies_positions_player_batting_batpost_merge, phillies_infielding_selected_columns, on = "player_id", how = "left")
phillies_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(phillies_positions_player_batting_batpost_infielding_merge, phillies_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
phillies_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(phillies_positions_player_batting_batpost_infielding_fieldpost_merge, phillies_pitching_selected_columns, on = "player_id", how = "left")
phillies_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(phillies_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, phillies_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
phillies_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(phillies_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, phillies_all_star_selected_columns, on = "player_id", how = "left")
phillies_everything = pd.merge(phillies_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, phillies_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
phillies_everything.fillna(0, inplace=True)
phillies_everything["Every_Single_Player_Point"] = phillies_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
phillies_max_rows_per_position = phillies_everything.loc[phillies_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
phillies_max_rows_per_position = phillies_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
phillies_everything['Every_Single_Player_Point'] = pd.to_numeric(phillies_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
phillies_of_top5 = phillies_everything[phillies_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
phillies_p_top5 = phillies_everything[phillies_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([phillies_of_top5, phillies_p_top5])

# Drop duplicates based on 'player_id' within phillies_max_rows_per_position
phillies_max_rows_per_position = pd.concat([phillies_max_rows_per_position, top5_combined])
phillies_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = phillies_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = phillies_everything[~phillies_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with phillies_max_rows_per_position
phillies_max_rows_per_position = pd.concat([phillies_max_rows_per_position, top10_remaining_players])

# Reset the index
phillies_max_rows_per_position = phillies_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
phillies_max_rows_per_position['pos'] = phillies_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
philidelphia_phillies = phillies_max_rows_per_position['Every_Single_Player_Point'].sum()




cubs_positions_player_merge = pd.merge(cubs_positions_infield_copy_selected_columns, cubs_player_data_selected_columns, on = "player_id", how = "left")
cubs_positions_player_batting_merge = pd.merge(cubs_positions_player_merge, cubs_batting_selected_columns, on = "player_id", how = "left")
cubs_positions_player_batting_batpost_merge = pd.merge(cubs_positions_player_batting_merge, cubs_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
cubs_positions_player_batting_batpost_infielding_merge = pd.merge(cubs_positions_player_batting_batpost_merge, cubs_infielding_selected_columns, on = "player_id", how = "left")
cubs_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(cubs_positions_player_batting_batpost_infielding_merge, cubs_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
cubs_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(cubs_positions_player_batting_batpost_infielding_fieldpost_merge, cubs_pitching_selected_columns, on = "player_id", how = "left")
cubs_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(cubs_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, cubs_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
cubs_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(cubs_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, cubs_all_star_selected_columns, on = "player_id", how = "left")
cubs_everything = pd.merge(cubs_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, cubs_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
cubs_everything.fillna(0, inplace=True)
cubs_everything["Every_Single_Player_Point"] = cubs_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
cubs_max_rows_per_position = cubs_everything.loc[cubs_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
cubs_max_rows_per_position = cubs_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
cubs_everything['Every_Single_Player_Point'] = pd.to_numeric(cubs_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
cubs_of_top5 = cubs_everything[cubs_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
cubs_p_top5 = cubs_everything[cubs_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([cubs_of_top5, cubs_p_top5])

# Drop duplicates based on 'player_id' within cubs_max_rows_per_position
cubs_max_rows_per_position = pd.concat([cubs_max_rows_per_position, top5_combined])
cubs_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = cubs_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = cubs_everything[~cubs_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with cubs_max_rows_per_position
cubs_max_rows_per_position = pd.concat([cubs_max_rows_per_position, top10_remaining_players])

# Reset the index
cubs_max_rows_per_position = cubs_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
cubs_max_rows_per_position['pos'] = cubs_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
chicago_cubs = cubs_max_rows_per_position['Every_Single_Player_Point'].sum()


reds_positions_player_merge = pd.merge(reds_positions_infield_copy_selected_columns, reds_player_data_selected_columns, on = "player_id", how = "left")
reds_positions_player_batting_merge = pd.merge(reds_positions_player_merge, reds_batting_selected_columns, on = "player_id", how = "left")
reds_positions_player_batting_batpost_merge = pd.merge(reds_positions_player_batting_merge, reds_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
reds_positions_player_batting_batpost_infielding_merge = pd.merge(reds_positions_player_batting_batpost_merge, reds_infielding_selected_columns, on = "player_id", how = "left")
reds_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(reds_positions_player_batting_batpost_infielding_merge, reds_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
reds_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(reds_positions_player_batting_batpost_infielding_fieldpost_merge, reds_pitching_selected_columns, on = "player_id", how = "left")
reds_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(reds_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, reds_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
reds_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(reds_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, reds_all_star_selected_columns, on = "player_id", how = "left")
reds_everything = pd.merge(reds_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, reds_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
reds_everything.fillna(0, inplace=True)
reds_everything["Every_Single_Player_Point"] = reds_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
reds_max_rows_per_position = reds_everything.loc[reds_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
reds_max_rows_per_position = reds_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
reds_everything['Every_Single_Player_Point'] = pd.to_numeric(reds_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
reds_of_top5 = reds_everything[reds_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
reds_p_top5 = reds_everything[reds_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([reds_of_top5, reds_p_top5])

# Drop duplicates based on 'player_id' within reds_max_rows_per_position
reds_max_rows_per_position = pd.concat([reds_max_rows_per_position, top5_combined])
reds_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = reds_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = reds_everything[~reds_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with reds_max_rows_per_position
reds_max_rows_per_position = pd.concat([reds_max_rows_per_position, top10_remaining_players])

# Reset the index
reds_max_rows_per_position = reds_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
reds_max_rows_per_position['pos'] = reds_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
cincinatti_reds = reds_max_rows_per_position['Every_Single_Player_Point'].sum()


brewers_positions_player_merge = pd.merge(brewers_positions_infield_copy_selected_columns, brewers_player_data_selected_columns, on = "player_id", how = "left")
brewers_positions_player_batting_merge = pd.merge(brewers_positions_player_merge, brewers_batting_selected_columns, on = "player_id", how = "left")
brewers_positions_player_batting_batpost_merge = pd.merge(brewers_positions_player_batting_merge, brewers_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
brewers_positions_player_batting_batpost_infielding_merge = pd.merge(brewers_positions_player_batting_batpost_merge, brewers_infielding_selected_columns, on = "player_id", how = "left")
brewers_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(brewers_positions_player_batting_batpost_infielding_merge, brewers_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
brewers_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(brewers_positions_player_batting_batpost_infielding_fieldpost_merge, brewers_pitching_selected_columns, on = "player_id", how = "left")
brewers_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(brewers_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, brewers_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
brewers_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(brewers_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, brewers_all_star_selected_columns, on = "player_id", how = "left")
brewers_everything = pd.merge(brewers_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, brewers_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
brewers_everything.fillna(0, inplace=True)
brewers_everything["Every_Single_Player_Point"] = brewers_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
brewers_max_rows_per_position = brewers_everything.loc[brewers_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
brewers_max_rows_per_position = brewers_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
brewers_everything['Every_Single_Player_Point'] = pd.to_numeric(brewers_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
brewers_of_top5 = brewers_everything[brewers_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
brewers_p_top5 = brewers_everything[brewers_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([brewers_of_top5, brewers_p_top5])

# Drop duplicates based on 'player_id' within brewers_max_rows_per_position
brewers_max_rows_per_position = pd.concat([brewers_max_rows_per_position, top5_combined])
brewers_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = brewers_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = brewers_everything[~brewers_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with brewers_max_rows_per_position
brewers_max_rows_per_position = pd.concat([brewers_max_rows_per_position, top10_remaining_players])

# Reset the index
brewers_max_rows_per_position = brewers_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
brewers_max_rows_per_position['pos'] = brewers_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
milwaukee_brewers = brewers_max_rows_per_position['Every_Single_Player_Point'].sum()


pirates_positions_player_merge = pd.merge(pirates_positions_infield_copy_selected_columns, pirates_player_data_selected_columns, on = "player_id", how = "left")
pirates_positions_player_batting_merge = pd.merge(pirates_positions_player_merge, pirates_batting_selected_columns, on = "player_id", how = "left")
pirates_positions_player_batting_batpost_merge = pd.merge(pirates_positions_player_batting_merge, pirates_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
pirates_positions_player_batting_batpost_infielding_merge = pd.merge(pirates_positions_player_batting_batpost_merge, pirates_infielding_selected_columns, on = "player_id", how = "left")
pirates_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(pirates_positions_player_batting_batpost_infielding_merge, pirates_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
pirates_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(pirates_positions_player_batting_batpost_infielding_fieldpost_merge, pirates_pitching_selected_columns, on = "player_id", how = "left")
pirates_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(pirates_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, pirates_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
pirates_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(pirates_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, pirates_all_star_selected_columns, on = "player_id", how = "left")
pirates_everything = pd.merge(pirates_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, pirates_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
pirates_everything.fillna(0, inplace=True)
pirates_everything["Every_Single_Player_Point"] = pirates_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
pirates_max_rows_per_position = pirates_everything.loc[pirates_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
pirates_max_rows_per_position = pirates_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
pirates_everything['Every_Single_Player_Point'] = pd.to_numeric(pirates_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
pirates_of_top5 = pirates_everything[pirates_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
pirates_p_top5 = pirates_everything[pirates_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([pirates_of_top5, pirates_p_top5])

# Drop duplicates based on 'player_id' within pirates_max_rows_per_position
pirates_max_rows_per_position = pd.concat([pirates_max_rows_per_position, top5_combined])
pirates_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = pirates_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = pirates_everything[~pirates_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with pirates_max_rows_per_position
pirates_max_rows_per_position = pd.concat([pirates_max_rows_per_position, top10_remaining_players])

# Reset the index
pirates_max_rows_per_position = pirates_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
pirates_max_rows_per_position['pos'] = pirates_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
pittsburg_pirates = pirates_max_rows_per_position['Every_Single_Player_Point'].sum()


cardinals_positions_player_merge = pd.merge(cardinals_positions_infield_copy_selected_columns, cardinals_player_data_selected_columns, on = "player_id", how = "left")
cardinals_positions_player_batting_merge = pd.merge(cardinals_positions_player_merge, cardinals_batting_selected_columns, on = "player_id", how = "left")
cardinals_positions_player_batting_batpost_merge = pd.merge(cardinals_positions_player_batting_merge, cardinals_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
cardinals_positions_player_batting_batpost_infielding_merge = pd.merge(cardinals_positions_player_batting_batpost_merge, cardinals_infielding_selected_columns, on = "player_id", how = "left")
cardinals_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(cardinals_positions_player_batting_batpost_infielding_merge, cardinals_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
cardinals_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(cardinals_positions_player_batting_batpost_infielding_fieldpost_merge, cardinals_pitching_selected_columns, on = "player_id", how = "left")
cardinals_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(cardinals_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, cardinals_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
cardinals_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(cardinals_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, cardinals_all_star_selected_columns, on = "player_id", how = "left")
cardinals_everything = pd.merge(cardinals_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, cardinals_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
cardinals_everything.fillna(0, inplace=True)
cardinals_everything["Every_Single_Player_Point"] = cardinals_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
cardinals_max_rows_per_position = cardinals_everything.loc[cardinals_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
cardinals_max_rows_per_position = cardinals_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
cardinals_everything['Every_Single_Player_Point'] = pd.to_numeric(cardinals_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
cardinals_of_top5 = cardinals_everything[cardinals_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
cardinals_p_top5 = cardinals_everything[cardinals_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([cardinals_of_top5, cardinals_p_top5])

# Drop duplicates based on 'player_id' within cardinals_max_rows_per_position
cardinals_max_rows_per_position = pd.concat([cardinals_max_rows_per_position, top5_combined])
cardinals_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = cardinals_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = cardinals_everything[~cardinals_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with cardinals_max_rows_per_position
cardinals_max_rows_per_position = pd.concat([cardinals_max_rows_per_position, top10_remaining_players])

# Reset the index
cardinals_max_rows_per_position = cardinals_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
cardinals_max_rows_per_position['pos'] = cardinals_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
st_louis_cardinals = cardinals_max_rows_per_position['Every_Single_Player_Point'].sum()





diamondbacks_positions_player_merge = pd.merge(diamondbacks_positions_infield_copy_selected_columns, diamondbacks_player_data_selected_columns, on = "player_id", how = "left")
diamondbacks_positions_player_batting_merge = pd.merge(diamondbacks_positions_player_merge, diamondbacks_batting_selected_columns, on = "player_id", how = "left")
diamondbacks_positions_player_batting_batpost_merge = pd.merge(diamondbacks_positions_player_batting_merge, diamondbacks_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
diamondbacks_positions_player_batting_batpost_infielding_merge = pd.merge(diamondbacks_positions_player_batting_batpost_merge, diamondbacks_infielding_selected_columns, on = "player_id", how = "left")
diamondbacks_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(diamondbacks_positions_player_batting_batpost_infielding_merge, diamondbacks_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
diamondbacks_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(diamondbacks_positions_player_batting_batpost_infielding_fieldpost_merge, diamondbacks_pitching_selected_columns, on = "player_id", how = "left")
diamondbacks_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(diamondbacks_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, diamondbacks_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
diamondbacks_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(diamondbacks_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, diamondbacks_all_star_selected_columns, on = "player_id", how = "left")
diamondbacks_everything = pd.merge(diamondbacks_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, diamondbacks_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
diamondbacks_everything.fillna(0, inplace=True)
diamondbacks_everything["Every_Single_Player_Point"] = diamondbacks_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
diamondbacks_max_rows_per_position = diamondbacks_everything.loc[diamondbacks_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
diamondbacks_max_rows_per_position = diamondbacks_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
diamondbacks_everything['Every_Single_Player_Point'] = pd.to_numeric(diamondbacks_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
diamondbacks_of_top5 = diamondbacks_everything[diamondbacks_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
diamondbacks_p_top5 = diamondbacks_everything[diamondbacks_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([diamondbacks_of_top5, diamondbacks_p_top5])

# Drop duplicates based on 'player_id' within diamondbacks_max_rows_per_position
diamondbacks_max_rows_per_position = pd.concat([diamondbacks_max_rows_per_position, top5_combined])
diamondbacks_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = diamondbacks_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = diamondbacks_everything[~diamondbacks_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with diamondbacks_max_rows_per_position
diamondbacks_max_rows_per_position = pd.concat([diamondbacks_max_rows_per_position, top10_remaining_players])

# Reset the index
diamondbacks_max_rows_per_position = diamondbacks_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
diamondbacks_max_rows_per_position['pos'] = diamondbacks_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
arizona_diamondbacks = diamondbacks_max_rows_per_position['Every_Single_Player_Point'].sum()


rockies_positions_player_merge = pd.merge(rockies_positions_infield_copy_selected_columns, rockies_player_data_selected_columns, on = "player_id", how = "left")
rockies_positions_player_batting_merge = pd.merge(rockies_positions_player_merge, rockies_batting_selected_columns, on = "player_id", how = "left")
rockies_positions_player_batting_batpost_merge = pd.merge(rockies_positions_player_batting_merge, rockies_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
rockies_positions_player_batting_batpost_infielding_merge = pd.merge(rockies_positions_player_batting_batpost_merge, rockies_infielding_selected_columns, on = "player_id", how = "left")
rockies_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(rockies_positions_player_batting_batpost_infielding_merge, rockies_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
rockies_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(rockies_positions_player_batting_batpost_infielding_fieldpost_merge, rockies_pitching_selected_columns, on = "player_id", how = "left")
rockies_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(rockies_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, rockies_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
rockies_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(rockies_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, rockies_all_star_selected_columns, on = "player_id", how = "left")
rockies_everything = pd.merge(rockies_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, rockies_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
rockies_everything.fillna(0, inplace=True)
rockies_everything["Every_Single_Player_Point"] = rockies_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
rockies_max_rows_per_position = rockies_everything.loc[rockies_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
rockies_max_rows_per_position = rockies_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
rockies_everything['Every_Single_Player_Point'] = pd.to_numeric(rockies_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
rockies_of_top5 = rockies_everything[rockies_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
rockies_p_top5 = rockies_everything[rockies_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([rockies_of_top5, rockies_p_top5])

# Drop duplicates based on 'player_id' within rockies_max_rows_per_position
rockies_max_rows_per_position = pd.concat([rockies_max_rows_per_position, top5_combined])
rockies_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = rockies_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = rockies_everything[~rockies_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with rockies_max_rows_per_position
rockies_max_rows_per_position = pd.concat([rockies_max_rows_per_position, top10_remaining_players])

# Reset the index
rockies_max_rows_per_position = rockies_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
rockies_max_rows_per_position['pos'] = rockies_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
colorado_rockies = rockies_max_rows_per_position['Every_Single_Player_Point'].sum()


dodgers_positions_player_merge = pd.merge(dodgers_positions_infield_copy_selected_columns, dodgers_player_data_selected_columns, on = "player_id", how = "left")
dodgers_positions_player_batting_merge = pd.merge(dodgers_positions_player_merge, dodgers_batting_selected_columns, on = "player_id", how = "left")
dodgers_positions_player_batting_batpost_merge = pd.merge(dodgers_positions_player_batting_merge, dodgers_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
dodgers_positions_player_batting_batpost_infielding_merge = pd.merge(dodgers_positions_player_batting_batpost_merge, dodgers_infielding_selected_columns, on = "player_id", how = "left")
dodgers_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(dodgers_positions_player_batting_batpost_infielding_merge, dodgers_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
dodgers_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(dodgers_positions_player_batting_batpost_infielding_fieldpost_merge, dodgers_pitching_selected_columns, on = "player_id", how = "left")
dodgers_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(dodgers_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, dodgers_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
dodgers_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(dodgers_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, dodgers_all_star_selected_columns, on = "player_id", how = "left")
dodgers_everything = pd.merge(dodgers_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, dodgers_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
dodgers_everything.fillna(0, inplace=True)
dodgers_everything["Every_Single_Player_Point"] = dodgers_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
dodgers_max_rows_per_position = dodgers_everything.loc[dodgers_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
dodgers_max_rows_per_position = dodgers_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
dodgers_everything['Every_Single_Player_Point'] = pd.to_numeric(dodgers_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
dodgers_of_top5 = dodgers_everything[dodgers_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
dodgers_p_top5 = dodgers_everything[dodgers_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([dodgers_of_top5, dodgers_p_top5])

# Drop duplicates based on 'player_id' within dodgers_max_rows_per_position
dodgers_max_rows_per_position = pd.concat([dodgers_max_rows_per_position, top5_combined])
dodgers_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = dodgers_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = dodgers_everything[~dodgers_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with dodgers_max_rows_per_position
dodgers_max_rows_per_position = pd.concat([dodgers_max_rows_per_position, top10_remaining_players])

# Reset the index
dodgers_max_rows_per_position = dodgers_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
dodgers_max_rows_per_position['pos'] = dodgers_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
los_angeles_dodgers = dodgers_max_rows_per_position['Every_Single_Player_Point'].sum()



padres_positions_player_merge = pd.merge(padres_positions_infield_copy_selected_columns, padres_player_data_selected_columns, on = "player_id", how = "left")
padres_positions_player_batting_merge = pd.merge(padres_positions_player_merge, padres_batting_selected_columns, on = "player_id", how = "left")
padres_positions_player_batting_batpost_merge = pd.merge(padres_positions_player_batting_merge, padres_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
padres_positions_player_batting_batpost_infielding_merge = pd.merge(padres_positions_player_batting_batpost_merge, padres_infielding_selected_columns, on = "player_id", how = "left")
padres_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(padres_positions_player_batting_batpost_infielding_merge, padres_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
padres_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(padres_positions_player_batting_batpost_infielding_fieldpost_merge, padres_pitching_selected_columns, on = "player_id", how = "left")
padres_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(padres_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, padres_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
padres_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(padres_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, padres_all_star_selected_columns, on = "player_id", how = "left")
padres_everything = pd.merge(padres_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, padres_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
padres_everything.fillna(0, inplace=True)
padres_everything["Every_Single_Player_Point"] = padres_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
padres_max_rows_per_position = padres_everything.loc[padres_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
padres_max_rows_per_position = padres_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
padres_everything['Every_Single_Player_Point'] = pd.to_numeric(padres_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
padres_of_top5 = padres_everything[padres_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
padres_p_top5 = padres_everything[padres_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([padres_of_top5, padres_p_top5])

# Drop duplicates based on 'player_id' within padres_max_rows_per_position
padres_max_rows_per_position = pd.concat([padres_max_rows_per_position, top5_combined])
padres_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = padres_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = padres_everything[~padres_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with padres_max_rows_per_position
padres_max_rows_per_position = pd.concat([padres_max_rows_per_position, top10_remaining_players])

# Reset the index
padres_max_rows_per_position = padres_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
padres_max_rows_per_position['pos'] = padres_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team
san_diego_padres = padres_max_rows_per_position['Every_Single_Player_Point'].sum()


giants_positions_player_merge = pd.merge(giants_positions_infield_copy_selected_columns, giants_player_data_selected_columns, on = "player_id", how = "left")
giants_positions_player_batting_merge = pd.merge(giants_positions_player_merge, giants_batting_selected_columns, on = "player_id", how = "left")
giants_positions_player_batting_batpost_merge = pd.merge(giants_positions_player_batting_merge, giants_batting_post_selected_columns, on = "player_id", how = "left", suffixes = ("_batting", "_batting_post"))
giants_positions_player_batting_batpost_infielding_merge = pd.merge(giants_positions_player_batting_batpost_merge, giants_infielding_selected_columns, on = "player_id", how = "left")
giants_positions_player_batting_batpost_infielding_fieldpost_merge = pd.merge(giants_positions_player_batting_batpost_infielding_merge, giants_fielding_post_selected_columns, on = "player_id", how = "left", suffixes = ("_fielding", "_fielding_post"))
giants_positions_player_batting_batpost_infielding_fieldpost_pitching_merge = pd.merge(giants_positions_player_batting_batpost_infielding_fieldpost_merge, giants_pitching_selected_columns, on = "player_id", how = "left")
giants_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge = pd.merge(giants_positions_player_batting_batpost_infielding_fieldpost_pitching_merge, giants_pitching_post_selected_columns, on = "player_id", how = "left", suffixes = ("_pitching", "_pitching_post"))
giants_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge = pd.merge(giants_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_merge, giants_all_star_selected_columns, on = "player_id", how = "left")
giants_everything = pd.merge(giants_positions_player_batting_batpost_infielding_fieldpost_pitching_pitchpost_allstar_merge, giants_player_awards_selected_columns, on = ["player_id" ], how = "left", suffixes = ("_all_stars", "_player_awards"))
giants_everything.fillna(0, inplace=True)
giants_everything["Every_Single_Player_Point"] = giants_everything.iloc[:, -8:].sum(axis=1)

# Group by 'Position' and find the rows with the maximum value in column 'B' for each group
giants_max_rows_per_position = giants_everything.loc[giants_everything.groupby("pos")["Every_Single_Player_Point"].idxmax()]

# Reset index for the new DataFrame
giants_max_rows_per_position = giants_max_rows_per_position.reset_index(drop=True)

# Convert 'Every_Single_Player_Point' to numeric (if it's not already)
giants_everything['Every_Single_Player_Point'] = pd.to_numeric(giants_everything['Every_Single_Player_Point'], errors='coerce')

# Filter for position "OF" and get top 5 rows with highest points
giants_of_top5 = giants_everything[giants_everything['pos'] == 'OF'].nlargest(3, 'Every_Single_Player_Point')

# Filter for position "P" and get top 5 rows with highest points
giants_p_top5 = giants_everything[giants_everything['pos'] == 'P'].nlargest(5, 'Every_Single_Player_Point')

# Concatenate the top 5 rows for each position
top5_combined = pd.concat([giants_of_top5, giants_p_top5])

# Drop duplicates based on 'player_id' within giants_max_rows_per_position
giants_max_rows_per_position = pd.concat([giants_max_rows_per_position, top5_combined])
giants_max_rows_per_position.drop_duplicates(subset=['player_id'], keep='first', inplace=True)

# Identify already added players
already_added_players = giants_max_rows_per_position['player_id']

# Filter remaining players
remaining_players = giants_everything[~giants_everything['player_id'].isin(already_added_players)]

# Get the top 10 remaining players based on total points
top10_remaining_players = remaining_players.nlargest(10, 'Every_Single_Player_Point')

# Concatenate these top 10 players with giants_max_rows_per_position
giants_max_rows_per_position = pd.concat([giants_max_rows_per_position, top10_remaining_players])

# Reset the index
giants_max_rows_per_position = giants_max_rows_per_position.reset_index(drop=True)

# Changing all outfield positions to OF for simplification
giants_max_rows_per_position['pos'] = giants_max_rows_per_position['pos'].replace(['CF', 'LF', 'RF'], 'OF')

# Creating the variable that has all the combined points for the team, naming it the full franchise (current team) name
san_francisco_giants = giants_max_rows_per_position['Every_Single_Player_Point'].sum()





"""
NATIONALS PLAYERS TO ADD:

Daniel Murphy (2016-2018), runner up mvp in 2016 and 2 time all star
Bryce Harper (2016-2018), 3 all stars in that span
Juan Soto (2018-2021), key world series helper
Max Scherzer (2016-2020), 2 cy youngs and world series helper
Stever Strasburg (2016-2019), world series mvp
Ryan Zimmerman (2016-2021), Mr. National
Anthony Rendon (2016-2019), key contributor to world series
Trea Turner (2016-2020), key contributor to world series

"""


"""
THE TOURNEY!!!!! :D

Replace the team names with the actual teams when it comes down to it, 
this is just a placeholder for how I will decide the games
"""
















"""
Example function to caculate game wins in the playoffs, will be modified
in the future to use current teams and their current point sum totals
"""






team_a = pd.DataFrame({'sum_total_points': [500]})
team_b = pd.DataFrame({'sum_total_points': [300]})

def determine_winner_and_scores(team_a_points, team_b_points):
    # Calculating the total points
    total_points = team_a_points + team_b_points
    
    # Generate a random number between 1 and the sum of both point totals
    random_number = np.random.randint(1, total_points + 1)
    
    if random_number <= team_a_points:
        # team_a wins
        winner = 'team_a'
        
        # Generating random scores for b teams in the event of a team a victory
        team_a_score = np.random.randint(1, 12)
        team_b_score = np.random.randint(0, team_a_score)

        # Edgecase for just in case the scores are the same
        if team_a_score == team_b_score: 
            team_b_score = team_b_score - 1

    else:
        # team_b wins
        winner = 'team_b'
        
        # Generating random scores for b teams in the event of a team b victory
        team_b_score = np.random.randint(1, 12)
        team_a_score = np.random.randint(0, team_b_score)
        
        # Edgecase for just in case the scores are the same
        if team_b_score == team_a_score: 
            team_a_score = team_a_score - 1

    return winner, team_a_score, team_b_score

# Getting the sum of total points from both teams
team_a_points = team_a['sum_total_points'].iloc[0]
team_b_points = team_b['sum_total_points'].iloc[0]

# Finding out the winner and each team's scores
winner, team_a_score, team_b_score = determine_winner_and_scores(team_a_points, team_b_points)

# Printing results
print(f"Winner: {winner}")
print(f"Team A Score: {team_a_score}")
print(f"Team B Score: {team_b_score}")



big_winner, nationals_score, astros_score = determine_winner_and_scores(washington_nationals, houston_astros)

# Printing results
print(f"Winner: {big_winner}")
print(f"Team A Score: {nationals_score}")
print(f"Team B Score: {astros_score}")



















































