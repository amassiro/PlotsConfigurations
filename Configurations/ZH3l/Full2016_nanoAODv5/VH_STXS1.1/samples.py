import os

global getSampleFiles
from LatinoAnalysis.Tools.commonTools import getSampleFiles, addSampleWeight, getBaseWnAOD

def getSampleFilesNano(inputDir,Sample,absPath=False):
    return getSampleFiles(inputDir,Sample,absPath,'nanoLatino_')

##############################################
###### Tree Directory according to site ######
##############################################

treeBaseDir = "/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/"

directoryMC     = os.path.join(treeBaseDir,"Summer16_102X_nAODv4_Full2016v5/MCl1loose2016v5__MCCorr2016v5__l2loose__l2tightOR2016v5/")
directoryDATA   = os.path.join(treeBaseDir,"Run2016_102X_nAODv4_Full2016v5/DATAl1loose2016v5__l2loose__l2tightOR2016v5/")
directoryFAKE   = os.path.join(treeBaseDir,"Run2016_102X_nAODv4_Full2016v5/DATAl1loose2016v5__l2loose__fakeW/")

################################################
############### WP #############################
################################################

#2016 
eleWP='mva_90p_Iso2016'
muWP='cut_Tight80x'

LepWPCut        = 'LepCut3l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF3l__ele_'+eleWP+'__mu_'+muWP

#... And the fakeW
fakeW = 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3l'

################################################
############ basic mc weights ##################
################################################

XSweight  = 'XSWeight'
SFweight  = 'SFweight3l*'+LepWPweight+'*'+LepWPCut+'*PrefireWeight*btagSF'

GenLepMatch2l = 'GenLepMatch2l'
GenLepMatch3l = 'GenLepMatch3l'

wz1jSF = '1.0'
wz2jSF = '1.0'
zg1jSF = '1.0'
zg2jSF = '1.0'

################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
    ['B','Run2016B-Nano14Dec2018_ver2-v1'] ,
    ['C','Run2016C-Nano14Dec2018-v1'] ,
    ['D','Run2016D-Nano14Dec2018-v1'] ,
    ['E','Run2016E-Nano14Dec2018-v1'] ,
    ['F','Run2016F-Nano14Dec2018-v1'] ,
    ['G','Run2016G-Nano14Dec2018-v1'] ,
    ['H','Run2016H-Nano14Dec2018-v1'] ,
]

DataSets = ['MuonEG','DoubleMuon','SingleMuon','DoubleEG','SingleElectron']

DataTrig = {
    'MuonEG'         : ' Trigger_ElMu' ,
    'SingleMuon'     : '!Trigger_ElMu && Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_ElMu && !Trigger_sngMu && Trigger_sngEl',
    'DoubleMuon'     : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && Trigger_dblMu',
    'DoubleEG'       : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && !Trigger_dblMu && Trigger_dblEl'
}

###########################################
#############  BACKGROUNDS  ###############
###########################################

samples['ZZ']  = {    'name': getSampleFilesNano(directoryMC,'ZZTo4L'),
                      'weight' : XSweight+'*'+SFweight+'*'+GenLepMatch3l+'*'+METFilter_MC,
                      'suppressNegativeNuisances' :['all'],
                      'FilesPerJob' : 5,
                  }

samples['WZ']  = {    'name'   : getSampleFilesNano(directoryMC,'WZTo3LNu')
                                +getSampleFilesNano(directoryMC,'WZTo3LNu_ext1'),
                      'weight' : '(( Alt$(CleanJet_pt[1],0) < 30 )*'+wz1jSF+'+( Alt$(CleanJet_pt[1],0) >= 30 )*'+wz2jSF+')*'+XSweight+'*'+SFweight+'*'+GenLepMatch3l+'*'+METFilter_MC ,
                      'suppressNegativeNuisances' :['all'],
                      'FilesPerJob' : 2,
                  }

WZbaseW = getBaseWnAOD(directoryMC,'Summer16_102X_nAODv4_Full2016v5',['WZTo3LNu','WZTo3LNu_ext1'])
addSampleWeight(samples,'WZ','WZTo3LNu',     WZbaseW+'/baseW')
addSampleWeight(samples,'WZ','WZTo3LNu_ext1',WZbaseW+'/baseW')

samples['VVV'] = {    'name': getSampleFilesNano(directoryMC,'WZZ')
                             +getSampleFilesNano(directoryMC,'ZZZ')
                             +getSampleFilesNano(directoryMC,'WWZ')
                             +getSampleFilesNano(directoryMC,'WWW'),
                      'weight' : XSweight+'*'+SFweight+'*'+GenLepMatch3l+'*'+METFilter_MC,
                      'suppressNegativeNuisances' :['all'],
                      'FilesPerJob' : 5,
                  }

