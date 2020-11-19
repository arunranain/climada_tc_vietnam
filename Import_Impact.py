from climada.engine import Impact
from Configuration import *


IMP_houses_TS = Impact()
IMP_houses_TS_45 = Impact()
IMP_houses_TS_85 = Impact()
IMP_houses_TS_eg_45 = Impact()
IMP_houses_TS_eg_85 = Impact()
IMP_houses_TS_eg_45_meas = Impact()
IMP_houses_TS_eg_85_meas = Impact()



IMP_agri_TS = Impact()
IMP_agri_TS_45 = Impact()
IMP_agri_TS_85 = Impact()
IMP_agri_TS_eg_45 = Impact()
IMP_agri_TS_eg_85 = Impact()
IMP_agri_TS_eg_45_meas = Impact()
IMP_agri_TS_eg_85_meas = Impact()


IMP_people_TS = Impact()
IMP_people_TS_45 = Impact()
IMP_people_TS_85 = Impact()
IMP_people_TS_eg_45 = Impact()
IMP_people_TS_eg_85 = Impact()
IMP_people_TS_eg_45_meas = Impact()
IMP_people_TS_eg_85_meas = Impact()

IMP_houses_TS.read_csv(project_folder + 'impacts/' + 'IMP_houses_TS.csv')
IMP_houses_TS_45.read_csv(project_folder + 'impacts/' + 'IMP_houses_TS_45.csv')
IMP_houses_TS_85.read_csv(project_folder + 'impacts/' + 'IMP_houses_TS_85.csv')
IMP_houses_TS_eg_45.read_csv(project_folder + 'impacts/' + 'IMP_houses_TS_eg_45')
IMP_houses_TS_eg_85.read_csv(project_folder + 'impacts/' + 'IMP_houses_TS_eg_85')
IMP_houses_TS_eg_45_meas.read_csv(project_folder + 'impacts/' + 'IMP_houses_TS_eg_45_meas')
IMP_houses_TS_eg_85_meas.read_csv(project_folder + 'impacts/' + 'IMP_houses_TS_eg_85_meas')



IMP_agri_TS.read_csv(project_folder + 'impacts/' + 'IMP_agri_TS.csv')
IMP_agri_TS_45.read_csv(project_folder + 'impacts/' + 'IMP_agri_TS_45.csv')
IMP_agri_TS_85.read_csv(project_folder + 'impacts/' + 'IMP_agri_TS_85.csv')
IMP_agri_TS_eg_45.read_csv(project_folder + 'impacts/' + 'IMP_agri_TS_eg_45')
IMP_agri_TS_eg_85.read_csv(project_folder + 'impacts/' + 'IMP_agri_TS_eg_85')
IMP_agri_TS_eg_45_meas.read_csv(project_folder + 'impacts/' + 'IMP_agri_TS_eg_45_meas')
IMP_agri_TS_eg_85_meas.read_csv(project_folder + 'impacts/' + 'IMP_agri_TS_eg_85_meas')


IMP_people_TS.read_csv(project_folder + 'impacts/' + 'IMP_people_TS.csv')
IMP_people_TS_45.read_csv(project_folder + 'impacts/' + 'IMP_people_TS_45.csv')
IMP_people_TS_85.read_csv(project_folder + 'impacts/' + 'IMP_people_TS_85.csv')
IMP_people_TS_eg_45.read_csv(project_folder + 'impacts/' + 'IMP_people_TS_eg_45')
IMP_people_TS_eg_85.read_csv(project_folder + 'impacts/' + 'IMP_people_TS_eg_85')
IMP_people_TS_eg_45_meas.read_csv(project_folder + 'impacts/' + 'IMP_people_TS_eg_45_meas')
IMP_people_TS_eg_85_meas.read_csv(project_folder + 'impacts/' + 'IMP_people_TS_eg_85_meas')




