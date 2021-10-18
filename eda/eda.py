
import pandas as pd 

data = pd.read_csv("data/indeed_job_dataset.csv") 

data["id_val"] = [val for val in data["Unnamed: 0"]]
data = data.drop("Unnamed: 0", 1)

data["Link"] = ["No Link" if type(i) != str else i for i in data["Link"]]
data["No_of_Skills"] = [int(i) for i in data["No_of_Skills"]]
data["No_of_Reviews"] = [float(i) for i in data["No_of_Reviews"]]
data["No_of_Stars"] = [int(i) for i in data["No_of_Stars"]]
data["Company"] = ["No Company Found" if type(i) != str else i for i in data["Company"]]
