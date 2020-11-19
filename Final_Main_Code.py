import numpy as np
from matplotlib import colors
from Configuration import *

## Exposure

# Houses

from climada.entity import Exposures, LitPop

# fl_EXP_houses = os.path.join(project_folder, 'EXP_housesGAR15LP_id_' + country + file_identifier + '.hdf5')
#
# EXP_houses = LitPop()
#
# if os.path.isfile(fl_EXP_houses):
#
#     EXP_houses.read_hdf5(fl_EXP_houses)
#
# else:
#     EXP_houses.set_country(countries=country, res_arcsec=30, reference_year=2020, fin_mode='norm')
#     EXP_houses['value'] = EXP_houses['value'] * house_assets
#     EXP_houses['if_TC'] = np.ones(len(EXP_houses['value'])).astype(int)
#     EXP_houses['if_TS'] = np.ones(len(EXP_houses['value'])).astype(int)
#
#     EXP_houses.set_geometry_points()
#
#     from Functions import define_region_id
#
#     EXP_houses['region_id'] = define_region_id(EXP_houses)
#
#     value_bool = np.percentile(EXP_houses.values[:, 0], percentile) < EXP_houses.values[:, 0]
#
#     # sum(EXP_houses['value'][value_bool])
#
#     EXP_houses['if_TC'][value_bool] = int(2)
#
#     EXP_houses['if_TS'][value_bool] = int(2)
#
#     EXP_houses.write_hdf5(fl_EXP_houses)
#
# EXP_houses.value_unit = '$'
#
# ## Agriculture
#
# fl_EXP_agri = os.path.join(project_folder, 'EXP_agri_id_' + country + file_identifier + '.hdf5')
#
# EXP_agri = Exposures()
#
# if os.path.isfile(fl_EXP_agri):
#
#     EXP_agri.read_hdf5(fl_EXP_agri)
#
# else:
#     import geopandas as gpd
#
#     agri_exp_path = '/Users/qinhan/Documents/AXA/ECA_Vietnam/Exposure/Agri_clip/EXP_agri_points.shp'
#
#     agri_exp = gpd.read_file(agri_exp_path)
#
#     agri_exp.rename(columns={'grid_code':'value'},inplace=True)
#
#     EXP_agri = Exposures(agri_exp)
#
#     EXP_agri.ref_year = 2020
#
#     EXP_agri.set_lat_lon()
#
#     EXP_agri.check()
#
#     EXP_agri['value'] = EXP_agri['value'] * 1000000
#
#     EXP_agri['if_TC'] = np.ones(len(EXP_agri['value'])).astype(int)
#
#     EXP_agri['if_TS'] = np.ones(len(EXP_agri['value'])).astype(int)
#
#     from Functions import define_region_id
#
#     EXP_agri['region_id'] = define_region_id(EXP_agri)
#
#     EXP_agri.write_hdf5(fl_EXP_agri)
#
# EXP_agri.value_unit = '$'
#
#
#
#
# fl_EXP_people = os.path.join(project_folder, 'EXP_people_id_' + country + file_identifier + '.hdf5')
#
# EXP_people = LitPop()
#
# if os.path.isfile(fl_EXP_people):
#
#     EXP_people.read_hdf5(fl_EXP_people)
#
# else:
#     EXP_people.set_country(countries=country, res_arcsec=30, reference_year=2020, fin_mode='norm', exponents=[0, 1])
#     EXP_people['value'] = EXP_people['value'] * population
#     EXP_people['if_TC'] = np.ones(len(EXP_people['value'])).astype(int)
#     EXP_people['if_TS'] = np.ones(len(EXP_people['value'])).astype(int)
#
#     EXP_people.set_geometry_points()
#
#     from Functions import define_region_id
#
#     EXP_people['region_id'] = define_region_id(EXP_people)
#
#     # sum(EXP_people['value'][value_bool])
#
#     EXP_people.value_unit = ''
#
#     EXP_people.write_hdf5(fl_EXP_people)


## Hazard

from Functions import intro_haz_tc

