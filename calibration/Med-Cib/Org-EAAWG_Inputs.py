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
OUT_LABEL = r'Test_1'
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
A_DATA_LIST = [ [ 0.58468288, 0.12044084 ],
                [ 0.06381925, 0.53650334 ], ]
"""A matrix for Tmax and Tmin"""
InFiler = os.path.normpath( os.path.join( CUR_DIR, "Inputs", 
                        "OWeath_Rho0_1991-2020_DFDict.pkl" ) )
with open( InFiler, 'rb' ) as IF:
    InDictM0 = pickle.load( IF )
# end with
OW_M0_IN = InDictM0[bas]
"""M0 matrix for calculating daily error or residual term"""
B_DATA_LIST = [ [ 0.76928373, 0.0 ],
                [ 0.19221789, 0.80370198 ], ]
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
DRY_SPELL_PARAMS = { 1 : [ 1.19802998168446, 0.158416853273040, 1.0 ], 
                     2 : [ 1.88825413813301, 0.281450535975017, 1.0 ], 
                     3 : [ 3.17052939741400, 0.376008524889633, 1.0 ], 
                     4 : [ 2.20407068036811, 0.290964950603887, 1.0 ], 
                     5 : [ 1.36001776768749, 0.202538620486077, 1.0 ], 
                     6 : [ 0.61986475283764, 0.079211162554898, 1.0 ], 
                     7 : [ 0.77647653551268, 0.074830462234001, 1.0 ], 
                     8 : [ 1.63392885988434, 0.191046180383138, 1.0 ], 
                     9 : [ 1.16495440378622, 0.155488399298109, 1.0 ], 
                    10 : [ 1.35083448784846, 0.161340413286858, 1.0 ], 
                    11 : [ 1.80885216974113, 0.215011585673341, 1.0 ], 
                    12 : [ 0.85551589217206, 0.117288553727117, 1.0 ], }
"""Dictionary of monthly parameters for negative binomial distributions to 
simulate dry spell durations. Parameters are N, P, and location. N must be 
greater than zero; P must be greater than zero and less than or equal to 1."""
WET_SPELL_PARAMS = { 1 : [ 13.6600677259703, 0.86232247884091, 1.0 ], 
                     2 : [ 13.6600677259703, 0.86232247884091, 1.0 ], 
                     3 : [ 13.6600677259703, 0.86232247884091, 1.0 ], 
                     4 : [ 13.6600677259703, 0.86232247884091, 1.0 ], 
                     5 : [ 1.25298881604319, 0.35829538705207, 1.0 ], 
                     6 : [ 3.17770018835852, 0.56614378824421, 1.0 ], 
                     7 : [ 6.14432354752617, 0.72705368149725, 1.0 ], 
                     8 : [ 4.15041657284395, 0.65798998844821, 1.0 ], 
                     9 : [ 3.36071126164268, 0.57870329082315, 1.0 ], 
                    10 : [ 5.74243527087449, 0.71165147517390, 1.0 ], 
                    11 : [ 24.1276171485544, 0.91070951660287, 1.0 ], 
                    12 : [ 24.1276171485544, 0.91070951660287, 1.0 ], }
"""Dictionary of monthly parameters for negative binomial distributions to 
simulate wet spell durations. Parameters are N, P, and location. N must be 
greater than zero; P must be greater than zero and less than or equal to 1."""

# Precipitation depth distribution parameters by month.
PRE_DEPTH_PARAMS = { 1 : [ 0.65332864702631, 0.917506695982624, 0.255, 12.5017962796866 ],
                     2 : [ 0.64065003400462, 0.996944682303184, 0.255, 9.19515277641484 ],
                     3 : [ 1.74535763261926, 0.532288752067096, 0.255, 1.8159951721309 ],
                     4 : [ 0.54472381545824, 1.11047428518533, 0.255, 14.5976138687417 ],
                     5 : [ 0.78700143940713, 0.88946839360371, 0.255, 15.8133817368788 ],
                     6 : [ 0.97597971990569, 0.77761884787869, 0.255, 8.95958471797809 ],
                     7 : [ 1.85378774990361, 0.54260354887422, 0.255, 2.12277306396721 ],
                     8 : [ 1.65589417057727, 0.53362927913926, 0.255, 2.5699135083752 ],
                     9 : [ 0.73019064112561, 0.97009834692482, 0.255, 14.987659963649 ],
                    10 : [ 1.84471294717675, 0.44458172746239, 0.255, 2.1168061936918 ],
                    11 : [ 1.99506284773963, 0.43996798799315, 0.255, 1.1327147086144 ],
                    12 : [ 1.60217109937658, 0.49653940880637, 0.255, 1.8966195212878 ], }
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

AVE_WET_TMAX_ADD = 0.5
"""Multiplier for average wet Tmax"""
AVE_DRY_TMAX_ADD = 0.5
"""Multiplier for average dry Tmax"""
AVE_WET_TMIN_ADD = 0.5
"""Multiplier for average wet Tmin"""
AVE_DRY_TMIN_ADD = 0.5
"""Multiplier for average dry Tmin"""

#-------------------------------------------------
# event dictionary
#    this one is for Blanco
EVENT_DICT = { "2-year" : [ int(2), [91.0, 111.0],], 
               "5-year" : [ int(5), [133.0, 166.0],],
               "10-year" : [ int(10), [170.0, 218.0],],
               "25-year" : [ int(25), [226.0, 299.0],],
               "50-year" : [ int(50), [275.0, 374.0],],
               "100-year" : [ int(100), [332.0, 461.0],], }
EVENT_KEYS = list( EVENT_DICT.keys() )


#EOF