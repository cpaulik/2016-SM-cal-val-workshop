from smap_io.interface import SMAPTs
ds = SMAPTs('/data/smap_ts/', parameters='soil_moisture')
ts = ds.read_ts(-73.96, 40.79)  # reading works by longitude and latitude
