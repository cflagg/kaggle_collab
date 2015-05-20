# initialize folder

# set the working directory; "../" suggests a relative path for R . Use this if you have not setup an R Project
setwd("../Documents/GitHub/kaggle_collab/titanic")

# read in data
test_data = read.csv(paste0(getwd(),"/data/test.csv"))
train_data = read.csv(paste0(getwd(),"/data/train.csv"))

# explore dimensions and structure
dim(train_data)
names(train_data)
summary(train_data)

# load some useful packages
library(plyr)
library(dplyr)
library(tidyr)
library(ggplot2)