fl_HAZ_tc = os.path.join(project_folder, 'HAZ_tc_mix50_' + country + file_identifier + '.hdf5')

HAZ_tc = intro_haz_tc(fl_HAZ_tc, cc=0)

ax = HAZ_tc.plot_rp_intensity()


# np.savetxt('/Users/qinhan/Documents/AXA/ECA_Vietnam/Model_output/TC_rpintensity.csv',inten_stats)

# fl_HAZ_tc_45 = os.path.join(project_folder, 'HAZ_tc_cc45_mix50_wof_' + country + file_identifier + '.hdf5')

# HAZ_tc_cc45 = intro_haz_tc(fl_HAZ_tc_45, cc=45)

# fl_HAZ_tc_85 = os.path.join(project_folder, 'HAZ_tc_cc85_mix50_wof_' + country + file_identifier + '.hdf5')

# HAZ_tc_cc85 = intro_haz_tc(fl_HAZ_tc_85, cc=85)

from Functions import intro_haz_ts

# fl_HAZ_ts = os.path.join(project_folder, 'HAZ_ts_mix50_CDEM_' + country + file_identifier + '.hdf5')
# #
# HAZ_ts = intro_haz_ts(fl_HAZ_ts, fl_HAZ_tc, cc = 0)


# HAZ_ts.plot_rp_intensity()

# np.savetxt('/Users/qinhan/Documents/AXA/ECA_Vietnam/Model_output/TS_rpintensity.csv',inten_stats)

# #
# # fl_HAZ_ts = os.path.join(project_folder, 'HAZ_ts_mix50_' + country + file_identifier + '.hdf5')
# #
# # HAZ_ts = intro_haz_ts(fl_HAZ_ts, fl_HAZ_tc, cc = 0)
#
# fl_HAZ_ts_45 = os.path.join(project_folder, 'HAZ_ts_cc45_mix50_wof_CDEM_' + country + file_identifier + '.hdf5')
#
# HAZ_ts_cc45 = intro_haz_ts(fl_HAZ_ts_45, fl_HAZ_tc_45, cc = 45)

# # fl_HAZ_ts_45 = os.path.join(project_folder, 'HAZ_ts_cc45_mix50_wof_' + country + file_identifier + '.hdf5')
# #
# # HAZ_ts_cc45 = intro_haz_ts(fl_HAZ_ts_45, fl_HAZ_tc_45, cc = 45)
#
# fl_HAZ_ts_85 = os.path.join(project_folder, 'HAZ_ts_cc85_mix50_wof_CDEM_' + country + file_identifier + '.hdf5')
#
# HAZ_ts_cc85 = intro_haz_ts(fl_HAZ_ts_85, fl_HAZ_tc_85, cc = 85)
#
# # fl_HAZ_ts_85 = os.path.join(project_folder, 'HAZ_ts_cc85_mix50_wof_' + country + file_identifier + '.hdf5')
# #
# # HAZ_ts_cc85 = intro_haz_ts(fl_HAZ_ts_85, fl_HAZ_tc_85, cc = 85)

print('Historical hazards completed')


from climada.entity import IFTropCyclone, ImpactFuncSet, ImpactFunc

## Impact function storm-houses

# IFs_TC_houses = ImpactFuncSet()
#
# if_tc_ru = IFTropCyclone()
# if_tc_ru.haz_type = 'TC'
# if_tc_ru.id = 1
# if_tc_ru.intensity_unit = 'm/s'
# if_tc_ru.intensity = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80])
# if_tc_ru.mdd = np.array([0, 0, 0, 0, 0.05, 0.20, 0.45, 0.65, 0.78])
# if_tc_ru.paa = np.ones(9)
# if_tc_ru.check()
#
# IFs_TC_houses.append(if_tc_ru)
#
# if_tc_ur = IFTropCyclone()
# if_tc_ur.haz_type = 'TC'
# if_tc_ur.id = 2
# if_tc_ur.intensity_unit = 'm/s'
# if_tc_ur.intensity = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80])
# if_tc_ur.mdd = np.array([0, 0, 0, 0, 0.05, 0.20, 0.45, 0.65, 0.78])
# if_tc_ur.paa = np.ones(9)
# if_tc_ur.check()
#
# IFs_TC_houses.append(if_tc_ur)

