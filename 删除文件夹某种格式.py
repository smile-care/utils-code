import os
def del_files(path):
  for root , dirs, files in os.walk(path):
    for name in files:
      if name.endswith(".xml"):   #指定要删除的格式，这里是jpg 可以换成其他格式
        os.remove(os.path.join(root, name))
        print ("Delete File: " + os.path.join(root, name))
# test
if __name__ == "__main__":
  path = 'G:\PyTorch-YOLOv3-master\data\yyyyy'
  del_files(path)