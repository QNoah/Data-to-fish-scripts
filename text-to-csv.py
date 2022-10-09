# pip install pandas

import pandas as pd #importeerd de package met als naam pd 

read_file = pd.read_csv(r'file.txt') # Hij leest de file waaruit hij de txt gaat halen
read_file.to_csv (r'file.csv', index =None) #hij wordt opgeslagen als file.csv in deze map waar wij nu inzitten.
input()
exit() #verlaat python
# read_file.to_csv (r'C:/Users/Q/Desktop/file.csv', index =None) je zou het ook op deze manier kunnen doen met jouw eigen naam
