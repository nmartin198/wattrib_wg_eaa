# -*- coding: utf-8 -*-
"""
.. module:: EAAWG_Inputs
   :platform: Windows, Linux
   :synopsis: Provides input specification and shared module information
 
.. moduleauthor:: Nick Martin <nmartin@swri.org>
 
Provides the inputs module where all input values and shared parameters can
be entered. This functionality can be replaced with a GUI in the future. Also
holds the shared  data structures.
 
"""
import pandas as pd
import pickle
import os
 
#------------------------------------------------------------------------
# Global simulation settings - these generally need to be changed
CUR_DIR = os.getcwd()
OUT_DIR = os.path.normpath( os.path.join( CUR_DIR, "Results" ) )
"""Location for model outputs"""
OUT_LABEL = r'Blanco'
"""Label to use for outputting files to OUT_DIR"""
OUT_SUB_DIR = "Simulated"
"""Output subdirectory"""
START_DATE = pd.Timestamp(2024, 1, 1, 0, )
"""Starting time for production of the stochastic synthetic time series"""
END_DATE = pd.Timestamp( 2065, 12, 31, 23, 59, )
"""Ending time for production of the stochastic synthetic time series"""
K_c = 1.00
"""Crop coefficient to go from ETo to PET. Coefficient derived by comparing
calculated ETo to independently calculated/measured PET from "station" data.
In this implementation, the crop coefficient is not used."""
LAT_DEG = 30.018 # Blanco
#LAT_DEG = 29.741 # Cibolo
#LAT_DEG = 29.678 # Frio
#LAT_DEG = 29.985 # Guadalupe
#LAT_DEG = 29.627 # Med-Cib
#LAT_DEG = 29.729 # Medina
#LAT_DEG = 29.701 # Nueces
#LAT_DEG = 29.574 # Sab-Med
#LAT_DEG = 29.617 # Sabinal
"""Latitude in degrees for the basin centroid"""
 
# parameters - usually do not need to be changed
WET_STATE = "wet"
"""Keyword for wet state"""
DRY_STATE = "dry"
"""Keyword for dry state"""
 
#------------------------------------------------------------------------
# Other weather parameter model files
bas = "Blanco"
InFiler = os.path.normpath( os.path.join( CUR_DIR, "Inputs",
                        "OWeath_Smooth_WetAve_1981-2010_DictDF.pkl" ) )
with open( InFiler, 'rb' ) as IF:
    InDictWA = pickle.load( IF )
# end with
OW_WET_AVE = InDictWA[bas]
"""Average wet day quantities by day of the year. Contains Tmax, Tmin, and Tave"""
InFiler = os.path.normpath( os.path.join( CUR_DIR, "Inputs",
                        "OWeath_Smooth_DryAve_1981-2010_DictDF.pkl" ) )
with open( InFiler, 'rb' ) as IF:
    InDictDA = pickle.load( IF )
# end with
OW_DRY_AVE = InDictDA[bas]
"""Average dry day quantities by day of the year. Contains Tmax, Tmin, and Tave"""
InFiler = os.path.normpath( os.path.join( CUR_DIR, "Inputs",
                        "OWeath_Smooth_WetStd_1981-2010_DictDF.pkl" ) )
with open( InFiler, 'rb' ) as IF:
    InDictWS = pickle.load( IF )
# end with
OW_WET_STD = InDictWS[bas]
"""Average wet day standard deviations for Tmax, Tmin, and Tave"""
InFiler = os.path.normpath( os.path.join( CUR_DIR, "Inputs",
                        "OWeath_Smooth_DryStd_1981-2010_DictDF.pkl" ) )
with open( InFiler, 'rb' ) as IF:
    InDictDS = pickle.load( IF )
# end with
OW_DRY_STD = InDictDS[bas]
"""Average dry day standard deviations for Tmax, Tmin, and Tave"""
 
# other weather parameters correlation matrices
A_DATA_LIST = [ [ 0.5139801, 0.25329464 ],
                [ -0.04809321, 0.70150028 ], ]
"""A matrix for Tmax and Tmin"""
InFiler = os.path.normpath( os.path.join( CUR_DIR, "Inputs",
                        "OWeath_Rho0_1991-2020_DFDict.pkl" ) )
with open( InFiler, 'rb' ) as IF:
    InDictM0 = pickle.load( IF )
# end with
OW_M0_IN = InDictM0[bas]
"""M0 matrix for calculating daily error or residual term"""
B_DATA_LIST = [ [ 0.73033623, 0.0 ],
                [ 0.26437591, 0.6866752 ], ]
""" B matrix for Tmax and Tmin"""
InFiler = os.path.normpath( os.path.join( CUR_DIR, "Inputs",
                        "OWeath_Rho1_1991-2020_DFDict.pkl" ) )
with open( InFiler, 'rb' ) as IF:
    InDictM1 = pickle.load( IF )
# end with
OW_M1_IN = InDictM1[bas]
"""M1 matrix for calculating daily error or residual term"""
 
