# nuisances

#nuisances = {}

# name of samples here must match keys in samples.py 

# imported from samples.py:
# samples, treeBaseDir, mcProduction, mcSteps
# imported from cuts.py
# cuts

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

try:
    mc_emb = [skey for skey in samples if skey != 'DATA' and skey != 'Dyveto' and not skey.startswith('Fake')]
    mc = [skey for skey in mc_emb if skey != 'Dyemb']
except NameError:
    mc = []
    cuts = {}
    nuisances = {}
    def makeMCDirectory(x=''):
        return ''

from LatinoAnalysis.Tools.HiggsXSection import HiggsXSection
HiggsXS = HiggsXSection()


cuts0j = []
cuts1j = []
cuts2j = []

for k in cuts:
  for cat in cuts[k]['categories']:
    if '0j' in cat: cuts0j.append(k+'_'+cat)
    elif '1j' in cat: cuts1j.append(k+'_'+cat)
    elif '2j' in cat: cuts2j.append(k+'_'+cat)
    else: print 'WARNING: name of category does not contain either 0j,1j,2j'

################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity

#nuisances['lumi'] = {
#    'name': 'lumi_13TeV_2018',
#    'type': 'lnN',
#    'samples': dict((skey, '1.025') for skey in mc if skey not in ['WW', 'top', 'DY'])
#}

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

#### FAKES

nuisances['fake_syst_em'] = {
    'name': 'CMS_fake_syst_em',
    'type': 'lnN',
    'samples': {
        'Fake_em': '1.3'
    },
    'cutspost': lambda self, cuts: [cut for cut in cuts if '20me' not in cut],
}

nuisances['fake_syst_me'] = {
    'name': 'CMS_fake_syst_me',
    'type': 'lnN',
    'samples': {
        'Fake_me': '1.3'
    },
    'cutspost': lambda self, cuts: [cut for cut in cuts if '20em' not in cut],
}

nuisances['fake_ele'] = {
    'name': 'CMS_fake_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWEleUp', 'fakeWEleDown'],
    }
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatEleUp', 'fakeWStatEleDown']
    }
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWMuUp', 'fakeWMuDown'],
    }
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatMuUp', 'fakeWStatMuDown'],
    }
}

##### B-tagger

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2018'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }

##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc_emb)
}

##### Electron Efficiency and energy scale

nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc_emb)
}

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('ElepTup_suffix'),
    'folderDown': makeMCDirectory('ElepTdo_suffix'),
    'AsLnN': '1'
}

if useEmbeddedDY:
  nuisances['electronpt_emb'] = {
    'name': 'CMS_scale_e_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp' : 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': {'Dyemb': ['1', '1']},
    'folderUp': treeBaseDir+'/Embedding2018_102X_nAODv6_Full2018v6/DATAl1loose2018v6__l2loose__l2tightOR2018v6__Embedding__EmbElepTup_suffix/',
    'folderDown': treeBaseDir+'/Embedding2018_102X_nAODv6_Full2018v6/DATAl1loose2018v6__l2loose__l2tightOR2018v6__Embedding__EmbElepTdo_suffix/',
    'AsLnN': '1'
  }

##### Muon Efficiency and energy scale

nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc_emb)
}

nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('MupTup_suffix'),
    'folderDown': makeMCDirectory('MupTdo_suffix'),
    'AsLnN': '1'
}

if useEmbeddedDY:
  nuisances['muonpt_emb'] = {
    'name': 'CMS_scale_m_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp' : 'MupTup',
    'mapDown': 'MupTdo',
    'samples': {'Dyemb': ['1', '1']},
    'folderUp': treeBaseDir+'/Embedding2018_102X_nAODv6_Full2018v6/DATAl1loose2018v6__l2loose__l2tightOR2018v6__Embedding__EmbMupTup_suffix/',
    'folderDown': treeBaseDir+'/Embedding2018_102X_nAODv6_Full2018v6/DATAl1loose2018v6__l2loose__l2tightOR2018v6__Embedding__EmbMupTdo_suffix/',
    'AsLnN': '1'
  }

##### Jet energy scale
jes_systs = ['JESAbsolute','JESAbsolute_2018','JESBBEC1','JESBBEC1_2018','JESEC2','JESEC2_2018','JESFlavorQCD','JESHF','JESHF_2018','JESRelativeBal','JESRelativeSample_2018']

