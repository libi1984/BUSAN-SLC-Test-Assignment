# BUSAN-SLC-Test-Assignment
#The aim of this Script is to visualize a single-look-complex (SLC) dataset of Busan Harbor collected #by one of Synspective’s Strix satellites. 
#This scripts opens SLC data set, performs filtering using Hanning window and save the original and processed plots in Folder

##Important Libraries
  https://docs.python.org/3/library/pathlib.html
  https://sarpy.readthedocs.io/en/latest/examples/first_example.html#read-sicd-like-complex-pixel-data
  https://docs.scipy.org/doc/scipy/tutorial/fft.html#:~:text=To%20simplify%20working%20with%20the%20FFT%20functions,%20scipy%20provides%20the
##Process Flow
     -The range-azimuth data read from SLC data
     -Converting data from Time domain to Frequency Domain
     -Shifting the frequency spectrum centered with zero frequency
     -Filtering using Hanning Window
     -Inverse FFT 
     -Plot the data and analyse the result
##Contributors
    Libi Mol V A
    

