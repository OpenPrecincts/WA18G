#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:43:34 2020

@author: baxterdemers
"""
import geopandas as gpd
import pandas as pd

county_abbreviation_to_county_name = {
    'AD': 'Adams',
    'AS': 'Asotin',
    'BE': 'Benton',
    'CH': 'Chelan',
    'CM': 'Clallam',
    'CR': 'Clark',
    'CU': 'Columbia',
    'CZ': 'Cowlitz',
    'DG': 'Douglas',
    'FE': 'Ferry',
    'FR': 'Franklin',
    'GA': 'Garfield',
    'GR': 'Grant',
    'GY': 'Grays Harbor',
    'IS': 'Island',
    'JE': 'Jefferson',
    'KI': 'King',
    'KP': 'Kitsap',
    'KS': 'Kittitas',
    'KT': 'Klickitat',
    'LE': 'Lewis',
    'LI': 'Lincoln',
    'MA': 'Mason',
    'OK': 'Okanogan',
    'PA': 'Pacific',
    'PE': 'Pend Oreille',
    'PI': 'Pierce',
    'SJ': 'San Juan',
    'SK': 'Skagit',
    'SM': 'Skamania',
    'SN': 'Snohomish',
    'SP': 'Spokane',
    'ST': 'Stevens',
    'TH': 'Thurston',
    'WK': 'Wahkiakum',
    'WL': 'Walla Walla',
    'WM': 'Whatcom',
    'WT': 'Whitman',
    'YA': 'Yakima'}

election_results_df_filepath = './sources/WA_G18_MIT.csv'
election_results_df = gpd.read_file(election_results_df_filepath)

precinct_shp_filepath = './sources/2018precincts_verified'
shp_df = gpd.read_file(precinct_shp_filepath)

election_results_df['loc_prec'] = election_results_df['precinct'].str.split(
    pat=' : ', expand=True)[0]
election_results_df.loc[election_results_df["precinct"].str.split(
    pat=',', expand=True)[0] == "Snohomish", 'loc_prec'] \
    = election_results_df['precinct'].str.split(pat=' : ', expand=True)[1]

kdf = gpd.read_file(
    './precinct_name_data/Voting_Districts_of_King_County__votdst_area.csv')
king_map = pd.Series(kdf.NAME.values, index=kdf.votdst).to_dict()
sdf = gpd.read_file('./precinct_name_data/2016.09.01-precincts.csv')
sno_map = pd.Series(sdf.PrecinctName.values, index=sdf.St_Code).to_dict()

shp_df['county'] = shp_df['CountyCd'].map(county_abbreviation_to_county_name)
shp_df.loc[shp_df.county == "Pierce",
           'PrcCode'] = shp_df["FullPrc"].str.slice(start=2)
shp_df['loc_prec'] = shp_df["county"].map(
    str) + "," + shp_df["PrcCode"].str.lstrip('0')

shp_df.loc[shp_df.county == "King", 'loc_prec'] = "King," + \
    shp_df.PrcCode.map(king_map)
king = shp_df[shp_df.CountyCd == 'KI']
shp_df.loc[shp_df.FullPrc == 'KI00000163', 'loc_prec'] = "King,BEL 48-0163"
shp_df.loc[shp_df.FullPrc == 'KI00000214', 'loc_prec'] = "King,BEL 48-0214"
shp_df.loc[shp_df.FullPrc == 'KI00002777', 'loc_prec'] = "King,BEL 48-2777"
shp_df.loc[shp_df.FullPrc == 'KI00001128', 'loc_prec'] = "King,DES 33-1128"

shp_df.loc[shp_df.county == "Kitsap", 'loc_prec'] = shp_df["county"].map(
    str) + ",1" + shp_df["PrcCode"].str.zfill(5)
kit = shp_df[shp_df.county == "Kitsap"]

shp_df.loc[shp_df.county == "Snohomish",
           'loc_prec'] = shp_df.FullPrc.map(sno_map)

result = election_results_df.merge(shp_df, on="loc_prec", how='outer')

print(result.head())
print(result.dtypes)
export = result.drop(columns=['geometry_x', 'geometry_y'])
export.to_csv('WA_G18_merged.csv')
