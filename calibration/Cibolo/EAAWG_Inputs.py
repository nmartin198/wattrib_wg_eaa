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
OUT_LABEL = r'Cibolo'
"""Label to use for outputting files to OUT_DIR"""
OUT_SUB_DIR = "Simulated"
"""Output subdirectory"""
START_DATE = pd.Timestamp(2024, 1, 1, 0, )
"""Starting time for production of the stochastic synthetic time series"""
END_DATE = pd.Timestamp( 2060, 12, 31, 23, 59, )
"""Ending time for production of the stochastic synthetic time series"""
K_c = 1.00
"""Crop coefficient to go from ETo to PET. Coefficient derived by comparing
calculated ETo to independently calculated/measured PET from "station" data.
In this implementation, the crop coefficient is not used."""
#LAT_DEG = 30.018 # Blanco
LAT_DEG = 29.741 # Cibolo
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
bas = "Cibolo"
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
A_DATA_LIST = [ [ 0.53157893, 0.23596473 ],
                [ -0.04095222, 0.70537809 ], ]
"""A matrix for Tmax and Tmin"""
InFiler = os.path.normpath( os.path.join( CUR_DIR, "Inputs",
                        "OWeath_Rho0_1991-2020_DFDict.pkl" ) )
with open( InFiler, 'rb' ) as IF:
    InDictM0 = pickle.load( IF )
# end with
OW_M0_IN = InDictM0[bas]
"""M0 matrix for calculating daily error or residual term"""
B_DATA_LIST = [ [ 0.72915806, 0.0 ],
                [ 0.25291034, 0.68319558 ], ]
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
DRY_SPELL_PARAMS = { 1 : [ 3.660968634626803, .3055005511132562, 2.0 ],
                     2 : [ 4.856279057627904, .2129798840757898, 2.0 ],
                     3 : [ 3.535301703470398, .3875874080667167, 2.0 ],
                     4 : [ 2.905213595185423, .3488543850934419, 2.0 ],
                     5 : [ 7.000000000000000, .3471186485067746, 2.0 ],
                     6 : [ 5.689427845939264, .2757823647177650, 2.0 ],
                     7 : [ 6.866254319941156, .3743586232204278, 2.0 ],
                     8 : [ 2.500000000000000, .4998543955633820, 2.0 ],
                     9 : [ 3.470464463209680, .2593441300774284, 2.0 ],
                    10 : [ 4.323781709519303, .1704475819587496, 2.0 ],
                    11 : [ 3.086264879273956, .1867975765300896, 2.0 ],
                    12 : [ 3.533274550321295, .4236333013376215, 2.0 ], }
"""Dictionary of monthly parameters for negative binomial distributions to
simulate dry spell durations. Parameters are N, P, and location. N must be
greater than zero; P must be greater than zero and less than or equal to 1."""
WET_SPELL_PARAMS = { 1 : [ 4.095608720937964, .5227390389074000, 1.0 ],
                     2 : [ 2.243189916912342, .6328833347142652, 1.0 ],
                     3 : [ 1.632792005286702, .4146813255356567, 1.0 ],
                     4 : [ 2.686756165781256, .5326353696338476, 1.0 ],
                     5 : [ 3.286206619800326, .5592297578570866, 1.0 ],
                     6 : [ 3.130354035724537, .3451462768431081, 1.0 ],
                     7 : [ 2.008056289817039, .4387512683979456, 1.0 ],
                     8 : [ 1.763207760300168, .5696746231399098, 1.0 ],
                     9 : [ 2.369851093899703, .3196537521222381, 1.0 ],
                    10 : [ 2.381421524364639, .4967679854744034, 1.0 ],
                    11 : [ 2.083573850820737, .6617344133870866, 1.0 ],
                    12 : [ 2.374313466183517, .6707624131055924, 1.0 ], }
"""Dictionary of monthly parameters for negative binomial distributions to
simulate wet spell durations. Parameters are N, P, and location. N must be
greater than zero; P must be greater than zero and less than or equal to 1."""
 
# Precipitation depth distribution parameters by month.
PRE_DEPTH_PARAMS = { 1 : [ .8401198990230728, 1.317937749948389, 0.255, 5.950352331028966 ],
                     2 : [ 1.056991868394011, 1.386146155764584, 0.255, 6.248014647638680 ],
                     3 : [ 1.196042616203949, 1.279582719687589, 0.255, 9.535340239780200 ],
                     4 : [ 1.151557742447307, 1.170162487770808, 0.255, 7.513745605189602 ],
                     5 : [ 1.235868749899750, 1.575838527983337, 0.255, 8.048172112091728 ],
                     6 : [ 1.561088409295203, 1.302547888277808, 0.255, 11.68625327465791 ],
                     7 : [ 1.033057838143965, 1.506175957751737, 0.255, 10.20516363488046 ],
                     8 : [ .8782542424358696, 1.594838076729760, 0.255, 9.128593378435634 ],
                     9 : [ 1.114387459184582, 1.357923406019448, 0.255, 11.01022080293756 ],
                    10 : [ 1.600000000000000, 1.214017537991835, 0.255, 10.00000000000000 ],
                    11 : [ .8135770381829656, 1.370657854690028, 0.255, 7.261576287128090 ],
                    12 : [ .7996564264148284, 1.318520297501624, 0.255, 5.286352378931830 ], }
"""Dictionary of monthly parameters for the generalized, two parameter gamma
distributions. The distribution parameters are 0 - a, 1 - c, 2 - loc, and
3 - scale. a must be greater than zero, and c must not be equal to zero."""
 
# maximum daily precipitation depth that can be used for each calendar month.
MON_MAX_PP = { 1 : 27.0,
               2 : 22.4,
               3 : 27.8,
               4 : 31.3,
               5 : 43.9,
               6 : 38.6,
               7 : 38.7,
               8 : 40.2,
               9 : 41.2,
               10 : 60.9,
               11 : 34.6,
               12 : 31.0, }
"""Maximum daily precipitation depth to allow for sampling from 2 parameter
gamma distributions. Us the 0.95 cumulative probability from the wet day
depth distributions for this."""
 
AVE_WET_TMAX_ADD = 5.524617536855794
"""Multiplier for average wet Tmax"""
AVE_DRY_TMAX_ADD = 8.000000000000000
"""Multiplier for average dry Tmax"""
AVE_WET_TMIN_ADD = .8257630242753764
"""Multiplier for average wet Tmin"""
AVE_DRY_TMIN_ADD = .8310800654325752
"""Multiplier for average dry Tmin"""
 
#-------------------------------------------------
# event dictionary
#    this one is for Cibolo
EVENT_DICT = { "2-year" : [ int(2), [91.0, 163.0786987124333],],
               "5-year" : [ int(5), [134.0, 250.0000000000000],],
               "10-year" : [ int(10), [171.0, 259.2213325613568],],
               "25-year" : [ int(25), [225.0, 295.0688467067946],],
               "50-year" : [ int(50), [272.0, 422.3049794188666],],
               "100-year" : [ int(100), [327.0, 499.1576927308558],], }
EVENT_KEYS = list( EVENT_DICT.keys() )
 
 
#EOF
