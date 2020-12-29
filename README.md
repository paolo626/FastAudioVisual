# FastAudioVisual 

## Usage
A cross-platform command line tool to count the amount of lines and files under current directory.

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

