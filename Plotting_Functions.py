import matplotlib.pyplot as plt

import matplotlib.colors as colors

import matplotlib.font_manager as font_manager

from Configuration import *

fontpath = '/System/Library/Fonts/Optima.ttc'

prop = font_manager.FontProperties(fname=fontpath)

plt.rcParams["font.weight"] = "bold"

plt.rcParams["axes.labelweight"] = "bold"

plt.rcParams.update(
    {'font.size': 15, 'axes.titlesize': 15, 'legend.fontsize': 15, 'font.family': [prop.get_name(), 'sans-serif']})


from Configuration import *





def plot_exp(figname, EXP_type, minmax):

    from climada.entity import Exposures

    EXP = Exposures()

    if EXP_type == 'houses':

        fl_EXP = os.path.join(project_folder, 'EXP_housesGAR15LP_id_' + country + file_identifier + '.hdf5')

    elif EXP_type == 'agri':

        fl_EXP = os.path.join(project_folder, 'EXP_agri_id_' + country + file_identifier + '.hdf5')

    else:

        fl_EXP = os.path.join(project_folder, 'EXP_people_id_' + country + file_identifier + '.hdf5')

    EXP.read_hdf5(fl_EXP)


    plt.rcParams.update(
        {'font.size': 9, 'axes.titlesize': 12, 'legend.fontsize': 12, 'font.family': [prop.get_name(), 'sans-serif']})

    norm = colors.LogNorm(vmin=minmax[0], vmax=minmax[1])

    ax = EXP.plot_hexbin(norm=norm, pop_name=False, cmap='RdBu_r', buffer=1)

    ax.set_title('')

    fig = plt.gcf()

    fig.set_size_inches(3.5, 6)

    plt.subplots_adjust(left=0.15, right=0.85, top=0.95, bottom=0.05)

    cbar = fig.axes[1]

    if EXP_type == 'people':

        cbar.set_ylabel('Population per km\u00b2')

    else:

        cbar.set_ylabel('Asset ($) per km\u00b2')


    # eps_figname = image_folder + 'EPS/' + figname + '.eps'

    png_figname = image_folder + 'PNG/' + figname + '.png'

    # plt.savefig(eps_figname, format = 'eps')

    plt.savefig(png_figname, format='png')

    plt.close()





def plot_imp(figname, EXP_type, minmax, IMP):

    plt.rcParams.update(
        {'font.size': 9, 'axes.titlesize': 12, 'legend.fontsize': 12, 'font.family': [prop.get_name(), 'sans-serif']})

    norm = colors.LogNorm(vmin=minmax[0], vmax=minmax[1])

    if 'diff' in figname:

        ax = IMP.plot_hexbin_eai_exposure(pop_name=False, norm=norm, cmap=cmap_red,buffer=1, ignore_zero=False)

    else:

        ax = IMP.plot_hexbin_eai_exposure(pop_name=False, norm=norm, cmap=cmap, buffer=1, ignore_zero=False)

    ax.set_title('')

    fig = plt.gcf()

    fig.set_size_inches(3.5, 6)

    plt.subplots_adjust(left=0.15, right=0.85, top=0.95, bottom=0.05)

    cbar = fig.axes[1]

    if EXP_type == 'people':

        cbar.set_ylabel('People affected per km\u00b2')

    else:

        cbar.set_ylabel('Damage ($) per km\u00b2')

    # eps_figname = image_folder + 'EPS/' + figname + '.eps'

    png_figname = image_folder + 'PNG/' + figname + '.png'

    # plt.savefig(eps_figname, format = 'eps')

    plt.savefig(png_figname)

    plt.close()


