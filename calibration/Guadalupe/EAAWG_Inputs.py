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
OUT_LABEL = r'Guadalupe'
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
#LAT_DEG = 29.741 # Cibolo
#LAT_DEG = 29.678 # Frio
LAT_DEG = 29.985 # Guadalupe
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
bas = "Guadalupe"
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
A_DATA_LIST = [ [ 0.54429194, 0.22858604 ],
                [ -0.04478881, 0.69200318 ], ]
"""A matrix for Tmax and Tmin"""
InFiler = os.path.normpath( os.path.join( CUR_DIR, "Inputs",
                        "OWeath_Rho0_1991-2020_DFDict.pkl" ) )
with open( InFiler, 'rb' ) as IF:
    InDictM0 = pickle.load( IF )
# end with
OW_M0_IN = InDictM0[bas]
"""M0 matrix for calculating daily error or residual term"""
B_DATA_LIST = [ [ 0.73382846, 0.0 ],
                [ 0.20971313 , 0.7094317 ], ]
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
DRY_SPELL_PARAMS = { 1 : [ 3.827692390954829, .2833830808096543, 2.0 ],
                     2 : [ 5.431072378965404, .2260817632002613, 2.0 ],
                     3 : [ 3.475254898014449, .3698174926380662, 2.0 ],
                     4 : [ 3.045066216074454, .3923204628330379, 2.0 ],
                     5 : [ 6.746541392361880, .3615870457890824, 2.0 ],
                     6 : [ 5.117208243724438, .3365797153287059, 2.0 ],
                     7 : [ 5.928458475239302, .3633211627112538, 2.0 ],
                     8 : [ 3.150113867209728, .5018974346087636, 2.0 ],
                     9 : [ 3.573550906550478, .2581335962555354, 2.0 ],
                    10 : [ 4.433642531945357, .1920310636056329, 2.0 ],
                    11 : [ 3.730287343667611, .1678938808272573, 2.0 ],
                    12 : [ 4.103878828413991, .3897912057973263, 2.0 ], }
"""Dictionary of monthly parameters for negative binomial distributions to
simulate dry spell durations. Parameters are N, P, and location. N must be
greater than zero; P must be greater than zero and less than or equal to 1."""
WET_SPELL_PARAMS = { 1 : [ 4.488000274705559, .5390761079243620, 1.0 ],
                     2 : [ 2.179856387830733, .7004645433291752, 1.0 ],
                     3 : [ 1.661162318366595, .4110738190189140, 1.0 ],
                     4 : [ 2.597763307330671, .5569869242888316, 1.0 ],
                     5 : [ 3.780728474963565, .5568102651312484, 1.0 ],
                     6 : [ 3.040622536869659, .4226562305566553, 1.0 ],
                     7 : [ 1.990205359138526, .4198346640642217, 1.0 ],
                     8 : [ 1.525555029281842, .5393947094149876, 1.0 ],
                     9 : [ 2.521120690176022, .3498211869118682, 1.0 ],
                    10 : [ 2.262994443731137, .5368445190325158, 1.0 ],
                    11 : [ 1.974216917360072, .6693232185657008, 1.0 ],
                    12 : [ 2.330086458105206, .7063361487764358, 1.0 ], }
"""Dictionary of monthly parameters for negative binomial distributions to
simulate wet spell durations. Parameters are N, P, and location. N must be
greater than zero; P must be greater than zero and less than or equal to 1."""
 
# Precipitation depth distribution parameters by month.
PRE_DEPTH_PARAMS = { 1 : [ .8476783900561514, 1.369914596834996, 0.255, 5.766573565002244 ],
                     2 : [ 1.013884450901211, 1.409175940610314, 0.255, 6.317731840148674 ],
                     3 : [ 1.202722433770511, 1.299619710442357, 0.255, 9.110083407000778 ],
                     4 : [ 1.166148555680612, 1.194000931615235, 0.255, 7.288603356476434 ],
                     5 : [ 1.223695416588134, 1.610465602394342, 0.255, 7.794875366224116 ],
                     6 : [ 1.519203745522942, 1.319704768321022, 0.255, 11.13884989133169 ],
                     7 : [ 1.024467179465048, 1.521104281673987, 0.255, 10.05887738209861 ],
                     8 : [ .9389925873694556, 1.633550608667177, 0.255, 9.590495757865338 ],
                     9 : [ 1.128796341255857, 1.456575266455255, 0.255, 9.946951325705818 ],
                    10 : [ 1.478347575636011, 1.277868072090102, 0.255, 9.824899313877422 ],
                    11 : [ .7795128640799368, 1.371586684130168, 0.255, 6.811991864890718 ],
                    12 : [ .8117581657260260, 1.332990135182247, 0.255, 5.239487053100812 ], }
"""Dictionary of monthly parameters for the generalized, two parameter gamma
distributions. The distribution parameters are 0 - a, 1 - c, 2 - loc, and
3 - scale. a must be greater than zero, and c must not be equal to zero."""
 
# maximum daily precipitation depth that can be used for each calendar month.
MON_MAX_PP = { 1 : 25.3,
               2 : 23.2,
               3 : 29.0,
               4 : 29.0,
               5 : 39.8,
               6 : 38.7,
               7 : 29.7,
               8 : 30.5,
               9 : 33.7,
               10 : 42.9,
               11 : 35.2,
               12 : 29.0, }
"""Maximum daily precipitation depth to allow for sampling from 2 parameter
gamma distributions. Us the 0.95 cumulative probability from the wet day
depth distributions for this."""
 
AVE_WET_TMAX_ADD = 5.147570603845456
"""Multiplier for average wet Tmax"""
AVE_DRY_TMAX_ADD = 7.179991175503242
"""Multiplier for average dry Tmax"""
AVE_WET_TMIN_ADD = .8372926208119018
"""Multiplier for average wet Tmin"""
AVE_DRY_TMIN_ADD = .8563813802769066
"""Multiplier for average dry Tmin"""
 
#-------------------------------------------------
# event dictionary
#    this one is for Guadalupe
EVENT_DICT = { "2-year" : [ int(2), [90.0, 158.3110069981192],],
               "5-year" : [ int(5), [132.0, 225.2933702506887],],
               "10-year" : [ int(10), [168.0, 258.6121127644105],],
               "25-year" : [ int(25), [221.0, 295.0684483839654],],
               "50-year" : [ int(50), [267.0, 431.3077095997755],],
               "100-year" : [ int(100), [320.0, 505.6948838934978],], }
EVENT_KEYS = list( EVENT_DICT.keys() )
 
 
#EOF
