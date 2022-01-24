# Hand washing movement classification

This repository contains code for hand washing movement classification based on the six key movements defined by the World Health Organization (WHO).

The work has been done as part of the projects:

* "Integration of reliable technologies for protection against Covid-19 in healthcare and high-risk areas", project No. VPP-COVID-2020/1-0004.
* Latvian Council of Science project: “Auto-mated hand washing quality control and quality evaluation system with real-time feedback”, No: lzp - Nr. 2020/2-0309


# Quick start guide

To start working with the data, follow these steps:
1. Download and extract the datasets
2. Preprocess the datasets by extrating frames from the video data, separating them in classes, and further separating them in test/trainval subsets.
3. (Optional.) Calculate optical flow on the datasets.
4. Train the neural network classifiers on the data.


You are going to need a Linux OS with TensorFlow, Kerase, OpenCV, and NumPy installed to run the scripts, and a modern GPU to train the neural networks.


# Detailed instructions

## 1. Datasets

The code support the following publicly available datasets:

* Real-world hospital data sets, collected at the Pauls Stradins Clinical University Hospital (abbreviated as PSKUS or PSCUH): https://zenodo.org/record/4537209
* Lab-based dataset collected at the Medical Education Technology Center (METC) of Riga Stradins University: https://zenodo.org/record/5808789
* The publicly available subset of the Kaggle Hand Wash Dataset: https://www.kaggle.com/realtimear/hand-wash-dataset

Follow the links on the webpages to download the datasets.

Once you have downloaded them, extract them, and oraganize then so that each dataset is located in a single folder.

* The PSKUS dataset should have files "summary.csv", "statistics.csv" and folders named "DataSet1", "DataSet2" etc. in the top-level directory. Also copy the file `statistics-with-locations.csv` from this repostitory to the PSKUS dataset folder. This will ensure that vides from the same camera location will be mixed in the test and trainval folders, making the neural network generalization requirements more challenging. 
* The METC dataset should have files "summary.csv", "statistics.csv" and folders named "interface_number_1", "interface_number_2", "interface_number_3" in the top-level directory.
* For the Kaggle dataset, you'll need to do some manual actions: see below. The resulsing dataset should be names `kaggle-dataset-6classes`.

For the Kaggle dataset, you currently need to manually re-sort the files so that they are all put in just 7 classes. This is because the other datasets do not distinguish between right and left hand washing. Put the wrist-washing videos in the class 0 ("Other") folder.


## 2. Preprocessing the data

The folders `dataset-kaggle`, `dataset-metc` and `dataset-pskus` have `separate-frames.py` scripts in them. Fix the paths in these scripts to match the locations of your datasets, and run the script to separate the video datasets in frames, video snippets, as well as separate these frames and shoter videos in `trainval` and `test` folders.


## 3. Calculate optical flow

This step is optional and only required if the merged neural network architecture is used.

Run the `calculate-optical-flow.py` script, and pass the target dataset's folder names as the command line argument to this script.


## 4. Train the classifiers.


For each dataset, three training scripts are provided. (Replace `xxx` with the name of the dataset.)

* `xxx-classify-frames.py` - the baseline single-frame architecture
* `xxx-classify-videos.py` - the time-distributed network architecture with GRU elements
* `xxx-classify-merged-network.py` - the two-stream network architecture with both RGB and Optical Flow inputs.

These scripts rely on a number of environmenal variables to set training parameters for the neural networks.
Unless you're fine with the default values, should set these parameters before running the scripts, e.g. with:

     export HANDWASH_NUM_EPOCHS=40

The variables are:

* "HANDWASH_NN" - the base model name, default "MobileNetV2"
* "HANDWASH_NUM_LAYERS" - the number of trainable layers (of the base model), default 0
* "HANDWASH_NUM_EPOCHS" - the max number of epochs. Early termination is still possible! Default: 20.
* "HANDWASH_NUM_FRAMES" - how many frames to concatenate as input to the TimeDistributed network? Default: 5.
* "HANDWASH_SUFFIX" - user-defined additional suffix of the result files of the experiment. Default: empty string.
* "HANDWASH_PRETRAINED_MODEL" - the path to a pretrained model. Used for transfer-learning experiments. Default: empty string (pretrained model not used, the base model with ImageNet weights is loaded instead.)
* "HANDWASH_EXTRA_LAYERS" - number of extra layers (dense) to add to the network before the top layer. Default: 0.


# References

For more detailed information, see the following articles:

* A. Elsts, M. Ivanovs, R. Kadikis, O. Sabelnikovs. CNN for Hand Washing Movement Classification: What Matters More — the Approach or the Dataset? Submitted to the International Conference on Image Processing Theory, Tools and Applications (IPTA) 2022.
* M. Lulla, A. Rutkovskis, A. Slavinska, A. Vilde, A. Gromova, M. Ivanovs, A. Skadins, R. Kadikis and A. Elsts. Hand Washing Video Dataset Annotated According to the World Health Organization’s Handwashing Guidelines. Data, 6(4), p.38. [[HTML]](https://www.mdpi.com/2306-5729/6/4/38/htm)
* M. Ivanovs, R. Kadikis, M. Lulla, A. Rutkovskis, A. Elsts, Automated Quality Assessment of Hand Washing Using Deep Learning, arXiv preprint, 2020. [[PDF]](https://arxiv.org/pdf/2011.11383.pdf)


# Contacts

The main author of this code can be reached via email for questions: atis.elsts@edi.lv or atis.elsts@gmail.com