# IMP_houses_TS.read_csv(project_folder + 'WF/' + 'IMP_houses_TS.csv')
# IMP_houses_TS_45.read_csv(project_folder + 'WF/' + 'IMP_houses_TS_45.csv')
# IMP_houses_TS_85.read_csv(project_folder + 'WF/' + 'IMP_houses_TS_85.csv')
# IMP_houses_TS_eg_45.read_csv(project_folder + 'WF/' + 'IMP_houses_TS_eg_45')
# IMP_houses_TS_eg_85.read_csv(project_folder + 'WF/' + 'IMP_houses_TS_eg_85')
# IMP_houses_TS_eg_45_meas.read_csv(project_folder + 'WF/' + 'IMP_houses_TS_eg_45_meas')
# IMP_houses_TS_eg_85_meas.read_csv(project_folder + 'WF/' + 'IMP_houses_TS_eg_85_meas')
#
#
#
# IMP_agri_TS.read_csv(project_folder + 'WF/' + 'IMP_agri_TS.csv')
# IMP_agri_TS_45.read_csv(project_folder + 'WF/' + 'IMP_agri_TS_45.csv')
# IMP_agri_TS_85.read_csv(project_folder + 'WF/' + 'IMP_agri_TS_85.csv')
# IMP_agri_TS_eg_45.read_csv(project_folder + 'WF/' + 'IMP_agri_TS_eg_45')
# IMP_agri_TS_eg_85.read_csv(project_folder + 'WF/' + 'IMP_agri_TS_eg_85')
# IMP_agri_TS_eg_45_meas.read_csv(project_folder + 'WF/' + 'IMP_agri_TS_eg_45_meas')
# IMP_agri_TS_eg_85_meas.read_csv(project_folder + 'WF/' + 'IMP_agri_TS_eg_85_meas')
#
#
# IMP_people_TS.read_csv(project_folder + 'WF/' + 'IMP_people_TS.csv')
# IMP_people_TS_45.read_csv(project_folder + 'WF/' + 'IMP_people_TS_45.csv')
# IMP_people_TS_85.read_csv(project_folder + 'WF/' + 'IMP_people_TS_85.csv')
# IMP_people_TS_eg_45.read_csv(project_folder + 'WF/' + 'IMP_people_TS_eg_45')
# IMP_people_TS_eg_85.read_csv(project_folder + 'WF/' + 'IMP_people_TS_eg_85')
# IMP_people_TS_eg_45_meas.read_csv(project_folder + 'WF/' + 'IMP_people_TS_eg_45_meas')
# IMP_people_TS_eg_85_meas.read_csv(project_folder + 'WF/' + 'IMP_people_TS_eg_85_meas')







IMP_houses_TC = Impact()
IMP_houses_TC_45 = Impact()
IMP_houses_TC_85 = Impact()
IMP_houses_TC_eg_45 = Impact()
IMP_houses_TC_eg_85 = Impact()
IMP_houses_TC_eg_45_meas = Impact()
IMP_houses_TC_eg_85_meas = Impact()



IMP_agri_TC = Impact()
IMP_agri_TC_45 = Impact()
IMP_agri_TC_85 = Impact()
IMP_agri_TC_eg_45 = Impact()
IMP_agri_TC_eg_85 = Impact()
IMP_agri_TC_eg_45_meas = Impact()
IMP_agri_TC_eg_85_meas = Impact()


IMP_people_TC = Impact()
IMP_people_TC_45 = Impact()
IMP_people_TC_85 = Impact()
IMP_people_TC_eg_45 = Impact()
IMP_people_TC_eg_85 = Impact()
IMP_people_TC_eg_45_meas = Impact()
IMP_people_TC_eg_85_meas = Impact()
#
IMP_houses_TC.read_csv(project_folder + 'impacts/' + 'IMP_houses_TC.csv')
IMP_houses_TC_45.read_csv(project_folder + 'impacts/' + 'IMP_houses_TC_45.csv')
IMP_houses_TC_85.read_csv(project_folder + 'impacts/' + 'IMP_houses_TC_85.csv')
IMP_houses_TC_eg_45.read_csv(project_folder + 'impacts/' + 'IMP_houses_TC_eg_45')
IMP_houses_TC_eg_85.read_csv(project_folder + 'impacts/' + 'IMP_houses_TC_eg_85')
IMP_houses_TC_eg_45_meas.read_csv(project_folder + 'impacts/' + 'IMP_houses_TC_eg_45_meas')
IMP_houses_TC_eg_85_meas.read_csv(project_folder + 'impacts/' + 'IMP_houses_TC_eg_85_meas')



