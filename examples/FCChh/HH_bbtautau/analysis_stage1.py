#Mandatory: List of processes


processList = {'pwp8_pp_hh_lambda100_5f_hhbbaa':{'chunks':100,'fraction':0.001},
              'mgp8_pp_bbtata_QED':{'chunks':10,'fraction':0.01},
              'mgp8_pp_bbtata_QCDQED':{'chunks':10,'fraction':0.01},
              #'mg_pp_bbjj_QCD_5f',
              'mgp8_pp_tt012j_5f':{'chunks':100,'fraction':0.001},
              #'mg_pp_h012j_5f',
              #'mg_pp_vh012j_5f',
              #'mg_pp_ttw_5f',
              #'mg_pp_ttww_4f',
              #'mg_pp_ttwz_5f',
              #'mgp8_pp_ttz_5f',
              #'mgp8_pp_ttzz_5f',
              #'mgp8_pp_tth01j_5f'
              }




#Mandatory: Production tag when running over EDM4Hep centrally produced events, this points to the yaml files for getting sample statistics
prodTag     = "FCChh/fcc_v04/"

#Optional: output directory, default is local dir
outputDir = "/eos/user/w/williams/FCChh-tutorial/output_stage1/"
#outputDir = "output_stage1/"

outputDirEos = "/eos/user/w/williams/FCChh-tutorial/output_stage1/"
#outputDirEos = "/eos/user/j/jalimena/FCCeeLLP/"
#eosType = "eosuser"

#Optional: ncpus, default is 4
nCPUS       = 4

#Optional running on HTCondor, default is False
runBatch    = False
#runBatch    = True

#Optional batch queue name when running on HTCondor, default is workday
batchQueue = "longlunch"

#Optional computing account when running on HTCondor, default is group_u_FCC.local_gen
compGroup = "group_u_FCC.local_gen"

#Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis():
        def analysers(df):

                df2 = (df

                #Access the various objects and their properties with the following syntax: .Define("<your_variable>", "<accessor_fct (name_object)>")
		#This will create a column in the RDataFrame named <your_variable> and filled with the return value of the <accessor_fct> for the given collection/object 
		#Accessor functions are the functions found in the C++ analyzers code that return a certain variable, e.g. <namespace>::get_n(object) returns the number 
		#of these objects in the event and <namespace>::get_pt(object) returns the pt of the object. Here you can pick between two namespaces to access either
		#reconstructed (namespace = ReconstructedParticle) or MC-level objects (namespace = MCParticle). 
		#For the name of the object, in principle the names of the EDM4HEP collections are used - photons, muons and electrons are an exception, see below

		#OVERVIEW: Accessing different objects and counting them
               
                ####################################################################################################
                # Get tags
                # .Define("Jet3",  "ReconstructedParticle::get(Jet3, ReconstructedParticles)")

               .Define("selected_jets", "ReconstructedParticle::sel_pt(50.)(Jet)")
               .Define("jet_pT",        "ReconstructedParticle::get_pt(Jet)")
               .Define("seljet_pT",     "ReconstructedParticle::get_pt(selected_jets)")
               .Alias("Jet3","Jet#3.index") 

               .Define("JET_btag", "ReconstructedParticle::getJet_btag(Jet3, ParticleIDs, ParticleIDs_0)")
               .Define("EVT_nbtag", "ReconstructedParticle::getJet_ntags(JET_btag)")

               .Define("btags", 'ReconstructedParticle::getJet_btag(Jet3, ParticleIDs, ParticleIDs_0)')

               .Define("n_bjets", "ReconstructedParticle::getJet_ntags(btags)")
 

               # Apply btagging mask to jets collection
               .Define("masked_bjet_e", "ReconstructedParticle::get_e(Jet)*btags")
               #.Define("masked_bjet_px", "getRP_px(Jet)*btags")
               #.Define("masked_bjet_py", "getRP_py(Jet)*btags")
               #.Define("masked_bjet_pz", "getRP_pz(Jet)*btags")
               #.Define("masked_bjet_pt", "getRP_pt(Jet)*btags")
               #.Define("masked_bjet_eta", "getRP_eta(Jet)*btags")
               #.Define("masked_bjet_phi", "getRP_phi(Jet)*btags")
               #.Define("masked_bjet_mass", "getRP_mass(Jet)*btags")


               # Get MC info
               .Alias("Particle0","Particle#0.index")
               .Alias("MCRecoAssociations0","MCRecoAssociations#0.index")
               .Alias("MCRecoAssociations1","MCRecoAssociations#1.index")
               .Define("MC_pdg", "MCParticle::get_pdg(Particle)")
               .Define("RP_MC_index", "ReconstructedParticle2MC::getRP2MC_index(MCRecoAssociations0, MCRecoAssociations1,ReconstructedParticles)")
               .Define("RP_MC_parentindex", "MCParticle::get_parentid(RP_MC_index,Particle,Particle0)")
               .Define("RP_MC_grandparentindex", "MCParticle::get_parentid(RP_MC_parentindex,Particle,Particle0)")
                #.Define("RP_MC_parentpdg", "getMC_parentpdg(RP_MC_parentindex, MC_pdg)")
                #.Define("RP_MC_grandparentpdg", "getMC_parentpdg(RP_MC_grandparentindex, MC_pdg)")

               # Fill branches
		

               #.Define("jet_e", "masked_jet_e[masked_jet_e!=0]")
               #.Define("jet_px", "masked_jet_px[masked_jet_px!=0]")
               #.Define("jet_py", "masked_jet_py[masked_jet_py!=0]")
               #.Define("jet_pz", "masked_jet_pz[masked_jet_pz!=0]")
               #.Define("jet_pt", "masked_jet_pt[masked_jet_pt!=0]")
               #.Define("jet_eta", "masked_jet_eta[masked_jet_eta!=0]")
               #.Define("jet_phi", "masked_jet_phi[masked_jet_phi!=0]")
               #.Define("jet_mass", "masked_jet_mass[masked_jet_mass!=0]")

               #.Define("bjet_e", "masked_bjet_e[masked_bjet_e!=0]")
               #.Define("bjet_px", "masked_bjet_px[masked_bjet_px!=0]")
               #.Define("bjet_py", "masked_bjet_py[masked_bjet_py!=0]")
               #.Define("bjet_pz", "masked_bjet_pz[masked_bjet_pz!=0]")
               #.Define("bjet_pt", "masked_bjet_pt[masked_bjet_pt!=0]")
               #.Define("bjet_eta", "masked_bjet_eta[masked_bjet_eta!=0]")
               #.Define("bjet_phi", "masked_bjet_phi[masked_bjet_phi!=0]")
               #.Define("bjet_mass", "masked_bjet_mass[masked_bjet_mass!=0]")

               #.Define("cjet_e", "masked_cjet_e[masked_cjet_e!=0]")
               #.Define("cjet_px", "masked_cjet_px[masked_cjet_px!=0]")
               #.Define("cjet_py", "masked_cjet_py[masked_cjet_py!=0]")
               #.Define("cjet_pz", "masked_cjet_pz[masked_cjet_pz!=0]")
               #.Define("cjet_pt", "masked_cjet_pt[masked_cjet_pt!=0]")
               #.Define("cjet_eta", "masked_cjet_eta[masked_cjet_eta!=0]")
               #.Define("cjet_phi", "masked_cjet_phi[masked_cjet_phi!=0]")
               #.Define("cjet_mass", "masked_cjet_mass[masked_cjet_mass!=0]")

               #.Define("tau_e", "masked_tau_e[masked_tau_e!=0]")
               #.Define("tau_px", "masked_tau_px[masked_tau_px!=0]")
               #.Define("tau_py", "masked_tau_py[masked_tau_py!=0]")
               #.Define("tau_pz", "masked_tau_pz[masked_tau_pz!=0]")
               #.Define("tau_pt", "masked_tau_pt[masked_tau_pt!=0]")
               #.Define("tau_eta", "masked_tau_eta[masked_tau_eta!=0]")
               #.Define("tau_phi", "masked_tau_phi[masked_tau_phi!=0]")
               #.Define("tau_mass", "masked_tau_mass[masked_tau_mass!=0]")              
               #.Define("tau_charge", "masked_tau_charge[masked_tau_charge!=0]")
		

               .Alias("Electron0", "Electron#0.index")
               .Alias("Muon0", "Muon#0.index")
               .Alias("Photon0", "Photon#0.index")
               .Define("electrons", "ReconstructedParticle::get(Electron0, ReconstructedParticles)")
               .Define("muons", "ReconstructedParticle::get(Muon0, ReconstructedParticles)")
               .Define("photons", "ReconstructedParticle::get(Photon0, ReconstructedParticles)")

               .Define("n_electrons", "ReconstructedParticle::get_n(electrons)")
               .Define("n_muons", "ReconstructedParticle::get_n(muons)")
               .Define("n_photons", "ReconstructedParticle::get_n(photons)")

               .Define("leptons", "ReconstructedParticle::merge(electrons, muons)")
               .Define("n_leptons", "ReconstructedParticle::get_n(leptons)")
               .Define("lepton_e", "ReconstructedParticle::get_e(leptons)")
               .Define("lepton_px", "ReconstructedParticle::get_px(leptons)")
               .Define("lepton_py", "ReconstructedParticle::get_py(leptons)")
               .Define("lepton_pz", "ReconstructedParticle::get_pz(leptons)")
               .Define("lepton_pt", "ReconstructedParticle::get_pt(leptons)")
               .Define("lepton_eta", "ReconstructedParticle::get_eta(leptons)")
               .Define("lepton_phi", "ReconstructedParticle::get_phi(leptons)")
               .Define("lepton_mass", "ReconstructedParticle::get_mass(leptons)")
               .Define("lepton_charge", "ReconstructedParticle::get_charge(leptons)")

               .Define("photon_e", "ReconstructedParticle::get_e(photons)")
               .Define("photon_px", "ReconstructedParticle::get_px(photons)")
               .Define("photon_py", "ReconstructedParticle::get_py(photons)")
               .Define("photon_pz", "ReconstructedParticle::get_pz(photons)")
               .Define("photon_pt", "ReconstructedParticle::get_pt(photons)")
               .Define("photon_eta", "ReconstructedParticle::get_eta(photons)")
               .Define("photon_phi", "ReconstructedParticle::get_phi(photons)")
               .Define("photon_mass", "ReconstructedParticle::get_mass(photons)")

               .Define("met", "ReconstructedParticle::get_pt(MissingET)")
               .Define("met_phi", "ReconstructedParticle::get_phi(MissingET)")
               .Define("met_eta", "ReconstructedParticle::get_eta(MissingET)")
               .Define("met_mass", "ReconstructedParticle::get_mass(MissingET)")
               .Define("met_px", "ReconstructedParticle::get_px(MissingET)")
               .Define("met_py", "ReconstructedParticle::get_py(MissingET)")
               .Define("met_pz", "ReconstructedParticle::get_pz(MissingET)")
               .Define("met_e", "ReconstructedParticle::get_e(MissingET)")

               #.Filter("n_leptons > 0")
               #.Filter("n_taus > 0")
               #.Filter("n_jets > 0")
               #.Filter("n_bjets >= 2")
               )
                return df2

        def output():
                branchList = [
		
                #"nontags",
                #"n_jets",
                #"jet_e",
                #"jet_px",
                #"jet_py",
                #"jet_pz",
                #"jet_pt",
                #"jet_eta",
                #"jet_phi",
                #"jet_mass",
		
                "jet_pT",
                "seljet_pT",
                "EVT_nbtag",
                "btags",
                "n_bjets",
                #"bjet_e",
                #"bjet_px",
                #"bjet_py",
                #"bjet_pz",
                #"bjet_pt",
                #"bjet_eta",
                #"bjet_phi",
                #"bjet_mass",
		

                #"ctags",
                #"n_cjets",
                #"cjet_e",
                #"cjet_px",
                #"cjet_py",
                #"cjet_pz",
                #"cjet_pt",
                #"cjet_eta",
                #"cjet_phi",
                #"cjet_mass",
		

                #"tautags",
                #"n_taus",
                #"tau_e",
                #"tau_px",
                #"tau_py",
                #"tau_pz",
                #"tau_pt",
                #"tau_eta",
                #"tau_phi",
                #"tau_mass",
                #"tau_charge",
		

                "met",
                "met_phi",
                "met_px",
                "met_py",
                "met_pz",
                "met_e",
                
                "n_leptons",
                "n_muons",
                "n_electrons",
                "lepton_e",
                "lepton_px",
                "lepton_py",
                "lepton_pz",
                "lepton_pt",
                "lepton_eta",
                "lepton_phi",
                "lepton_mass",
                "lepton_charge",

                # Uncomment for diphoton information
                "n_photons",
                "photon_pt",
                "photon_eta",
                "photon_phi",
                "photon_mass",
                "photon_e",
                "photon_px",
                "photon_py",
                "photon_pz",

		]

                return branchList