## Impact function surge-houses

IFs_TS_houses = ImpactFuncSet()

if_ts_ru = ImpactFunc()
if_ts_ru.id = 1
if_ts_ru.haz_type = 'TS'
if_ts_ru.intensity_unit = 'm'
if_ts_ru.intensity = np.array([0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0])
if_ts_ru.mdd = np.array([0, 0.33, 0.49, 0.62, 0.72, 0.87, 0.93, 0.98, 1.0])
if_ts_ru.paa = np.ones(9)
if_ts_ru.check()

IFs_TS_houses.append(if_ts_ru)

if_ts_ur = ImpactFunc()
if_ts_ur.id = 2
if_ts_ur.haz_type = 'TS'
if_ts_ur.intensity = np.array([0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0])
if_ts_ur.mdd = np.array([0, 0.33, 0.49, 0.62, 0.72, 0.87, 0.93, 0.98, 1.0])
if_ts_ur.paa = np.ones(9)
if_ts_ur.check()

IFs_TS_houses.append(if_ts_ur)

## Impact for agriculture

## Impact function storm-agri

# IFs_TC_agri = ImpactFuncSet()
#
# if_tc_agri = IFTropCyclone()
# if_tc_agri.haz_type = 'TC'
# if_tc_agri.id = 1
#
# V_HALF = 56.7 # vary value of v_half here
#
# if_tc_agri.set_emanuel_usa(v_thresh=25.7, v_half=V_HALF, scale=1)
#
# IFs_TC_agri.append(if_tc_agri)

## Impact function surge-agri

IFs_TS_agri = ImpactFuncSet()

if_ts_agri = ImpactFunc()
if_ts_agri.id = 1
if_ts_agri.haz_type = 'TS'
if_ts_agri.intensity_unit = 'm'
if_ts_agri.intensity = np.array([0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5])
if_ts_agri.mdd = np.array([0,0.01,0.02,0.12,0.43,0.73,0.89,0.95,0.98,1.0])
if_ts_agri.paa = np.ones(10)
if_ts_agri.check()

IFs_TS_agri.append(if_ts_agri)


# Impact function storm-people

# IFs_TC_people = ImpactFuncSet()
#
# if_tc_people = IFTropCyclone()
# if_tc_people.haz_type = 'TC'
# if_tc_people.id = 1
# if_tc_people.intensity_unit = 'm/s'
#
# if_tc_people.intensity = np.arange(0, 100, 0.5)
# if_tc_people.paa = np.ones(if_tc_people.intensity.size)
# if_tc_people.mdd = np.zeros(if_tc_people.intensity.size)
# for idx in range(if_tc_people.mdd.size):
#     if if_tc_people.intensity[idx] >= storm_threshold:
#         if_tc_people.mdd[idx] = 1
#
# if_tc_people.check()
#
# IFs_TC_people.append(if_tc_people)


## Impact function surge-people

IFs_TS_people = ImpactFuncSet()

if_ts_people = ImpactFunc()
if_ts_people.haz_type = 'TS'
if_ts_people.id = 1
if_ts_people.intensity_unit = 'm'

if_ts_people.intensity = np.arange(0, 10, 0.05)
if_ts_people.paa = np.ones(if_ts_people.intensity.size)
if_ts_people.mdd = np.zeros(if_ts_people.intensity.size)
for idx in range(if_ts_people.mdd.size):
    if if_ts_people.intensity[idx] >= surge_threshold:
        if_ts_people.mdd[idx] = 1

if_ts_people.check()

IFs_TS_people.append(if_ts_people)


## Calculate impact

from climada.engine import Impact