for js in jes_systs:
  nuisances[js] = {
      'name': 'CMS_scale_'+js,
      'kind': 'suffix',
      'type': 'shape',
      'mapUp': js+'up',
      'mapDown': js+'do',
      'samples': dict((skey, ['1', '1']) for skey in mc),
      'folderUp': makeMCDirectory('JESup_suffix'),
      'folderDown': makeMCDirectory('JESdo_suffix'),
      'AsLnN': '1'
  }

##### MET energy scale

nuisances['met'] = {
    'name': 'CMS_scale_met_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'METup',
    'mapDown': 'METdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('METup_suffix'),
    'folderDown': makeMCDirectory('METdo_suffix'),
    'AsLnN': '1'
}

##### Di-Tau vetoing for embedding
if useEmbeddedDY: 
  nuisances['embedveto']  = {
                  'name'  : 'CMS_embed_veto_2018',
                  'kind'  : 'weight',
                  'type'  : 'shape',
                  'samples'  : {
                     'Dyemb'    : ['1', '1'],
                     'Dyveto'   : ['0.1', '-0.1'],
                  }
  }

##### Pileup

nuisances['PU'] = {
    'name': 'CMS_PU_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'DY': ['0.993259983266*(puWeightUp/puWeight)', '0.997656381501*(puWeightDown/puWeight)'],
        'top': ['1.00331969187*(puWeightUp/puWeight)', '0.999199609528*(puWeightDown/puWeight)'],
        'WW': ['1.0033022059*(puWeightUp/puWeight)', '0.997085330608*(puWeightDown/puWeight)'],
        'ggH_hww': ['1.0036768006*(puWeightUp/puWeight)', '0.995996570285*(puWeightDown/puWeight)'],
        'qqH_hww': ['1.00374694528*(puWeightUp/puWeight)', '0.995878596852*(puWeightDown/puWeight)'],
    },
    'AsLnN': '1',
}

