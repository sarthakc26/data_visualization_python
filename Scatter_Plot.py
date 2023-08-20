
import matplotlib.pyplot as plt 
#stock price range of a week 
ugar_sugar = [530,480,520,460,600]
jyoti_res = [300,280,390,400,450]
avalon = [380,340,400,450,420]
yes_bank = [120,200,250,300,350]

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#days = range(1,5)

plt.scatter(days,ugar_sugar, label = 'Ugar_sugar', color = 'green', marker = 'o')
plt.scatter(days,jyoti_res, label = 'Jyoti_res', color = 'Yellow', marker = 'o')
plt.scatter(days, avalon, label = 'Avalon', color = 'red', marker = 'o')
plt.scatter(days, yes_bank, label = 'Yes_Bank', color = 'orange', marker = 'o')
#label - for representing a box at upper left 
#marker - for getting good view at turning points 

plt.xlabel('Days')
plt.ylabel('Price')
plt.legend(loc = 'upper left')
plt.title('Stock information on daily time-frame ')
plt.ylim(100,600)
#setting limit of x-axis 
plt.grid(True)
plt.show()
