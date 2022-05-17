import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.close("all")

dataURL = 'https://github.com/owid/covid-19-data/raw/master/public/data/vaccinations/country_data/Germany.csv'
df = pd.read_csv(dataURL)


def fully_vaccinated_r(range_start, range_end):
    fully_vac = []
    for index in range(range_start, range_end):
        fully_vac.append(df['people_fully_vaccinated'][index])
    return fully_vac
    #takes fully vaccinated in a range from the dataFrame and returns it


def fully_vaccinated():
    out = pd.DataFrame(df, columns=['people_fully_vaccinated'])
    #print(out)
    out.plot(kind='line', xlabel = 'amount of people')
    plt.show()


out=pd.DataFrame(fully_vaccinated_r(10,15))
out.plot(kind='line', xlabel='amount of people')
plt.show()

