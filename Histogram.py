
import matplotlib.pyplot as plt 
#stock price range of a week 
ugar_sugar = [200,300,333,530,480,520,460,600]
bins = [100,200,300,400,500,500,600,700,800,900,1000]

plt.hist(ugar_sugar, bins, label = 'Ugar_sugar')

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
