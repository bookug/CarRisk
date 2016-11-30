#!/bin/bash

#alias xgboost="/home/zengli/XGBOOST/xgboost"
export xgboost=/home/zengli/XGBOOST/xgboost
pred="car.txt.valid"
#pred="car.txt.train"
answer="pred.txt"
function computeRMSE()
{
	echo -n "now to compute the rmse: ${pred} ${answer} \n"
	awk 'BEGIN{sum=0}{if(NR==FNR){s[FNR]=$1} else{d=$1-s[FNR];sum = sum + d*d;}}END{sum=sqrt(sum/FNR);print sum;}' ${pred} ${answer}
}

# map the data to features. For convenience we only use 7 original attributes and encode them as features in a trivial way 
python mapfeat.py
# split train and validation
python mknfold.py car.txt 1 10
# training and output the models
${xgboost} car.conf
# output predictions of test data
#${xgboost} car.conf task=pred model_in=0100.model
${xgboost} car.conf task=pred model_in=0021.model
#${xgboost} car.conf task=pred model_in=0040.model
#to compute rmse
computeRMSE

# print the boosters of 0002.model in dump.raw.txt
#xgboost car.conf task=dump model_in=0020.model name_dump=dump.raw.txt
# print the boosters of 0002.model in dump.nice.txt with feature map
#xgboost car.conf task=dump model_in=0020.model fmap=featmap.txt name_dump=dump.nice.txt 

# cat the result
#cat dump.nice.txt

