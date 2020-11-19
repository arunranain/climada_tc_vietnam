import matplotlib.pyplot as plt

import numpy as np

import matplotlib.colors as colors

from Configuration import *


import copy

from Import_Impact import *

from Plotting_Functions import plot_exp, plot_imp, plot_EFC, plot_EFC_adapt, plot_CB_and_CBevent



figname1, figname2= 'CB_houses_TC', 'CB_event_houses_TC'

plot_CB_and_CBevent(figname1,figname2,'houses','TC',[0,35],[0,3.7e10])


figname1, figname2= 'CB_houses_TS', 'CB_event_houses_TS'

plot_CB_and_CBevent(figname1,figname2,'houses','TS',[0,35],[0,3.7e10])



figname1, figname2= 'CB_agri_TC', 'CB_event_agri_TC'

plot_CB_and_CBevent(figname1,figname2,'agri','TC',[0,14],[0,9.5e9])



figname1, figname2= 'CB_agri_TS', 'CB_event_agri_TS'

plot_CB_and_CBevent(figname1,figname2,'agri','TS',[0,14],[0,9.5e9])



figname1, figname2= 'CB_people_TC', 'CB_event_people_TC'

plot_CB_and_CBevent(figname1,figname2,'people','TC',[0,35],[0,1.3e7])



figname1, figname2= 'CB_people_TS', 'CB_event_people_TS'

plot_CB_and_CBevent(figname1,figname2,'people','TS',[0,35],[0,1.3e7])




## Houses

figname = 'EXP_houses'

plot_exp(figname,'houses',[500,4.0e8])


figname = 'IMP_houses_TC'

plot_imp(figname,'houses',[1,1.0e8],IMP_houses_TC)



figname = 'IMP_houses_TS'

plot_imp(figname,'houses',[1,1.0e8],IMP_houses_TS)


figname = 'IMP_houses_TC_diff45'

IMP_houses_TC_diff45 = copy.deepcopy(IMP_houses_TC)

IMP_houses_TC_diff45.eai_exp = IMP_houses_TC_45.eai_exp - IMP_houses_TC.eai_exp

plot_imp(figname,'houses',[1,1.0e6],IMP_houses_TC_diff45)



figname = 'IMP_houses_TC_diff85'

IMP_houses_TC_diff85 = copy.deepcopy(IMP_houses_TC)

IMP_houses_TC_diff85.eai_exp = IMP_houses_TC_85.eai_exp - IMP_houses_TC.eai_exp

plot_imp(figname,'houses',[1,1.0e6],IMP_houses_TC_diff85)



figname = 'IMP_houses_TS_diff45'

IMP_houses_TS_diff45 = copy.deepcopy(IMP_houses_TS)

IMP_houses_TS_diff45.eai_exp = IMP_houses_TS_45.eai_exp - IMP_houses_TS.eai_exp

plot_imp(figname,'houses',[1,1.0e6],IMP_houses_TS_diff45)



figname = 'IMP_houses_TS_diff85'

IMP_houses_TS_diff85 = copy.deepcopy(IMP_houses_TS)

IMP_houses_TS_diff85.eai_exp = IMP_houses_TS_85.eai_exp - IMP_houses_TS.eai_exp

plot_imp(figname,'houses',[1,1.0e6],IMP_houses_TS_diff85)


figname = 'EFC_houses_TC'

plot_EFC(figname,'houses',[0,5.2e10],IMP_houses_TC,IMP_houses_TC_45,IMP_houses_TC_85)


figname = 'EFC_houses_TS'

plot_EFC(figname,'houses',[0,5.2e10],IMP_houses_TS,IMP_houses_TS_45,IMP_houses_TS_85)


figname = 'EFC_houses_TC_adapt'

plot_EFC_adapt(figname,'TC','houses',[0,5.2e10],IMP_houses_TC_eg_45,IMP_houses_TC_eg_85,IMP_houses_TC_eg_45_meas,IMP_houses_TC_eg_85_meas)


figname = 'EFC_houses_TS_adpat'

plot_EFC_adapt(figname,'TS','houses',[0,5.2e10],IMP_houses_TS_eg_45,IMP_houses_TS_eg_85,IMP_houses_TS_eg_45_meas,IMP_houses_TS_eg_85_meas)





## Agriculture


figname = 'EXP_agri'

plot_exp(figname,'agri',[5.0e4,1.0e6])


figname = 'IMP_agri_TC'

plot_imp(figname,'agri',[1.0e0,1.0e4],IMP_agri_TC)

figname = 'IMP_agri_TS'

plot_imp(figname,'agri',[1.0e0,1.0e4],IMP_agri_TS)


figname = 'IMP_agri_TC_diff45'

IMP_agri_TC_diff45 = copy.deepcopy(IMP_agri_TC)

IMP_agri_TC_diff45.eai_exp = IMP_agri_TC_45.eai_exp - IMP_agri_TC.eai_exp

