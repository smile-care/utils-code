import os
import xml.etree.ElementTree as ET
from PIL import Image
import numpy as np

img_path = 'G:\Deep_Learning\kaggle\global-wheat-detection\dataset/train/'                   #原图.jpg文件的路径
labels_path = 'G:\Deep_Learning\kaggle\global-wheat-detection\demo\labels/'                    #labels中.txt文件的路径
annotations_path = 'G:\Deep_Learning\kaggle\global-wheat-detection\demo/Annotations/'          #生成的xml文件需要保存的路径
labels = os.listdir(labels_path)
# clsnames_path = '/home/anngic/label/bdd100k_labels/BD100K_10.names'     #names文件的路径   
# with open(clsnames_path,'r') as f:
#     classes = f.readlines()
#     classes = [cls.strip('\n') for cls in classes]

classes = ['maitou']
def write_xml(imgname,filepath,labeldicts):                     #参数imagename是图片名（无后缀）
    root = ET.Element('Annotation')                             #创建Annotation根节点
    ET.SubElement(root, 'filename').text = str(imgname)         #创建filename子节点（无后缀）
    sizes = ET.SubElement(root,'size')                          #创建size子节点            
    ET.SubElement(sizes, 'width').text = '1024'                 #没带脑子直接写了原图片的尺寸......
    ET.SubElement(sizes, 'height').text = '1024'
    ET.SubElement(sizes, 'depth').text = '3'                    #图片的通道数：img.shape[2]
    for labeldict in labeldicts:
        objects = ET.SubElement(root, 'object')                 #创建object子节点
        ET.SubElement(objects, 'name').text = labeldict['name']        #BDD100K_10.names文件中  
                                                                       #的类别名
        ET.SubElement(objects, 'pose').text = 'Unspecified'
        ET.SubElement(objects, 'truncated').text = '0'
        ET.SubElement(objects, 'difficult').text = '0'
        bndbox = ET.SubElement(objects,'bndbox')
        ET.SubElement(bndbox, 'xmin').text = str(int(labeldict['xmin']))
        ET.SubElement(bndbox, 'ymin').text = str(int(labeldict['ymin']))
        ET.SubElement(bndbox, 'xmax').text = str(int(labeldict['xmax']))
        ET.SubElement(bndbox, 'ymax').text = str(int(labeldict['ymax']))
    tree = ET.ElementTree(root)
    tree.write(filepath, encoding='utf-8')

i = 0
for label in labels:                                           #批量读.txt文件
    with open(labels_path + label, 'r') as f:
        img_id = os.path.splitext(label)[0]
        contents = f.readlines()
        labeldicts = []
        for content in contents:
            img = np.array(Image.open(img_path+label.strip('.txt') + '.jpg'))
            sh,sw = img.shape[0],img.shape[1]                  #img.shape[0]是图片的高度720
                                                               #img.shape[1]是图片的宽度720
            content = content.strip('\n').split()
            x=float(content[1])*sw
            y=float(content[2])*sh
            w=float(content[3])*sw
            h=float(content[4])*sh
            new_dict = {'name': classes[int(content[0])],
                        'difficult': '0',
                        'xmin': x+1-w/2,                      #坐标转换公式看另一篇文章....
                        'ymin': y+1-h/2,
                        'xmax': x+1+w/2,
                        'ymax': y+1+h/2
                        }
            labeldicts.append(new_dict)
        write_xml(img_id, annotations_path + label.strip('.txt') + '.xml', labeldicts)
        print(str(label.strip('.txt') + '.xml')+' 转换成功')
        i = i + 1
print('共',i,'次')