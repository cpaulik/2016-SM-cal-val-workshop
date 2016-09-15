from smap_io.interface import SMAPTs
smap_reader = SMAPTs('/data/smap_ts/', parameters='soil_moisture')
ts = smap_reader.read_ts(-73.96, 40.79)  # reading works by longitude and latitude