# IMP_houses_TC = Impact()
# IMP_houses_TC.calc(EXP_houses, IFs_TC_houses, HAZ_tc)
# freq_curve_houses_TC = IMP_houses_TC.calc_freq_curve()  # impact exceedence frequency curve
# # freq_curve_houses_TC.plot()
# print('Expected average annual impact houses TC: {:.3e} USD'.format(IMP_houses_TC.aai_agg))
#
#
# # fl_IMP_houses_TC = os.path.join(project_folder, 'IMP_houses_TC_' + country + file_identifier + '.xlsx')
# # IMP_houses_TC.write_excel(fl_IMP_houses_TC)
# # print('excel writen')
#
# IMP_houses_TC_45 = Impact()
# IMP_houses_TC_45.calc(EXP_houses, IFs_TC_houses, HAZ_tc_cc45)
# # freq_curve_houses_TC_45 = IMP_houses_TC_45.calc_freq_curve()  # impact exceedence frequency curve
# # freq_curve_houses_TC_45.plot()
# print('Expected average annual impact cc45 houses TC: {:.3e} USD'.format(IMP_houses_TC_45.aai_agg))
# #
# # # #
# IMP_houses_TC_85 = Impact()
# IMP_houses_TC_85.calc(EXP_houses, IFs_TC_houses, HAZ_tc_cc85)
# # freq_curve_houses_TC_85 = IMP_houses_TC_85.calc_freq_curve() # impact exceedence frequency curve
# # freq_curve_houses_TC_85.plot()
# print('Expected average annual impact cc85 houses TC: {:.3e} USD'.format(IMP_houses_TC_85.aai_agg))

IMP_houses_TS = Impact()
IMP_houses_TS.calc(EXP_houses, IFs_TS_houses, HAZ_ts)
# freq_curve_houses_TS = IMP_houses_TS.calc_freq_curve()  # impact exceedence frequency curve
# freq_curve_houses_TS.plot()
print('Expected average annual impact houses TS: {:.3e} USD'.format(IMP_houses_TS.aai_agg))
# IMP_houses_TS.plot_hexbin_eai_exposure()

IMP_houses_TS_45 = Impact()
IMP_houses_TS_45.calc(EXP_houses, IFs_TS_houses, HAZ_ts_cc45)
# freq_curve_houses_TS_45 = IMP_houses_TS_45.calc_freq_curve()  # impact exceedence frequency curve
# freq_curve_houses_TS.plot()
print('Expected average annual impact cc45 houses TS: {:.3e} USD'.format(IMP_houses_TS_45.aai_agg))
# IMP_houses_TS.plot_hexbin_eai_exposure()

IMP_houses_TS_85 = Impact()
IMP_houses_TS_85.calc(EXP_houses, IFs_TS_houses, HAZ_ts_cc85)
# freq_curve_houses_TS_85 = IMP_houses_TS_85.calc_freq_curve()  # impact exceedence frequency curve
# freq_curve_houses_TS.plot()
print('Expected average annual impact cc85 houses TS: {:.3e} USD'.format(IMP_houses_TS_85.aai_agg))
# IMP_houses_TS.plot_hexbin_eai_exposure()


IMP_agri_TS = Impact()
IMP_agri_TS.calc(EXP_agri, IFs_TS_agri, HAZ_ts)
freq_curve_agri_TS = IMP_agri_TS.calc_freq_curve()  # impact exceedence frequency curve
# freq_curve_houses_TS.plot()
print('Expected average annual impact agri TS: {:.3e} USD'.format(IMP_agri_TS.aai_agg))
# IMP_houses_TS.plot_hexbin_eai_exposure()

IMP_agri_TS_45 = Impact()
IMP_agri_TS_45.calc(EXP_agri, IFs_TS_agri, HAZ_ts_cc45)
freq_curve_agri_TS_45 = IMP_agri_TS_45.calc_freq_curve()  # impact exceedence frequency curve
# freq_curve_houses_TS.plot()
print('Expected average annual impact cc45 agri TS: {:.3e} USD'.format(IMP_agri_TS_45.aai_agg))
# IMP_houses_TS.plot_hexbin_eai_exposure()