##### PS
nuisances['PS_ISR']  = {
    'name': 'PS_ISR',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'VgS'    : ['1.0000536116408023*(nCleanGenJet==0) + 1.0100100693580492*(nCleanGenJet==1) + 0.959068359375*(nCleanGenJet==2) + 0.9117049260469496*(nCleanGenJet>=3)', '0.9999367833485968*(nCleanGenJet==0) + 0.9873682892005163*(nCleanGenJet==1) + 1.0492717737268518*(nCleanGenJet==2) + 1.1176958835210322*(nCleanGenJet>=3)'],
        'ggWW'   : ['1.040233912070831*(nCleanGenJet==0) + 0.9611236379290876*(nCleanGenJet==1) + 0.9014289294088699*(nCleanGenJet==2) + 0.864310738090035*(nCleanGenJet>=3)', '0.9510305474211223*(nCleanGenJet==0) + 1.0433432942960381*(nCleanGenJet==1) + 1.1271383507266095*(nCleanGenJet==2) + 1.1885756983901514*(nCleanGenJet>=3)'],
        'WW'     : ['1.0005237869294796*(nCleanGenJet==0) + 1.0157425373134328*(nCleanGenJet==1) + 0.9644598124510606*(nCleanGenJet==2) + 0.9271488926223369*(nCleanGenJet>=3)', '0.9993553300024391*(nCleanGenJet==0) + 0.9806102300995024*(nCleanGenJet==1) + 1.042603303739856*(nCleanGenJet==2) + 1.0950369125887705*(nCleanGenJet>=3)'],
        'top'    : ['1.0020618369910668*(nCleanGenJet==0) + 1.0063081530771556*(nCleanGenJet==1) + 1.0094298425968304*(nCleanGenJet==2) + 0.9854207999040726*(nCleanGenJet>=3)', '0.9974340279269026*(nCleanGenJet==0) + 0.9920634820709106*(nCleanGenJet==1) + 0.988226385054923*(nCleanGenJet==2) + 1.017968568319235*(nCleanGenJet>=3)'],
        'DY'     : ['0.9998177685645392*(nCleanGenJet==0) + 1.0080838149428026*(nCleanGenJet==1) + 1.0057948912950987*(nCleanGenJet==2) + 0.9721358221196619*(nCleanGenJet>=3)', '1.0003244155266309*(nCleanGenJet==0) + 0.9897992135367016*(nCleanGenJet==1) + 0.9928782069009531*(nCleanGenJet==2) + 1.0348902921423981*(nCleanGenJet>=3)'],
        'VVV'    : ['1.0270826786253018*(nCleanGenJet==0) + 1.0198703447307862*(nCleanGenJet==1) + 1.0109191915514344*(nCleanGenJet==2) + 0.9838184220287978*(nCleanGenJet>=3)', '0.9661665482954546*(nCleanGenJet==0) + 0.9751744967838527*(nCleanGenJet==1) + 0.9859624782745712*(nCleanGenJet==2) + 1.0202995039288625*(nCleanGenJet>=3)'],
        'ggH_hww': ['1.0007510488273352*(nCleanGenJet==0) + 1.0152476349471342*(nCleanGenJet==1) + 0.9645590929269297*(nCleanGenJet==2) + 0.9189171704206691*(nCleanGenJet>=3)', '0.9989909143752528*(nCleanGenJet==0) + 0.9814978813068076*(nCleanGenJet==1) + 1.0416554335980368*(nCleanGenJet==2) + 1.1060543963750413*(nCleanGenJet>=3)'],
        'qqH_hww': ['1.0008858084852863*(nCleanGenJet==0) + 1.001293920824975*(nCleanGenJet==1) + 1.0013304143711548*(nCleanGenJet==2) + 0.9875473532521144*(nCleanGenJet>=3)', '0.9987483211480337*(nCleanGenJet==0) + 0.9982952329209852*(nCleanGenJet==1) + 0.9983076740658964*(nCleanGenJet==2) + 1.016023412328836*(nCleanGenJet>=3)'],
        'WH_hww' : ['1.0006979353025824*(nCleanGenJet==0) + 1.0014529360558138*(nCleanGenJet==1) + 1.0007920644457673*(nCleanGenJet==2) + 0.996814275350521*(nCleanGenJet>=3)', '0.9990367459746422*(nCleanGenJet==0) + 0.9980712824836634*(nCleanGenJet==1) + 0.9989875513096169*(nCleanGenJet==2) + 1.0039628146069568*(nCleanGenJet>=3)'],
        'ZH_hww' : ['1.0008198940532742*(nCleanGenJet==0) + 1.001574300159756*(nCleanGenJet==1) + 1.0014892423703352*(nCleanGenJet==2) + 0.9982835923429388*(nCleanGenJet>=3)', '0.9991322211949244*(nCleanGenJet==0) + 0.9979828392772856*(nCleanGenJet==1) + 0.9980190791034156*(nCleanGenJet==2) + 1.0021025907582017*(nCleanGenJet>=3)'],
    },
}

