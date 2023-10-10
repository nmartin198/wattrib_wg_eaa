# -*- coding: utf-8 -*-
"""
.. module:: WG_SpellLength
   :platform: Windows, Linux
   :synopsis: Classes and logic to deal with spell lengths

.. moduleauthor:: Nick Martin <nmartin@swri.org>

Spell lengths are handled with negative binomial distributions
"""
# imports
import numpy as np
from scipy import stats as scstats


class CreateDistError(Exception):
    """Custom exception error for when something happens with a distribution
    """
    def __init__(self, arg):
        self.args = arg

class NegBinomial(object):
    """Negative binomial distribution object for use in the Weather 
    Generator. Negative binomial distributions are used for spell lengths.
    The SciPy negative binomial distribution is defined by two shape parameters 
    N and P. N is the number of successes, and P is the probability of a 
    single success. N must be greater than zero, and P is greater than zero 
    and less than or equal to 1."""
    
    def __init__(self, N, P, location=0, name="Custom negative binomial" ):
        """Override of default initialization method"""
        super().__init__()
        # do some checks and assign our properties
        if not isinstance( N, float ):
            ErrorMsg = "N must be a float!!!"
            raise CreateDistError( ErrorMsg )
        if not isinstance( P, float ):
            ErrorMsg = "P must be a float!!!"
            raise CreateDistError( ErrorMsg )
        # check the ranges
        if ( N <= 0.0 ) or ( N > 1000.0 ):
            ErrorMsg = "N greater than 1000.0 or less than 0.0!!!"
            raise CreateDistError( ErrorMsg )
        if ( P <= 0.0 ) or ( P >= 10 ):
            ErrorMsg = "P greater >= 1.0 or <= 0.0!!!"
            raise CreateDistError( ErrorMsg )
        self.name = name
        self.nbinom = scstats.nbinom( N, P, loc=location )
    
    def ranval1( self, rstate):
        """With the specified val between 0.0 and 1.0, which is essentially
        a probability, return the corresponding value from the cdf.
        
        Args:
            rstate (np.random_state): the random state for the sampler
            
        Returns:
            numd (int): the sampled number of days for the spell length
            
        """
        numda = self.nbinom.rvs( size=1, random_state=rstate )
        numd = numda[0]
        return numd
    
    def ranArray( self, asize, rstate ):
        """Sample asize values and put them in an array
        
        Args:
            asize (int) = size of the return array
            rstate (np.random_state): the random state for the sampler
            
        Returns:
            numda (np.array): the corresponding array of spell lengths
            
        """
        numda = self.nbinom.rvs( size=asize, random_state=rstate )
        return numda


class WetStateSampler(object):
    """A wet state probability sampler. Use this to track the random
    state and produce reproduceable sampling sequences. This uses the numpy
    random.uniform distribution to draw the random numbers.
    """
    
    def __init__( self, wet_state_seed=None ):
        """Default initialization method"""
        super().__init__()
        self.ranstate = np.random.RandomState(seed=wet_state_seed)
    
    def getSingleVal( self, ):
        """Produce a single value from the random sampler from a uniform
        distribution between [0.0 - 1.0]
        """
        return self.ranstate.uniform(low=0.0, high=1.0)
    
    def getSampleArray( self, N ):
        """Produce a sample of random numbers between 0.0 and 1.0 of size N.
        Will return a numpy array"""
        return self.ranstate.uniform(low=0.0, high=1.0, size=N)

class DryStateSampler(object):
    """A dry state probability sampler. Use this to track the random
    state and produce reproduceable sampling sequences. This uses the numpy
    random.uniform distribution to draw the random numbers.
    """
    
    def __init__( self, dry_state_seed=None ):
        """Default initialization method"""
        super().__init__()
        self.ranstate = np.random.RandomState(seed=dry_state_seed)
    
    def getSingleVal( self, ):
        """Produce a single value from the random sampler from a uniform
        distribution between [0.0 - 1.0]
        """
        return self.ranstate.uniform(low=0.0, high=1.0)
    
    def getSampleArray( self, N ):
        """Produce a sample of random numbers between 0.0 and 1.0 of size N.
        Will return a numpy array"""
        return self.ranstate.uniform(low=0.0, high=1.0, size=N)

#EOF