IMP_agri_TS_85 = Impact()
IMP_agri_TS_85.calc(EXP_agri, IFs_TS_agri, HAZ_ts_cc85)
freq_curve_agri_TS_85 = IMP_agri_TS_85.calc_freq_curve()  # impact exceedence frequency curve
# freq_curve_houses_TS.plot()
print('Expected average annual impact cc85 agri TS: {:.3e} USD'.format(IMP_agri_TS_85.aai_agg))
# IMP_houses_TS.plot_hexbin_eai_exposure()


# IMP_agri_TC = Impact()
# IMP_agri_TC.calc(EXP_agri, IFs_TC_agri, HAZ_tc)
# freq_curve_agri_TC = IMP_agri_TC.calc_freq_curve()  # impact exceedence frequency curve
# # freq_curve_houses_TS.plot()
# print('Expected average annual impact agri TC: {:.3e} USD'.format(IMP_agri_TC.aai_agg))
# # IMP_houses_TS.plot_hexbin_eai_exposure()
#
# IMP_agri_TC_45 = Impact()
# IMP_agri_TC_45.calc(EXP_agri, IFs_TC_agri, HAZ_tc_cc45)
# freq_curve_agri_TC_45 = IMP_agri_TC_45.calc_freq_curve()  # impact exceedence frequency curve
# # freq_curve_houses_TS.plot()
# print('Expected average annual impact cc45 agri TC: {:.3e} USD'.format(IMP_agri_TC_45.aai_agg))
# # IMP_houses_TS.plot_hexbin_eai_exposure()
#
# IMP_agri_TC_85 = Impact()
# IMP_agri_TC_85.calc(EXP_agri, IFs_TC_agri, HAZ_tc_cc85)
# freq_curve_agri_TC_85 = IMP_agri_TC_85.calc_freq_curve()  # impact exceedence frequency curve
# # freq_curve_houses_TS.plot()
# print('Expected average annual impact cc85 agri TC: {:.3e} USD'.format(IMP_agri_TC_85.aai_agg))
# # IMP_houses_TS.plot_hexbin_eai_exposure()

# #
# IMP_people_TC = Impact()
# IMP_people_TC.calc(EXP_people, IFs_TC_people, HAZ_tc)
# # freq_curve_people_TC = IMP_people_TC.calc_freq_curve()  # impact exceedence frequency curve
# # freq_curve_people_TC.plot()
# print('Expected average annual impact people TC: {:.3e}'.format(IMP_people_TC.aai_agg))
#
# IMP_people_TC_45 = Impact()
# IMP_people_TC_45.calc(EXP_people, IFs_TC_people, HAZ_tc_cc45)
# # freq_curve_people_TC = IMP_people_TC.calc_freq_curve()  # impact exceedence frequency curve
# # freq_curve_people_TC.plot()
# print('Expected average annual impact people TC cc45: {:.3e}'.format(IMP_people_TC_45.aai_agg))
#
# IMP_people_TC_85 = Impact()
# IMP_people_TC_85.calc(EXP_people, IFs_TC_people, HAZ_tc_cc85)
# # freq_curve_people_TC = IMP_people_TC.calc_freq_curve()  # impact exceedence frequency curve
# # freq_curve_people_TC.plot()
# print('Expected average annual impact people TC cc85: {:.3e}'.format(IMP_people_TC_85.aai_agg))


#
# IMP_people_TS = Impact()
# IMP_people_TS.calc(EXP_people, IFs_TS_people, HAZ_ts)
# # freq_curve_people_TS = IMP_people_TS.calc_freq_curve()  # impact exceedence frequency curve
# # freq_curve_people_TS.plot()
# print('Expected average annual impact people TS: {:.3e} USD'.format(IMP_people_TS.aai_agg))
#
# IMP_people_TS_45 = Impact()
# IMP_people_TS_45.calc(EXP_people, IFs_TS_people, HAZ_ts_cc45)
# # freq_curve_people_TS = IMP_people_TS.calc_freq_curve()  # impact exceedence frequency curve
# # freq_curve_people_TS.plot()
# print('Expected average annual impact people TS cc45: {:.3e} USD'.format(IMP_people_TS_45.aai_agg))
#
# IMP_people_TS_85 = Impact()
# IMP_people_TS_85.calc(EXP_people, IFs_TS_people, HAZ_ts_cc85)
# # freq_curve_people_TS = IMP_people_TS.calc_freq_curve()  # impact exceedence frequency curve
# # freq_curve_people_TS.plot()
# print('Expected average annual impact people TS cc85: {:.3e} USD'.format(IMP_people_TS_85.aai_agg))
#