nuisances['PS_FSR']  = {
    'name': 'PS_FSR',
    'kind': 'weight',
    'type': 'shape',
    'samples': { 
        'VgS'    : ['0.9976593177227735*(nCleanGenJet==0) + 1.0016125187585532*(nCleanGenJet==1) + 1.0049344618055556*(nCleanGenJet==2) + 1.0195631514301164*(nCleanGenJet>=3)', '1.0026951855766457*(nCleanGenJet==0) + 1.0008132148661049*(nCleanGenJet==1) + 1.003949291087963*(nCleanGenJet==2) + 0.9708160910230832*(nCleanGenJet>=3)'],
        'ggWW'   : ['0.9910563426395067*(nCleanGenJet==0) + 1.0069894351287263*(nCleanGenJet==1) + 1.016616376034912*(nCleanGenJet==2) + 1.015902717074592*(nCleanGenJet>=3)', '1.0147395976461193*(nCleanGenJet==0) + 0.9860219489006646*(nCleanGenJet==1) + 0.9694680606617647*(nCleanGenJet==2) + 0.9489845115821678*(nCleanGenJet>=3)'],
        'WW'     : ['0.995462478372054*(nCleanGenJet==0) + 1.0052129975124378*(nCleanGenJet==1) + 1.008836750560578*(nCleanGenJet==2) + 0.9984120564941189*(nCleanGenJet>=3)', '1.008927720738437*(nCleanGenJet==0) + 0.995163868159204*(nCleanGenJet==1) + 0.9911024228315418*(nCleanGenJet==2) + 0.9763787172658678*(nCleanGenJet>=3)'],
        'top'    : ['0.9910899786333963*(nCleanGenJet==0) + 0.9990635702054794*(nCleanGenJet==1) + 1.002141744200183*(nCleanGenJet==2) + 1.0129742776372779*(nCleanGenJet>=3)', '1.0068843378231833*(nCleanGenJet==0) + 0.998988498438759*(nCleanGenJet==1) + 0.9952696584115224*(nCleanGenJet==2) + 0.9790955840673237*(nCleanGenJet>=3)'],
        'DY'     : ['0.9958763409773141*(nCleanGenJet==0) + 1.0041335498093422*(nCleanGenJet==1) + 1.0163363150953029*(nCleanGenJet==2) + 1.0296733670670226*(nCleanGenJet>=3)', '1.0066775262249232*(nCleanGenJet==0) + 0.9945601465681602*(nCleanGenJet==1) + 0.9662459619335311*(nCleanGenJet==2) + 0.9479423453563661*(nCleanGenJet>=3)'],
        'VVV'    : ['0.9809047855490748*(nCleanGenJet==0) + 0.9823641498350338*(nCleanGenJet==1) + 0.9976414629808243*(nCleanGenJet==2) + 1.0077953569413387*(nCleanGenJet>=3)', '1.035388723727876*(nCleanGenJet==0) + 1.0347339790465233*(nCleanGenJet==1) + 1.0017058788771533*(nCleanGenJet==2) + 0.9829344116371653*(nCleanGenJet>=3)'],
        'ggH_hww': ['0.9936588910230489*(nCleanGenJet==0) + 1.0087564198432573*(nCleanGenJet==1) + 1.014636529653396*(nCleanGenJet==2) + 1.00399261707105*(nCleanGenJet>=3)','1.0125063182369591*(nCleanGenJet==0) + 0.9846168672324244*(nCleanGenJet==1) + 0.9778204449152542*(nCleanGenJet==2) + 1.0014057292097962*(nCleanGenJet>=3)'],
        'qqH_hww': ['0.9902864012471768*(nCleanGenJet==0) + 0.9950165165635796*(nCleanGenJet==1) + 1.0024778632714528*(nCleanGenJet==2) + 1.0132965690130387*(nCleanGenJet>=3)', '1.0171041801597582*(nCleanGenJet==0) + 1.0088822239287307*(nCleanGenJet==1) + 0.9946938338710369*(nCleanGenJet==2) + 0.9782409053438381*(nCleanGenJet>=3)'],
        'WH_hww' : ['0.9864466858859676*(nCleanGenJet==0) + 0.9911412676207558*(nCleanGenJet==1) + 1.0047988929561447*(nCleanGenJet==2) + 1.0135375714689319*(nCleanGenJet>=3)', '1.022768308571873*(nCleanGenJet==0) + 1.0147067259919833*(nCleanGenJet==1) + 0.9932121652658327*(nCleanGenJet==2) + 0.9807301742549035*(nCleanGenJet>=3)'],
        'ZH_hww' : ['0.98702584755388*(nCleanGenJet==0) + 0.9881328970299905*(nCleanGenJet==1) + 1.0046199525397077*(nCleanGenJet==2) + 1.0091561054313662*(nCleanGenJet>=3)', '1.0236225630459734*(nCleanGenJet==0) + 1.0213677207764504*(nCleanGenJet==1) + 0.9933149152918336*(nCleanGenJet==2) + 0.978832627595614*(nCleanGenJet>=3)'],
    },
}


# An overall 1.5% UE uncertainty will cover all the UEup/UEdo variations
# And we don't observe any dependency of UE variations on njet
nuisances['UE']  = {
                'name'  : 'UE_CP5',
                'skipCMS' : 1,
                'type': 'lnN',
                'samples': dict((skey, '1.015') for skey in mc), 
}

#nuisances['UE']  = {
#                'name'  : 'UE_CP5',
#                'skipCMS' : 1,
#                'kind'  : 'tree',
#                'type'  : 'shape',
#                'samples'  : {
#                  'WW'      : ['1.0017139', '0.99350287'],
#                  'ggH_hww' : ['1.0272226', '1.0123689'],
#                  'qqH_hww' : ['1.0000192', '0.98367442']
#                },
#                'folderUp': makeMCDirectory('UEup'),
#                'folderDown': makeMCDirectory('UEdo'),
#                'AsLnN'      : '1',
#}