def plot_EFC(figname,EXP_type,yaxis,IMP,IMP_45,IMP_85):

    freq_curve_house_tc_500 = IMP.calc_freq_curve(np.linspace(1, 500, 500))
    freq_curve_house_tc_500_85 = IMP_85.calc_freq_curve(np.linspace(1, 500, 500))
    freq_curve_house_tc_500_45 = IMP_45.calc_freq_curve(np.linspace(1, 500, 500))

    tc_imp_500 = freq_curve_house_tc_500.impact
    tc_imp_500_85 = freq_curve_house_tc_500_85.impact
    tc_imp_500_45 = freq_curve_house_tc_500_45.impact
    # tc_imp_500_eg_85 = freq_curve_houses_tc_500_eg_85.impact
    rp = freq_curve_house_tc_500.return_per

    plt.rcParams.update(
        {'font.size': 21, 'axes.titlesize': 21, 'legend.fontsize': 12, 'font.family': [prop.get_name(), 'sans-serif']})

    plt.plot(rp, tc_imp_500, label="Current climate", linewidth=3.0, color='tab:blue')
    plt.plot(rp, tc_imp_500_85, label='RCP8.5', linewidth=3.0, color='tab:red')
    plt.plot(rp, tc_imp_500_45, label='RCP4.5', linewidth=3.0, color='tab:orange')
    # plt.plot(rp,tc_imp_500_eg_85,label = 'rcp 8.5 with economic growth',color=(0.92, 0.22, 0.20),linewidth=3.0)
    plt.legend(loc='lower right')
    # plt.yscale('log')
    # plt.xscale('log')
    plt.xlabel('Return period (year)')

    if EXP_type == 'people':

        plt.ylabel('Number of people affected')

    else:

        plt.ylabel('Impact ($)')

    plt.title('')

    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

    plt.ylim(yaxis)

    fig = plt.gcf()

    fig.set_size_inches(8.5, 6.375)

    plt.subplots_adjust(left=0.15, right=0.9, top=0.85, bottom=0.2)

    png_figname = image_folder + 'PNG/' + figname + '.png'

    fig.savefig(png_figname)

    plt.close()


def plot_EFC_adapt(figname,HAZ_type,EXP_type,yaxis,IMP_eg_45,IMP_eg_85,IMP_eg_45_meas,IMP_eg_85_meas):

    from climada.entity import Measure

    meas_comb = Measure()
    meas_comb.name = 'Combined'
    meas_comb.color_rgb = np.array([1, 1, 1])
    gabion_maintain = 130
    meas_comb.cost = (1300 + gabion_maintain) * 150 * 1000

    if HAZ_type == 'TC':

        meas_comb.haz_type = 'TC'

        meas_comb.hazard_inten_imp = (1, -4)

    elif HAZ_type == 'TS':

        meas_comb.haz_type = 'TS'

        meas_comb.hazard_inten_imp = (1, -3)


    freq_curve_500_eg_85 = IMP_eg_85.calc_freq_curve(np.linspace(1, 500, 500))
    imp_500_eg_85 = freq_curve_500_eg_85.impact


    freq_curve_500_eg_45 = IMP_eg_45.calc_freq_curve(np.linspace(1, 500, 500))
    imp_500_eg_45 = freq_curve_500_eg_45.impact


    freq_curve_500_eg_85_meas = IMP_eg_85_meas.calc_freq_curve(np.linspace(1, 500, 500))
    imp_500_eg_85_meas = freq_curve_500_eg_85_meas.impact


    freq_curve_500_eg_45_meas = IMP_eg_45_meas.calc_freq_curve(np.linspace(1, 500, 500))
    imp_500_eg_45_meas = freq_curve_500_eg_45_meas.impact

    plt.rcParams.update(
        {'font.size': 21, 'axes.titlesize': 21, 'legend.fontsize': 12, 'font.family': [prop.get_name(), 'sans-serif']})

    rp = freq_curve_500_eg_85.return_per
    # plt.plot(rp, ts_imp_500, label = "current climate",linewidth=3.0)
    # plt.plot(rp,ts_imp_500_85,label = 'rcp 8.5 (extreme scenario)',linewidth=3.0)
    plt.plot(rp, imp_500_eg_85, label='RCP8.5 + Economic growth', color='tab:red', linewidth=3.0)
    plt.plot(rp, imp_500_eg_85_meas, label='RCP8.5 + Economic growth + Adaptation measures', color='tab:red',
             linewidth=3.0, linestyle='--')
    plt.plot(rp, imp_500_eg_45, label='RCP4.5 + Economic growth', color='tab:orange', linewidth=3.0)
    plt.plot(rp, imp_500_eg_45_meas, label='RCP4.5 + Economic growth + Adaptation measures', color='tab:orange',
             linewidth=3.0, linestyle='--')

    plt.legend()
    # plt.yscale('log')
    plt.xlabel('Return period (year)')


    if EXP_type == 'people':

        plt.ylabel('Number of people affected')

    else:

        plt.ylabel('Impact ($)')

    plt.title('')

    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

    plt.ylim(yaxis)

    fig = plt.gcf()

    fig.set_size_inches(8.5, 6.375)

    plt.subplots_adjust(left=0.15, right=0.9, top=0.85, bottom=0.2)

    png_figname = image_folder + 'PNG/' + figname + '.png'

    fig.savefig(png_figname)

    plt.close()


