import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/melissa/neutrinos_4ferm/class_nu_int/output/Geff2_m-23_cl_lensed.dat', '/Users/melissa/neutrinos_4ferm/class_nu_int/output/lcdm_m-06_cl_lensed.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['Geff2_m-23_cl_lensed', 'lcdm_m-06_cl_lensed']

fig, ax = plt.subplots()
y_axis = ['TT']
tex_names = ['TT']
x_axis = 'l'
ax.set_xlabel('$\ell$', fontsize=16)
plt.show()