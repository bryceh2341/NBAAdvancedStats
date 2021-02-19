import csv
import matplotlib.pyplot as plt 
import seaborn as sns; sns.set_theme(color_codes=True)
import numpy as np

oppFT = []
opp3 = []
teamDistOff = []
teamSpeedOff = []

#opens CSV file
with open('2019-2020 Opponent General Stats and Distance Tracking.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    for row in csv_reader:
            #skips first line
        if line_count == 0: 
            pass
            line_count += 1
        else:
            #calculates goals scored per game
            oppFT.append(float(row[10]))
            #calculates goals allowed per game
            opp3.append(float(row[28]))
            teamDistOff.append(float(row[23]))
            teamSpeedOff.append(float(row[26]))
    
correlation_matrix = np.corrcoef(teamSpeedOff, oppFT)
correlation_xy = correlation_matrix[0,1]
r_squaredOf = str(round(correlation_xy**2,4))
#creates the plot for offense
ax = sns.regplot(teamSpeedOff, oppFT,  color='fuchsia')
# plotting the points
plt.scatter(teamSpeedOff, oppFT, color='indigo') 
# naming the x axis
plt.xlabel('Average Team Offense Speed\n' + 'R-Squared: ' + r_squaredOf) 
# naming the y axis 
plt.ylabel('Opponent FT%')
# giving a title to my graph 
plt.title('Opponent FT% vs. Average Offensive Player Speed')
# function to show the plot
plt.show()

correlation_matrix1 = np.corrcoef(teamDistOff, oppFT)
correlation_xy1 = correlation_matrix1[0,1]
r_squaredOf1 = str(round(correlation_xy1**2,4))
#creates the plot for offense
ax = sns.regplot(teamDistOff, oppFT,  color='lawngreen')
# plotting the points
plt.scatter(teamDistOff, oppFT, color='darkslategray') 
# naming the x axis
plt.xlabel('Average Team Offense Distance Traveled\n' + 'R-Squared: ' + r_squaredOf1) 
# naming the y axis 
plt.ylabel('Opponent FT%')
# giving a title to my graph 
plt.title('Opponent FT% vs. Average Offensive Player Distance')
# function to show the plot
plt.show()

correlation_matrix2 = np.corrcoef(teamSpeedOff, opp3)
correlation_xy2 = correlation_matrix2[0,1]
r_squaredOf2 = str(round(correlation_xy2**2,4))
#creates the plot for offense
ax = sns.regplot(teamSpeedOff, opp3,  color='cyan')
# plotting the points
plt.scatter(teamSpeedOff, opp3, color='navy') 
# naming the x axis
plt.xlabel('Average Team Offense Speed\n' + 'R-Squared: ' + r_squaredOf2) 
# naming the y axis 
plt.ylabel('Opponent Wid Open 3pt%')
# giving a title to my graph 
plt.title('Opponent Wide Open 3pt% vs. Average Offensive Player Speed')
# function to show the plot
plt.show()

correlation_matrix3 = np.corrcoef(teamDistOff, opp3)
correlation_xy3 = correlation_matrix3[0,1]
r_squaredOf3 = str(round(correlation_xy3**2,4))
#creates the plot for offense
ax = sns.regplot(teamDistOff, opp3,  color='yellow')
# plotting the points
plt.scatter(teamDistOff, opp3, color='darkgoldenrod') 
# naming the x axis
plt.xlabel('Average Team Offense Distance Traveled\n' + 'R-Squared: ' + r_squaredOf3) 
# naming the y axis 
plt.ylabel('Opponent Wide Open 3pt%')
# giving a title to my graph 
plt.title('Opponent Wide Open 3pt% vs. Average Offensive Player Distance')
# function to show the plot
plt.show()
