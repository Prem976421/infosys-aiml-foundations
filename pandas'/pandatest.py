import pandas as pd
car_price_dict = {'Swift':  700000,
                       'Jazz' :  800000,
                       'Civic' : 1600000,
                       'Altis' : 1800000,
                       'Gallardo': 30000000
                      }
car_price = pd.Series(car_price_dict)

car_manu_dict = {'Swift':  'maruti',
                       'Jazz' :  'Honda',
                       'Civic' : 'Honda',
                       'Altis' : 'Toyota',
                       'Gallardo': 'lamborgini'}
car_manu = pd.Series(car_manu_dict)

#Creating a DataFrame from car_price Series
print(pd.DataFrame({'car price' : car_price, 'car manufact': car_manu}))
