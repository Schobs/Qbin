"""
Default configurations for uncertainty estimation using Quantile Binning
"""

from yacs.config import CfgNode as CN

# -----------------------------------------------------------------------------
# Config definition
# -----------------------------------------------------------------------------

_C = CN()

# -----------------------------------------------------------------------------
# Dataset
# -----------------------------------------------------------------------------
_C.DATASET = CN()
_C.DATASET.SOURCE = "https://github.com/pykale/data/raw/main/tabular/cardiac_landmark_uncertainty/Uncertainty_tuples.zip"
_C.DATASET.ROOT = "../data/cardiac_landmark_uncertainty/"
_C.DATASET.BASE_DIR = "Uncertainty_tuples"
_C.DATASET.FILE_FORMAT = "zip"
_C.DATASET.CONFIDENCE_INVERT = [["S-MHA", True], ["E-MHA", True], ["E-CPV", False]]
_C.DATASET.DATA = "4CH"
_C.DATASET.LANDMARKS = [0, 1, 2]
_C.DATASET.NUM_FOLDS = 8



_C.DATASET.UE_PAIRS_VAL = "uncertainty_pairs_valid"
_C.DATASET.UE_PAIRS_TEST = "uncertainty_pairs_test"


# ---------------------------------------------------------------------------- #
# Uncertainty Estimation Pipeline Parameters
# ---------------------------------------------------------------------------- #
_C.PIPELINE = CN()

# Can choose to evalute over a single value or multiple values for Q (# bins). You can:
# 1) Evaluate over each value of Q (set COMPARE_INDIVIDUAL_Q = True). For each Q it will compare DATASET.MODELS and DATASET.UNCERTAINTY_ERROR_PAIRS against eachother.
# 2) Compare results of a single model and a single uncertainty error pair (set COMPARE_Q_VALUES = True). 

_C.PIPELINE.NUM_QUANTILE_BINS = [5] 

#~# 1)
# Compare uncertainty measures AND models over each single value of Q? 
_C.PIPELINE.COMPARE_INDIVIDUAL_Q = True 
# [NAME, KEY (error in CSV), KEY (uncertainty in csv)]
_C.PIPELINE.INDIVIDUAL_Q_UNCERTAINTY_ERROR_PAIRS = [
    ["S-MHA", "S-MHA Error", "S-MHA Uncertainty"],
    ["E-MHA", "E-MHA Error", "E-MHA Uncertainty"],
    ["E-CPV", "E-CPV Error", "E-CPV Uncertainty"],
]

# Key for model name found in path.
_C.PIPELINE.INDIVIDUAL_Q_MODELS = ["U-NET", "PHD-NET"]
#~#


#~# 2)
# Compare a single uncertainty measure on single model through various values of Q bins e.g. 5, 10, 20 
_C.PIPELINE.COMPARE_Q_VALUES = False
_C.PIPELINE.COMPARE_Q_MODELS = ["PHD-NET"] # Which model to compare over values of Q.
_C.PIPELINE.COMPARE_Q_UNCERTAINTY_ERROR_PAIRS= [["E-MHA", "E-MHA Error", "E-MHA Uncertainty"]] # Which uncertainty estimation measure to compare over values of Q.  # TODO: test to make sure this is 2D
#~#


_C.PIPELINE.COMBINE_MIDDLE_BINS = False #Combine middle bins into 1 super bin
_C.PIPELINE.PIXEL_TO_MM_SCALE = 1.0
_C.PIPELINE.IND_LANDMARKS_TO_SHOW = [-1] # -1 means show all landmarks individually, [] means show none
_C.PIPELINE.SHOW_IND_LANDMARKS = False # Show results for individual landmarks?

# ---------------------------------------------------------------------------- #
# Visualization
# ---------------------------------------------------------------------------- #
_C.IM_KWARGS = CN()
_C.IM_KWARGS.cmap = "gray"
_C.MARKER_KWARGS = CN()
_C.MARKER_KWARGS.marker = "o"
_C.MARKER_KWARGS.markerfacecolor = (1, 1, 1, 0.1)
_C.MARKER_KWARGS.markeredgewidth = 1.5
_C.MARKER_KWARGS.markeredgecolor = "r"

_C.WEIGHT_KWARGS = CN()
_C.WEIGHT_KWARGS.markersize = 6
_C.WEIGHT_KWARGS.alpha = 0.7
_C.BOXPLOT = CN()
_C.BOXPLOT.SAMPLES_AS_DOTS = True 
_C.BOXPLOT.ERROR_LIM = 64 # Where to cut off Y axis for boxplot
_C.BOXPLOT.SHOW_SAMPLE_INFO_MODE = "All" # "None", "All", "Average" - shows % of samples per bin


# ---------------------------------------------------------------------------- #
# Misc options
# ---------------------------------------------------------------------------- #
_C.OUTPUT = CN()


_C.OUTPUT.SAVE_FOLDER = "../results"
_C.OUTPUT.SAVE_PREPEND= "8std_27_07_22"
_C.OUTPUT.SAVE_FIGURES = False

def get_cfg_defaults():
    return _C.clone()
