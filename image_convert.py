from PIL import Image
import os 
# http://www.sharejs.com

#该代码片段来自于: http://www.sharejs.com/codes/python/8729

for file in os.listdir('orig'):
	if file.endswith('.png'):
		image_file = Image.open(os.path.join('orig',file)) # open colour image
		image_file = image_file.convert('L') # convert image to black and white
		image_file.save(os.path.join('result', file[:-4] + '_grey.png')) #[:-4]將.png這四個字不寫入


