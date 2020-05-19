import pandas as pd
import os
import numpy as np
import csv
import re
from kmeans import kmeans, avg_iou

csv_path = r'G:\Deep_Learning\kaggle\global-wheat-detection\dataset\train.csv'
CLUSTERS = 9

df = pd.read_csv(csv_path)
def process_bbox(df):
    ids = []
    values = []
    imd = np.unique(df['image_id'])
    df['bbox'] = df['bbox'].apply(lambda x: eval(x))
    # for image_id in os.listdir(train_dir):
    #     image_id = image_id.split('.')[0]
    #     if image_id not in imd :
    #         ids.append(image_id)
    #         values.append(str([-1,-1,-1,-1]))
    # new_df = {'image_id':ids, 'bbox':values}
    # new_df = pd.DataFrame(new_df)
    df = df[['image_id','bbox']]
    # df.append(new_df)
    df = df.reset_index(drop=True)
    df['x'] = df['bbox'].apply(lambda x: x[0])
    df['y'] = df['bbox'].apply(lambda x: x[1])
    df['w'] = df['bbox'].apply(lambda x: x[2])
    df['h'] = df['bbox'].apply(lambda x: x[3])

    df.drop(columns=['bbox'],inplace=True)
    return df

df_ = process_bbox(df)
df_idx = df_.set_index("image_id")
bbox = df_idx.reset_index(drop=True)
bbox_arr = bbox.to_numpy()
w_h = bbox_arr[:,(2,3)]
# anchors = []
# for b in w_h[:5]:
#     anchors.append(b)

data = np.array(w_h)
out = kmeans(data, k=CLUSTERS)
print("Accuracy: {:.2f}%".format(avg_iou(data, out) * 100))
print("Boxes:\n {}".format(out))

ratios = np.around(out[:, 0] / out[:, 1], decimals=2).tolist()
print("Ratios:\n {}".format(sorted(ratios)))