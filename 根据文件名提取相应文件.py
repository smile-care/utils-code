# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 21:03:44 2018
@author: Fsl
"""
import shutil
#这个库复制文件比较省事
 
def objFileName():
    '''
    生成文件名列表
    :return:
    '''
    local_file_name_list = r'G:\研究生文件夹（深大）\机器学习\磁瓦\磁瓦(标注数据)\dataset\name.txt'
    #指定名单
    obj_name_list = []
    for i in open(local_file_name_list,'r'):
        obj_name_list.append(i.replace('\n',''))
    return obj_name_list
 
def copy_img():
    '''
    复制、重命名、粘贴文件
    :return:
    '''
    local_img_name=r'G:\研究生文件夹（深大）\机器学习\磁瓦\磁瓦(标注数据)\dataset\JPEGImages'
    #指定要复制的图片路径
    path = r'G:\研究生文件夹（深大）\机器学习\磁瓦\磁瓦(标注数据)\dataset\2'
    #指定存放图片的目录
    for i in objFileName():
        new_obj_name = i+'.jpg'
        shutil.copy(local_img_name+'/'+new_obj_name,path+'/'+new_obj_name)
 
if __name__ == '__main__':
    copy_img()