def plot_CB_and_CBevent(figname1, figname2, EXP_type, HAZ_type, yaxis1, yaxis2):

    from climada.entity import Entity, Measure, MeasureSet
    from climada.engine import CostBenefit
    from climada.entity import DiscRates
    import copy, os

    from climada.entity import Exposures
    from climada.hazard import TropCyclone, TCSurge
    from climada.entity import IFTropCyclone, ImpactFuncSet, ImpactFunc

    EXP = Exposures()

    IFs = ImpactFuncSet()

    Meas = MeasureSet()

    disc = DiscRates()




    if EXP_type == 'people':

        fl_EXP_people = os.path.join(project_folder, 'EXP_people_id_' + country + file_identifier + '.hdf5')

        EXP.read_hdf5(fl_EXP_people)

        disc.years = np.arange(2000, 2100)

        disc.rates = np.zeros(disc.years.size)

    elif EXP_type == 'houses':

        fl_EXP_houses = os.path.join(project_folder, 'EXP_housesGAR15LP_id_' + country + file_identifier + '.hdf5')

        EXP.read_hdf5(fl_EXP_houses)

        disc.years = np.arange(2000, 2100)

        disc.rates = np.ones(disc.years.size) * disc_rate

    elif EXP_type == 'agri':

        fl_EXP_agri = os.path.join(project_folder, 'EXP_agri_id_' + country + file_identifier + '.hdf5')

        EXP.read_hdf5(fl_EXP_agri)

        EXP.value_unit = '$'

        disc.years = np.arange(2000, 2100)

        disc.rates = np.ones(disc.years.size) * disc_rate




    if HAZ_type == 'TC':

        HAZ = TropCyclone()

        fl_HAZ_tc = os.path.join(project_folder, 'HAZ_tc_mix50_' + country + file_identifier + '.hdf5')

        HAZ.read_hdf5(fl_HAZ_tc)

        HAZ_cc = TropCyclone()

        fl_HAZ_tc_85 = os.path.join(project_folder, 'HAZ_tc_cc85_mix50_wf_' + country + file_identifier + '.hdf5')

        HAZ_cc.read_hdf5(fl_HAZ_tc_85)

        TC_meas1 = Measure()
        TC_meas1.name = 'Mangrove'
        TC_meas1.haz_type = 'TC'
        TC_meas1.color_rgb = np.array([0.16, 0.62, 0.56])
        mangrove_maintain = 4000000
        TC_meas1.cost = 172 * 1000000 * 0.000043 * 1160 * 1000 * 150 / 10000 + mangrove_maintain * 30
        TC_meas1.mdd_impact = (1, 0)
        TC_meas1.paa_impact = (1, 0)
        TC_meas1.hazard_inten_imp = (1, -4)  # reduces intensity by 4


        Meas.append(TC_meas1)
        Meas.check()




    else:

        HAZ = TCSurge()

        fl_HAZ_ts = os.path.join(project_folder, 'HAZ_ts_mix50_CDEM_' + country + file_identifier + '.hdf5')

        HAZ.read_hdf5(fl_HAZ_ts)

        HAZ_cc = TCSurge()

        fl_HAZ_ts_85 = os.path.join(project_folder, 'HAZ_ts_cc85_mix50_wf_CDEM_' + country + file_identifier + '.hdf5')

        HAZ_cc.read_hdf5(fl_HAZ_ts_85)

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


        Meas.append(TS_meas1)
        Meas.append(TS_meas2)
        Meas.append(TS_meas3)
        Meas.check()



    if EXP_type == 'houses':

        if HAZ_type == 'TC':

            if_tc_ru = IFTropCyclone()
            if_tc_ru.haz_type = 'TC'
            if_tc_ru.id = 1
            if_tc_ru.intensity_unit = 'm/s'
            if_tc_ru.intensity = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80])
            if_tc_ru.mdd = np.array([0, 0, 0, 0, 0.05, 0.20, 0.45, 0.65, 0.78])
            if_tc_ru.paa = np.ones(9)
            if_tc_ru.check()

            IFs.append(if_tc_ru)

            if_tc_ur = IFTropCyclone()
            if_tc_ur.haz_type = 'TC'
            if_tc_ur.id = 2
            if_tc_ur.intensity_unit = 'm/s'
            if_tc_ur.intensity = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80])
            if_tc_ur.mdd = np.array([0, 0, 0, 0, 0.05, 0.20, 0.45, 0.65, 0.78])
            if_tc_ur.paa = np.ones(9)
            if_tc_ur.check()

            IFs.append(if_tc_ur)

        else:

            if_ts_ru = ImpactFunc()
            if_ts_ru.id = 1
            if_ts_ru.haz_type = 'TS'
            if_ts_ru.intensity_unit = 'm'
            if_ts_ru.intensity = np.array([0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0])
            if_ts_ru.mdd = np.array([0, 0.33, 0.49, 0.62, 0.72, 0.87, 0.93, 0.98, 1.0])
            if_ts_ru.paa = np.ones(9)
            if_ts_ru.check()

            IFs.append(if_ts_ru)

            if_ts_ur = ImpactFunc()
            if_ts_ur.id = 2
            if_ts_ur.haz_type = 'TS'
            if_ts_ur.intensity = np.array([0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0])
            if_ts_ur.mdd = np.array([0, 0.33, 0.49, 0.62, 0.72, 0.87, 0.93, 0.98, 1.0])
            if_ts_ur.paa = np.ones(9)
            if_ts_ur.check()

            IFs.append(if_ts_ur)

    elif EXP_type == 'agri':

        if HAZ_type == 'TC':

            if_tc_agri = IFTropCyclone()
            if_tc_agri.haz_type = 'TC'
            if_tc_agri.id = 1

            V_HALF = 56.7  # vary value of v_half here

            if_tc_agri.set_emanuel_usa(v_thresh=25.7, v_half=V_HALF, scale=1)

            IFs.append(if_tc_agri)

        else:

            if_ts_agri = ImpactFunc()
            if_ts_agri.id = 1
            if_ts_agri.haz_type = 'TS'
            if_ts_agri.intensity_unit = 'm'
            if_ts_agri.intensity = np.array([0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5])
            if_ts_agri.mdd = np.array([0,0.01,0.02,0.12,0.43,0.73,0.89,0.95,0.98,1.0])
            if_ts_agri.paa = np.ones(10)
            if_ts_agri.check()

            IFs.append(if_ts_agri)

    else:

        if HAZ_type == 'TC':

            if_tc_people = IFTropCyclone()
            if_tc_people.haz_type = 'TC'
            if_tc_people.id = 1
            if_tc_people.intensity_unit = 'm/s'

            if_tc_people.intensity = np.arange(0, 100, 0.5)
            if_tc_people.paa = np.ones(if_tc_people.intensity.size)
            if_tc_people.mdd = np.zeros(if_tc_people.intensity.size)
            for idx in range(if_tc_people.mdd.size):
                if if_tc_people.intensity[idx] >= storm_threshold:
                    if_tc_people.mdd[idx] = 1

            if_tc_people.check()

            IFs.append(if_tc_people)

        else:

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

            IFs.append(if_ts_people)

    ENT = Entity()

    ENT.exposures = EXP

    ENT.impact_funcs = IFs

    ENT.measures = Meas

    ENT.disc_rates = disc

    ENT.check()

    ## Future houses entity

    EXP_future = copy.deepcopy(EXP)

    if EXP_type == 'houses':

        EXP_future['value'] = EXP_future['value'] * ur_houses_asset_growth

    elif EXP_type == 'agri':

        EXP_future['value'] = EXP_future['value'] * agri_asset_growth

    elif EXP_type == 'people':

        EXP_future['value'] = EXP_future['value'] * population_growth

    ENT_future = copy.deepcopy(ENT)

    ENT_future.exposures = EXP_future

    ENT_future.exposures.ref_year = horizon

    ENT_future.check()


    cost_ben = CostBenefit()


    cost_ben.calc(HAZ, ENT, HAZ_cc, ENT_future, future_year=horizon)  # prints costs and benefits


    plt.rcParams.update(
        {'font.size': 9, 'axes.titlesize': 12, 'legend.fontsize': 12, 'font.family': [prop.get_name(), 'sans-serif']})

    if EXP_type != 'people':

        ax1 = cost_ben.plot_cost_benefit()

        fig = plt.gcf()

        fig.set_size_inches(5.7, 3.2)

        plt.subplots_adjust(left=0.12, right=0.95, top=0.9, bottom=0.2)

        plt.ylim(yaxis1)

        # plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

        png_figname1 = image_folder + 'PNG/' + figname1 + '.png'

        fig.savefig(png_figname1)

        plt.close()

        ax2 = cost_ben.plot_event_view()

        fig = plt.gcf()

        fig.set_size_inches(5.7, 3.2)

        plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.2)

        plt.ylim(yaxis2)

        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

        png_figname2 = image_folder + 'PNG/' + figname2 + '.png'

        fig.savefig(png_figname2)

        plt.close()

        # ax3 = cost_ben.plot_waterfall_accumulated(HAZ, ENT, ENT_future, plot_arrow=False)
        #
        # ax3.set_xticklabels(
        #     ['Accumulated risk \nfrom 2020', 'Extra risk by \n economic development', 'Extra risk by \n climate change',
        #      'Accumulated risk \ntill ' + str(horizon)])
        #
        # ax3.set_title('')
        #
        # fig = plt.gcf()
        #
        # fig.set_size_inches(5.7, 3.2)
        #
        # plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)
        #
        # plt.ylim(yaxis3)
        #
        # plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        #
        # png_figname3 = image_folder + 'PNG/' + figname3 + '.png'
        #
        # fig.savefig(png_figname3)
        #
        # plt.close()

    else:

        ax2 = cost_ben.plot_event_view()

        fig = plt.gcf()

        fig.set_size_inches(5.7, 3.2)

        ax2.set_ylabel('Number of people affected')

        plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.2)

        plt.ylim(yaxis2)

        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

        png_figname2 = image_folder + 'PNG/' + figname2 + '.png'

        fig.savefig(png_figname2)

        plt.close()


        # ax3 = cost_ben.plot_waterfall_accumulated(HAZ, ENT, ENT_future, plot_arrow=False)
        #
        # ax3.set_ylabel('Number of people affected')
        #
        # ax3.set_xticklabels(
        #     ['Accumulated risk \nfrom 2020', 'Extra risk by \n population growth', 'Extra risk by \n climate change',
        #      'Accumulated risk \ntill ' + str(horizon)])
        #
        # ax3.set_title('')
        #
        # # ax3.texts = ax3.texts / ([yaxis3[1]] / float(str(yaxis3[1])[0:2]) * 10)
        #
        # ax3.texts[0].set_text()
        #
        # fig = plt.gcf()
        #
        # fig.set_size_inches(5.7, 3.2)
        #
        # plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)
        #
        # png_figname3 = image_folder + 'PNG/' + figname3 + '.png'
        #
        # plt.ylim(yaxis3)
        #
        # plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        #
        # fig.savefig(png_figname3)
        #
        # plt.close()


