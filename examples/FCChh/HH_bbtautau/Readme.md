
This directory now contains a first update of files that can be used to run a skeleton fcc-hh workflow using the FCCAnalysis package.

It follows the workflow laid out in the central FCC software tutorial: https://hep-fcc.github.io/fcc-tutorials/master/index.html

To run the workflow, execute:

```
git clone git@github.com:sarahlouisewilliams/FCCAnalyses.git
cd FCCAnalyses/
git checkout fccuk-hhtutorial-swmay2023
source ./setup.sh 
fccanalysis build

fccanalysis run examples/FCChh/HH_bbtautau/analysis_stage1.py
fccanalysis final examples/FCChh/HH_bbtautau/analysis_final.py 
fccanalysis plots examples/FCChh/HH_bbtautau/analysis_plots.py
```
