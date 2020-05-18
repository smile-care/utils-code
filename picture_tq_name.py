# import os
# dir1='G:/研究生文件夹（深大）/深度学习/PyTorch-YOLOv3-master/data/images'#图片文件存放地址
# txt1 = 'G:/研究生文件夹（深大）/深度学习/PyTorch-YOLOv3-master/picture_tq_name/name.txt'#图片文件名存放txt文件地址
# f1 = open(txt1,'a')#打开文件流
# for filename in os.listdir(dir1):
#     f1.write('G:/研究生文件夹（深大）/深度学习/PyTorch-YOLOv3-master/data/images' + str(filename))#只保存名字，去除后缀.jpg
#     f1.write("\n")#换行
# f1.close()#关闭文件流


import sys
import os 
data_dir = "G:\PyTorch-YOLOv3-master\data\images"
file_list = [] 
write_file_name = r'G:\PyTorch-YOLOv3-master\picture_tq_name\name.txt'
write_file = open(write_file_name, "w")
tt=os.listdir(data_dir)
for file in tt:
    if file.endswith(".jpg"):
        write_name = file
        file_list.append(write_name)
# print(file_list)
for current_line in range(len(file_list)): 
     write_file.write('G:\pytorch-yolov3\PyTorch-YOLOv3-master\data/./images/' + str(file_list[current_line] + '\n'))
write_file.close()
 