plot_imp(figname,'agri',[1.0e0,1.0e4],IMP_agri_TC_diff45)



figname = 'IMP_agri_TC_diff85'

IMP_agri_TC_diff85 = copy.deepcopy(IMP_agri_TC)

IMP_agri_TC_diff85.eai_exp = IMP_agri_TC_85.eai_exp - IMP_agri_TC.eai_exp

plot_imp(figname,'agri',[1.0e0,1.0e4],IMP_agri_TC_diff85)



figname = 'IMP_agri_TS_diff45'

IMP_agri_TS_diff45 = copy.deepcopy(IMP_agri_TS)

IMP_agri_TS_diff45.eai_exp = IMP_agri_TS_45.eai_exp - IMP_agri_TS.eai_exp

plot_imp(figname,'agri',[1.0e0,1.0e4],IMP_agri_TS_diff45)



figname = 'IMP_agri_TS_diff85'

IMP_agri_TS_diff85 = copy.deepcopy(IMP_agri_TS)

IMP_agri_TS_diff85.eai_exp = IMP_agri_TS_85.eai_exp - IMP_agri_TS.eai_exp

plot_imp(figname,'agri',[1.0e0,1.0e4],IMP_agri_TS_diff85)




figname = 'EFC_agri_TC'

plot_EFC(figname,'agri',[0,1.0e10],IMP_agri_TC,IMP_agri_TC_45,IMP_agri_TC_85)


figname = 'EFC_agri_TS'

plot_EFC(figname,'agri',[0,1.0e10],IMP_agri_TS,IMP_agri_TS_45,IMP_agri_TS_85)


figname = 'EFC_agri_TC_adapt'

plot_EFC_adapt(figname,'TC','agri',[0,1.0e10],IMP_agri_TC_eg_45,IMP_agri_TC_eg_85,IMP_agri_TC_eg_45_meas,IMP_agri_TC_eg_85_meas)


figname = 'EFC_agri_TS_adpat'

plot_EFC_adapt(figname,'TS','agri',[0,1.0e10],IMP_agri_TS_eg_45,IMP_agri_TS_eg_85,IMP_agri_TS_eg_45_meas,IMP_agri_TS_eg_85_meas)







## People


figname = 'EXP_people'

plot_exp(figname,'people', [1.0, 6.0e4])


figname = 'IMP_people_TC'

plot_imp(figname,'people',[1.0,1.0e2],IMP_people_TC)

figname = 'IMP_people_TS'

plot_imp(figname,'people',[1.0,1.0e2],IMP_people_TS)


figname = 'IMP_people_TC_diff45'

IMP_people_TC_diff45 = copy.deepcopy(IMP_people_TC)

IMP_people_TC_diff45.eai_exp = IMP_people_TC_45.eai_exp - IMP_people_TC.eai_exp

plot_imp(figname,'people',[1.0,1.0e2],IMP_people_TC_diff45)



figname = 'IMP_people_TC_diff85'

IMP_people_TC_diff85 = copy.deepcopy(IMP_people_TC)

IMP_people_TC_diff85.eai_exp = IMP_people_TC_85.eai_exp - IMP_people_TC.eai_exp

plot_imp(figname,'people',[1.0,1.0e2],IMP_people_TC_diff85)



figname = 'IMP_people_TS_diff45'

IMP_people_TS_diff45 = copy.deepcopy(IMP_people_TS)

IMP_people_TS_diff45.eai_exp = IMP_people_TS_45.eai_exp - IMP_people_TS.eai_exp

plot_imp(figname,'people',[1.0,1.0e2],IMP_people_TS_diff45)



figname = 'IMP_people_TS_diff85'

IMP_people_TS_diff85 = copy.deepcopy(IMP_people_TS)

IMP_people_TS_diff85.eai_exp = IMP_people_TS_85.eai_exp - IMP_people_TS.eai_exp

plot_imp(figname,'people',[1.0,1.0e2],IMP_people_TS_diff85)


figname = 'EFC_people_TC'

plot_EFC(figname,'people',[0,2.0e7],IMP_people_TC,IMP_people_TC_45,IMP_people_TC_85)


figname = 'EFC_people_TS'

plot_EFC(figname,'people',[0,2.0e7],IMP_people_TS,IMP_people_TS_45,IMP_people_TS_85)


figname = 'EFC_people_TC_adapt'

plot_EFC_adapt(figname,'TC','people',[0,2.0e7],IMP_people_TC_eg_45,IMP_people_TC_eg_85,IMP_people_TC_eg_45_meas,IMP_people_TC_eg_85_meas)


figname = 'EFC_people_TS_adpat'

plot_EFC_adapt(figname,'TS','people',[0,2.0e7],IMP_people_TS_eg_45,IMP_people_TS_eg_85,IMP_people_TS_eg_45_meas,IMP_people_TS_eg_85_meas)