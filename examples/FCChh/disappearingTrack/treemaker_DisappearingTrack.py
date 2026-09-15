import os, copy

# list of processes
processList = {
    "mgp8_pp_tt012j_5f_84TeV": {
        "fraction": 1,
        "crossSection": 31838.8464905,
    },
}

outputDir   = "/eos/user/w/williams/FCChh-Summer2026/outputs/DisappearingTrack/stage1"
# Define the input dir (optional)
# inputDir    = "/eos/experiment/fcc/hh/generation/DelphesEvents/fcc_v07/II/"
inputDir    = "/eos/user/w/williams/FCChh-Summer2026"

# prodTag= "FCChh/generation/DelphesEvents/fcc_v07/II/"

n_threads = 4
# Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis:

    # __________________________________________________________
    # Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2
    def analysers(df):

        # __________________________________________________________
        # Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2
        df = df.Define("weight", "EventHeader.weight")

        # ----------------------------------------------------------
        # Muons
        # ----------------------------------------------------------

        df = df.Alias("Muon0", "Muon_objIdx.index")

        df = df.Define(
            "muons_all",
            "FCCAnalyses::ReconstructedParticle::get(Muon0, ReconstructedParticles)",
        )

        # pT > 20 GeV
        df = df.Define(
            "muons",
            "FCCAnalyses::ReconstructedParticle::sel_pt(20.)(muons_all)",
        )

        df = df.Define(
            "muons_pt",
            "FCCAnalyses::ReconstructedParticle::get_pt(muons)",
        )
        df = df.Define(
            "muons_eta",
            "FCCAnalyses::ReconstructedParticle::get_eta(muons)",
        )
        df = df.Define(
            "muons_phi",
            "FCCAnalyses::ReconstructedParticle::get_phi(muons)",
        )
        df = df.Define(
            "muons_q",
            "FCCAnalyses::ReconstructedParticle::get_charge(muons)",
        )
        df = df.Define(
            "muons_n",
            "FCCAnalyses::ReconstructedParticle::get_n(muons)",
        )


        # ----------------------------------------------------------
        # Electrons
        # ----------------------------------v------------------------

        df = df.Alias("Electron0", "Electron_objIdx.index")

        df = df.Define(
            "electrons_all",
            "FCCAnalyses::ReconstructedParticle::get(Electron0, ReconstructedParticles)",
        )

        # pT > 20 GeV
        df = df.Define(
            "electrons",
            "FCCAnalyses::ReconstructedParticle::sel_pt(20.)(electrons_all)",
        )

        df = df.Define(
            "electrons_pt",
            "FCCAnalyses::ReconstructedParticle::get_pt(electrons)",
        )
        df = df.Define(
            "electrons_eta",
            "FCCAnalyses::ReconstructedParticle::get_eta(electrons)",
        )
        df = df.Define(
            "electrons_phi",
            "FCCAnalyses::ReconstructedParticle::get_phi(electrons)",
        )
        df = df.Define(
            "electrons_q",
            "FCCAnalyses::ReconstructedParticle::get_charge(electrons)",
        )
        df = df.Define(
            "electrons_n",
            "FCCAnalyses::ReconstructedParticle::get_n(electrons)",
        )

        # ----------------------------------------------------------
        # Remove selected leptons before jet clustering
        # ----------------------------------------------------------
        
        df = df.Define(
            "ReconstructedParticlesNoMuons",
            "FCCAnalyses::ReconstructedParticle::remove(ReconstructedParticles, muons)"
        )

        df = df.Define(
            "ReconstructedParticlesNoLeptons",
            "FCCAnalyses::ReconstructedParticle::remove(ReconstructedParticlesNoMuons, electrons)"
        )
        
        # ----------------------------------------------------------
        # Prepare inputs to FastJet
        # ----------------------------------------------------------
        df = df.Define(
            "ReconstructedParticlesForJets",
            "FCCAnalyses::ReconstructedParticle::sel_pt(1e-6)(ReconstructedParticlesNoLeptons)"
        )

        df = df.Define(
            "RPNoLep_px",
            "FCCAnalyses::ReconstructedParticle::get_px(ReconstructedParticlesForJets)"
        )

        df = df.Define(
            "RPNoLep_py",
            "FCCAnalyses::ReconstructedParticle::get_py(ReconstructedParticlesForJets)"
        )

        df = df.Define(
            "RPNoLep_pz",
            "FCCAnalyses::ReconstructedParticle::get_pz(ReconstructedParticlesForJets)"
        )

        df = df.Define(
            "RPNoLep_m",
            "FCCAnalyses::ReconstructedParticle::get_mass(ReconstructedParticlesForJets)"
        )

        df = df.Define(
            "pseudo_jets","JetClusteringUtils::set_pseudoJets_xyzm(RPNoLep_px,RPNoLep_py,RPNoLep_pz,RPNoLep_m)"
        )

        df = df.Define(
            "n_pseudo_jets",
            "pseudo_jets.size()"
        )
        # ----------------------------------------------------------
        # anti-kT R=0.4
        # ----------------------------------------------------------
        df = df.Define(
            "pseudojet_bad",
            """
            bool bad = false;
            for (const auto &p : pseudo_jets) {
                if (!std::isfinite(p.px()) ||
                    !std::isfinite(p.py()) ||
                    !std::isfinite(p.pz()) ||
                    !std::isfinite(p.E())) {
                    bad = true;
                }
            }
            return bad;
            """
        )

        #df = df.Filter("!pseudojet_bad")
     

        df = df.Define(
            "debug_bad_pseudojets",
            """
            if (pseudojet_bad) {
                std::cout << "BAD EVENT" << std::endl;

                for (size_t i = 0; i < pseudo_jets.size(); ++i) {
                    const auto &p = pseudo_jets[i];

                    if (!std::isfinite(p.px()) ||
                        !std::isfinite(p.py()) ||
                        !std::isfinite(p.pz()) ||
                        !std::isfinite(p.E())) {

                        std::cout
                            << "particle " << i
                            << " px=" << p.px()
                            << " py=" << p.py()
                            << " pz=" << p.pz()
                            << " E="  << p.E()
                            << " m="  << p.m()
                            << std::endl;
                    }
                }
            }
            return true;
            """
        )

        #df = df.Filter("!debug_bad_pseudojets")
       
 
        
        
        df = df.Define(
            "clustered_jets_ak4",
            "JetClustering::clustering_antikt(0.4, 0, 0., 0, 0)(pseudo_jets)"
        )

        df = df.Define(
            "jets_ak4",
            "JetClusteringUtils::get_pseudoJets(clustered_jets_ak4)"
        )

        df = df.Define(
            "jetconstituents_ak4",
            "JetClusteringUtils::get_constituents(clustered_jets_ak4)"
        )


        # ----------------------------------------------------------
        # Jet quantities
        # ----------------------------------------------------------

        df = df.Define(
            "jets_ak4_pt",
            "JetClusteringUtils::get_pt(jets_ak4)"
        )

        df = df.Define(
            "jets_ak4_eta",
            "JetClusteringUtils::get_eta(jets_ak4)"
        )

        df = df.Define(
            "jets_ak4_phi",
            "JetClusteringUtils::get_phi(jets_ak4)"
        )

        df = df.Define(
            "jets_ak4_m",
            "JetClusteringUtils::get_m(jets_ak4)"
        )

        df = df.Define(
            "jets_ak4_n",
            "static_cast<int>(jets_ak4.size())"
        )
        

        df = df.Define(
            "missing_p",
            "FCCAnalyses::ReconstructedParticle::get_p(MissingET)",
        )

        # ----------------------------------------------------------
        # Event selection
        # ----------------------------------------------------------

        # At least one electron or muon with pT > 20 GeV
        df = df.Filter("muons_n + electrons_n >= 1")


        return df

    # __________________________________________________________
    # Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        branchList = [
            "muons_pt",
            "muons_eta",
            "muons_phi",
            "muons_q",
            "muons_n",
            "electrons_pt",
            "electrons_eta",
            "electrons_phi",
            "electrons_q",
            "electrons_n",  
            "missing_p",
            "n_pseudo_jets",
            "jets_ak4_pt",
            "jets_ak4_eta",
            "jets_ak4_phi",
            "jets_ak4_m",
            "jets_ak4_n"
        ]

        return branchList