## Adaptation measures

from climada.entity import Measure
from climada.entity import MeasureSet

## Measures for storm
#
# TC_meas1 = Measure()
# TC_meas1.name = 'Mangrove'
# TC_meas1.haz_type = 'TC'
# TC_meas1.color_rgb = np.array([0.16, 0.62, 0.56])
# mangrove_maintain = 4000000
# TC_meas1.cost = 172*1000000*0.000043*1160*1000*150/10000 + mangrove_maintain * 30
# TC_meas1.mdd_impact = (1, 0)
# TC_meas1.paa_impact = (1, 0)
# TC_meas1.hazard_inten_imp = (1, -4) # reduces intensity by 4


# TC_meas2 = Measure()
# TC_meas2.name = 'Early warning system'
# TC_meas2.haz_type = 'TC'
# TC_meas2.color_rgb = np.array([0.62, 0.01, 0.03])
# mangrove_maintain = 4000000
# TC_meas2.cost = 172*1000000*0.000043*1160*1000*150/10000 + mangrove_maintain * 30
# TC_meas2.mdd_impact = (1, 0)
# TC_meas2.paa_impact = (1, 0)
# TC_meas2.hazard_inten_imp = (1, -4) # reduces intensity by 4

# TC_meas2 = Measure()
# TC_meas2.name = 'Insurance'
# TC_meas2.haz_type = 'TC'
# TC_meas2.color_rgb = np.array([0.92, 0.22, 0.20])
# TC_meas2.risk_transf_attach = IMP_houses_TC.calc_freq_curve(15).impact
# TC_meas2.risk_transf_cover = IMP_houses_TC.calc_freq_curve(100).impact
# # TC_meas2.cost = IMP_houses_TC.aai_agg * ((1-1/((1+disc_rate)**(horizon-2020+1)))/(1-1/(1+disc_rate))) * 1.1
# TC_meas2.cost = insu_cost_TC_houses * TC_meas2.risk_transf_cover
#
#
# freq_curve_houses_TC.plot()
# imp_new, risk_transf = TC_meas2.calc_impact(EXP_houses, IFs_TC_houses, HAZ_tc)
# imp_new.calc_freq_curve().plot()
# print('risk_transfer {:.3}'.format(risk_transf.aai_agg))


# TC_meas_set = MeasureSet()
# TC_meas_set.append(TC_meas1)
# # TC_meas_set.append(TC_meas2)
# TC_meas_set.check()


## Measures for surge

TS_meas1 = Measure()
TS_meas1.name = 'Mangrove'
TS_meas1.haz_type = 'TS'
TS_meas1.exp_region_id = [1, 2]
TS_meas1.color_rgb = np.array([0.16, 0.62, 0.56])
mangrove_maintain = 4000000
TS_meas1.cost = 172 * 1000000 * 0.000043 * 1160 * 1000 * 150 / 10000 + mangrove_maintain * 30  # 361,664,400$
TS_meas1.mdd_impact = (1, 0)
TS_meas1.paa_impact = (1, 0)
TS_meas1.hazard_inten_imp = (1, -0.5)  # reduces intensity by 0.5m

TS_meas2 = Measure()
TS_meas2.name = 'Seadykes'
TS_meas2.haz_type = 'TS'
TS_meas2.color_rgb = np.array([0.91, 0.77, 0.42])
TS_meas2.exp_region_id = [1]
seadyke_maintain = 200
TS_meas2.cost = (110 * 1000000 * 0.000043 + seadyke_maintain * 30) * 150 * 1000
TS_meas2.hazard_inten_imp = (1, -2)  # protect against event once every 15 years