IMP_agri_TC.read_csv(project_folder + 'impacts/' + 'IMP_agri_TC.csv')
IMP_agri_TC_45.read_csv(project_folder + 'impacts/' + 'IMP_agri_TC_45.csv')
IMP_agri_TC_85.read_csv(project_folder + 'impacts/' + 'IMP_agri_TC_85.csv')
IMP_agri_TC_eg_45.read_csv(project_folder + 'impacts/' + 'IMP_agri_TC_eg_45')
IMP_agri_TC_eg_85.read_csv(project_folder + 'impacts/' + 'IMP_agri_TC_eg_85')
IMP_agri_TC_eg_45_meas.read_csv(project_folder + 'impacts/' + 'IMP_agri_TC_eg_45_meas')
IMP_agri_TC_eg_85_meas.read_csv(project_folder + 'impacts/' + 'IMP_agri_TC_eg_85_meas')


IMP_people_TC.read_csv(project_folder + 'impacts/' + 'IMP_people_TC.csv')
IMP_people_TC_45.read_csv(project_folder + 'impacts/' + 'IMP_people_TC_45.csv')
IMP_people_TC_85.read_csv(project_folder + 'impacts/' + 'IMP_people_TC_85.csv')
IMP_people_TC_eg_45.read_csv(project_folder + 'impacts/' + 'IMP_people_TC_eg_45')
IMP_people_TC_eg_85.read_csv(project_folder + 'impacts/' + 'IMP_people_TC_eg_85')
IMP_people_TC_eg_45_meas.read_csv(project_folder + 'impacts/' + 'IMP_people_TC_eg_45_meas')
IMP_people_TC_eg_85_meas.read_csv(project_folder + 'impacts/' + 'IMP_people_TC_eg_85_meas')




# IMP_houses_TC.read_csv(project_folder + 'WF/' + 'IMP_houses_TC.csv')
# IMP_houses_TC_45.read_csv(project_folder + 'WF/' + 'IMP_houses_TC_45.csv')
# IMP_houses_TC_85.read_csv(project_folder + 'WF/' + 'IMP_houses_TC_85.csv')
# IMP_houses_TC_eg_45.read_csv(project_folder + 'WF/' + 'IMP_houses_TC_eg_45')
# IMP_houses_TC_eg_85.read_csv(project_folder + 'WF/' + 'IMP_houses_TC_eg_85')
# IMP_houses_TC_eg_45_meas.read_csv(project_folder + 'WF/' + 'IMP_houses_TC_eg_45_meas')
# IMP_houses_TC_eg_85_meas.read_csv(project_folder + 'WF/' + 'IMP_houses_TC_eg_85_meas')
#
#
#
# IMP_agri_TC.read_csv(project_folder + 'WF/' + 'IMP_agri_TC.csv')
# IMP_agri_TC_45.read_csv(project_folder + 'WF/' + 'IMP_agri_TC_45.csv')
# IMP_agri_TC_85.read_csv(project_folder + 'WF/' + 'IMP_agri_TC_85.csv')
# IMP_agri_TC_eg_45.read_csv(project_folder + 'WF/' + 'IMP_agri_TC_eg_45')
# IMP_agri_TC_eg_85.read_csv(project_folder + 'WF/' + 'IMP_agri_TC_eg_85')
# IMP_agri_TC_eg_45_meas.read_csv(project_folder + 'WF/' + 'IMP_agri_TC_eg_45_meas')
# IMP_agri_TC_eg_85_meas.read_csv(project_folder + 'WF/' + 'IMP_agri_TC_eg_85_meas')
#
#
# IMP_people_TC.read_csv(project_folder + 'WF/' + 'IMP_people_TC.csv')
# IMP_people_TC_45.read_csv(project_folder + 'WF/' + 'IMP_people_TC_45.csv')
# IMP_people_TC_85.read_csv(project_folder + 'WF/' + 'IMP_people_TC_85.csv')
# IMP_people_TC_eg_45.read_csv(project_folder + 'WF/' + 'IMP_people_TC_eg_45')
# IMP_people_TC_eg_85.read_csv(project_folder + 'WF/' + 'IMP_people_TC_eg_85')
# IMP_people_TC_eg_45_meas.read_csv(project_folder + 'WF/' + 'IMP_people_TC_eg_45_meas')
# IMP_people_TC_eg_85_meas.read_csv(project_folder + 'WF/' + 'IMP_people_TC_eg_85_meas')
#



