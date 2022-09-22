import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data taken from https://cfpub.epa.gov/ghgdata/inventoryexplorer/#allsectors/allsectors/allgas/econsect/all
data = pd.read_csv("data.csv")

# year = np.unique(data['Year'].values)

year = []
for x in range(1990, 2021):
    year.append(x)

# total = data.iloc[7].tolist()
# del total[0]

transportation = data.iloc[0].tolist()
del transportation[0]
electricity = data.iloc[1].tolist()
del electricity[0]
industry = data.iloc[2].tolist()
del industry[0]
agriculture = data.iloc[3].tolist()
del agriculture[0]
commercial = data.iloc[4].tolist()
del commercial[0]
residential = data.iloc[5].tolist()
del residential[0]
territories = data.iloc[6].tolist()
del territories[0]

print(territories)

plt.stackplot(year, territories, residential, commercial, agriculture, industry,
              electricity, transportation, labels=['territories', 'residential', 'commercial',
                                                   'agriculture', 'industry', 'electricity', 'transportation'])

plt.title('U.S. Greenhouse Gas Emissions by Economic Sector, 1990-2020')
plt.xlabel('Year')
plt.ylabel('Emissions (Million Metric Tons of CO2 Equivalent)')
plt.legend()
plt.margins(x=0)
plt.show()
