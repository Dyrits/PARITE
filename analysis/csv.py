import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from os import path
import logging as lg
# import matplotlib as mil
# mil.use('TkAgg')

lg.basicConfig(level=lg.DEBUG)


class SetOfParliamentMembers:
    def __init__(self, name):
        self.name = name

    def data_from_csv(self, csv_file):
        self.dataframe = pd.read_csv(csv_file, sep=";")
        
    def data_from_dataframe(self, dataframe):
        self.dataframe = dataframe

    def __repr__(self):
        return f"The set includes {len(self.dataframe)} members."
    
    def display_chart(self):
        data = self.dataframe
        female_mps = data[data.sexe == "F"]
        male_mps = data[data.sexe == "H"]

        counts = [len(female_mps), len(male_mps)]
        counts = np.array(counts)
        nb_mps = counts.sum()
        proportions = counts / nb_mps

        labels = ["Female ({})".format(counts[0]), "Male ({})".format(counts[1])]

        fig, ax = plt.subplots()
        ax.axis("equal")
        ax.pie(
                proportions,
                labels=labels,
                autopct="%1.1f pourcents"
                )
        plt.title("{} ({} MPs)".format(self.name, nb_mps))
        plt.show()

    def split_by_political_party(self):
        result = {}
        data = self.dataframe
        
        # SQL >> SELECT DISTINCT parti_ratt_financier WHERE parti_ratt_financier IS NOT NULL:
        all_parties = data["parti_ratt_financier"].dropna().unique() 

        for party in all_parties:
            data_subset = data[data.parti_ratt_financier == party] # Set of data for a party
            subset = SetOfParliamentMembers('MPs from party "{}"'.format(party)) # Creation of a class with the name of the party
            subset.data_from_dataframe(data_subset) # The self.dataframe property is set with the medhod with the set of data as argument.
            result[party] = subset # The dictionnary `result` is set with the  party as a key, and the object as a value.

        return result


def launch_analysis(data_file, 
                    by_party=False, 
                    info=False):
    directory = path.dirname(path.dirname(__file__))
    path_to_file = path.join(directory, "data", data_file)
    sopm = SetOfParliamentMembers("All MPs")
    sopm.data_from_csv(path_to_file)
    
    if info:
        print(sopm)
    
    
    # Display the chart:
    sopm.display_chart()
    # Display the chart by party:
    if by_party:
        for subset in sopm.split_by_political_party().values():
            subset.display_chart()

if __name__ == "__main__":
    launch_analysis('current_mps.csv')
