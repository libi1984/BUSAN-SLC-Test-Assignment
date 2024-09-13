# BUSAN-SLC-Test-Assignment
#The aim of this Script is to visualize a single-look-complex (SLC) dataset of Busan Harbor collected #by one of Synspective’s Strix satellites. 
#This scripts opens SLC data set, performs filtering using Hanning window and save the original and processed plots in Folder

##Important Libraries
  https://docs.python.org/3/library/pathlib.html
  https://sarpy.readthedocs.io/en/latest/examples/first_example.html#read-sicd-like-complex-pixel-data
  https://docs.scipy.org/doc/scipy/tutorial/fft.html#:~:text=To%20simplify%20working%20with%20the%20FFT%20functions,%20scipy%20provides%20the

 #How to run the script
#Download and save the data in Folder "SLC_Folder" in same directory
#Create a folder "Saved_plots" in same directory
#Run the script
##Process Flow
     -The range-azimuth data read from SLC data
     -Converting data from Time domain to Frequency Domain
     -Shifting the frequency spectrum centered with zero frequency
     -Filtering using Hanning Window
     -Inverse FFT 
     -Plot the data and analyse the result
#The Original and Post processed images will be save in Folder    "Saved_plots". One plot shows the Original and Post processed datain entire range and azimuth. Second plot shows the zoomed data for Busan Harbor 
     
##Contributors
    Libi Mol V A
    

