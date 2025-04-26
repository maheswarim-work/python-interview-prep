# import pandas

import pandas as pd

mydataset = {
    'cars': ["bmw", "benz"],
    'passings': [5, 3]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
