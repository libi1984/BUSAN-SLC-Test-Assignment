import pathlib
from sarpy.io.complex.converter import open_complex   

sicd_path = pathlib.Path("./IMG-VV-STRIXB-20220811T004713Z-SMSLC-SICD.nitf")
reader = open_complex(str(sicd_path))
print('image size as tuple ={}'.format(reader.get_data_size_as_tuple()))
slc = reader[:]
print(slc.dtype, slc.shape)