# CarRisk
predict the risk of a car applying for inssurance

分别在train和valid上作预测，统计各自的准确率
还可以考虑交叉验证
TODO:all codes in python and called in shell
to compute rmse in the python code
linear / logistic / bossion
the validation k can be adjusted
tree booster better than linear booster
统计数据信息：是否有明显的倾斜现象，即有些风险指数对应特别多？
各个属性和风险指数的相关关系，是否有些属性可以放弃不选，因为它们无用且可能产生干扰？

汽车投保风险指数预测

## 问题描述

某保险公司销售一种汽车保险，需要对汽车状态进行评估。现在你需要学习一个模型，可以根据汽车的各项指标对汽车的投保风险进行打分。
投保风险是从0到70的正整数，数值越大代表风险越高。
此时可用线性回归，如果先将y值映射到[0,1]，那么可用logistic回归。

## 预测目标

预测汽车的投保风险。

## 训练特征

汽车的32个指标。

## 问题抽象

一个典型的回归任务。

## 训练数据

共40000条数据
每行34列，第1列是车辆id，第2列是汽车投保风险值（y值），第3-34列是汽车特征（x值）。
32个特征中，有数值型，有类别型。

## 测试数据

每行33列，第一列是车辆id，第2到33列是汽车特征（x值）


