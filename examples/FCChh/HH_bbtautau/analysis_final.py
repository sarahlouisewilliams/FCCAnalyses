#Input directory where the files produced at the stage1 level are
inputDir  = "/eos/user/w/williams/FCChh-tutorial/output_stage1/"
#inputDir = "output_stage1/"

#Output directory where the files produced at the final-selection level are
outputDir  = "output_finalSel/"

#Integrated luminosity for scaling number of events (required only if setting doScale to true)
#intLumi = 150e6 #pb^-1
intLumi = 30e6 #pb^-1

#Scale event yields by intLumi and cross section (optional)
doScale = True

#Save event yields in a table (optional)
#saveTabular = True

processList = {
    #run over the full statistics from stage1
    'pwp8_pp_hh_lambda100_5f_hhbbaa':{},
    'mgp8_pp_bbtata_QED':{},
    'mgp8_pp_bbtata_QCDQED':{},
    'mgp8_pp_tt012j_5f':{},
}

#Link to the dictonary that contains all the cross section information etc...
procDict = "/afs/cern.ch/work/w/williams/public/FCChh-tutorial/FCCAnalyses/FCChh_procDict_fcc_v04.json"

#Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
procDictAdd={
    #"MySample_p8_ee_ZH_ecm240":{"numberOfEvents": 10000000, "sumOfWeights": 10000000, "crossSection": 0.201868, "kfactor": 1.0, "matchingEfficiency": 1.0}
}

#Number of CPUs to use
nCPUS = 2

#produces ROOT TTrees, default is False
doTree = False

###Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {
    "sel0":"seljet_pT.size()>6",
}

###Dictionary for prettier names of cuts (optional)
cutLabels = {
    "sel0": "At least 7 jets with pT$>$50 GeV",
}

###Optinally Define new variables
defineList = {"seljet_pT_0":"seljet_pT.at(0)",
               "seljet_pT_1":"seljet_pT.at(1)",
               "seljet_pT_2":"seljet_pT.at(2)",
               "seljet_pT_3":"seljet_pT.at(3)",
               "seljet_pT_4":"seljet_pT.at(4)",
               "seljet_pT_5":"seljet_pT.at(5)"}

###Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {
    "jet_pt_0":{"name":"seljet_pT_0","title":"Leading jet p_{T} [GeV]","bin":100,"xmin":0,"xmax":4000},
    "jet_pt_1":{"name":"seljet_pT_1","title":"Sub leading jet p_{T} [GeV]","bin":100,"xmin":0,"xmax":4000},
    "jet_pt_2":{"name":"seljet_pT_2","title":"3rd jet p_{T} [GeV]","bin":100,"xmin":0,"xmax":4000},
    "jet_pt_3":{"name":"seljet_pT_3","title":"4th jet p_{T} [GeV]","bin":100,"xmin":0,"xmax":4000},
    "jet_pt_4":{"name":"seljet_pT_4","title":"5th jet p_{T} [GeV]","bin":100,"xmin":0,"xmax":4000},
    "jet_pt_5":{"name":"seljet_pT_5","title":"6th jet p_{T} [GeV]","bin":100,"xmin":0,"xmax":4000},
}