####### Generic "cross section uncertainties"

apply_on = {
    'top': [
        'isSingleTop * 1.0816 + isTTbar',
        'isSingleTop * 0.9184 + isTTbar'
    ]
}

nuisances['singleTopToTTbar'] = {
    'name': 'singleTopToTTbar',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': apply_on
}

## Top pT reweighting uncertainty

nuisances['TopPtRew'] = {
    'name': 'CMS_topPtRew',   # Theory uncertainty
    'kind': 'weight',
    'type': 'shape',
    'samples': {'top': ["1.", "1./Top_pTrw"]},
    'symmetrize': True
}

nuisances['VgStar'] = {
    'name': 'CMS_hww_VgStarScale',
    'type': 'lnN',
    'samples': {
        'VgS_L': '1.25'
    }
}

nuisances['VZ'] = {
    'name': 'CMS_hww_VZScale',
    'type': 'lnN',
    'samples': {
        'VgS_H': '1.16'
    }
}

###### pdf uncertainties

valuesggh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH','125.09','pdf','sm')
valuesggzh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','pdf','sm')
valuesbbh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','bbH','125.09','pdf','sm')

nuisances['pdf_Higgs_gg'] = {
    'name': 'pdf_Higgs_gg',
    'samples': {
        'ggH_hww': valuesggh,
        'ggH_htt': valuesggh,
        'ggZH_hww': valuesggzh,
        'bbH_hww': valuesbbh
    },
    'type': 'lnN',
}

values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','pdf','sm')

nuisances['pdf_Higgs_ttH'] = {
    'name': 'pdf_Higgs_ttH',
    'samples': {
        'ttH_hww': values
    },
    'type': 'lnN',
}

valuesqqh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm')
valueswh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','pdf','sm')
valueszh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','pdf','sm')

nuisances['pdf_Higgs_qqbar'] = {
    'name': 'pdf_Higgs_qqbar',
    'type': 'lnN',
    'samples': {
        'qqH_hww': valuesqqh,
        'qqH_htt': valuesqqh,
        'WH_hww': valueswh,
        'WH_htt': valueswh,
        'ZH_hww': valueszh,
        'ZH_htt': valueszh
    },
}

nuisances['pdf_qqbar'] = {
    'name': 'pdf_qqbar',
    'type': 'lnN',
    'samples': {
        'Vg': '1.04',
        'VZ': '1.04',  # PDF: 0.0064 / 0.1427 = 0.0448493
        'VgS': '1.04', # PDF: 0.0064 / 0.1427 = 0.0448493
    },
}

nuisances['pdf_Higgs_gg_ACCEPT'] = {
    'name': 'pdf_Higgs_gg_ACCEPT',
    'samples': {
        'ggH_hww': '1.006',
        'ggH_htt': '1.006',
        'ggZH_hww': '1.006',
        'bbH_hww': '1.006'
    },
    'type': 'lnN',
}

nuisances['pdf_gg_ACCEPT'] = {
    'name': 'pdf_gg_ACCEPT',
    'samples': {
        'ggWW': '1.006',
    },
    'type': 'lnN',
}

nuisances['pdf_Higgs_qqbar_ACCEPT'] = {
    'name': 'pdf_Higgs_qqbar_ACCEPT',
    'type': 'lnN',
    'samples': {
        'qqH_hww': '1.002',
        'qqH_htt': '1.002',
        'WH_hww': '1.003',
        'WH_htt': '1.003',
        'ZH_hww': '1.002',
        'ZH_htt': '1.002',
    },
}

nuisances['pdf_qqbar_ACCEPT'] = {
    'name': 'pdf_qqbar_ACCEPT',
    'type': 'lnN',
    'samples': {
        'VZ': '1.001',
    },
}

##### Renormalization & factorization scales

## Shape nuisance due to QCD scale variations for DY
# LHE scale variation weights (w_var / w_nominal)

## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']

nuisances['QCDscale_V'] = {
    'name': 'QCDscale_V',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {'DY': variations},
    'AsLnN': '1'
}

