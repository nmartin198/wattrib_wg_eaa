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
OUT_LABEL = r'Medina'
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
LAT_DEG = 29.729 # Medina
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
bas = "Medina"
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
A_DATA_LIST = [ [ 0.5538868, 0.21266316 ],
                [ -0.0370473, 0.68672035 ], ]
"""A matrix for Tmax and Tmin"""
InFiler = os.path.normpath( os.path.join( CUR_DIR, "Inputs",
                        "OWeath_Rho0_1991-2020_DFDict.pkl" ) )
with open( InFiler, 'rb' ) as IF:
    InDictM0 = pickle.load( IF )
# end with
OW_M0_IN = InDictM0[bas]
"""M0 matrix for calculating daily error or residual term"""
B_DATA_LIST = [ [ 0.73915485, 0.0 ],
                [ 0.19643863, 0.71442698], ]
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
DRY_SPELL_PARAMS = { 1 : [ 3.828653394248433, .2904762215286570, 2.0 ],
                     2 : [ 4.764543640630750, .2055881327426108, 2.0 ],
                     3 : [ 3.242510379730563, .3584079674658192, 2.0 ],
                     4 : [ 2.958454781654550, .3376795760189228, 2.0 ],
                     5 : [ 6.610639936009604, .3283596228066935, 2.0 ],
                     6 : [ 5.323419229586656, .3020494227259420, 2.0 ],
                     7 : [ 5.971218175944210, .4135764446502964, 2.0 ],
                     8 : [ 3.138454245888752, .5012462092436358, 2.0 ],
                     9 : [ 3.383820330270589, .2574462019304237, 2.0 ],
                    10 : [ 4.630065115165784, .1762698829006547, 2.0 ],
                    11 : [ 3.154756397472413, .1927395071343758, 2.0 ],
                    12 : [ 4.085801018542923, .4201343011310370, 2.0 ], }
"""Dictionary of monthly parameters for negative binomial distributions to
simulate dry spell durations. Parameters are N, P, and location. N must be
greater than zero; P must be greater than zero and less than or equal to 1."""
WET_SPELL_PARAMS = { 1 : [ 4.558382962469758, .5635465145558790, 1.0 ],
                     2 : [ 2.042792646607727, .6713226254049920, 1.0 ],
                     3 : [ 1.697089614072221, .4568601789393538, 1.0 ],
                     4 : [ 2.808609594735905, .5628805811292324, 1.0 ],
                     5 : [ 3.669244341939914, .5233076065814550, 1.0 ],
                     6 : [ 2.956651211912192, .3952125202428632, 1.0 ],
                     7 : [ 1.917186274125454, .4120391448114438, 1.0 ],
                     8 : [ 1.729202385537204, .5878545012077752, 1.0 ],
                     9 : [ 2.458948567425803, .3512935426455051, 1.0 ],
                    10 : [ 2.200032883170959, .5844497390359634, 1.0 ],
                    11 : [ 1.909126186603285, .5918643624368618, 1.0 ],
                    12 : [ 2.194413600779789, .6867315625618914, 1.0 ], }
"""Dictionary of monthly parameters for negative binomial distributions to
simulate wet spell durations. Parameters are N, P, and location. N must be
greater than zero; P must be greater than zero and less than or equal to 1."""
 
# Precipitation depth distribution parameters by month.
PRE_DEPTH_PARAMS = { 1 : [ .8292333584628184, 1.375751646548801, 0.255, 5.835753291294420 ],
                     2 : [ 1.026114228311398, 1.361140070895049, 0.255, 6.171500760027492 ],
                     3 : [ 1.170632564518031, 1.332417883880119, 0.255, 8.828219913895232 ],
                     4 : [ 1.145902037911005, 1.180555211846569, 0.255, 7.537207039460982 ],
                     5 : [ 1.148848007153241, 1.614684239509531, 0.255, 7.192582641382532 ],
                     6 : [ 1.600000000000000, 1.345482334600400, 0.255, 12.00000000000000 ],
                     7 : [ 1.055093973782708, 1.535756530597420, 0.255, 10.37122818809219 ],
                     8 : [ .8798939548554876, 1.652109004065138, 0.255, 8.892499816714038 ],
                     9 : [ 1.167261383230754, 1.411976590350415, 0.255, 12.00000000000000 ],
                    10 : [ 1.600000000000000, 1.297810558727849, 0.255, 10.00000000000000 ],
                    11 : [ .8314385926299188, 1.390393434061780, 0.255, 7.286151527710824 ],
                    12 : [ .8138245815575304, 1.352092858419400, 0.255, 5.523792360923190 ], }
"""Dictionary of monthly parameters for the generalized, two parameter gamma
distributions. The distribution parameters are 0 - a, 1 - c, 2 - loc, and
3 - scale. a must be greater than zero, and c must not be equal to zero."""
 
# maximum daily precipitation depth that can be used for each calendar month.
MON_MAX_PP = { 1 : 24.8,
               2 : 22.8,
               3 : 29.3,
               4 : 31.2,
               5 : 44.8,
               6 : 37.6,
               7 : 37.8,
               8 : 34.6,
               9 : 40.6,
               10 : 37.8,
               11 : 33.0,
               12 : 26.1, }
"""Maximum daily precipitation depth to allow for sampling from 2 parameter
gamma distributions. Us the 0.95 cumulative probability from the wet day
depth distributions for this."""
 
AVE_WET_TMAX_ADD = 5.358905500662722
"""Multiplier for average wet Tmax"""
AVE_DRY_TMAX_ADD = 7.420985455243838
"""Multiplier for average dry Tmax"""
AVE_WET_TMIN_ADD = .8366956684783006
"""Multiplier for average wet Tmin"""
AVE_DRY_TMIN_ADD = .8758796791255582
"""Multiplier for average dry Tmin"""
 
#-------------------------------------------------
# event dictionary
#    this one is for Medina
EVENT_DICT = { "2-year" : [ int(2), [95.0, 158.2011214040169],],
               "5-year" : [ int(5), [140.0, 250.0000000000000],],
               "10-year" : [ int(10), [177.0, 265.7728609092270],],
               "25-year" : [ int(25), [234.0, 290.3528043767288],],
               "50-year" : [ int(50), [286.0, 420.0214614283059],],
               "100-year" : [ int(100), [339.0, 512.4549545087822],], }
EVENT_KEYS = list( EVENT_DICT.keys() )
 
 
#EOF
