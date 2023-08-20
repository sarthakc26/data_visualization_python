import matplotlib.pyplot as plt 
labels = ['Facebook', 'Instagram', 'Whatsapp', 'Youtube', 'Linkedin']
views = [230,800,1200,200,666]
explode = [0,0,0,0,0.2]
plt.pie(views, labels = labels, explode=explode, autopct='%1.1f%%', shadow='true', wedgeprops= {'width' : 0.3})
plt.show()