nuisances['QCDscale_VV'] = {
    'name': 'QCDscale_VV',
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
        'Vg': variations,
        'VZ': variations,
        'VgS': variations
    }
}

nuisances['QCDscale_ggVV'] = {
    'name': 'QCDscale_ggVV',
    'type': 'lnN',
    'samples': {
        'ggWW': '1.15',
    },
}

##### Renormalization & factorization scales
nuisances['WWresum0j']  = {
  'name'  : 'CMS_hww_WWresum_0j',
  'skipCMS' : 1,
  'kind'  : 'weight',
  'type'  : 'shape',
  'samples'  : {
     'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
   },
  'cutspost'  : lambda self, cuts: [cut for cut in cuts if '0j' in cut]
}

nuisances['WWqscale0j']  = {
   'name'  : 'CMS_hww_WWqscale_0j',
   'skipCMS' : 1,
   'kind'  : 'weight',
   'type'  : 'shape',
   'samples'  : {
      'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
    },
   'cutspost'  : lambda self, cuts: [cut for cut in cuts if '0j' in cut]
}

nuisances['WWresum1j']  = {
  'name'  : 'CMS_hww_WWresum_1j',
  'skipCMS' : 1,
  'kind'  : 'weight',
  'type'  : 'shape',
  'samples'  : {
     'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
   },
  'cutspost'  : lambda self, cuts: [cut for cut in cuts if '1j' in cut]
}

nuisances['WWqscale1j']  = {
   'name'  : 'CMS_hww_WWqscale_1j',
   'skipCMS' : 1,
   'kind'  : 'weight',
   'type'  : 'shape',
   'samples'  : {
      'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
    },
   'cutspost'  : lambda self, cuts: [cut for cut in cuts if '1j' in cut]
}

nuisances['WWresum2j']  = {
  'name'  : 'CMS_hww_WWresum_2j',
  'skipCMS' : 1,
  'kind'  : 'weight',
  'type'  : 'shape',
  'samples'  : {
     'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
   },
  'cutspost'  : lambda self, cuts: [cut for cut in cuts if '2j' in cut]
}

nuisances['WWqscale2j']  = {
   'name'  : 'CMS_hww_WWqscale_2j',
   'skipCMS' : 1,
   'kind'  : 'weight',
   'type'  : 'shape',
   'samples'  : {
      'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
    },
   'cutspost'  : lambda self, cuts: [cut for cut in cuts if '2j' in cut]
}

# Uncertainty on SR/CR ratio
nuisances['CRSR_accept_DY'] = {
    'name': 'CMS_hww_CRSR_accept_DY',
    'type': 'lnN',
    'samples': {'DY': '1.02'},
    'cuts': [cut for cut in cuts if '_CR_' in cut],
    'cutspost': (lambda self, cuts: [cut for cut in cuts if '_DY_' in cut]),
}

# Uncertainty on SR/CR ratio
nuisances['CRSR_accept_top'] = {
    'name': 'CMS_hww_CRSR_accept_top',
    'type': 'lnN',
    'samples': {'top': '1.01'},
    'cuts': [cut for cut in cuts if '_CR_' in cut],
    'cutspost': (lambda self, cuts: [cut for cut in cuts if '_top_' in cut]),
}

# Theory uncertainty for ggH
#
#
#   THU_ggH_Mu, THU_ggH_Res, THU_ggH_Mig01, THU_ggH_Mig12, THU_ggH_VBF2j, THU_ggH_VBF3j, THU_ggH_PT60, THU_ggH_PT120, THU_ggH_qmtop
#
#   see https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsWG/SignalModelingTools

thus = [
    ('THU_ggH_Mu', 'ggH_mu'),
    ('THU_ggH_Res', 'ggH_res'),
    ('THU_ggH_Mig01', 'ggH_mig01'),
    ('THU_ggH_Mig12', 'ggH_mig12'),
    ('THU_ggH_VBF2j', 'ggH_VBF2j'),
    ('THU_ggH_VBF3j', 'ggH_VBF3j'),
    ('THU_ggH_PT60', 'ggH_pT60'),
    ('THU_ggH_PT120', 'ggH_pT120'),
    ('THU_ggH_qmtop', 'ggH_qmtop')
]

