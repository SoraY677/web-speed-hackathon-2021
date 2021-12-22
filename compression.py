'''
メディア関係の圧縮スクリプト
'''

import os
import sys
import glob

from PIL import Image

_arg = sys.argv[1]
_file_list = ''

def switch_compression():
	global _arg, _file_list
	print(_arg)
	if _arg == 'image':
		_file_list = glob.glob("./public/images/*")
		for file_path in _file_list:
			compress_image(file_path)
	elif _arg == 'profile':
		_file_list = glob.glob("./public/images/profiles/*")
		for file_path in _file_list:
			compress_profile(file_path)
	else:
		print('err:引数が必要です。')


def compress_image(filepath):
	print(filepath)
	if os.path.isfile(filepath):
		img = Image.open(filepath)
		c_width = 500
		c_height = int(c_width / img.width * img.height)
		img_resize = img.resize((c_width, c_height))
		img_resize.save(filepath)

def compress_profile(filepath):
	print(filepath)
	if os.path.isfile(filepath):
		img = Image.open(filepath)
		c_width = 62
		c_height = int(c_width  / img.width * img.height)
		img_resize = img.resize((c_width, c_height))
		img_resize.save(filepath)


switch_compression()



img = Image.open