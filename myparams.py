# myparams.py

# specify the params that are fixed throughout the evolution

import numpy as np

# Input parameters for grid and evolution here
N_r = 120 # num points on physical grid
N_t = 101 # time resolution (only for outputs, not for integration)
R = 60 # Maximum outer radius
T = 3.0 # Maximum evolution time

# coefficients for bssn and gauge evolution
eta = 1.0 # 1+log slicing damping coefficient
sigma = 1.0 # kreiss-oliger damping coefficient
eight_pi_G = 8.0 * np.pi * 1.0 # Newtons constant, we take G=c=1
scalar_mu = 1.0 # this is an inverse length scale related to the scalar compton wavelength

# These values are hardcoded or calculated from the inputs above
# so should not be changed
dx = R/N_r
dt = T/N_t
num_ghosts = 3
N = N_r + num_ghosts * 2 
r = np.linspace(-(num_ghosts-0.5)*dx, R+(num_ghosts-0.5)*dx, N)
t = np.linspace(0, T-dt, N_t)
oneoverdx  = 1.0 / dx
oneoverdxsquared = oneoverdx * oneoverdx