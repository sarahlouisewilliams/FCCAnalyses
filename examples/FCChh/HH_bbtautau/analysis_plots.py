import ROOT

# global parameters
intLumi        = 30.0e+06 #in pb-1

###If scaleSig=0 or scaleBack=0, we don't apply any additional scaling, on top of the normalization to cross section and integrated luminosity, as defined in finalSel.py
###If scaleSig or scaleBack is not defined, plots will be normalized to 1
#scaleSig       = 0.
#scaleBack      = 0.
ana_tex        = 'pp #rightarrow HH'
delphesVersion = '3.4.2'
energy         = 100
collider       = 'FCC-hh'
inputDir       = 'output_finalSel/'
#formats        = ['png','pdf']
formats        = ['pdf']
yaxis          = ['lin','log']
stacksig       = ['nostack']
outdir         = 'plots/'
splitLeg       = True

variables = [

    #jet variables
    "jet_pt_0",
    "jet_pt_1",
    "jet_pt_2",
    "jet_pt_3",
    "jet_pt_4",
    "jet_pt_5",
             ]

    
###Dictionary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['HHbbtautau']  = [
    "sel0",
]

extralabel = {}
extralabel['sel0'] = "Pre selection (at least 7 jets)"

colors = {}
colors['hh_lambda100'] = ROOT.kOrange+1


colors['EWK'] = ROOT.kAzure-4
colors['QCD+EWK'] = ROOT.kCyan-9
colors['Top'] = ROOT.kViolet-4

plots = {}
plots['HHbbtautau'] = {'signal':{
                     'hh_lambda100':['pwp8_pp_hh_lambda100_5f_hhbbaa'],

},
                'backgrounds':{
                    'EWK':['mgp8_pp_bbtata_QED'],
                    'QCD+EWK': ['mgp8_pp_bbtata_QCDQED'],
                    'Top': ['mgp8_pp_tt012j_5f'],
                }
                }


legend = {}
legend['hh_lambda100'] = 'hh signal (#lambda_{hhh}=100)'

legend['EWK'] = 'EWK'
legend['QCD+EWK'] = 'QCD+EWK'
legend['Top'] = 'Top'

