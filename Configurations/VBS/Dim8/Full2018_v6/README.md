Dimension 8 : new model
====

Test of new model for EFT also for Dim8 operators

    /afs/cern.ch/work/j/jixiao/public/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6
    nanoLatino_WWJJ_SS_WToLNu_EWK_aQGC__part0.root
    

1. There are 99 points in reweight_card.dat [1], the unit is 1/Tev^4=10^（-12）/GeV^4
    http://jixiao.web.cern.ch/jixiao/InputCards/WWjj_SS_dim8_ewk_qcd_reweight_card.dat


2. To map each point to the operators, you can find the lhacode for parameters here
    http://jixiao.web.cern.ch/jixiao/InputCards/parameters.py

3. Weights for aQGC are available in LHEReweightingWeight branch




Create histograms
====

Produce shapes:

    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=espresso
    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=workday 
    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=workday  --dry-run
    
    
Check if jobs are done by doing:

    condor_q
    
Add root files:

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files
    

Resubmit if needed:

    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__ZZ4L.10.jds
    
    
    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__ggWW.0.sh

    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__ZZ4L.15.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__TVX.6.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Vg.0.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.0.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.1.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.2.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.3.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.4.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.23.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.24.jds


    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__ZZ4L.12.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__TVX.6.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.1.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.2.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.3.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.4.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.23.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.24.jds
    
    
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__TVX.6.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.1.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.2.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.3.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.4.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.23.jds
    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.24.jds

    
    espresso -> workday

    sed -i 's/original/new/g' file.txt

    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__TVX.6.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.1.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.2.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.3.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.4.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.23.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.24.jds

    
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__Vg.4.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__Vg.6.jds
        
    export _condor_SCHEDD_HOST="bigbird17.cern.ch"
    
    
    
    
    
    
    
    
    
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__DATA.13.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__DATA.23.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__DATA.24.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.1.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.13.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.23.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.24.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.27.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__TVX.2.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__TVX.6.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__TVX.8.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Vg.0.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__VgS1.1.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WZ_EWK.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WZ_QCD.1.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.0.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.1.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.2.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.3.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.4.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__ZZ4L.13.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__ZZ4L.15.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__ZZ4L.16.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__ZZ4L.5.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__ZZ4L.9.jds



--> Missing root file: plots_VBS_SS_l2_2018_ALL_ZZ4L.9.root
--> Missing root file: plots_VBS_SS_l2_2018_ALL_ZZ4L.13.root
--> Missing root file: plots_VBS_SS_l2_2018_ALL_ZZ4L.15.root
--> Missing root file: plots_VBS_SS_l2_2018_ALL_ZZ4L.16.root
--> Missing root file: plots_VBS_SS_l2_2018_ALL_TVX.2.root
--> Missing root file: plots_VBS_SS_l2_2018_ALL_TVX.6.root
--> Missing root file: plots_VBS_SS_l2_2018_ALL_TVX.8.root
--> Missing root file: plots_VBS_SS_l2_2018_ALL_Vg.0.root
--> Missing root file: plots_VBS_SS_l2_2018_ALL_WrongSign.1.root
--> Missing root file: plots_VBS_SS_l2_2018_ALL_WrongSign.2.root
--> Missing root file: plots_VBS_SS_l2_2018_ALL_WrongSign.3.root
--> Missing root file: plots_VBS_SS_l2_2018_ALL_WrongSign.4.root
--> Missing root file: plots_VBS_SS_l2_2018_ALL_Fake_lep.1.root
--> Missing root file: plots_VBS_SS_l2_2018_ALL_Fake_lep.23.root
--> Missing root file: plots_VBS_SS_l2_2018_ALL_Fake_lep.24.root
--> Missing root file: plots_VBS_SS_l2_2018_ALL_DATA.13.root
--> Missing root file: plots_VBS_SS_l2_2018_ALL_DATA.23.root
--> Missing root file: plots_VBS_SS_l2_2018_ALL_DATA.24.root

    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__DATA.13.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__DATA.23.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__DATA.24.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.1.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.23.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.24.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__TVX.2.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__TVX.6.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__TVX.8.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Vg.0.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.1.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.2.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.3.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.4.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__ZZ4L.13.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__ZZ4L.15.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__ZZ4L.16.jds
    sed -i 's/espresso/workday/g'   /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__ZZ4L.9.jds

    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__DATA.13.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__DATA.23.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__DATA.24.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.1.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.23.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Fake_lep.24.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__TVX.2.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__TVX.6.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__TVX.8.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__Vg.0.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.1.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.2.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.3.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__WrongSign.4.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__ZZ4L.13.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__ZZ4L.15.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__ZZ4L.16.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Postprocessing/jobs/mkShapes__VBS_SS_l2_2018/mkShapes__VBS_SS_l2_2018__ALL__ZZ4L.9.jds

    
    
    
    
    
Plots
====

Make plots:


    mkPlot.py --pycfg=configuration.py --inputFile=rootFile_l2_2018/plots_VBS_SS_l2_2018.root
    mkPlot.py --pycfg=configuration.py --inputFile=rootFile_l2_2018/plots_VBS_SS_l2_2018.root  --plotNormalizedDistributions
    mkPlot.py --pycfg=configuration.py --inputFile=rootFile_l2_2018/plots_VBS_SS_l2_2018.root  --plotNormalizedDistributionsTHstack
    

Datacard
====

Make datacard:


    mkDatacards.py --pycfg=configuration.py --inputFile=rootFile_l2_2018/plots_VBS_SS_l2_2018.root



    
EFT fit
====

    cd /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/AnalyticAnomalousCoupling/CMSSW_10_2_13/src/HiggsAnalysis/AnalyticAnomalousCoupling
    cmsenv
    cd -
    

    text2workspace.py     datacards_l2_2018/ssww_leppt0_jetpt30/pt1/datacard.txt    -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFT:analiticAnomalousCouplingEFT   -o   model_test.root   
    
    combine -M MultiDimFit model_test.root  --algo=grid --points 240  -m 125   -t -1 --expectSignal=1     \
        --redefineSignalPOIs k_cDim8_k1 \
        --setParameters r=1,k_cDim8_k1=0  \
        --freezeParameters r   \
        --setParameterRanges k_cDim8_k1=-10,10     \
        --verbose -1
    
    
    cd /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/AnalyticAnomalousCoupling/CMSSW_10_2_13/src/HiggsAnalysis/AnalyticAnomalousCoupling/test/
    
    r99t /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/TestValsecchi/CMSSW_10_2_15_patch2/src/PlotsConfigurations/Configurations/VBS/Dim8/Full2018_v6/higgsCombineTest.MultiDimFit.mH125.root \
         /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/TestValsecchi/CMSSW_10_2_15_patch2/src/PlotsConfigurations/Configurations/VBS/Dim8/Full2018_v6/higgsCombineTest.MultiDimFit.mH125.root \
         draw.cxx\(\"k_cDim8_k1\"\)

         
         
    
    
    
    