print('Expected average annual impact houses TS: {:.2e}'.format(IMP_houses_TS.aai_agg))
print('Expected average annual impact houses TS cc45: {:.2e}'.format(IMP_houses_TS_45.aai_agg))
print('Expected average annual impact houses TS cc85: {:.2e}'.format(IMP_houses_TS_85.aai_agg))
print('Expected average annual impact houses TS cc85: {:.2e}'.format(IMP_houses_TS_eg_45.aai_agg))
print('Expected average annual impact houses TS cc85: {:.2e}'.format(IMP_houses_TS_eg_85.aai_agg))
print('Expected average annual impact houses TS cc85: {:.2e}'.format(IMP_houses_TS_eg_45_meas.aai_agg))
print('Expected average annual impact houses TS cc85: {:.2e}'.format(IMP_houses_TS_eg_85_meas.aai_agg))



print('Maximum payout houses TS cc85 10: {:.3e}'.format(IMP_houses_TS_eg_85.calc_freq_curve(10).impact))

print('Maximum payout houses TS cc85 25: {:.3e}'.format(IMP_houses_TS_eg_85.calc_freq_curve(25).impact))

print('Maximum payout houses TS cc85 100: {:.3e}'.format(IMP_houses_TS_eg_85.calc_freq_curve(100).impact))

print('Maximum payout houses TS cc85 adapt 10: {:.3e}'.format(IMP_houses_TS_eg_85_meas.calc_freq_curve(10).impact))

print('Maximum payout houses TS cc85 adapt 25: {:.3e}'.format(IMP_houses_TS_eg_85_meas.calc_freq_curve(25).impact))

print('Maximum payout houses TS cc85 adapt 100: {:.3e}'.format(IMP_houses_TS_eg_85_meas.calc_freq_curve(100).impact))


# print('Expected average annual impact agri TS: {:.2e}'.format(IMP_agri_TS.aai_agg))
# print('Expected average annual impact agri TS cc45: {:.2e}'.format(IMP_agri_TS_45.aai_agg))
# print('Expected average annual impact agri TS cc85: {:.2e}'.format(IMP_agri_TS_85.aai_agg))
# print('Expected average annual impact agri TS cc85: {:.2e}'.format(IMP_agri_TS_eg_45.aai_agg))
# print('Expected average annual impact agri TS cc85: {:.2e}'.format(IMP_agri_TS_eg_85.aai_agg))
# print('Expected average annual impact agri TS cc85: {:.2e}'.format(IMP_agri_TS_eg_45_meas.aai_agg))
# print('Expected average annual impact agri TS cc85: {:.2e}'.format(IMP_agri_TS_eg_85_meas.aai_agg))


# print('Expected average annual impact people TS: {:.2e}'.format(IMP_people_TS.aai_agg))
# print('Expected average annual impact people TS cc45: {:.2e}'.format(IMP_people_TS_45.aai_agg))
# print('Expected average annual impact people TS cc85: {:.2e}'.format(IMP_people_TS_85.aai_agg))
# print('Expected average annual impact people TS cc85: {:.2e}'.format(IMP_people_TS_eg_45.aai_agg))
# print('Expected average annual impact people TS cc85: {:.2e}'.format(IMP_people_TS_eg_85.aai_agg))
# print('Expected average annual impact people TS cc85: {:.2e}'.format(IMP_people_TS_eg_45_meas.aai_agg))
# print('Expected average annual impact people TS cc85: {:.2e}'.format(IMP_people_TS_eg_85_meas.aai_agg))