TS_meas3 = Measure()
TS_meas3.name = 'Gabions'
TS_meas3.haz_type = 'TS'
TS_meas3.color_rgb = np.array([0.65, 0.65, 0.55])
TS_meas3.exp_region_id = [1]
gabion_maintain = 130
TS_meas3.cost = (1300 + gabion_maintain) * 150 * 1000
TS_meas2.cost = (110 * 1000000 * 0.000043 + 0.7 * seadyke_maintain * 30) * 150 * 1000  # protect against event once every 20 years
TS_meas3.hazard_inten_imp = (1, -0.5)

TS_meas_set = MeasureSet()
TS_meas_set.append(TS_meas1)
TS_meas_set.append(TS_meas2)
TS_meas_set.append(TS_meas3)
TS_meas_set.check()

print('measure set built')

from climada.entity import Entity
from climada.engine import CostBenefit
from climada.entity import DiscRates
import copy

disc = DiscRates()
disc.years = np.arange(2000, 2100)
disc.rates = np.ones(disc.years.size) * disc_rate

people_disc = DiscRates()
people_disc.years = np.arange(2000, 2100)
people_disc.rates = np.zeros(people_disc.years.size)

ENT_houses = Entity()

ENT_houses.exposures = EXP_houses

ENT_houses.impact_funcs = IFs_TS_houses

ENT_houses.measures = TS_meas_set

ENT_houses.disc_rates = disc

ENT_houses.check()

## Future houses entity

value_bool = np.percentile(EXP_houses.values[:, 0], percentile) < EXP_houses.values[:, 0]

EXP_houses_future = copy.deepcopy(EXP_houses)

EXP_houses_future['value'][value_bool] *= ur_houses_asset_growth

EXP_houses_future['value'][np.invert(value_bool)] *= ru_houses_asset_growth

ENT_houses_future = copy.deepcopy(ENT_houses)

ENT_houses_future.exposures = EXP_houses_future

ENT_houses_future.exposures.ref_year = horizon

ENT_houses_future.check()

print('house entity built')

ENT_agri = Entity()

ENT_agri.exposures = EXP_agri

ENT_agri.impact_funcs = IFs_TS_agri

ENT_agri.measures = TS_meas_set

ENT_agri.disc_rates = disc

ENT_agri.check()

## Future houses entity

EXP_agri_future = copy.deepcopy(EXP_agri)

EXP_agri_future ['value'] *= agri_asset_growth

ENT_agri_future = copy.deepcopy(ENT_agri)

ENT_agri_future.exposures = EXP_agri_future

ENT_agri_future.exposures.ref_year = horizon

ENT_agri_future.check()

print('agri entity built')


# ENT_people = Entity()
#
# ENT_people.exposures = EXP_people
#
# ENT_people.impact_funcs = IFs_TC_people
#
# ENT_people.measures = TC_meas_set
#
# ENT_people.disc_rates = people_disc
#
# ENT_people.check()
#
# ## Future houses entity
#
# EXP_people_future = copy.deepcopy(EXP_people)
#
# EXP_people_future ['value'] *= population_growth
#
# ENT_people_future = copy.deepcopy(ENT_people)
#
# ENT_people_future.exposures = EXP_people_future
#
# ENT_people_future.exposures.ref_year = horizon
#
# ENT_people_future.check()
#
# print('people entity built')





cost_ben_houses = CostBenefit()
cost_ben_houses.calc(HAZ_ts, ENT_houses, HAZ_ts_cc85, ENT_houses_future, future_year=horizon)  # prints costs and benefits


cost_ben_agri = CostBenefit()
cost_ben_agri.calc(HAZ_ts, ENT_agri, HAZ_ts_cc85, ENT_agri_future, future_year=horizon)  # prints costs and benefits


# cost_ben_people = CostBenefit()
# cost_ben_people.calc(HAZ_tc, ENT_people, HAZ_tc_cc85, ENT_people_future, future_year=horizon)  # prints costs and benefits

# ENT_agri = Entity()
# ENT_agri.exposures = EXP_agri
# ENT_agri.impact_funcs = IFs_TS_agri
# ENT_agri.measures = TS_meas_set
# ENT_agri.disc_rates = disc
# ENT_agri.check()