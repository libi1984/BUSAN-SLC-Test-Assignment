import pathlib
from sarpy.io.complex.converter import open_complex 
import numpy as np
import matplotlib.pyplot as plt  

#Read Data
sicd_path = pathlib.Path("./IMG-VV-STRIXB-20220811T004713Z-SMSLC-SICD.nitf")
reader = open_complex(str(sicd_path))
print('image size as tuple ={}'.format(reader.get_data_size_as_tuple()))
slc = reader[:]
print(slc.dtype, slc.shape) # Shape shows row (range) and column (Azimuth) dimension

#Overview Image in dB scale
data_dB = 20 * np.log10(np.abs(slc))
min_dB = np.min(data_dB)
max_dB = np.max(data_dB)
#print(f"Min dB: {min_dB}")
#print(f"Max dB: {max_dB}")
plt.imshow(data_dB, cmap='gray')
plt.title('Strix-Stripmap dataset of Busan (Orginal)')
plt.xlabel('Azimuth') 
plt.ylabel('Range') 
plt.yticks(np.arange(0, 5000, 1000)) 
plt.colorbar(shrink=0.25)
plt.clim(min_dB/2,max_dB/2)
plt.show()