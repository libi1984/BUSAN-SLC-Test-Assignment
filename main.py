##################################################
#The aim of this Script is to visualize a single-look-complex (SLC) dataset of Busan Harbor collected
#by one of Synspective’s Strix satellites. 
#This scripts opens SLC data set, performs filtering using Hanning window and save the original and processed plots in Folder
#Author:-Libi Mol V. A
#Date:-13th September 2024
##################################################
import pathlib
from sarpy.io.complex.converter import open_complex 
import numpy as np
import matplotlib.pyplot as plt  
import scipy.fftpack as fft
from datetime import datetime

#Functions for Plotting the original and zoomed data
def fig_change(axis, image, color_limit, fig_shrink, title, x_label, y_label, x_ticks_ticks=None, y_ticks_ticks=None, x_ticks_labels=None, y_ticks_labels=None):
        axis.set_title(title)
        axis.set_xlabel(x_label)
        axis.set_ylabel(y_label)
        if x_ticks_labels is not None:
                axis.set_xticks(ticks=x_ticks_ticks, labels=x_ticks_labels)
        elif x_ticks_ticks is not None:
                axis.set_xticks(ticks=x_ticks_ticks)
        if y_ticks_labels is not None:
                axis.set_yticks(ticks=y_ticks_ticks, labels=y_ticks_labels)
        elif y_ticks_ticks is not None:
                axis.set_yticks(ticks=y_ticks_ticks)
        image.set_clim(color_limit[0], color_limit[1])
        cbar =fig.colorbar(image, ax=axis,shrink=fig_shrink)
        cbar.set_label('Power (dB)')

#Folders for SLC data and Plots
data_folder = "SLC_data"    #SICD SLC data folder
save_folder = "Saved_Plots" #Saved Plots

#Data plot File name creation
get_date = lambda: datetime.now().strftime("%Y%m%d_%H%M%S_") #to get the date and time 
concat_date_file_path = lambda name: pathlib.Path(save_folder, (get_date()+name)) #to put the date and time in File name to differentiate different plots


#Read Data
sicd_path = pathlib.Path(data_folder, "IMG-VV-STRIXB-20220811T004713Z-SMSLC-SICD.nitf")
reader = open_complex(str(sicd_path))
print('image size as tuple ={}'.format(reader.get_data_size_as_tuple()))
slc = reader[:]
print(slc.dtype, slc.shape) # dtype shows data format, Shape shows row (range) and column (Azimuth) dimension


#FFT Calculation and Windowing
window_data = np.empty_like(slc)
for i in range(slc.shape[1]):
        # FFT in each rangeline and shift  zero frequency in center
        fft_transform = np.fft.fftshift(fft.fft(slc[:,i ]))
        # Create hanning window as specified in Asssignment
        window = np.hanning(slc.shape[0])
        Spec_hanning_window = window ** 3
        #Apply Window
        window_fft = fft_transform * Spec_hanning_window
        # Shifting the frequency spectrum back and IFFT
        window_data[:,i ] = np.fft.ifft(np.fft.ifftshift(window_fft)) 

#Overview Image in dB scale
 #Based on nitf document from NSG, Image Pixel power=real(row,col)^2+imag(row,col)^2
print(f"Min dB: {np.min(20 * np.log10(np.abs(slc)))}")
print(f"Max dB: {np.max(20 * np.log10(np.abs(slc)))}")

#Plotting Original and Processed data together
#original data
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.27, 11.69))
im1 = ax1.imshow((20 * np.log10(np.abs(slc))), cmap='bone')
color_limit = (-40, 20)#limits taken for better Picture Clarity (when MindB, MaxdB scale is used picture quality is not good)
fig_change(axis=ax1, image=im1, title='StrixB:Stripmap dataset of Busan(Original)', 
            x_label='Azimuth', y_label='Range',
            y_ticks_ticks=np.arange(0, 5000, 1000), 
            color_limit=color_limit, fig_shrink=0.25)
#oFiltered data
im2=plt.imshow(20 * np.log10(np.abs(window_data)), cmap='bone')
fig_change(axis=ax2, image=im2, title='StrixB:Stripmap dataset of Busan(Filtered)', 
            x_label='Azimuth', y_label='Range',
            y_ticks_ticks=np.arange(0, 5000, 1000), 
            color_limit=color_limit, fig_shrink=0.25)
#Saving the Figure
plt.savefig(concat_date_file_path('StrixB_data_Busan_Original_and_Filtered.png'))

#Zoomed Plots of Busan Harbor
range_st, range_end = 1100, 2100 #range start and end given in assignment
az_st, az_end = 13100, 14500  #azimuth start and end given in assignment
#Busan Harbor data -Origina and Filtered
zoomed_data_org = slc[range_st:range_end, az_st:az_end]
zoomed_data_Filt = window_data[range_st:range_end, az_st:az_end]
#Zoomed plot of Original data
fig, (ax3, ax4) = plt.subplots(2, 1, figsize=(8.27, 11.69))
im3 = ax3.imshow(20 * np.log10(np.abs(zoomed_data_org)), cmap='bone')
fig_change(axis=ax3, image=im3, title='StrixB:Stripmap dataset of Busan Harbor(Original)', 
            x_label='Azimuth', y_label='Range',
            x_ticks_ticks=np.arange(0, az_end - az_st, step=200), x_ticks_labels=np.arange(az_st, az_end, step=200),
            y_ticks_ticks=np.arange(0, range_end - range_st, step=200), y_ticks_labels=np.arange(range_st, range_end, step=200),
            color_limit=color_limit, fig_shrink=1)
#Zommed plot of Filtered Data
im4=plt.imshow(20 * np.log10(np.abs(zoomed_data_Filt)), cmap='bone')
fig_change(axis=ax4, image=im4, title='StrixB:Stripmap dataset of Busan Harbor(Filtered)', 
            x_label='Azimuth', y_label='Range',
            x_ticks_ticks=np.arange(0, az_end - az_st, step=200), x_ticks_labels=np.arange(az_st, az_end, step=200),
            y_ticks_ticks=np.arange(0, range_end - range_st, step=200), y_ticks_labels=np.arange(range_st, range_end, step=200),
            color_limit=color_limit, fig_shrink=1)
#Save the Busan Harbor Data Figure
plt.savefig(concat_date_file_path('StrixB_data_Busan_Harbor_zoomed_Original_and_Filtered.png'))
