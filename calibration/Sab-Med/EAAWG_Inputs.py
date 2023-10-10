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
OUT_LABEL = r'Sab-Med'
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
LAT_DEG = 29.574 # Sab-Med
#LAT_DEG = 29.617 # Sabinal
"""Latitude in degrees for the basin centroid"""
 
# parameters - usually do not need to be changed
WET_STATE = "wet"
"""Keyword for wet state"""
DRY_STATE = "dry"
"""Keyword for dry state"""
 
#------------------------------------------------------------------------
# Other weather parameter model files
bas = "Sab-Med"
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
A_DATA_LIST = [ [ 0.57127776, 0.19579602 ],
                [ -0.03851124, 0.69469401 ], ]
"""A matrix for Tmax and Tmin"""
InFiler = os.path.normpath( os.path.join( CUR_DIR, "Inputs",
                        "OWeath_Rho0_1991-2020_DFDict.pkl" ) )
with open( InFiler, 'rb' ) as IF:
    InDictM0 = pickle.load( IF )
# end with
OW_M0_IN = InDictM0[bas]
"""M0 matrix for calculating daily error or residual term"""
B_DATA_LIST = [ [ 0.73505987, 0.0 ],
                [ 0.19766135, 0.70680104 ], ]
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
DRY_SPELL_PARAMS = { 1 : [ 3.740777923199010, .3249969568679143, 2.0 ],
                     2 : [ 5.574998597136796, .2024371580290416, 2.0 ],
                     3 : [ 3.635957054530490, .4189167334469213, 2.0 ],
                     4 : [ 2.500000000000000, .2918511992496175, 2.0 ],
                     5 : [ 6.222437117783766, .3349475643263091, 2.0 ],
                     6 : [ 6.576672755838162, .3247584415632807, 2.0 ],
                     7 : [ 6.257843561612704, .3623641318953476, 2.0 ],
                     8 : [ 3.325060348161774, .5072630161715434, 2.0 ],
                     9 : [ 3.709588026884284, .2446541390233758, 2.0 ],
                    10 : [ 5.369718054868170, .2119402142967543, 2.0 ],
                    11 : [ 3.432215392353454, .1674967802614759, 2.0 ],
                    12 : [ 3.569966023772638, .3462477135588231, 2.0 ], }
"""Dictionary of monthly parameters for negative binomial distributions to
simulate dry spell durations. Parameters are N, P, and location. N must be
greater than zero; P must be greater than zero and less than or equal to 1."""
WET_SPELL_PARAMS = { 1 : [ 4.597905412516718, .5305756879496768, 1.0 ],
                     2 : [ 2.130935212019002, .7514410461848200, 1.0 ],
                     3 : [ 1.764357052432383, .4553070425809920, 1.0 ],
                     4 : [ 2.713924404763747, .6259102385237850, 1.0 ],
                     5 : [ 3.408502140478791, .5578382432867716, 1.0 ],
                     6 : [ 3.195005890179601, .3384828818564932, 1.0 ],
                     7 : [ 2.105870837465084, .4446679798931848, 1.0 ],
                     8 : [ 1.567762775253444, .5271015203701312, 1.0 ],
                     9 : [ 2.590762396982343, .3242143927492383, 1.0 ],
                    10 : [ 2.288350662340187, .5362206280064838, 1.0 ],
                    11 : [ 2.026163271166753, .6736758452568744, 1.0 ],
                    12 : [ 2.072702200963381, .7674020050649906, 1.0 ], }
"""Dictionary of monthly parameters for negative binomial distributions to
simulate wet spell durations. Parameters are N, P, and location. N must be
greater than zero; P must be greater than zero and less than or equal to 1."""
 
# Precipitation depth distribution parameters by month.
PRE_DEPTH_PARAMS = { 1 : [ .7965001452029394, 1.381951230139294, 0.255, 5.491626186645594 ],
                     2 : [ 1.072480964462015, 1.426195277541088, 0.255, 6.382969242126650 ],
                     3 : [ 1.230354530867675, 1.232827183337322, 0.255, 8.972562680855392 ],
                     4 : [ 1.158584724452124, 1.177691318514651, 0.255, 7.145902999683076 ],
                     5 : [ 1.187092247348352, 1.523687150096653, 0.255, 7.653922255320344 ],
                     6 : [ 1.493464309801131, 1.422004737427071, 0.255, 10.23688117879416 ],
                     7 : [ 1.043953881885999, 1.490334982619947, 0.255, 9.938928950793744 ],
                     8 : [ .8472653844734380, 1.655370807853825, 0.255, 8.356317124525122 ],
                     9 : [ 1.123644843965409, 1.405264879138407, 0.255, 10.33846070855050 ],
                    10 : [ 1.600000000000000, 1.290858228150316, 0.255, 10.00000000000000 ],
                    11 : [ .8470952384546920, 1.384754227935993, 0.255, 7.058726331526518 ],
                    12 : [ .7632168566732558, 1.344801150324949, 0.255, 5.611836639914578 ], }
"""Dictionary of monthly parameters for the generalized, two parameter gamma
distributions. The distribution parameters are 0 - a, 1 - c, 2 - loc, and
3 - scale. a must be greater than zero, and c must not be equal to zero."""
 
# maximum daily precipitation depth that can be used for each calendar month.
MON_MAX_PP = { 1 : 25.9,
               2 : 23.7,
               3 : 35.1,
               4 : 33.8,
               5 : 46.3,
               6 : 38.4,
               7 : 41.9,
               8 : 45.1,
               9 : 41.3,
               10 : 44.8,
               11 : 27.5,
               12 : 28.2, }
"""Maximum daily precipitation depth to allow for sampling from 2 parameter
gamma distributions. Us the 0.95 cumulative probability from the wet day
depth distributions for this."""
 
AVE_WET_TMAX_ADD = 5.032641648009198
"""Multiplier for average wet Tmax"""
AVE_DRY_TMAX_ADD = 7.003640577461118
"""Multiplier for average dry Tmax"""
AVE_WET_TMIN_ADD = .8771622493324812
"""Multiplier for average wet Tmin"""
AVE_DRY_TMIN_ADD = .9207373933390424
"""Multiplier for average dry Tmin"""
 
#-------------------------------------------------
# event dictionary
#    this one is for Sab-Med
EVENT_DICT = { "2-year" : [ int(2), [94.0, 155.6121025105842],],
               "5-year" : [ int(5), [138.0, 250.0000000000000],],
               "10-year" : [ int(10), [175.0, 260.3631051404210],],
               "25-year" : [ int(25), [231.0, 286.7491007233371],],
               "50-year" : [ int(50), [280.0, 419.8114118549458],],
               "100-year" : [ int(100), [337.0, 515.5074401622208],], }
EVENT_KEYS = list( EVENT_DICT.keys() )
 
 
#EOF