samples['Zg']  = {    'name':  getSampleFilesNano(directoryMC,'Zg'),
                      'weight' : '(( Alt$(CleanJet_pt[1],0) < 30 )*'+zg1jSF+'+( Alt$(CleanJet_pt[1],0) >= 30 )*'+zg2jSF+')*'+XSweight+'*'+SFweight+'*'+GenLepMatch3l+'*'+METFilter_MC ,
                      'suppressNegativeNuisances' :['all'],
                      'FilesPerJob' : 5,
                  }

samples['ttZ']  = {    'name': getSampleFilesNano(directoryMC,'TTZjets'),
                       'weight' : XSweight+'*'+SFweight+'*'+GenLepMatch2l+'*'+METFilter_MC,
                       'suppressNegativeNuisances' :['all'],
                       'FilesPerJob' : 5,
                   }

####################################
############# Signal ###############
####################################

samples['WH_htt']  = {  'name': getSampleFilesNano(directoryMC,'HWminusJ_HToTauTau_M125')
                               +getSampleFilesNano(directoryMC,'HWplusJ_HToTauTau_M125')
                               +getSampleFilesNano(directoryMC,'HZJ_HToTauTau_M125'),
                        'weight' : XSweight+'*'+SFweight+'*'+GenLepMatch3l+'*'+METFilter_MC,
                        'suppressNegativeNuisances' :['all'],
                        'FilesPerJob' : 5,
                    }

if os.path.exists('HTXS_categories.py') :
  handle = open('HTXS_categories.py','r')
  exec(handle)
  handle.close()

samples['WH_hww']  = { 'name': getSampleFilesNano(directoryMC,'HWminusJ_HToWW_M125_PrivateNano')
                              +getSampleFilesNano(directoryMC,'HWplusJ_HToWW_M125_PrivateNano'),
                       'weight' : XSweight+'*'+SFweight+'*'+GenLepMatch3l+'*'+METFilter_MC,
                       'suppressNegativeNuisances' :['all'],
                       'FilesPerJob' : 5,
                   }

samples['WH_hww']['subsamples'] = {}
for cat,cut in categorization_wh.iteritems():
    samples['WH_hww']['subsamples'][cat] = cut

samples['ZH_hww']  = {  'name': getSampleFilesNano(directoryMC,'HZJ_HToWW_M125_PrivateNano'),
                        'weight' : XSweight+'*'+SFweight+'*'+GenLepMatch3l+'*'+METFilter_MC,
                        'suppressNegativeNuisances' :['all'],
                        'FilesPerJob' : 5,
                    }

samples['ggZH_hww'] = {  'name': getSampleFilesNano(directoryMC,'ggZH_HToWW_M125_PrivateNano'),
                         'weight' : XSweight+'*'+SFweight+'*'+GenLepMatch3l+'*'+METFilter_MC,
                         'suppressNegativeNuisances' :['all'],
                         'FilesPerJob' : 5,
                     }

samples['ZH_hww']['subsamples'] = {}
samples['ggZH_hww']['subsamples'] = {}
for cat,cut in categorization_zh.iteritems():
    samples['ZH_hww']['subsamples'][cat] = cut
    samples['ggZH_hww']['subsamples'][cat] = cut

###########################################
################## FAKE ###################
###########################################

samples['Fake']  = {   'name': [] ,
                       'weight' : fakeW+'*EMTFbug_veto*'+METFilter_DATA,
                       'weights' : [],
                       'isData': ['all'],
                       'FilesPerJob' : 20 ,
                   }

###########################################
################## DATA ###################
###########################################

samples['DATA']  = {   'name': [] ,
                       'weight' : 'EMTFbug_veto*'+METFilter_DATA+'*'+LepWPCut,
                       'weights' : [],
                       'isData': ['all'],
                       'FilesPerJob' : 20 ,
                   }

for Run in DataRun :
    directoryDATARun = directoryDATA.format(Run[0])
    directoryFAKERun = directoryFAKE.format(Run[0])
    for DataSet in DataSets :
        FileTargetDATA = getSampleFilesNano(directoryDATARun,DataSet+'_'+Run[1],True)
        FileTargetFAKE = getSampleFilesNano(directoryFAKERun,DataSet+'_'+Run[1],True)
        for iFile in FileTargetDATA:
            samples['DATA']['name']   .append(iFile)
            samples['DATA']['weights'].append(DataTrig[DataSet])
        for iFile in FileTargetFAKE:
            samples['Fake']['name']   .append(iFile)
            samples['Fake']['weights'].append(DataTrig[DataSet])
                
samples['Fake']['subsamples'] = {
    'em': 'abs(ZH3l_pdgid_l) == 11',
    'me': 'abs(ZH3l_pdgid_l) == 13'
}