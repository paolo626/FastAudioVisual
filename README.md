# FastAudioVisual   ![license](https://img.shields.io/badge/License-MIT-brightgreen.svg)




Our project is developed [here](https://blog.csdn.net/liupeng19970119/article/details/111881802).  The goal finish time is March 01, 2021 
## What is FastAudioVisual?
FastAudioVisual is a tool that allows us to develop and analyse research in the audiovisual domain. The framework of this model as follow:
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201230114511204.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpdXBlbmcxOTk3MDExOQ==,size_16,color_FFFFFF,t_70)

As we can see that this project has five parts.  Here is the detail of each part.

1. DataRegular: It causes many questions due to different file structure in  some research. In this work,  we develop a series of functions to make your database regular with the next step. All of these funfunctions arested and regular by RAVDESS which is a big database in multimodal emotion recognition.
2. FeatureExtract:   





























# Develop and Iteration

























## 3. 功能内容与具体
## 4. 后期维护与迭代

## Installation
You can install, upgrade, uninstall count-line with these commands(without $):
```
$ pip install count-line
$ pip install --upgrade count-line
$ pip unstall count-line
```

## Help
```
usage: line.py [-h] [-s SUFFIX | -f FILTER] [-d]

count the amount of lines and files under the current directory

optional arguments:
  -h, --help            show this help message and exit
  -s SUFFIX, --suffix SUFFIX
                        count by suffix file name, format: .suffix1.suffix2...
                        e.g: .cpp.py (without space)
  -f FILTER, --filter FILTER
                        count without filter name, format: .suffix1.suffix2...
                        e.g: .cpp.py (without space)
  -d, --detail          show detail results
```

## Examples
1. Count all files under the current directory:
```
$ line
Search in /Users/macbook/Desktop/Examples1/
file count: 4
line count: 373
```
2. Count all files under the current directory with detail results:
```
$ line -d
Search in /Users/macbook/Desktop/Examples2/

		========================================
		文件后缀名	文件数		总行数
		

		   .py		5		397
		

		   .cpp		240		11346
		

		总文件数: 245	总行数: 11743
		========================================
		

```
3. Count specified files under the current directory, using -s to pass suffix as parameters, if there are more than one parameter, don't have space, for example, count cpp files and python files:
```
$ line -s .cpp.py
Search in /Users/macbook/Desktop/Examples3/
file count: 3
line count: 243
$ line -s .cpp.py -d
Search in /Users/macbook/Desktop/Examples3/

		========================================
		文件后缀名	文件数		总行数
		

		   .py		5		397
		

		   .cpp		240		11346
		

		总文件数: 245	总行数: 11743
		========================================
		
```
4. Count files under the current directory with filter:
```
$ line -f .py -d
Search in /Users/macbook/Desktop/Examples4/

		========================================
		文件后缀名	文件数		总行数
		

		   .cpp		240		11346
		

		总文件数: 240	总行数: 11528
		========================================
$ line -d
Search in /Users/macbook/Desktop/Examples4/

		========================================
		文件后缀名	文件数		总行数
		

		   .py		5		397
		

		   .cpp		240		11346
		

		总文件数: 245	总行数: 11743
		========================================

		
```

