from smap_io import SPL3SMP_Ds
root_path = os.path.join('path', 'to', 'local', 'smap_data')
ds = SPL3SMP_Ds(root_path)
image = ds.read(datetime(2015, 4, 1))  # we can read the images by date
