import pandas as pd
from fastmeteo import Grid

mmg = Grid(local_store="/tmp/era5-zarr")

flight = pd.DataFrame(
    {
        "timestamp": ["2021-10-12T01:10:00", "2021-10-12T01:20:00"],
        "icao24": ["abc123", "abc123"],
        "latitude": [40.3, 42.5],
        "longitude": [4.2, 6.6],
        "altitude": [25_000, 30_000],
    }
)

print(flight)

flight_new = mmg.interpolate(flight)

print(flight_new)
