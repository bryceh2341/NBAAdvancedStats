import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#Open and read my 2021 NBA Draft Big Board
df = pd.read_csv("2021 NBA Draft.csv", encoding= 'unicode_escape')
#List of the items in the radar charts
col_list = ['Player','Scoring %', 'Shot Creation%', 'Shooting%', 'Finishing%', 'Playmaking%', 'Rebounding%', 'Defense%']
#Cutting the dataframe to the relevant information
df = df[col_list]
#Sets the index to the player name
df.set_index('Player', inplace=True)
#List of labels int he radar chart
labels = ['Scoring', 'Shot Creation', 'Shooting', 'Finishing', 'Playmaking', 'Rebounding', 'Defense']
# Number of variables we're plotting.
num_vars = len(labels)

# Split the circle into even parts and save the angles
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

#Complete the circle
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

num_players = int(input("How many prospects would you like to look at (max 4)?: "))
#Function to plot the players
def add_to_radar(playername, color):
  values = df.loc[playername].tolist()
  values += values[:1]
  ax.plot(angles, values, color=color, linewidth=1, label=playername)
  ax.fill(angles, values, color=color, alpha=0.2)
#Plots the players depending on how many 
if num_players == 1:
    player = input("Enter player name: ")
    add_to_radar(player, 'red')
    ax.set_title(player, y=1.08)
if num_players == 2:
    player1 = input("Enter player 1 name: ")
    player2 = input("Enter player 2 name: ")
    add_to_radar(player1, 'red')
    add_to_radar(player2, 'blue')
    ax.set_title(player1+'/'+player2+' Comparison', y=1.08)
if num_players == 3:
    player1 = input("Enter player 1 name: ")
    player2 = input("Enter player 2 name: ")  
    player3 = input("Enter player 3 name: ") 
    add_to_radar(player1, 'red')
    add_to_radar(player2, 'blue')
    add_to_radar(player3, 'green')
    ax.set_title(player1+'/'+player2+'/'+player3+' Comparison', y=1.08)
if num_players == 4:
    player1 = input("Enter player 1 name: ")
    player2 = input("Enter player 2 name: ")  
    player3 = input("Enter player 3 name: ") 
    player4 = input("Enter player 4 name: ") 
    add_to_radar(player1, 'red')
    add_to_radar(player2, 'blue')
    add_to_radar(player3, 'lime')
    add_to_radar(player4, 'yellow')
    ax.set_title(player1+'/'+player2+'/'+player3+'/'+player4+' Comparison', y=1.08)

# Fix axis to go in the right order and start at 12 o'clock.
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Draw axis lines for each angle and label.
ax.set_thetagrids(np.degrees(angles), labels)

# Go through labels and adjust alignment based on where it is in the circle.
for label, angle in zip(ax.get_xticklabels(), angles):
  if angle in (0, np.pi):
    label.set_horizontalalignment('center')
  elif 0 < angle < np.pi:
    label.set_horizontalalignment('left')
  else:
    label.set_horizontalalignment('right')

# Ensure radar goes from 0 to 100.
ax.set_ylim(0, 100)

# Set position of y-labels (0-100) to be in the middle of the first two axes.
ax.set_rlabel_position(180 / num_vars)
# Change the color of the tick labels.
ax.tick_params(colors='#222222')
# Make the y-axis (0-100) labels smaller.
ax.tick_params(axis='y', labelsize=8)
# Change the color of the circular gridlines.
ax.grid(color='#706e6e')
# Change the color of the outermost gridline
ax.spines['polar'].set_color('#222222')
# Change the background color inside the circle itself.
ax.set_facecolor('#b3b1b1')
# Add a legend as well.
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))