# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 12:18:15 2020

@author: Florian Jehn
"""
import os
import pandas as pd


# Valid Countries from the european union
EU = ["Austria", "Belgium", "Bulgaria", "Croatia", "Republic of Cyprus",
             "Czech Republic", "Denmark", "Estonia", "Finland", "France", 
             "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia",
             "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", 
             "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden"]

# Valid food 
cereals = ["Wheat", "Maize", "Rice", "Sorghum", "Barley", "Rye", "Oats",
           "Millet", "Triticale", "Buckwheat", "Fonio", "Quinoa", "Canary seed"]

oil_seed = ["Soya beans", "Groundnuts", "Castor bean", "Linseed", "Mustard",
            "Niger seed", "Rapeseed", "Safflower", "Sesame", "Sunflower", 
            "Shea tree (shea butter or karite nuts)", "Tung tree" , "Jojoba",
            "Poppy", "Tallow tree", "Coconuts", "Olives", "Oil palms"]

leguminous = ["Beans", "Broad beans", "Chickpeas", "Cowpeas", "Lentils",
             "Lupins" ,"Peas", "Pigeon peas", "Bambara beans", "Vetches"]

protein_crops = cereals + oil_seed + leguminous 


def crop_production(EU, protein_crops):
    """
    Reads, sorts and saves the food production for the protein crops

    Returns
    -------
    None.
    """
    se = os.sep
    filepath = ".." + se + ".." + se + "Data" + se + "Production_Crops_E_All_Data" + se + "Production_Crops_E_All_Data_NOFLAG.csv"    
    protein_prod_df = pd.read_csv(filepath,  sep=",", encoding="latin-1")
    # Only consider the relevant years
    protein_prod_df = protein_prod_df[['Area', 'Item', 'Element', 'Unit', "Y2005", "Y2017"]]
    # Select only EU countries
    protein_prod_df = protein_prod_df.loc[protein_prod_df["Area"].isin(EU),:]
    # Only consider production amonut
    protein_prod_df = protein_prod_df.loc[protein_prod_df["Element"] == "Production",:]
    # Only consider protein crops
    protein_prod_df = protein_prod_df.loc[protein_prod_df["Item"].isin(protein_crops),:]
    protein_prod_df.to_csv("european_protein_crops_production.csv")
    return protein_prod_df
    
    
def trade(EU, protein_crops):
    """
    Reads, sorts and saves the worldwide trade for the protein crops

    Returns
    -------
    None.
    """
    se = os.sep
    filepath = ".." + se + ".." + se + "Data" + se + "Trade_DetailedTradeMatrix_E_All_Data" + se + "Trade_DetailedTradeMatrix_E_All_Data_NOFLAG.csv"    
    protein_trade_df = pd.read_csv(filepath,  sep=",", encoding="latin-1")
    # Only consider the relevant years
    protein_trade_df = protein_trade_df[["Reporter Countries", "Partner Countries",
                                       "Item", "Element", "Unit", "Y2005", "Y2017"]]
    # Only consider imports
    protein_trade_df = protein_trade_df.loc[protein_trade_df["Element"] == "Import Quantity"]
    # Only consider EU countries
    protein_trade_df = protein_trade_df.loc[protein_trade_df["Reporter Countries"].isin(EU),:]
    # Only consider protein_crops
    protein_trade_df = protein_trade_df.loc[protein_trade_df["Item"].isin(protein_crops),:]
    protein_trade_df.to_csv("european_protein_crops_imports")
    return protein_trade_df


protein_prod_df =  crop_production(EU, protein_crops)
protein_trade_df = trade(EU, protein_crops)



