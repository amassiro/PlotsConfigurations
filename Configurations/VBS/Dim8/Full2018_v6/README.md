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

    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__NonPrompt/mkShapes__NonPrompt__ALL__DATA.19.jds
    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__ggWW.0.sh

    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__Vg.4.jds
       
    espresso -> workday

    sed -i 's/original/new/g' file.txt

    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__Vg.4.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__Vg.6.jds
        
    export _condor_SCHEDD_HOST="bigbird17.cern.ch"
    
    
    
Plots
====

Make plots:


    mkPlot.py --pycfg=configuration.py --inputFile=rootFile/plots_ggH.root
    mkPlot.py --pycfg=configuration.py --inputFile=rootFile/plots_ggH.root  --plotNormalizedDistributions
    

Datacard
====

Make datacard:


    mkDatacards.py --pycfg=configuration.py --inputFile=rootFile/plots_ggH.root


        

