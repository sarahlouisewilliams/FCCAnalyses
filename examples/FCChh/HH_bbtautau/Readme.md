
This directory now contains a first update of files that can be used to run a skeleton fcc-hh workflow using the FCCAnalysis package.

It follows the workflow laid out in the central FCC software tutorial: https://hep-fcc.github.io/fcc-tutorials/fast-sim-and-analysis/fccanalyses/doc/starterkit/FccFastSimAnalysis/Readme.html#part-ii-analyse-with-fccanalyses

To run the workflow, execute:

```
fccanalysis run examples/FCChh/HH_bbtautau/analysis_stage1.py
fccanalysis final examples/FCChh/HH_bbtautau/analysis_final.py 
fccanalysis plots examples/FCChh/HH_bbtautau/analysis_plots.py
```
