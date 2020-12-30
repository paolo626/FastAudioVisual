#!/usr/bin/env python
import os
import glob
import argparse
import fnmatch
from collections import defaultdict

__version__ = '0.1.2'
__author__ = 'hj24'

class LineCounter(object):

	def __init__(self, dir):
		# current location
		self.current_dir = dir

		# Core counters for the number of lines and files 
		self.line_count = 0
		self.file_count = 0

		# sets to record the filter files suffix or specific files suffix
		self.select_suffix = set()
		self.filter_suffix = set()

		# dict for detail results, default count = 0
		self.final_files_dict = defaultdict(int)
		self.files_lines_dict = defaultdict(int)

		# set for files' name
		self.final_files = set()

	def __repr__(self):

		info = '''
		author: \t{}
		count-line version: \t{}
		'''
		return info.format(__version__, __author__)

	def filter_mod(self, filter_list):
		self.filter_suffix = {f for f in filter_list}

		self.find_files(self.current_dir, mod='filter')

		for file in self.final_files:
			self.analyze_files(file)

	def specific_mod(self, suffix_list):

		self.select_suffix = {s for s in suffix_list}
		
		self.find_files(self.current_dir, mod='specific')
		
		for file in self.final_files:
			self.analyze_files(file)

	def normal_mod(self):

		self.find_files(self.current_dir, mod='normal')

		for file in self.final_files:
			self.analyze_files(file)

	def find_files(self, path, mod):
		root = path
		
		files_or_folders = os.listdir(path)

		for item in files_or_folders:
			# ignore hidden files
			if item[0] != '.':		
				if os.path.isdir(root + os.sep + item):
					sub_path = root + os.sep + item
					self.find_files(sub_path, mod=mod)

				elif os.path.isfile(root + os.sep + item):
					if mod == 'normal':
						self.add_file(root + os.sep, item)

					elif mod == 'filter':
						if self.filter_conditions(root + os.sep + item):
							self.add_file(root + os.sep, item)

					elif mod == 'specific':
						if self.specific_conditions(root + os.sep + item):
							self.add_file(root + os.sep, item)

	def filter_conditions(self, path):
		for f in self.filter_suffix:
			if path.endswith(f):
				return False
		return True

	def specific_conditions(self, path):
		for s in self.select_suffix:
			if path.endswith(s):
				return True
		return False

	def add_file(self, path, name):
		self.final_files.add(path + name)
		file_name = name.split('.')[-1]
		self.final_files_dict[file_name] += 1

	# analyze single file: update self.line_count, self.file_count
	def analyze_files(self, file):
		#if file not in self.filter_suffix:
		file_line = self.count_lines(file)

		file_name = file.split('.')[-1]
		self.files_lines_dict[file_name] += file_line

		self.line_count += file_line
		self.file_count += 1

	# count lines of single file
	def count_lines(self, file):
		cnt = 0
		for file_line in open(file, 'rb'):
			cnt += 1
		return cnt
			
	def show_results(self):
		print(f'file count: {self.file_count}')
		print(f'line count: {self.line_count}')

	def show_detail_results(self):
		info = '''
		=====================================================
		\t文件后缀名\t文件数\t\t总行数
		'''

		data = '''
		   \t.{}\t\t{}\t\t{}
		'''

		end = '''
		\t总文件数: {}\t总行数: {}
		=====================================================
		'''

		print(info)

		for (k, v) in self.final_files_dict.items():
			print(data.format(k, v, self.files_lines_dict[k]))

		print(end.format(self.file_count, self.line_count))

def main():
	__usage__ = "count the amount of lines and files under the current directory"
	parser = argparse.ArgumentParser(description=__usage__)

	group = parser.add_mutually_exclusive_group()
	group.add_argument("-s", "--suffix", type=str, 
						help="count by suffix file name, format: .suffix1.suffix2... e.g: .cpp.py (without space)")
	group.add_argument("-f", "--filter", type=str, 
						help="count without filter name, format: .suffix1.suffix2... e.g: .cpp.py (without space)")
	parser.add_argument("-d", "--detail", action="store_true",
						help="show detail results")
	
	args = parser.parse_args()

	current_dir = os.getcwd()
	counter = LineCounter(current_dir)

	print('Search in {}'.format(current_dir + os.sep))

	if args.filter:
		args_list = args.filter.split('.')
		args_list.remove('')
		counter.filter_mod(args_list)
	elif args.suffix:
		args_list = args.suffix.split('.')
		args_list.remove('')
		counter.specific_mod(args_list)
	else:
		counter.normal_mod()

	if args.detail:
		counter.show_detail_results()
	else:
		counter.show_results()
		
if __name__ == '__main__':
	main()