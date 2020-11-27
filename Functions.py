from climada.hazard import TCTracks, TropCyclone, TCSurge
from climada.util.constants import WP_stormtracks, fl_mekong, fl_redriver
from Configuration import *
import numpy as np


def define_region_id(exp):

    import geopandas as gpd
    import pandas as pd
    import numpy as np

    mekong = gpd.read_file(fl_mekong)
    north = gpd.read_file(fl_redriver)

    mekong = mekong.to_crs(epsg=4326)
    north = north.to_crs(epsg=4326)

    south = mekong.envelope
    north = north.envelope

    in_south = []
    in_north = []

    points = exp.geometry
    for p in points:
        in_south.append(p.within(south[0]))
        in_north.append(p.within(north[0]))

    in_south = 1 * np.array(in_south)
    in_north = 2 * np.array(in_north)

    in_south_series = pd.Series(in_south)
    in_north_series = pd.Series(in_north)

    exp_id = in_south_series + in_north_series

    return exp_id


def tracks_ID(storm_range=hist_storms):

    import pandas as pd
    import numpy as np

    lon_min = storm_range.lon_min
    lat_min = storm_range.lat_min
    lon_max = storm_range.lon_max
    lat_max = storm_range.lat_max
    start_year = storm_range.start_year
    end_year = storm_range.end_year

    # lon_min, lat_min, lon_max, lat_max = 102, 8.5, 110, 23.5

    box = np.array([[lat_min, lat_max], [lon_min, lon_max]])
    #
    year_range = [start_year,end_year]

    # reading ibtracs (csv version)
    ibtracs = pd.read_csv(WP_stormtracks, skiprows=[1], delimiter=',',
                          usecols=['SID', 'NAME', 'ISO_TIME', 'LAT', 'LON', 'USA_WIND'])
    ibtracs[['LAT', 'LON', 'USA_WIND']] = ibtracs[['LAT', 'LON', 'USA_WIND']].apply(pd.to_numeric,
                                                                                    args={'errors': 'coerce'})
    ibtracs['ISO_TIME'] = pd.to_datetime(ibtracs['ISO_TIME'])

    # just setting time to the right format to perform comparisons (simpler version is to use int(ibtracs.SID[:4]) which is exactly the year of the event)
    time_bounds = (np.datetime64('{}-01-01T00:00:00.000000000'.format(year_range[0])),
                   np.datetime64('{}-01-01T00:00:00.000000000'.format(year_range[1] + 1)))

    # filters
    region = (ibtracs.LAT >= box[0, 0]) & (ibtracs.LAT <= box[0, 1]) & (ibtracs.LON >= box[1, 0]) & (
                ibtracs.LON <= box[1, 1])

    period = (ibtracs.ISO_TIME >= time_bounds[0]) & (ibtracs.ISO_TIME < time_bounds[1])

    # intensity = (ibtracs.USA_WIND >= min_wind)

    # gathering storm ids
    selection = region & period

    ID = np.unique(ibtracs.SID[selection])

    return list(ID)


def centr_gen(fl_centr):

    import geopandas as gpd
    import pandas as pd
    from climada.hazard import Centroids

    centr = Centroids()

    if os.path.isfile(fl_centr):

        centr.read_hdf5(fl_centr)

    else:

        print('creating centroids')

        mekong = gpd.read_file(fl_mekong)
        mekong = mekong.to_crs(epsg=4326)
        south = mekong.envelope

        from climada.util.coordinates import dist_to_coast
        from climada.entity import LitPop
        import numpy as np

        EXP_1km = LitPop()
        EXP_1km.set_country(countries = country, res_arcsec= 30, reference_year=2020, fin_mode='norm')
        EXP_1km.set_geometry_points()
        EXP_1km.check()

        coast_bool = dist_to_coast(EXP_1km.centroid) < coast_range

        value_bool = np.percentile(EXP_1km.values[:,0], percentile) < EXP_1km.values[:,0]

        points = EXP_1km.geometry

        mekong_bool = []

        for p in points:

            mekong_bool.append(p.within(south[0]))

        mekong_bool = np.asarray(mekong_bool)

        fine_res = coast_bool | value_bool | mekong_bool

        fine_lat = EXP_1km['latitude'][fine_res]

        fine_lon = EXP_1km['longitude'][fine_res]

        del EXP_1km

        EXP_5km = LitPop()
        EXP_5km.set_country(countries = country, res_arcsec= 150, reference_year=2020, fin_mode='norm')
        EXP_5km.set_geometry_points()
        EXP_5km.check()

        coarse_lat = EXP_5km['latitude']

        coarse_lon = EXP_5km['longitude']

        lat = pd.concat([fine_lat,coarse_lat],ignore_index=True)

        lat = lat.to_numpy()

        lon = pd.concat([fine_lon,coarse_lon],ignore_index=True)

        lon = lon.to_numpy()

        del EXP_5km

        centr.set_lat_lon(lat,lon,crs=mekong.crs)

        centr.set_geometry_points()

        centr.check()

        centr.write_hdf5(fl_centr)

    return centr


def intro_haz_tc(fl_haz_tc, cc, number_random_walk = number_rdw):

    haz_tc = TropCyclone()

    if os.path.isfile(fl_haz_tc):

        haz_tc.read_hdf5(fl_haz_tc)

    elif cc == 0:

        sel_ibtracs = TCTracks()

        ID = tracks_ID()

        sel_ibtracs.read_ibtracs_netcdf(storm_id=ID)

        print('tracks selected')

        sel_ibtracs.calc_random_walk(ens_size=number_random_walk)

        print('probabilistic events generated')

        sel_ibtracs.equal_timestep()

        print('equal timestep')

        centr = centr_gen(fl_centroids)

        haz_tc.set_from_tracks(sel_ibtracs, centr)

        print('HAZ finished')

        haz_tc.check()

        haz_tc.write_hdf5(fl_haz_tc)

    elif cc == 45:

        haz_tc_cc0 = intro_haz_tc(fl_HAZ_tc_cc0, 0)

        haz_tc = haz_tc_cc0.set_climate_scenario_knu(ref_year=horizon,rcp_scenario=45)

        haz_tc.write_hdf5(fl_haz_tc)

    elif cc == 85:

        haz_tc_cc0 = intro_haz_tc(fl_HAZ_tc_cc0, 0)

        haz_tc = haz_tc_cc0.set_climate_scenario_knu(ref_year=horizon, rcp_scenario=85)

        haz_tc.write_hdf5(fl_haz_tc)

    return haz_tc

def intro_haz_ts(fl_haz_ts, fl_haz_tc, cc):

    haz_ts = TCSurge()

    if os.path.isfile(fl_haz_ts):

        haz_ts.read_hdf5(fl_haz_ts)

    else:

        haz_tc = intro_haz_tc(fl_haz_tc,cc)

        haz_ts.set_from_winds(haz_tc, dem_product='SRTM3',add_sea_level_rise=sea_level_rise[cc])

        haz_ts.write_hdf5(fl_haz_ts)

    return haz_ts
