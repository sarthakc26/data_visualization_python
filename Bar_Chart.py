
import matplotlib.pyplot as plt 
#stock price range of a week 
ugar_sugar = [530,480,520,460,600]
jyoti_res = [300,280,390,400,450]

#days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
x = range(1,6)

plt.bar([a - 0.25 for a in x ],ugar_sugar, label = 'Ugar_sugar', width = 0.25,color = 'green', align ='edge')
plt.bar([a+0.25 for a in x],jyoti_res, label = 'Jyoti_res', width = -0.25,color = 'red', align = 'edge')

#label - for representing a box at upper left 
#marker - for getting good view at turning points 

plt.xlabel('Days')
plt.ylabel('Price')
plt.legend(loc = 'upper left')
plt.title('Stock information on daily time-frame ')
plt.ylim(100,700)
#setting limit of x-axis 
plt.grid(True)
plt.show()
