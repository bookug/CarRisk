# CarRisk
predict the risk of a car applying for inssurance

统计数据信息：是否有明显的倾斜现象，即有些风险指数对应特别多？
各个属性和风险指数的相关关系，是否有些属性可以放弃不选，因为它们无用且可能产生干扰？
数据倾斜现象严重，风险指数为1的记录个数占了主要，而对于该风险，哟徐诶属性可能根本不具有区分度，比如最后一个特征。
应该如何处理这种情况？避免数据倾斜？移除无用属性？
---
还可以考虑交叉验证
regression: linear / logistic(须先把目标值预处理为0-1之间) / bossion
多种损失函数的度量：rmse，或者log？。。。
数据划分时，分为5份取一份做验证，或者分为10份？
(tree booster better than linear booster)
---
1、仅仅靠参数的调整和模型的小幅优化，想要让模型的表现有个大幅度提升是不可能的。GBM的最高得分是0.8487，XGBoost的最高得分是0.8494。确实是有一定的提升，但是没有达到质的飞跃。 
2、要想让模型的表现有一个质的飞跃，需要依靠其他的手段，诸如，特征工程(feature egineering) ，模型组合(ensemble of model),以及堆叠(stacking)等。




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


