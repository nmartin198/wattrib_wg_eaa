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
OUT_LABEL = r'Med-Cib'
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
#LAT_DEG = 30.018 # Blanco
#LAT_DEG = 29.741 # Cibolo
#LAT_DEG = 29.678 # Frio
#LAT_DEG = 29.985 # Guadalupe
LAT_DEG = 29.627 # Med-Cib
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
bas = "Med-Cib"
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
A_DATA_LIST = [ [ 0.5445484, 0.21648021 ],
                [ -0.02866402, 0.69770329 ], ]
"""A matrix for Tmax and Tmin"""
InFiler = os.path.normpath( os.path.join( CUR_DIR, "Inputs",
                        "OWeath_Rho0_1991-2020_DFDict.pkl" ) )
with open( InFiler, 'rb' ) as IF:
    InDictM0 = pickle.load( IF )
# end with
OW_M0_IN = InDictM0[bas]
"""M0 matrix for calculating daily error or residual term"""
B_DATA_LIST = [ [ 0.73052685, 0.0 ],
                [ 0.26161958, 0.68176198 ], ]
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
DRY_SPELL_PARAMS = { 1 : [ 3.501605917510033, .3366499191594062, 2.0 ],
                     2 : [ 5.184066480542836, .1662888843175642, 2.0 ],
                     3 : [ 3.289123474404067, .4669919419767528, 2.0 ],
                     4 : [ 2.500000000000000, .3440511978740193, 2.0 ],
                     5 : [ 6.071205219637568, .3148675448264468, 2.0 ],
                     6 : [ 4.815137772933390, .3047337500796121, 2.0 ],
                     7 : [ 6.958242648760296, .3222360064942200, 2.0 ],
                     8 : [ 2.531647955103439, .5500000000000000, 2.0 ],
                     9 : [ 3.000000000000000, .2009189340462274, 2.0 ],
                    10 : [ 4.979583211786568, .2239539692501011, 2.0 ],
                    11 : [ 3.177340932630381, .1574619830890345, 2.0 ],
                    12 : [ 3.238967311333946, .4723063205452868, 2.0 ], }
"""Dictionary of monthly parameters for negative binomial distributions to
simulate dry spell durations. Parameters are N, P, and location. N must be
greater than zero; P must be greater than zero and less than or equal to 1."""
WET_SPELL_PARAMS = { 1 : [ 4.128798243711389, .5745686173369864, 1.0 ],
                     2 : [ 2.758503637066464, .7791685600340230, 1.0 ],
                     3 : [ 2.215826255401915, .5186182102804840, 1.0 ],
                     4 : [ 2.869991028099904, .6739318211574176, 1.0 ],
                     5 : [ 3.884262160974557, .5449186359007642, 1.0 ],
                     6 : [ 3.177646039463023, .3925383980953268, 1.0 ],
                     7 : [ 1.497842885735523, .3468858563015942, 1.0 ],
                     8 : [ 1.091910339795442, .4416377523884613, 1.0 ],
                     9 : [ 2.237601018720186, .3073927144358665, 1.0 ],
                    10 : [ 2.707534717488421, .5206688072266190, 1.0 ],
                    11 : [ 2.389189982482549, .6950180850600726, 1.0 ],
                    12 : [ 3.253597068240374, .6565415000284840, 1.0 ], }
"""Dictionary of monthly parameters for negative binomial distributions to
simulate wet spell durations. Parameters are N, P, and location. N must be
greater than zero; P must be greater than zero and less than or equal to 1."""
 
# Precipitation depth distribution parameters by month.
PRE_DEPTH_PARAMS = { 1 : [ .7454465477550128, 1.316444255197120, 0.255, 5.730116886223030 ],
                     2 : [ 1.076805970167109, 1.410146500451674, 0.255, 6.979842942350968 ],
                     3 : [ 1.334306931910491, 1.243420794723613, 0.255, 9.445404721505086 ],
                     4 : [ 1.307999721965959, 1.194785619131917, 0.255, 7.867573701972114 ],
                     5 : [ 1.120198946835361, 1.635628370706010, 0.255, 6.949813979400344 ],
                     6 : [ 1.600000000000000, 1.364081918876445, 0.255, 10.99034043749953 ],
                     7 : [ 1.093107970443279, 1.547370757619612, 0.255, 10.88655566256303 ],
                     8 : [ .8838464884576280, 1.800131791011618, 0.255, 8.957045674000534 ],
                     9 : [ 1.481065248203688, 1.488816859756280, 0.255, 10.82026392422729 ],
                    10 : [ 1.600000000000000, 1.338759604626117, 0.255, 10.00000000000000 ],
                    11 : [ .7657349528419384, 1.477793266613445, 0.255, 6.985826524808912 ],
                    12 : [ .8251251418303616, 1.265129356332888, 0.255, 5.728029122926214 ], }
"""Dictionary of monthly parameters for the generalized, two parameter gamma
distributions. The distribution parameters are 0 - a, 1 - c, 2 - loc, and
3 - scale. a must be greater than zero, and c must not be equal to zero."""
 
# maximum daily precipitation depth that can be used for each calendar month.
MON_MAX_PP = { 1 : 22.8,
               2 : 23.0,
               3 : 27.9,
               4 : 38.1,
               5 : 40.3,
               6 : 39.1,
               7 : 36.9,
               8 : 40.5,
               9 : 44.2,
               10 : 63.8,
               11 : 32.4,
               12 : 27.8, }
"""Maximum daily precipitation depth to allow for sampling from 2 parameter
gamma distributions. Us the 0.95 cumulative probability from the wet day
depth distributions for this."""
 
AVE_WET_TMAX_ADD = 6.923498211263358
"""Multiplier for average wet Tmax"""
AVE_DRY_TMAX_ADD = 8.000000000000000
"""Multiplier for average dry Tmax"""
AVE_WET_TMIN_ADD = .9279728175558450
"""Multiplier for average wet Tmin"""
AVE_DRY_TMIN_ADD = .8799171380943790
"""Multiplier for average dry Tmin"""
 
#-------------------------------------------------
# event dictionary
#    this one is for Med-Cib
EVENT_DICT = { "2-year" : [ int(2), [91.0, 170.5560502589862],],
               "5-year" : [ int(5), [133.0, 250.0000000000000],],
               "10-year" : [ int(10), [169.0, 291.8101832824848],],
               "25-year" : [ int(25), [221.0, 319.5495576499549],],
               "50-year" : [ int(50), [265.0, 455.4028817464568],],
               "100-year" : [ int(100), [317.0, 476.3970716976496],], }
EVENT_KEYS = list( EVENT_DICT.keys() )
 
 
#EOF
