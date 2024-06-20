import numpy as np
import pandas as pd
from apyori import apriori

store_data = pd.read_excel('data.xls')

records = []
for i in range(0, 51):
    records.append([str(store_data.values[i,j]) for j in range(0, 6)])

association_rules = apriori(records, min_support=0.10, min_confidence=0.7, min_lift=1.2, min_length=2)
association_results = list(association_rules)

result = []
for item in association_results:
    pair = item[0]
    items = [x for x in pair]

    value0 = str(items[0])
    value1 = str(items[1])
    value2 = str(item[1])[:6]
    value3 = str(item[2][0][2])[:6]
    value4 = str(item[2][0][3])[:6]

    rowset = [value0, value1, value2, value3, value4]
    result.append(rowset)

    label = ['Item 1', 'Item 2', 'Support', 'Confidence', 'Lift']
    store_suggestion = pd.DataFrame.from_records(result, columns=label)

print(store_suggestion)
store_suggestion.describe()
# store_suggestion.to_excel('store_suggestion.xlsx')