#
print('Expected average annual impact houses TC: {:.4e}'.format(IMP_houses_TC.aai_agg))
print('Expected average annual impact houses TC cc45: {:.4e}'.format(IMP_houses_TC_45.aai_agg))
print('Expected average annual impact houses TC cc85: {:.4e}'.format(IMP_houses_TC_85.aai_agg))
# print('Expected average annual impact houses TC cc85: {:.2e}'.format(IMP_houses_TC_eg_45.aai_agg))
# print('Expected average annual impact houses TC cc85: {:.2e}'.format(IMP_houses_TC_eg_85.aai_agg))
# print('Expected average annual impact houses TC cc85: {:.2e}'.format(IMP_houses_TC_eg_45_meas.aai_agg))
# print('Expected average annual impact houses TC cc85: {:.2e}'.format(IMP_houses_TC_eg_85_meas.aai_agg))


print('Expected average annual impact houses TC: {:.4e}'.format(IMP_houses_TC.calc_freq_curve(10).impact))
print('Expected average annual impact houses TC: {:.4e}'.format(IMP_houses_TC.calc_freq_curve(25).impact))
print('Expected average annual impact houses TC: {:.4e}'.format(IMP_houses_TC.calc_freq_curve(100).impact))

print('Expected average annual impact houses TC: {:.4e}'.format(IMP_houses_TC_85.calc_freq_curve(10).impact))
print('Expected average annual impact houses TC: {:.4e}'.format(IMP_houses_TC_85.calc_freq_curve(25).impact))
print('Expected average annual impact houses TC: {:.4e}'.format(IMP_houses_TC_85.calc_freq_curve(100).impact))




#
# print('Expected average annual impact agri TC: {:.2e}'.format(IMP_agri_TC.aai_agg))
# print('Expected average annual impact agri TC cc45: {:.2e}'.format(IMP_agri_TC_45.aai_agg))
# print('Expected average annual impact agri TC cc85: {:.2e}'.format(IMP_agri_TC_85.aai_agg))
# print('Expected average annual impact agri TC cc85: {:.2e}'.format(IMP_agri_TC_eg_45.aai_agg))
# print('Expected average annual impact agri TC cc85: {:.2e}'.format(IMP_agri_TC_eg_85.aai_agg))
# print('Expected average annual impact agri TC cc85: {:.2e}'.format(IMP_agri_TC_eg_45_meas.aai_agg))
# print('Expected average annual impact agri TC cc85: {:.2e}'.format(IMP_agri_TC_eg_85_meas.aai_agg))


# print('Expected average annual impact people TC: {:.2e}'.format(IMP_people_TC.aai_agg))
# print('Expected average annual impact people TC cc45: {:.2e}'.format(IMP_people_TC_45.aai_agg))
# print('Expected average annual impact people TC cc85: {:.2e}'.format(IMP_people_TC_85.aai_agg))
# print('Expected average annual impact people TC cc85: {:.2e}'.format(IMP_people_TC_eg_45.aai_agg))
# print('Expected average annual impact people TC cc85: {:.2e}'.format(IMP_people_TC_eg_85.aai_agg))
# print('Expected average annual impact people TC cc85: {:.2e}'.format(IMP_people_TC_eg_45_meas.aai_agg))
# print('Expected average annual impact people TC cc85: {:.2e}'.format(IMP_people_TC_eg_85_meas.aai_agg))

#
# print('Maximum payout agri TC cc85: {:.3e}'.format(IMP_agri_TC_eg_85_meas.calc_freq_curve(100).impact - IMP_agri_TC_eg_85_meas.calc_freq_curve(5).impact))
#
# print('Maximum payout houses TC cc85: {:.3e}'.format(IMP_houses_TC_eg_85_meas.calc_freq_curve(100).impact - IMP_houses_TC_eg_85_meas.calc_freq_curve(10).impact))
#
#
# print('Maximum payout agri TS cc85: {:.3e}'.format(IMP_agri_TS_eg_85_meas.calc_freq_curve(100).impact - IMP_agri_TS_eg_85_meas.calc_freq_curve(5).impact))
#
# print('Maximum payout houses TS cc85: {:.3e}'.format(IMP_houses_TS_eg_85_meas.calc_freq_curve(100).impact - IMP_houses_TS_eg_85_meas.calc_freq_curve(10).impact))