#------------------------------------------------------------------------
# distribution specifications
# For spell length distributions assume that one distribution applies to
#  the entire study area
DRY_SPELL_PARAMS = { 1 : [ 3.084460000000000, .2384300000000000, 2.0 ],
                     2 : [ 5.728710000000000, .2346500000000000, 2.0 ],
                     3 : [ 2.799350000000000, .2647000000000000, 2.0 ],
                     4 : [ 2.745980000000000, .1507500000000000, 2.0 ],
                     5 : [ 2.973420000000000, .4156900000000000, 2.0 ],
                     6 : [ 6.356770000000000, .3805200000000000, 2.0 ],
                     7 : [ 7.000000000000000, .1641900000000000, 2.0 ],
                     8 : [ 2.814080000000000, .1542000000000000, 2.0 ],
                     9 : [ 7.000000000000000, .1492400000000000, 2.0 ],
                    10 : [ 2.768080000000000, .5124300000000002, 2.0 ],
                    11 : [ 5.218570000000000, .1580800000000000, 2.0 ],
                    12 : [ 5.917210000000000, .1300000000000000, 2.0 ], }
"""Dictionary of monthly parameters for negative binomial distributions to
simulate dry spell durations. Parameters are N, P, and location. N must be
greater than zero; P must be greater than zero and less than or equal to 1."""
WET_SPELL_PARAMS = { 1 : [ 4.331640000000000, .3348200000000000, 1.0 ],
                     2 : [ 5.000000000000000, .6982900000000000, 1.0 ],
                     3 : [ 5.000000000000000, .3953200000000000, 1.0 ],
                     4 : [ 3.486930000000000, .6663300000000000, 1.0 ],
                     5 : [ .8867900000000000, .2510800000000001, 1.0 ],
                     6 : [ 4.749070000000000, .4070000000000000, 1.0 ],
                     7 : [ 3.728820000000000, .2500000000000000, 1.0 ],
                     8 : [ 4.508400000000000, .3121600000000000, 1.0 ],
                     9 : [ .9312100000000000, .6788200000000000, 1.0 ],
                    10 : [ 3.872950000000000, .2993500000000000, 1.0 ],
                    11 : [ 5.000000000000000, .8000000000000000, 1.0 ],
                    12 : [ .8614600000000000, .8000000000000000, 1.0 ], }
"""Dictionary of monthly parameters for negative binomial distributions to
simulate wet spell durations. Parameters are N, P, and location. N must be
greater than zero; P must be greater than zero and less than or equal to 1."""
 
# Precipitation depth distribution parameters by month.
PRE_DEPTH_PARAMS = { 1 : [ 1.669780000000000, .7000000000000000, 0.255, 5.537450000000000 ],
                     2 : [ .7847200000000000, 2.594560000000000, 0.255, 11.38800000000000 ],
                     3 : [ 1.436390000000000, 2.379030000000000, 0.255, 4.880470000000000 ],
                     4 : [ 1.698210000000000, 2.376170000000000, 0.255, 5.512020000000000 ],
                     5 : [ .7897400000000000, 2.583850000000000, 0.255, 11.66110000000000 ],
                     6 : [ .7186000000000000, .8055300000000000, 0.255, 4.954060000000000 ],
                     7 : [ .7896200000000000, .7424900000000000, 0.255, 9.182950000000000 ],
                     8 : [ 1.463960000000000, .7571600000000002, 0.255, 10.26520000000000 ],
                     9 : [ 1.547300000000000, .6915700000000000, 0.255, 11.30650000000000 ],
                    10 : [ 1.444840000000000, .6081600000000000, 0.255, 6.010950000000000 ],
                    11 : [ 1.304270000000000, .7910600000000000, 0.255, 9.489570000000000 ],
                    12 : [ 1.417460000000000, 2.498440000000000, 0.255, 4.626250000000000 ], }
"""Dictionary of monthly parameters for the generalized, two parameter gamma
distributions. The distribution parameters are 0 - a, 1 - c, 2 - loc, and
3 - scale. a must be greater than zero, and c must not be equal to zero."""
 
# maximum daily precipitation depth that can be used for each calendar month.
MON_MAX_PP = { 1 : 30.9,
               2 : 21.0,
               3 : 28.7,
               4 : 27.9,
               5 : 45.9,
               6 : 36.3,
               7 : 34.3,
               8 : 37.7,
               9 : 38.0,
               10 : 62.3,
               11 : 39.1,
               12 : 32.5, }
"""Maximum daily precipitation depth to allow for sampling from 2 parameter
gamma distributions. Us the 0.95 cumulative probability from the wet day
depth distributions for this."""
 
AVE_WET_TMAX_ADD = 5.794700000000000
"""Multiplier for average wet Tmax"""
AVE_DRY_TMAX_ADD = 5.998720000000000
"""Multiplier for average dry Tmax"""
AVE_WET_TMIN_ADD = 2.141640000000000
"""Multiplier for average wet Tmin"""
AVE_DRY_TMIN_ADD = 2.129330000000000
"""Multiplier for average dry Tmin"""
 
#-------------------------------------------------
# event dictionary
#    this one is for Blanco
EVENT_DICT = { "2-year" : [ int(2), [91.0, 201.7600000000000],],
               "5-year" : [ int(5), [133.0, 140.0000000000000],],
               "10-year" : [ int(10), [170.0, 300.7600000000000],],
               "25-year" : [ int(25), [226.0, 354.3400000000000],],
               "50-year" : [ int(50), [275.0, 465.6500000000000],],
               "100-year" : [ int(100), [332.0, 526.3100000000000],], }
EVENT_KEYS = list( EVENT_DICT.keys() )
 
 
#EOF