for name, vname in thus:
    updown = [vname, '2.-%s' % vname]
    
    nuisances[name] = {
        'name': name,
        'skipCMS': 1,
        'kind': 'weight',
        'type': 'shape',
        'samples': {
          'ggH_hww': updown,
          #'ggH_htt': updown
        }
    }

#### QCD scale uncertainties for Higgs signals other than ggH

values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm')

nuisances['QCDscale_qqH'] = {
    'name': 'QCDscale_qqH', 
    'samples': {
        'qqH_hww': values,
        'qqH_htt': values
    },
    'type': 'lnN'
}

valueswh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm')
valueszh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','scale','sm')

nuisances['QCDscale_VH'] = {
    'name': 'QCDscale_VH', 
    'samples': {
        'WH_hww': valueswh,
        'WH_htt': valueswh,
        'ZH_hww': valueszh,
        'ZH_htt': valueszh
    },
    'type': 'lnN',
}

values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','scale','sm')

nuisances['QCDscale_ggZH'] = {
    'name': 'QCDscale_ggZH', 
    'samples': {
        'ggZH_hww': values
    },
    'type': 'lnN',
}

values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','scale','sm')

nuisances['QCDscale_ttH'] = {
    'name': 'QCDscale_ttH',
    'samples': {
        'ttH_hww': values
    },
    'type': 'lnN',
}

nuisances['QCDscale_WWewk'] = {
    'name': 'QCDscale_WWewk',
    'samples': {
        'WWewk': '1.11',
    },
    'type': 'lnN'
}

nuisances['QCDscale_qqbar_ACCEPT'] = {
    'name': 'QCDscale_qqbar_ACCEPT',
    'type': 'lnN',
    'samples': {
        'qqH_hww': '1.003',
        'qqH_htt': '1.003',
        'WH_hww': '1.010',
        'WH_htt': '1.010',
        'ZH_hww': '1.015',
        'ZH_htt': '1.015',
    }
}

#FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['QCDscale_gg_ACCEPT'] = {
    'name': 'QCDscale_gg_ACCEPT',
    'samples': {
        'ggH_htt': '1.012',
        'ggH_hww': '1.012',
        'ggZH_hww': '1.012',
        'ggWW': '1.012',
    },
    'type': 'lnN',
}

## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '0',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}

##rate parameters
nuisances['DYttnorm0j']  = {
               'name'  : 'CMS_hww_DYttnorm0j',
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : cuts0j
              }

nuisances['DYttnorm1j']  = {
               'name'  : 'CMS_hww_DYttnorm1j',
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : cuts1j
              }

nuisances['DYttnorm2j']  = {
                 'name'  : 'CMS_hww_DYttnorm2j',
                 'samples'  : {
                     'DY' : '1.00',
                     },
                 'type'  : 'rateParam',
                 'cuts'  : cuts2j
                }


nuisances['WWnorm0j']  = {
               'name'  : 'CMS_hww_WWnorm0j',
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : cuts0j
              }

nuisances['ggWWnorm0j']  = {
               'name'  : 'CMS_hww_WWnorm0j',
               'samples'  : {
                   'ggWW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : cuts0j
              }

nuisances['WWnorm1j']  = {
               'name'  : 'CMS_hww_WWnorm1j',
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : cuts1j
              }

nuisances['ggWWnorm1j']  = {
               'name'  : 'CMS_hww_WWnorm1j',
               'samples'  : {
                   'ggWW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : cuts1j
              }

nuisances['WWnorm2j']  = {
               'name'  : 'CMS_hww_WWnorm2j',
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : cuts2j
              }

nuisances['ggWWnorm2j']  = {
               'name'  : 'CMS_hww_WWnorm2j',
               'samples'  : {
                   'ggWW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : cuts2j
              }

nuisances['Topnorm0j']  = {
               'name'  : 'CMS_hww_Topnorm0j',
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : cuts0j
              }

nuisances['Topnorm1j']  = {
               'name'  : 'CMS_hww_Topnorm1j',
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : cuts1j
              }

nuisances['Topnorm2j']  = {
               'name'  : 'CMS_hww_Topnorm2j',
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : cuts2j
              }


for n in nuisances.values():
    n['skipCMS'] = 1

print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))
