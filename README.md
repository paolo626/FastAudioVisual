# FastAudioVisual   ![license](https://img.shields.io/badge/License-MIT-brightgreen.svg)




Our project is developed [here](https://blog.csdn.net/liupeng19970119/article/details/111881802).  The goal finish time is August 01, 2021 
## What is FastAudioVisual?
FastAudioVisual is a tool that allows us to develop and analyse research in the audiovisual domain. The framework of this model as follow:
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230114511204.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpdXBlbmcxOTk3MDExOQ==,size_16,color_FFFFFF,t_70)

As we can see that this project has five parts.  Here is the detail of each part.

1. DataRegular: It causes many questions due to different file structure in  some research. In this work,  we develop a series of functions to make your database regular with the next step. All of these funfunctions arested and regular by RAVDESS which is a big database in multimodal emotion recognition.

2. FeatureExtract: Features extraction is important for  model study.  There are many features can be extracted for input. For audio, MFCC, FBank, crossing-zero rate and soon on can be used.  For visual, gray, RGB, optical flow diagram can be used. In this part, we will build some API to extract these features.

3. SampleModel: With the develop of hardwares, deep learning has got siginificant improvement in every area. Many area has been regular by deep learning. Therefore, we collect some classical model  for  basic research. This part will make you have a enough evaluate and experiment. (In the beginning, I struggled to choose Pytorch and fastai).

4. ModelDesign: In this part, we focus on audiovisual fusion method and model design for audiovisual other domain( including loss  , framework, other trick.).  It collect some research work and code. Also, we can replace simplemodel into this part. Making the result is better.  

5. Analysis: Based on above parts, we will using some tool to analysis the result of this experiment. Such as confusion matrix, CAM, feature distrbution. 
6. Test:  Some demo for using this project. 
7. Others: It includes some paper or blog for this area. 


In general, All of these design is for developing your audiovisual research fastly by this ttool!


