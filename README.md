# MutSig-TME

The repository consists of files written in Python language used to annalize mutational signatures and tumor microenvironment.

## boxploting

The 'boxplotting.ipynb' notebook contains results of general analysis of the 3 IF panels and signature count panel. It produces boxplots of counts for each file and a bar chart for patients with each signature.

## phenotype_counting

This programme is used to create files with counts of different phenotype for each patient. The input should be a folder with files for every patient.

## phenotype_translating

This file contains code that transaltes the phenotypes found in phenotype_counting into cell types. The arguments taken by this programme are: a file path with phenotypes to translate, the output file path, and dictionary path.

## correlations

The two correlations files contain similar code. They both take data from two files: signature counts and cell type counts. Scatter plots of counts of every combination of cell type and mutational signature are created. Then Spearman's correlation is computed for each pair of data. The 'correlations_IF_supplementary.ipynb' is a notebook with results of the code for three panels from the mIF thechnology as well as the supplementary biomarkers (PDL-1 scores and IF dispersion). The 'correlations_IMC.ipynb' containt results for two panels obtained with the IMC technology.

## clustering

The 'clustering_IF2.ipynb' file is a result of running the K-means clustering for every number of clusters between 2 and 10. It produces the silhouette plots, heatmap clusterings, polots with average correlations for each cluster. Also average silhouette score and inertias for every number of clusters are plotted.

## bubble heatmap

This file includes a code that creates heatmaps of correlations with regard to the p-values. It also draws seperation lines for each cluster. The 'bubble_heatmap.ipynb' notebook contains results for the IF2 panel, IMC Panel 1 and the supplementary biomarkers.


