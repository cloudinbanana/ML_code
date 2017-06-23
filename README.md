## src文档帮助

src目录下包含以下文档：BasicDataStruct，DataAnalysis，discretize，continuous，FeatureSelection，ModelEvaluate，utils，dtree_discretizer

### BasicDataStruct
    基本的数据结构，方便数据预处理、特征提取等各类操作。
    定义一个数据类，拥有以下几个属性：
        X：dataframe，有列名（变量名）和索引（每个样本的ID）。
        Y：series，有索引（对应X的索引，标识每个样本）。
        feature_cont：连续型变量列表。
        feature_binary：0-1离散型变量列表（不需要one hot，可以直接使用）。
        feature_cate：多取值离散型变量列表（需要one hot或者连续化）。
        model_type：标识分类或者回归。
    
    同时拥有以下几种方法（操作），可能会对变量列表进行增、删等：
        delete：删除已有的列，并同步修改变量列表。
        select：选择已有的某几列，并同步修改变量列表，实际上和delete方法的作用差不多，只是方便选择。
        add：增加新的列，并同步修改变量列表（对已有列可以考虑替换或者重命名后增加）。
        addObj：将当前对象与另一个对象合并。
        delFeature：改变离散型变量列表（删）。
        addFeature：改变离散型变量列表（增）。
        rename：改变变量名称。
        current_state：打印当前状态，包括当前各类变量的数量及名称。

### DataAnalysis
    描述性统计量、缺失值、异常值统计
    相关系数计算、热力图
    单变量分析图: 直方密度图、箱线图（连续型），柱形图（离散型）
    单变量与Y（单一）的分析图: 样本数量和Y组内比例柱形图（离散型Y），均值柱形图（连续型Y）
    单变量与Y（可多个）的分析图: 样本数量和Y均值柱形图（离散型Y或连续型Y）
    两个变量X与Y（可多个）的分析图: 0-1离散型Y创建1的占比热力图；连续型Y创建均值热力图

### discretize
    分位数离散化
    等分点离散化
    标准差离散化
    决策树离散化

### continuous
    条件概率连续化
    WOE连续化
    Label连续化编码（改写版）
    独热编码（改写版）

### FeatureSelection
	变量筛选模块。

### modelbaseline
    五种机器学习模型，以及网格搜索结果。


### ModelEvaluate
    计算KS值及对应分割点
    计算KS值，输出对应分割点和累计分布函数曲线图
    计算AUC值，并输出ROC曲线
    画好坏人分数分布对比直方图
    画整体分数的直方图（左Y轴）和每个区间内正类人群占比曲线趋势图（右Y轴）
    根据真实标签和预测概率计算模型指标

### dtree_discretizer
	协助DTDiscretizer将sklearn的决策树中的tree_.feature转化成二叉树

### utils
一些辅助函数。