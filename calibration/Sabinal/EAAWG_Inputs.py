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
OUT_LABEL = r'Sabinal'
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
#LAT_DEG = 29.985 # Guadalupe
#LAT_DEG = 29.627 # Med-Cib
#LAT_DEG = 29.729 # Medina
#LAT_DEG = 29.701 # Nueces
#LAT_DEG = 29.574 # Sab-Med
LAT_DEG = 29.617 # Sabinal
"""Latitude in degrees for the basin centroid"""
 
# parameters - usually do not need to be changed
WET_STATE = "wet"
"""Keyword for wet state"""
DRY_STATE = "dry"
"""Keyword for dry state"""
 
#------------------------------------------------------------------------
# Other weather parameter model files
bas = "Sabinal"
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
A_DATA_LIST = [ [ 0.57505088, 0.19625891 ],
                [ -0.03582433, 0.686391 ], ]
"""A matrix for Tmax and Tmin"""
InFiler = os.path.normpath( os.path.join( CUR_DIR, "Inputs",
                        "OWeath_Rho0_1991-2020_DFDict.pkl" ) )
with open( InFiler, 'rb' ) as IF:
    InDictM0 = pickle.load( IF )
# end with
OW_M0_IN = InDictM0[bas]
"""M0 matrix for calculating daily error or residual term"""
B_DATA_LIST = [ [ 0.73450016, 0.0 ],
                [ 0.18187828, 0.71721575 ], ]
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
DRY_SPELL_PARAMS = { 1 : [ 3.790181482362350, .2885691548740135, 2.0 ],
                     2 : [ 5.174467499099766, .1880514971586596, 2.0 ],
                     3 : [ 3.197649337261313, .3540233308540961, 2.0 ],
                     4 : [ 2.500000000000000, .3397336652669280, 2.0 ],
                     5 : [ 6.772020420539480, .3392779885009719, 2.0 ],
                     6 : [ 5.439974594382614, .3020641619301636, 2.0 ],
                     7 : [ 6.090389305854374, .3637757196006433, 2.0 ],
                     8 : [ 3.213981720498469, .5141505531233628, 2.0 ],
                     9 : [ 3.791681607690385, .2524134932970206, 2.0 ],
                    10 : [ 4.770300888006634, .2175938870471790, 2.0 ],
                    11 : [ 3.000000000000000, .1766012500693149, 2.0 ],
                    12 : [ 3.654129431994489, .3949681830010041, 2.0 ], }
"""Dictionary of monthly parameters for negative binomial distributions to
simulate dry spell durations. Parameters are N, P, and location. N must be
greater than zero; P must be greater than zero and less than or equal to 1."""
WET_SPELL_PARAMS = { 1 : [ 4.872193874101646, .6044380145484592, 1.0 ],
                     2 : [ 2.161345963742213, .6308929202275508, 1.0 ],
                     3 : [ 1.593284679796201, .4666865940059044, 1.0 ],
                     4 : [ 2.368981282025571, .6285465138052446, 1.0 ],
                     5 : [ 3.599867191691955, .5246103439546480, 1.0 ],
                     6 : [ 2.813640784536197, .3579075787354139, 1.0 ],
                     7 : [ 1.773475689949307, .4194130550832893, 1.0 ],
                     8 : [ 1.708177169330607, .6059646869347494, 1.0 ],
                     9 : [ 2.476337983814686, .3412650668817272, 1.0 ],
                    10 : [ 2.519770978482347, .5287248108148100, 1.0 ],
                    11 : [ 2.141811615262282, .6104491368190654, 1.0 ],
                    12 : [ 2.429688891161391, .6878490099387422, 1.0 ], }
"""Dictionary of monthly parameters for negative binomial distributions to
simulate wet spell durations. Parameters are N, P, and location. N must be
greater than zero; P must be greater than zero and less than or equal to 1."""
 
# Precipitation depth distribution parameters by month.
PRE_DEPTH_PARAMS = { 1 : [ .7929208883086358, 1.348371424602030, 0.255, 5.397801076289334 ],
                     2 : [ 1.028380186604692, 1.384030081175227, 0.255, 6.272262153733040 ],
                     3 : [ 1.109525003250556, 1.295076638435226, 0.255, 8.696611973708684 ],
                     4 : [ 1.100587807843035, 1.234352031859039, 0.255, 7.166313865064116 ],
                     5 : [ 1.169753040002509, 1.612624340284856, 0.255, 7.561144487355744 ],
                     6 : [ 1.486792871061536, 1.392832039742012, 0.255, 10.45923268497752 ],
                     7 : [ 1.038009412401667, 1.493977286772722, 0.255, 9.895122915165692 ],
                     8 : [ .8471816835860476, 1.606711785558349, 0.255, 8.567933943192132 ],
                     9 : [ 1.124537496243925, 1.432987668102489, 0.255, 10.03801988765173 ],
                    10 : [ 1.591678521042560, 1.291561677657892, 0.255, 10.00000000000000 ],
                    11 : [ .8050634568889986, 1.396829606024511, 0.255, 6.918230229498412 ],
                    12 : [ .8056378314191058, 1.337729958766528, 0.255, 5.611063737079760 ], }
"""Dictionary of monthly parameters for the generalized, two parameter gamma
distributions. The distribution parameters are 0 - a, 1 - c, 2 - loc, and
3 - scale. a must be greater than zero, and c must not be equal to zero."""
 
# maximum daily precipitation depth that can be used for each calendar month.
MON_MAX_PP = { 1 : 25.5,
               2 : 23.1,
               3 : 35.6,
               4 : 38.4,
               5 : 43.3,
               6 : 40.5,
               7 : 43.1,
               8 : 38.1,
               9 : 46.3,
               10 : 48.3,
               11 : 36.1,
               12 : 29.9, }
"""Maximum daily precipitation depth to allow for sampling from 2 parameter
gamma distributions. Us the 0.95 cumulative probability from the wet day
depth distributions for this."""
 
AVE_WET_TMAX_ADD = 5.320279356168166
"""Multiplier for average wet Tmax"""
AVE_DRY_TMAX_ADD = 7.111211767401008
"""Multiplier for average dry Tmax"""
AVE_WET_TMIN_ADD = .8553802422274228
"""Multiplier for average wet Tmin"""
AVE_DRY_TMIN_ADD = .8553242929606504
"""Multiplier for average dry Tmin"""
 
#-------------------------------------------------
# event dictionary
#    this one is for Sabinal
EVENT_DICT = { "2-year" : [ int(2), [94.0, 155.1089022059936],],
               "5-year" : [ int(5), [139.0, 250.0000000000000],],
               "10-year" : [ int(10), [177.0, 252.0239997099458],],
               "25-year" : [ int(25), [235.0, 284.9238790463976],],
               "50-year" : [ int(50), [286.0, 419.0469891376835],],
               "100-year" : [ int(100), [345.0, 509.0996282109630],], }
EVENT_KEYS = list( EVENT_DICT.keys() )
 
 
#EOF
