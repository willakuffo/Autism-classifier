# from scipy.io import arff
# import pandas as pd

# data = arff.loadarff('Autism-Screening-Child-Data/Autism-Child-Data.arff')
# df = pd.DataFrame(data[0])

# df.head()

f = open("Autism-Screening-Child-Data/Autism-Child-Data.arff","r")
print(f.read())
