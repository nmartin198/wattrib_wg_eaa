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
OUT_LABEL = r'Nueces'
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
LAT_DEG = 29.701 # Nueces
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
bas = "Nueces"
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
A_DATA_LIST = [ [ 0.56509443, 0.22120385 ],
                [ -0.038851, 0.70448358 ], ]
"""A matrix for Tmax and Tmin"""
InFiler = os.path.normpath( os.path.join( CUR_DIR, "Inputs",
                        "OWeath_Rho0_1991-2020_DFDict.pkl" ) )
with open( InFiler, 'rb' ) as IF:
    InDictM0 = pickle.load( IF )
# end with
OW_M0_IN = InDictM0[bas]
"""M0 matrix for calculating daily error or residual term"""
B_DATA_LIST = [ [ 0.71990138, 0.0 ],
                [ 0.19895933, 0.69818032 ], ]
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
DRY_SPELL_PARAMS = { 1 : [ 4.128459360409045, .2837919289923093, 2.0 ],
                     2 : [ 5.265718173405454, .1970069159562905, 2.0 ],
                     3 : [ 3.817495653906875, .3413168548320703, 2.0 ],
                     4 : [ 3.097871489691143, .3154228521932192, 2.0 ],
                     5 : [ 6.534651057188388, .3166460984565947, 2.0 ],
                     6 : [ 5.472874193941606, .3071757118119164, 2.0 ],
                     7 : [ 6.085299062657204, .3610418972932788, 2.0 ],
                     8 : [ 3.057606824160712, .4844182210951020, 2.0 ],
                     9 : [ 4.060470501592422, .2466128511643998, 2.0 ],
                    10 : [ 4.528817499763006, .2157166804059844, 2.0 ],
                    11 : [ 3.377312650836125, .1710171219441572, 2.0 ],
                    12 : [ 4.369109463820790, .3802447744248852, 2.0 ], }
"""Dictionary of monthly parameters for negative binomial distributions to
simulate dry spell durations. Parameters are N, P, and location. N must be
greater than zero; P must be greater than zero and less than or equal to 1."""
WET_SPELL_PARAMS = { 1 : [ 4.356163627821460, .6688006691830348, 1.0 ],
                     2 : [ 2.282930976508177, .6874939392590562, 1.0 ],
                     3 : [ 1.645901764313229, .4955621353348984, 1.0 ],
                     4 : [ 2.291162794438903, .6879031403501756, 1.0 ],
                     5 : [ 3.624910546552453, .5918657263229018, 1.0 ],
                     6 : [ 2.820418690212256, .4191310821931794, 1.0 ],
                     7 : [ 1.789005567720359, .4647073540133074, 1.0 ],
                     8 : [ 1.789221474283539, .6288625070880412, 1.0 ],
                     9 : [ 2.389504477046086, .3721916153491064, 1.0 ],
                    10 : [ 2.323075473414931, .5621673703528366, 1.0 ],
                    11 : [ 2.136518215336479, .6472412726107660, 1.0 ],
                    12 : [ 2.385152481083520, .7126395194411822, 1.0 ], }
"""Dictionary of monthly parameters for negative binomial distributions to
simulate wet spell durations. Parameters are N, P, and location. N must be
greater than zero; P must be greater than zero and less than or equal to 1."""
 
# Precipitation depth distribution parameters by month.
PRE_DEPTH_PARAMS = { 1 : [ .7679515623877258, 1.364952504860196, 0.255, 5.246224242931976 ],
                     2 : [ .9932444191324498, 1.391853450425920, 0.255, 6.104480106103344 ],
                     3 : [ 1.082059879273105, 1.340696308524367, 0.255, 8.091008120914362 ],
                     4 : [ 1.047618318553918, 1.232068192351620, 0.255, 6.771822004100686 ],
                     5 : [ 1.147222805680636, 1.604204457107761, 0.255, 7.290078443844240 ],
                     6 : [ 1.440592216356894, 1.408415610990605, 0.255, 10.02583295096071 ],
                     7 : [ 1.006386752893395, 1.509236656582419, 0.255, 9.508316954175482 ],
                     8 : [ .8642490098494158, 1.624545274018433, 0.255, 8.689440525026800 ],
                     9 : [ 1.072619232301736, 1.457313266645617, 0.255, 9.492978384125492 ],
                    10 : [ 1.555647451400388, 1.298923743636142, 0.255, 9.640798925349030 ],
                    11 : [ .7766225253900610, 1.390250197428879, 0.255, 6.779705879019698 ],
                    12 : [ .7685726862075082, 1.351094057841565, 0.255, 5.363589029390388 ], }
"""Dictionary of monthly parameters for the generalized, two parameter gamma
distributions. The distribution parameters are 0 - a, 1 - c, 2 - loc, and
3 - scale. a must be greater than zero, and c must not be equal to zero."""
 
# maximum daily precipitation depth that can be used for each calendar month.
MON_MAX_PP = { 1 : 20.3,
               2 : 19.3,
               3 : 28.7,
               4 : 28.0,
               5 : 32.3,
               6 : 35.0,
               7 : 30.0,
               8 : 31.5,
               9 : 38.4,
               10 : 45.6,
               11 : 32.8,
               12 : 22.8, }
"""Maximum daily precipitation depth to allow for sampling from 2 parameter
gamma distributions. Us the 0.95 cumulative probability from the wet day
depth distributions for this."""
 
AVE_WET_TMAX_ADD = 5.116794262007600
"""Multiplier for average wet Tmax"""
AVE_DRY_TMAX_ADD = 6.069547098573634
"""Multiplier for average dry Tmax"""
AVE_WET_TMIN_ADD = .8499020119243158
"""Multiplier for average wet Tmin"""
AVE_DRY_TMIN_ADD = .8673081743287436
"""Multiplier for average dry Tmin"""
 
#-------------------------------------------------
# event dictionary
#    this one is for Nueces
EVENT_DICT = { "2-year" : [ int(2), [87.0, 148.6963349373110],],
               "5-year" : [ int(5), [130.0, 240.3813949000024],],
               "10-year" : [ int(10), [166.0, 252.4510059134694],],
               "25-year" : [ int(25), [221.0, 288.5689817964987],],
               "50-year" : [ int(50), [268.0, 419.6183139795467],],
               "100-year" : [ int(100), [323.0, 506.0534865497088],], }
EVENT_KEYS = list( EVENT_DICT.keys() )
 
 
#EOF
