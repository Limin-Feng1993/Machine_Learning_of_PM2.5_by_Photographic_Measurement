# Machine-Learning_Prediction_of_PM2.5_by_Photographic_Measurement

This folder contains the data and code in a published article “Performance Evaluation of Photographic Measurement in the Machine-Learning Prediction of Ground PM2.5 Concentration”.

Citation: 

Feng, L., Yang, T. & Wang, Z. Performance Evaluation of Photographic Measurement in the Machine-Learning Prediction of Ground PM2.5 Concentration. Atmospheric Environment, 118623 (2021). DOI: https://doi.org/10.1016/j.atmosenv.2021.118623.

___________________________________________________________________________________________________________________________________________________________________________

本文是笔者已发表在学术期刊《Atmospheric Environment》上的一篇文章的中文版，有删节。考虑到版权问题，本文不附原图，Figure在期刊网址可获得公开版。

![文章首页](https://upload-images.jianshu.io/upload_images/17085473-613fac6e51870490.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 1. 背景介绍

2021年5月10日，著名科学杂志《Nature》发表一篇题为《Smartphone science: apps test  and track infectious diseases》的文章，提到了智能手机的拍摄功能逐渐在科学研究中发挥重要作用。文章指出，全球有数十亿部正在使用中的智能手机，这为疾病追踪、诊断和公民科学 (**Citizen Science**) 提供了前所未有的机会。在公民科学中，最为重要的组成部分是智能手机科学 (**Smartphone Science**) 。例如研究人员用手机的拍摄功能复现了价格动辄高达5万美元的台式荧光显微镜做出的结果，成本只花了不到40美元。

无独有偶，相机拍摄，或者称之为图像观测，因其较低的部署成本和简便性，在气象领域也有广阔的应用前景。气象垂直观测的稀缺性和稀疏性，严重制约了天气和空气污染的精准预测与分析。普通公众通常很难免费、方便地获取气象数据，尤其是高时空分辨率的地基观测数据。至于基于气球的探测数据，例如通过无线电探空仪测量气象参数的垂直剖面，可获取的观测站点更加稀少，时间分辨率也更低。然而，气象参数的垂向廓线对于空气污染的向前预测和向后分析是必不可少的<sup>1-4</sup>。风温廓线的垂直分布在一定高度范围内趋于均匀，但也包含风切变和逆温层<sup>5,6</sup>。在白天，地面产生的湍流增强了热量和动量的垂直交换，因此海拔约1-2 公里以下的风和温度在垂直方向上均匀分布，梯度很小。此外，大气颗粒物和水汽也在近地表空气中均匀混合，形成不稳定的边界层<sup>7,8</sup>。边界层内部的空气组分与上面的空气有明显差别，例如空气污染物浓度的显著差异<sup>9,10</sup>。该边界的存在是因为一个逆温层覆盖了边界层的顶部并抑制了热湍流的继续上升<sup>11</sup>。边界层高度 (BLH) 表征气溶胶湍流混合、扩散和传输的程度<sup>12-14</sup>，并且与大气细颗粒物 (本文中的PM<sub>2.5</sub>) 的浓度负相关<sup>13</sup><sup>, </sup><sup>15</sup><sup>, </sup><sup>16</sup>。而在夜间，由于缺少太阳辐射能量的输入，来自地表的湍流和向上的热通量减弱，温度廓线在距地面几十米内出现逆温层<sup>17,18</sup>。大气颗粒物向上扩散受阻，集中分布在地表空气中，从而形成稳定的夜间边界层 (NBL)，此时地表空气容易受到严重污染<sup>19-21</sup>。

上述边界层的典型昼夜变化通常出现在没有云、雾和降水过程发生的内陆地区 (海岸地区边界层变化更为复杂)。事实上，气象廓线的变化非常复杂，BLH的确定也有不同学者采用不同的方法。传统上，BLH是通过探空仪器对温度、湿度和风等气象参数的垂向观测来识别垂直梯度和切变来判断的<sup>22-24</sup>。然而，这种BLH的测定存在其本身固有的缺陷<sup>23,25</sup>。首先，探空资料的时空分辨率较低，在中国只有大约一百多个站点，每12小时发射一次探空观测 (因为经济成本的制约)。然而，边界层的变化是高频发生的。湍流的时间尺度从小涡的几秒到最大涡流的半小时不等，相应的空间尺度从几毫米到几百米不等<sup>26,27</sup>。探空观测很难捕捉到亚格网尺度 (< 0.1° × 0.1°) 以及分钟级别的边界层变化。对于这个问题，一般的解决方法是边界层方案的参数化<sup>28,29</sup>。此外，云、雾和降水过程对边界层结构和地面PM<sub>2.5</sub>浓度都有重要影响<sup>30-32</sup>。类似于下沉逆温，低云抑制上升的热湍流，降低BLH，并形成云顶边界层<sup>33</sup>，尤其是在下午的早些时候<sup>34</sup>。当雾形成时，湍流扩散减弱并抑制边界层的发展<sup>14,35</sup>。此外，降水通过清除气溶胶和从云顶去除液滴来破坏边界层的生长<sup>36,37</sup>。有研究发现BLH与PM<sub>2.5</sub>在降水前呈强负相关，降水后呈弱相关<sup>19</sup>。由于缺乏水平覆盖范围，单站点的气象观测可能无法捕捉到局地的雾、云和降水过程。因此，我们需要一种经济成本低、时间分辨率高、适合大规模应用的方法，以弥补气象观测和参数化方案的不足。

气溶胶浓度以及云雾降水过程都会影响大气透明度和能见度，直接决定太阳光和人造光在大气中的散射、折射和吸收过程。激光雷达 (LIDAR) 通常用于观测气溶胶粒子在不同波长下的散射和吸收效应，例如被广泛采用的 532 nm 和1024 nm后向散射和消光系数。但是，LIDAR只能探测到观测点上方的狭长气柱。当其判定BLH是基于气溶胶浓度的分层，很容易将残留层、抬升的烟羽和低云错误的识别为边界层顶<sup>38-40</sup>。此外，LIDAR仪器价格昂贵且需要频繁维护，这限制了它的广泛应用和高空间分辨率观测。除了激光雷达，大气散射的可见光也可以用普通的相机捕捉到。普通相机可以低成本地进行摄影观测，时间分辨率可达分钟级，超过公开的气象数据，并能捕捉到在大范围的垂直平面上的天气过程<sup>41,42</sup>。 更重要的是，相机可以随时联网，照片以公众能轻松访问的形式实时发布。此外，图像的预测和外推比数值天气预报更容易。现阶段计算机视觉技术非常成熟，为处理图像数据提供了强大的工具，不需要以超级计算机来求解大气流体动力学的偏微分方程。

机器学习和人工智能领域的进步也将增强我们对自然科学的理解，例如利用人工神经网络，预测天气雷达回波的图像<sup>43,44</sup>。但是，机器学习的作用不应该被过分夸大，而是应该结合学科领域知识应用于具体的场景<sup>45</sup>。在本文的研究中，我们使用普通相机自动拍摄白天的天空和夜间的灯光。图像观测并不是一种全新的技术。广义上讲，所有基于遥感图像的方法都是图像观测。遥感是指通过使用与物体不直接接触的传感器测量物体的辐射信号（例如可见光和红外光），从而收集有关物体的信息<sup>46,47</sup>。传感器有很多种，例如基于卫星的传感器探测到的遥感图像，也可以是本研究中的民用相机。照片中的颜色特征代表了大气颗粒物对可见光的散射效应，并记录了云雾和降水过程。基于这些图像特征与再分析气象数据的结合，我们采用机器学习方法来预测地面PM<sub>2.5</sub>浓度。我们还讨论了图像特征及其在机器学习模型中发挥的作用，并指出了本研究中应用的机器学习方法的优缺点以及未来可能改进的方向。

## 2. 方法

### 2.1 地面观测

自动拍摄相机放置在中国科学院大气物理研究所（IAP，北京，116.38°E，39.97°N，约10 m高度）的屋顶上，每隔30分钟进行一次观测。从2019年5月到2020年3月，相机连续拍摄了13000多张图像，每个像素包含红 (R)、绿 (G)、蓝 (B) 三个亮度通道。我们提取了图像天空和地面部分像素中R、G 和 B 通道的平均值（图 1）。天空和地面两部分的分割大约是每张照片的 50% （顶部和底部）。每小时PM<sub>2.5</sub>浓度是从生态环境部公开的空气质量数据中获得的。所选站点位于奥林匹克体育中心 (116.41°E， 40.00°N) 的森林公园内，距离 IAP 站点约 2 公里。为了匹配空气质量监测数据的时间分辨率，所有变量都转换为小时平均值。IAP 附近没有探空观测，可用的探测站点距离约 30 公里。因此，我们使用了再分析数据中的各高度层的气象参数。本文的数据和代码可在 GitHub 上获取：https://github.com/Limin-Feng1993/Machine_Learning_of_PM2.5_by_Photographic_Measurement。

### 2.2 再分析数据

来自ECMWF（欧洲中期天气预报中心）的综合预报系统 (IFS) 的 ERA5 数据是目前流行的全球天气数据源。ECMWF 将数值天气预报模型的输出与来自世界各地的历史观测结果相结合，并利用数据同化技术将这些数据一起重新分析，生成全球完整且一致的数据ERA5，时间分辨率达到了每小时。我们下载了ERA5每小时再分析数据，包括 BLH、风、温度、降水和位势高度，高度层为地表和两个等压高度层（850 hPa 和 500 hPa）。选定的经纬度网格 (0.25°×0.25°) 和时间段与图像观测一致，以便许合并数据。特别指出，ERA5中边界层高度的计算方法是总理查德森数法<sup>48</sup>。

### 2.3 机器学习方法

目前应用最广泛的机器学习可分为两类：神经网络算法（如CNN、RNN、LSTM）和树算法（如随机森林、GBDT、XGBoost）。因此，我们选择了决策树<sup>49</sup>  和多层感知机（MLP）模型<sup>50</sup>。其中，决策树模型来自于Python-sklearn模块中的分类回归树（CART）模型，它是随机森林、XGBoost、GBDT的基础。同样，MLP也是最基础的简单神经网络。决策树模型是基于if-then-else逻辑推理规则的白盒模型，过程透明，结果可解释，应用时无需对数据进行归一化（即保留每个变量的原始单位）。相比之下，MLP是一种前馈神经网络，应用时需要对数据进行归一化处理，否则误差（损失函数）不会收敛。MLP 过程是一个黑匣子，结果无法解释，但误差很小。MLP中的参数是通过自动选择的，因此MLP的预测存在随机性。我们将神经网络的隐藏层数设置为三层，每层包含三个神经元。这个3 层 9 神经元 MLP 的其他参数还包括 learning_rate = 0.001、batch_size = 500 和 random_seed = 1。这种简单的设置最大限度地减少了计算功耗，在笔记本电脑上误差收敛所需的时间不到 1 分钟。在应用机器学习模型时，数据必须满足“独立同分布（IID）随机变量”假设。由于昼夜边界层的差异较大，因此需要将白天和夜间数据分开，以确保 IID 假设成立。

### 2.4 因果推理方法

在一个复杂系统中确定变量之间的因果效应是非常困难的。一方面，变量的时间序列变化是非线性的，这是由于潜在变量的存在。两个变量可能会从强正相关突然或者逐渐变为弱相关甚至负相关。另一方面，即使发现变量之间存在相关性，相关性也不代表因果关系，例如，共同变量可能导致多个变量呈现虚假相关性。在一个确定性的因果关系中，Y = βX + ε，其中 ε 是随机误差，β = 因果性 + 混淆 + 选择偏差<sup>51,52</sup>。因果性不随环境变化，是稳定可解释的，是所有学科都追求的量。混淆是指由于某些潜在或共同变量而产生的虚假相关性。选择偏差是选择统计样本时引起的相关性，随数据集的不同而不同。一般来说，选择偏差随着数据量的增加而减小。在本文中，我们选择了 DoWhy 模型（[https://github.com/microsoft/dowhy](https://github.com/microsoft/dowhy))<sup>53</sup>，旨在找到真正的因果效应（β 的第一项），并忽略由混淆和选择偏差引起的虚假相关性。除了由 Judea Pearl 创建的贝叶斯推理网络（因果图）<sup>54</sup>，DoWhy 模型也采用了Donald Rubin开发的Potential Outcomes 模型<sup>55</sup>，并将这两种方法组合成统一的范式。对于具有大量非线性过程的复杂系统，例如边界层内的过程，DoWhy 模型仍然可能给出虚假的因果效应的估计。然而，为了简化问题，我们选择使用该统计推断作为参考。

## 3 结果与讨论

### 3.1 变量间的非线性相关和不确定性分析

首先，我们需要探索数据以选择合适的变量作为机器学习模型的输入，即特征工程。特征工程是机器学习的核心部分，但不能以编程的方式自动化，因为它基于经验和领域知识。输入变量的数量应尽可能少，以保证模型输出的准确性的同时尽量节省计算时间。

在白天，三分之二的阳光在大气中散射并漫射整个天空，包括瑞利散射和米氏散射。阳光到达地表并被植物吸收，叶绿素吸收中心波长为0.45 μm（蓝光）和 0.65 μm（红光），反射绿光（0.54 μm）。夜间，人工光源发出的光也在空气中散射，亮度与大气透明度有关，与光波长无关。我们提取了照片天空和地面部分R、G和B通道的平均亮度，然后绘制了核密度估计 (KDE)，它使用平滑峰值函数 (Kernel) 来模拟真实的概率分布曲线。在白天，天空部分蓝光的概率分布与绿光相似，而地面部分红光和绿光的概率分布在相似。换句话说，红光R 和蓝光B的概率分布在天空和地面部分都有很大不同（图 2）。因此，蓝光与红光亮度的比值 (B/R) 和总 RGB 亮度 (R + G + B) 可以用作输入变量，它们是照片的代表性特征。我们选择的照片特征包括B/R_sky、B/R_ground、RGB_sky和RGB_ground，分别代表天空部分的B/R比、地面部分的B/R比、天空部分的总RGB亮度，以及地面部分的总 RGB 亮度。

蓝红比B/R表征可见光被大气颗粒物散射的程度。白天地面PM<sub>2.5</sub>浓度与B/R_sky的关系如图3(a)所示。散点图包含大约 7000 个小时值，PM<sub>2.5</sub>浓度与 B/R_sky 之间关系非常复杂，大致可以分为三组。第一组是当 B/R_sky 较小（≈ 1），且地面PM<sub>2.5</sub>浓度出现高水平（> 150 μg/mm<sup>3</sup>）时；第二组是B/R_sky较大（>1.3），且PM<sub>2.5</sub>浓度偏低（< 50 μg/m<sup>3</sup>）；第三组介于前两组之间，二者之间的关系是不确定的、随机的或混乱的，表明存在其他潜在因素的影响。我们用玻尔兹曼函数拟合这些散射；然而，只有一些散点分布在这条拟合曲线周围，表明这条曲线是经验性的。尽管如此，我们仍然可以使用这条拟合曲线来解释PM<sub>2.5</sub>浓度与 B/R_sky 之间的关系。白天，当B/R较大时，天空呈现深蓝色，这是由于瑞利散射的短波较强，表明大气透明度较高，因此地面PM<sub>2.5</sub>浓度较低。反之，当B/R较小时，天空呈现白色或灰色（R≈G≈B），说明大量颗粒物的米氏散射效应较强，因此PM<sub>2.5</sub>浓度较高。米氏散射的程度与波长无关，因此 R、G 和 B 通道亮度值几乎相等。这种解释是基于大气颗粒物混合均匀的假设（即靠近地面和高空的气溶胶浓度相近且来源相同），RGB 通道亮度反映的是整个气柱的气溶胶浓度。除了气溶胶和水汽含量外，由于太阳高度角的变化，B/R比随时间变化，这给B/R_sky与PM<sub>2.5</sub>浓度的关系带来了不确定性。

在日出和日落时刻，大部分短波的蓝光被折射掉，天空呈现红色。此时瑞利散射效应较弱，无法通过B/R比来区分米氏散射的强弱，从而使得B/R_sky与PM<sub>2.5</sub>浓度的关系不清楚。因此，我们将日出和日落时段放入夜间数据中。事实上，早上和晚上确实分别是夜间边界层的结束和初始状态。在夜间，与太阳光相比，人造光和相机之间的距离很小（100-2000 米），因此光的散射与波长无关，反映大气颗粒物散射效应的是总RGB亮度。夜间总RGB亮度比白天小一个数量级左右，所以夜间数据信噪比较小，误差较大。由于人工光照条件不同，光色的昼夜变化给B/R比带来了噪声。尽管如此，夜间 PM<sub>2.5</sub> 浓度仍与 B/R 比（B/R_sky、B/R_ground）有关。我们绘制了夜间 PM<sub>2.5</sub>浓度与 R 和 B 值之间的关系，如图 S1 所示。与 R_ground 值相比，似乎高 PM<sub>2.5</sub>浓度出现在比B_sky 值更高的 R_sky 值，尤其是在 10 < R_sky < 60 时。PM<sub>2.5</sub>浓度与 R_ground 和 B_ground 的关系没有明显的规律，表明夜间光源的异质性，这由地面部分 R、G 和 B 值的双峰分布再次证实（图 S2）。为了更进一步，我们采用了 R、G和 B 值来聚类PM<sub>2.5</sub>浓度，见图 4。结果表明PM<sub>2.5</sub> 浓度以不同的斜率分布在 R-B坐标轴中（图 4c），而以均匀斜率 (Y = X) 分布在 B-G坐标轴中。R-G 坐标轴中的斜率也略有不同（图 4b）。换句话说，重要的是 B/R 比，而不是 B/G 或 G/R 比。

在白天数据中，我们得到一个经验拟合函数来表示地面PM<sub>2.5</sub>浓度与B/R_sky的关系：

![经验拟合函数](https://upload-images.jianshu.io/upload_images/17085473-3b5c50313d646e87.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

它是一种凭经验的拟合，而不是基于统计工具。虽然参数的选择是主观的，但仍然是基于对大量数据的归纳分析。值 500 实际上代表了在地面PM<sub>2.5</sub>浓度最高水平的两倍（很容易看到约为 250 μg/m<sup>3</sup>）。同样的分布也出现在 OSC 站点地面 PM<sub>2.5</sub> 浓度和 BLH 之间的关系中（图 3（b））。同样，我们获得了PM<sub>2.5</sub>与 BLH 的经验拟合函数：

![经验拟合函数](https://upload-images.jianshu.io/upload_images/17085473-809d4e58cf652d23.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

请注意，仍有大量散点未分布在拟合曲线周围，可能是因为未考虑湿沉降（雾、降水等）的清除作用。然而，在无降水、无污染物外部输送 (沙尘、外来传输污染气团等)、局部排放源强度恒定的边界层中，大气颗粒浓度随BLH的减小呈指数增加的结论仍然合理。

### 3.2 机器学习中图像特征与BLH的重要性对比

数据的正态分布和同质性是所有机器学习算法的前提假设。我们计算了照片特征（B/R_sky、B/R_ground、RGB_sky 和  RGB_ground）的平均值 (μ) 和标准偏差 (σ)，并绘制了相应的正态分布以及实际分布（图 S3）。这四个特征不是严格的正态分布，其中 B/R_sky 显示偏斜分布，B/R_ground 和 RGB_ground 显示双峰分布（图 S3）。然而，不存在严格遵守 IID 假设的真实数据集，我们仍然将数据视为近似的正态分布。此外，人工神经网络需要对输入变量进行归一化，固定在 0-1 的范围内，而决策树模型不需要这个操作。需要注意的是，归一化只会加快损失函数（预测误差）的收敛速度，并不会改变数据的正态分布特性。

边界层总是与大尺度强迫处于准平衡状态，即边界层过程发生的相对较快，并在几小时内对外强迫力做出响应<sup>56</sup>。大尺度引导气流导致气象参数之间的空间相关性和一致性。大尺度强迫引导近地表天气，如行星波（如罗斯贝波），其特征一般选择 500 hPa 处的位势高度，其等于重力加速度乘以高度 (gh)。高位势高度表明地表高压系统，通常带来低风速的静态天气<sup>57</sup>。边界层上方的自由大气与地面的摩擦力可忽略不计，其中的大尺度气流可近似为无粘性不可压缩流体，满足伯努利定律：势能增大，动能减小，即，总能量是守恒的。我们用这个公式来计算单位体积大气流体的重力势能 (J)：GE = ρgh，其中密度 ρ = P × 29/(8314 × T)，P 是气压 (500 hPa)，T 是温度（K），g = 9.8 m/s<sup>2</sup>，29是空气的平均分子量（g/mol），8314是气体常数。最大 BLH 通常在 1-2 km（对应于 850 hPa）范围内，因此该水平的动能也很重要。我们使用该公式计算动能 (J)：KE = 1/2 ×ρV<sup>2</sup>，其中V是风速 (m/s)。

最后我们选择了输入变量集 X = ['B/R_sky', 'RGB_sky', 'B/R_ground', 'RGB_ground', 'BLH', 'KE_850', 'GE_500', 'T2m', 'U10', 'V10', 'TP', 'SP']，其中 KE_850 代表 850 hPa（边界层顶部）处的动能，GE_500 代表 500 hPa 处的重力势能（表征大尺度气流），T2m 为地表气温，U10 和V10 为地表风分量，TP 为总降水量（mm），SP 为地表气压（Pa）。因变量 (Y) 是地面PM<sub>2.5</sub>浓度。

边界层过程在昼夜有显著差异，因此模型需要分别学习白天和夜间数据集。在机器学习中，过拟合很常见，亦即已知训练数据集上的表现优于未知的测试数据集。过度拟合通常是由于模型过于复杂。以白天数据作为输入，在6层深度决策树上，模型在训练和测试数据集表现相似，确定系数 (R<sup>2</sup>) 大约等于 0.5，并且没有过度拟合。当决策树的深度大于 6 级时，在测试数据上的误差反而增加，表明模型过度拟合（图 S4（a））。因此，在权衡高精度和防止过度拟合后，我们选择了 6 层决策树作为性价比最高的模型。训练集上的均方根误差 (RMSE_train) 为 25 μg/m<sup>3</sup>，RMSE_test = 29 μg/m<sup>3</sup>。误差较大的主要原因是模型简单，PM<sub>2.5</sub>浓度分布不均，其中包含少数高值（即数据的肥尾分布），对模型影响较大（图S4（b））。

为了更好地解释决策树的输出，需要对其进行后修剪（切断分支）并手动合并以阐明核心主干（图 5（a））。在 CART 模型中，我们使用了 Python-sklearn 模块，该模块采用误差平方和（SSE）作为划分标准。它遍历特征（如B/R_sky），将每个特征的每个分区值作为一个树节点，通过这些树节点将样本划分为左右子树，然后选择特征在决策树中的顺序和每个具有最小 SSE 的区分值。在白天决策树中，初始根节点为 B/R_sky = 1.14。在洁净的天气（PM<sub>2.5</sub> < 20 μg/m<sup>3</sup>），B/R_sky 很大（> 1.21），BLH 大于 1104 m。在稍大的 B/R_sky 范围 (1.14–1.21) 中，如果总 RGB_sky 亮度较低 (< 556)，地面PM<sub>2.5</sub>浓度仍然增加到 > 32 μg/m<sup>3</sup>。当 B/R_sky 较小（<1.14）时，RGB_ground 总亮度较高，B/R_ground 较大，PM<sub>2.5</sub> > 69 μg/m<sup>3</sup>，有时达到污染水平。照片的地面部分主要是绿色植被。RGB_ground 总亮度高，B/R_ground 大，说明叶绿素对红光的吸收减弱，红光变大，通常在冬天，容易出现重污染。冬季植被冠层面积减少可能会减弱其对空气污染物的吸收和沉降作用<sup>58,59</sup>，但这不在本文的讨论范围内，排放源强度的季节性变化可能更为重要。总之，在白天，B/R_sky 在决策树确定PM<sub>2.5</sub>浓度过程中的优先级高于 BLH。

决策树模型的误差没有达到机器学习的最小水平。因此，我们使用 MLP，设置为 3 层神经网络，共有 9 个人工神经元，以接近最佳性能。MLP 在 30 次迭代后将误差收敛到可接受的水平，测试数据集上的 RMSE ≈ 3 μg/m<sup>3</sup>（图 S5（a））。然而，MLP 是一个黑盒模型，我们无法知道神经网络内部的预测过程，因此结果是不可解释的。

当涉及到夜间数据作为模型输入时，6 层决策树仍然是最佳选择，训练数据上的 R<sup>2</sup> = 0.7，测试数据上的 R<sup>2</sup> = 0.5（图 S6（a））。无论决策树的深度如何，该模型在训练集上的表现都优于在测试集上的表现，表明模型过拟合。在决定系数方面，决策树在夜间数据上的表现优于白天数据，因为PM<sub>2.5</sub>浓度的高低值在夜间分布更均匀（图 S6（b））。这是因为边界层内的湍流运动在夜间较弱，细颗粒物浓度普遍较高，PM<sub>2.5</sub>浓度的时间变化不如白天剧烈。

在夜间决策树中，初始根节点为RGB_sky = 21（图 5（b））。照片的天空部分还包含不同颜色和亮度的人工灯光（图1）。RGB_sky > 21 被认为是在早晚有少量阳光，或者在有强灯光的夜间，而RGB_sky < 21 被认为是完全没有光的夜间时段。当相机捕捉到足够量的可见光时（RGB_sky > 21），如果BLH > 31 m且B/R_sky > 1.35，则PM<sub>2.5</sub>浓度小于47 μg/m<sup>3</sup>，空气质量良好。相反，当BLH < 31 m 且B/R_sky < 0.39 时，PM<sub>2.5</sub> 浓度> 99 μg/m<sup>3</sup>，表明处于污染状态。当相机没有捕捉到可见光 (RGB_sky < 21) 时， 如果 B/R_sky < 0.43 和 BLH < 19 m，则 PM<sub>2.5</sub>浓度大于 40 μg/m<sup>3</sup>。晚上，在决策树的判定中起关键作用的是BLH，B/R_sky的重要性与BLH不相上下。相比之下，地面部分的两个参数RGB_ground和B/R_ground在决策树的分支中，代表附近（<100 m）的人造光。 MLP 在夜间数据和白天数据上的表现一样，在 30 次迭代后将误差收敛到可接受的水平，测试数据集上的 RMSE ≈ 3 μg/m<sup>3</sup>（图 S5（b））。

### 3.3 代表性案例

选取几个有代表性的例子来说明图像特征与气象条件和地面PM<sub>2.5</sub>浓度的相关性。在一个晴天，云量0%，天空部分红色通道平均值R_sky = 152，绿色通道G_sky = 197，蓝色通道B_sky = 208，PM<sub>2.5</sub> = 7 μg/m<sup>3</sup>（图 1(a))。在云量达到 50% 左右的一天，如图 1(b) 所示，R_sky = 181，G_sky = 193，B_sky = 198，PM<sub>2.5</sub> = 2 μg/m<sup>3</sup>。当云层遮挡太阳光时，天空中红光亮度增加，蓝绿光变化不大，说明大粒径的云滴对太阳光的散射主要是在长波波段。

雾和霾天气的情况不同。雾天，R_sky = 201，G_sky = 201，B_sky = 196，PM<sub>2.5</sub> = 25 μg/m<sup>3</sup>（图1（c））。这个大雾天能见度很低，因为雾滴的散射作用和PM<sub>2.5</sub>起到了类似的作用。散射的阳光是白色的，R/G/B 通道值几乎相同。雾霾天，R_sky = 191，G_sky = 195，B_sky = 192，PM<sub>2.5</sub> = 200 μg/m<sup>3</sup>，见图1（d）。雾天，天空中的三个RGB通道均低于雾天，而PM<sub>2.5</sub>浓度达到重污染水平。

到了晚上，晴夜和降水的情况也不同。在晴朗的夜晚，R_sky = 29，G_sky = 24，B_sky = 18，R_ground = 9，G_ground=10，B_ground = 6，PM<sub>2.5</sub> = 73 μg/m<sup>3</sup>（图 1（e））。降水发生时（2019-06-01 09:00 下雨），R_sky = 52，G_sky = 47，B_sky = 40，R_ground = 7，G_ground = 8，B_ground = 5，PM<sub>2.5</sub> = 39 μg/m<sup>3</sup>（图. 1(f))。夜间出现降水时，人工灯光被雨滴散射，相机捕捉到的光面积较大，但亮度减弱，因此地面部分RGB的平均值下降。同时，PM<sub>2.5</sub>浓度偏低，说明气溶胶颗粒被降水清除，NBL的发展中断。此外，灯光亮度不稳定，导致夜间数据存在样本选择偏差和随机误差。

### 3.4 变量间的因果效应

这里我们用DoWhy模型分析了图像特征与PM<sub>2.5</sub>的因果关系。DoWhy模型采用后门准则方法确定变量之间的因果关系，消除了因共同变量而产生的虚假相关性，保留了真实的因果关系<sup>60</sup>。我们假设照片的 RGB（代表整个气柱的气溶胶浓度）、大尺度气流的势能和动能的相互转换以及未知的势变量 U（云雾过程、降水等) 对地面PM<sub>2.5</sub>浓度 (Y) 产生因果影响。我们设置 X = ['B/R_sky', 'B/R_ground', 'RGB_sky', 'RGB_ground']。KE_850 和 GE_500 被认为是共同变量，因为大尺度强迫同时影响大气透明度和PM<sub>2.5</sub>浓度。在输入到 DoWhy 模型之前，所有变量都被归一化到 [0, 1] 的范围内，以使它们无量纲。根据显著性检验获得的 p 值，通常认为在 p < 0.01 时具有统计显着性，并且在 p < 0.001 时非常显着。在白天数据中，统计推断表明X（四个图像特征）对PM<sub>2.5</sub>浓度的影响具有统计学意义（p < 0.001），因果效应为+94 μg/m<sup>3</sup>。在这里，这种因果效应意味着在图像特征的最大变化下，对PM<sub>2.5</sub>浓度的影响是增加了 94 μg/m<sup>3</sup>。相比之下，在夜间数据中，X 对PM<sub>2.5</sub>浓度的影响也具有统计学意义（p < 0.001），因果关系为 +46 μg/m<sup>3</sup>。图像特征的重要性在夜间减弱，如前所述，BLH 在决策树预测夜间PM<sub>2.5</sub>浓度方面起着至关重要的作用。

## 4. 结论

对于照片的天空和地面部分，平均蓝色亮度和平均红色亮度的概率分布显着不同。天空部分蓝红通道比（B/R_sky）表征可见光对大气颗粒物的散射效应，与地面PM<sub>2.5</sub>浓度呈非线性负相关。在白天，在决策树确定PM<sub>2.5</sub>浓度时，B/R_sky 的优先级高于边界层高度 (BLH)。晚上，BLH在决策树的确定中起到关键作用，B/R_sky的重要性与BLH不相上下。图像观测可以有效地用于补偿探空观测的稀疏空间和时间分辨率。考虑到机器学习中的误差仍然较大，需要进一步的研究以获得更好的图像处理方法。

本研究中应用的人工神经网络方法的优点是预测PM<sub>2.5</sub>浓度的准确性高，RMSE 为 1-3 μg/m<sup>3</sup>。然而，我们无法推导出变量之间的因果效应，结果也无法解释。决策树模型的误差比神经网络大一个数量级，但其确定PM<sub>2.5</sub>浓度的过程是透明的，图像特征的重要性是可以量化的。机器学习未来的发展方向应该是提高模型的可解释性，克服其黑盒性质，同时保证预测的准确性。


### 参考文献

1	Wen, C. et al. A novel spatiotemporal convolutional long short-term neural network for air pollution prediction. Science of The Total Environment 654, 1091-1099 (2019).

2	Cabaneros, S. M. S., Calautit, J. K. & Hughes, B. R. A review of artificial neural network models for ambient air pollution prediction. Environmental Modelling and Software 119, 285-304 (2019).

3	Qi, Z. et al. Deep Air Learning: Interpolation, Prediction, and Feature Analysis of Fine-Grained Air Quality. IEEE Transactions on Knowledge and Data Engineering 30, 2285-2297 (2018).

4	An, Z. et al. Severe haze in northern China: A synergy of anthropogenic emissions and atmospheric processes. Proceedings of the National Academy of Sciences 116, 8657-8666 (2019).

5	Fan, J. et al. Dominant role by vertical wind shear in regulating aerosol effects on deep convective clouds. Journal of Geophysical Research: Atmospheres 114 (2009).

6	Luhar, A. K. The influence of vertical wind direction shear on dispersion in the convective boundary layer, and its incorporation in coastal fumigation models. Boundary-Layer Meteorology 102, 1-38 (2002).

7	Conzemius, R. J. & Fedorovich, E. Dynamics of sheared convective boundary layer entrainment. Part I: Methodological background and large-eddy simulations. Journal of the atmospheric sciences 63, 1151-1178 (2006).

8	Fedorovich, E., Nieuwstadt, F. T. M. & Kaiser, R. Numerical and laboratory study of horizontally evolving convective boundary layer. Part II: Effects of elevated wind shear and surface roughness. Journal of Atmospheric Sciences 58, 546-560 (2001).

9	Miao, Y., Liu, S. & Huang, S. Synoptic pattern and planetary boundary layer structure associated with aerosol pollution during winter in Beijing, China. Science of the Total Environment 682, 464-474 (2019).

10	Miao, Y. & Liu, S. Linkages between aerosol pollution and planetary boundary layer structure in China. Science of the Total Environment 650, 288-296 (2019).

11	Fedorovich, E., Kaiser, R., Rau, M. & Plate, E. Wind tunnel study of turbulent flow structure in the convective boundary layer capped by a temperature inversion. Journal of Atmospheric Sciences 53, 1273-1289 (1996).

12	Miao, Y. et al. Impacts of synoptic condition and planetary boundary layer structure on the trans-boundary aerosol transport from Beijing-Tianjin-Hebei region to northeast China. Atmospheric Environment 181, 1-11 (2018).

13	Luan, T., Guo, X., Guo, L. & Zhang, T. Quantifying the relationship between PM 2.5 concentration, visibility and planetary boundary layer height for long-lasting haze and fog–haze mixed events in Beijing. Atmospheric Chemistry and Physics 18, 203-225 (2018).

14	Han, S. et al. Boundary layer structure and scavenging effect during a typical winter haze-fog episode in a core city of BTH region, China. Atmospheric Environment 179, 187-200 (2018).

15	Miao, Y. et al. Interaction between planetary boundary layer and PM 2.5 pollution in megacities in China: A Review. Current Pollution Reports 5, 261-271 (2019).

16	Li, X. et al. Impact of planetary boundary layer structure on the formation and evolution of air-pollution episodes in Shenyang, Northeast China. Atmospheric Environment 214, 116850 (2019).

17	Cohn, S. A. & Angevine, W. M. Boundary Layer Height and Entrainment Zone Thickness Measured by Lidars and Wind-Profiling Radars. Journal of Applied Meteorology 39, 1233-1247 (2000).

18	Su, T., Li, Z. & Kahn, R. Relationships between the planetary boundary layer height and surface pollutants derived from lidar observations over China: regional pattern and influencing factors. Atmos. Chem. Phys. 18, 15921-15935 (2018).

19	Wang, C. et al. Relationship analysis of PM 2.5 and boundary layer height using an aerosol and turbulence detection lidar. Atmospheric Measurement Techniques 12, 3303-3315 (2019).

20	Petäjä, T. et al. Enhanced air pollution via aerosol-boundary layer feedback in China. Scientific Reports 6, 18998 (2016).

21	Yang, Y. et al. Long‐term trends of persistent synoptic circulation events in planetary boundary layer and their relationships with haze pollution in winter half year over eastern China. Journal of Geophysical Research: Atmospheres 123, 10-991 (2018).

22	Seidel, D. J., Ao, C. O. & Li, K. Estimating climatological planetary boundary layer heights from radiosonde observations: Comparison of methods and uncertainty analysis. Journal of Geophysical Research: Atmospheres 115 (2010).

23	Sawyer, V. & Li, Z. Detection, variations and intercomparison of the planetary boundary layer depth from radiosonde, lidar and infrared spectrometer. Atmospheric Environment 79, 518-528 (2013).

24	Liu, S. & Liang, X.-Z. Observed diurnal cycle climatology of planetary boundary layer height. Journal of Climate 23, 5790-5809 (2010).

25	Seibert, P. et al. Review and intercomparison of operational methods for the determination of the mixing height. Atmospheric Environment 34, 1001-1027 (2000).
26	Stull, R. B. An introduction to boundary layer meteorology. Vol. 13 (Springer Science & Business Media, 2012).

27	Garratt, J. R. The atmospheric boundary layer. Earth-Science Reviews 37, 89-134 (1994).

28	Hu, X.-M., Nielsen-Gammon, J. W. & Zhang, F. Evaluation of three planetary boundary layer schemes in the WRF model. Journal of Applied Meteorology and Climatology 49, 1831-1844 (2010).

29	Deardorff, J. W. Parameterization of the planetary boundary layer for use in general circulation models. Monthly Weather Review 100, 93-106 (1972).

30	Lou, M. et al. On the Relationship Between Aerosol and Boundary Layer Height in Summer in China Under Different Thermodynamic Conditions. Earth and Space Science 6, 887-901 (2019).

31	Bretherton, C. S. et al. Cloud, aerosol, and boundary layer structure across the northeast Pacific stratocumulus–cumulus transition as observed during CSET. Monthly Weather Review 147, 2083-2103 (2019).

32	Zhang, W. et al. On the summertime planetary boundary layer with different thermodynamic stability in China: A radiosonde perspective. Journal of Climate 31, 1451-1465 (2018).

33	Hogan, R. J., Grant, A. L. M., Illingworth, A. J., Pearson, G. N. & O'Connor, E. J. Vertical velocity variance and skewness in clear and cloud-topped boundary layers as revealed by Doppler lidar. Quarterly Journal of the Royal Meteorological Society 135, 635-643 (2009).

34	Guo, J. et al. The climatology of planetary boundary layer height in China derived from radiosonde and reanalysis data. Atmos. Chem. Phys. 16, 13309-13319 (2016).

35	Liu, D., Yang, J., Niu, S. & Li, Z. On the evolution and structure of a radiation fog event in Nanjing. Advances in Atmospheric Sciences 28, 223-237.

36	Li, Z. et al. Aerosol and boundary-layer interactions and impact on air quality. National Science Review 4, 810-833 (2017).

37	Radke, L. F., Hobbs, P. V. & Eltgroth, M. W. Scavenging of aerosol particles by precipitation. Journal of Applied Meteorology and Climatology 19, 715-722 (1980).

38	Li, H. et al. Evaluation of retrieval methods of daytime convective boundary layer height based on lidar data. Journal of Geophysical Research: Atmospheres 122, 4578-4593 (2017).

39	Baars, H., Ansmann, A., Engelmann, R. & Althausen, D. Continuous monitoring of the boundary-layer top with lidar. Atmospheric Chemistry and Physics 8, 7281-7296 (2008).

40	Huang, L., Jiang, J. H., Tackett, J. L., Su, H. & Fu, R. Seasonal and diurnal variations of aerosol extinction profile and type distribution from CALIPSO 5-year observations. Journal of Geophysical Research: Atmospheres 118, 4572-4596 (2013).

41	Feng, L. et al. Identify the contribution of elevated industrial plume to ground air quality by optical and machine learning methods. Environmental Research Communications (2020).

42	Gross, K. C., Bradley, K. C. & Perram, G. P. Remote Identification and Quantification of Industrial Smokestack Effluents via Imaging Fourier-Transform Spectroscopy. Environmental Science & Technology 44, 9390-9397 (2010).

43	Shi, E., Li, Q., Gu, D. & Zhao, Z. Weather radar echo extrapolation method based on convolutional neural networks. Journal of Computer Applications 38, 661-665 (2018).

44	Shi, X. et al. Convolutional LSTM network: A machine learning approach for precipitation nowcasting. Advances in neural information processing systems 2015, 802-810 (2015).

45	Reichstein, M. et al. Deep learning and process 
understanding for data-driven Earth system science. Nature 566, 195-204 (2019).

46	Van der Meer, F. Remote-sensing image analysis and geostatistics. International Journal of Remote Sensing 33, 5644-5676 (2012).

47	Asrar, G. & Asra, G. Theory and applications of optical remote sensing.  (1989).

48	Seidel, D. J. et al. Climatology of the planetary boundary layer over the continental United States and Europe. Journal of Geophysical Research: Atmospheres 117 (2012).

49	Myles, A. J., Feudale, R. N., Liu, Y., Woody, N. A. & Brown, S. D. An introduction to decision tree modeling. Journal of Chemometrics: A Journal of the Chemometrics Society 18, 275-285 (2004).

50	Gardner, M. W. & Dorling, S. R. Artificial neural networks (the multilayer perceptron)—a review of applications in the atmospheric sciences. Atmospheric environment 32, 2627-2636 (1998).

51	Glymour, C., Zhang, K. & Spirtes, P. Review of causal discovery methods based on graphical models. Frontiers in genetics 10, 524 (2019).

52	Pearl, J., Glymour, M. & Jewell, N. P. Causal inference in statistics: A primer.  (John Wiley & Sons, 2016).

53	Sharma, A. & Kiciman, E. DoWhy: An End-to-End Library for Causal Inference. arXiv preprint arXiv:2011.04216 (2020).
54	Pearl, J. Causal diagrams for empirical research. Biometrika 82, 669-688 (1995).

55	Rubin, D. B. Causal inference using potential outcomes: Design, modeling, decisions. Journal of the American Statistical Association 100, 322-331 (2005).

56	Beljaars, A. The parametrization of the planetary boundary layer. ECMWF Meteorological Training Course Lecture Series, 1-57 (1992).

57	Zhang, Y., Fan, J., Chen, X., Ashkenazy, Y. & Havlin, S. Significant Impact of Rossby Waves on Air Pollution Detected by Network Analysis. Geophysical Research Letters 46, 12476-12485 (2019).

58	Feng, L., Yu, Y., Gao, H. & Yao, X. Surface water formation on the natural surface under supersaturation: from local water balance to air pollutant deposition. Air Quality, Atmosphere & Health (2020).

59	Fowler, D. et al. Atmospheric composition change: ecosystems–atmosphere interactions. Atmospheric Environment 43, 5193-5267 (2009).

60	Pearl, J. Causal inference. Causality: Objectives and Assessment, 39-58 (2010).


