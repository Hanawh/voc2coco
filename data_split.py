# This script split voc annatation(xml) to following directory according to .txt in YOUR_ROOT 
# test_xml, trainval_xml, val_xml, *train_xml, test_data, trainval_data, val_data, *train_data
# * means may not have this directory
# Please enter the absolute path of data root
# eg. sudo python data_split.py --root /home/wh/VOC2007 --out_dirs /home/data
import argparse
import os
from os import path as osp
import shutil

def get_args_parser():
    parser = argparse.ArgumentParser('split', add_help=False)
    parser.add_argument('--root', default=None, type=str)
    parser.add_argument('--out_dirs', default=None, type=str)
    return parser

def data_split(root, out_dirs):
    anno_dir = osp.join(root, 'Annotations')
    img_dir = osp.join(root, 'JPEGImages')
    txt_dir = osp.join(root, 'ImageSets/Main')
    txts = [osp.join(txt_dir, t) for t in os.listdir(txt_dir)]
    for txt in txts:
        typefile = txt.strip().split('/')[-1].split('.')[0]
        xml_makedir = osp.join(out_dirs, typefile+'_xml')
        img_makedir = osp.join(out_dirs, typefile+'_data')
        if not osp.exists(xml_makedir):
            os.makedirs(xml_makedir)
        if not osp.exists(img_makedir):
            os.makedirs(img_makedir)
        
        f = open(txt)
        for line in f:
            img = osp.join(img_dir, line.strip()+'.jpg')
            xml = osp.join(anno_dir, line.strip()+'.xml')

            img_path = osp.join(img_makedir, line.strip()+'.jpg')
            xml_path = osp.join(xml_makedir, line.strip()+'.xml')
            
            shutil.copyfile(img, img_path)
            shutil.copyfile(xml, xml_path)



if __name__ == '__main__':
    parser = argparse.ArgumentParser('VOC-split', parents=[get_args_parser()])
    args = parser.parse_args()
    if args.root is not None and args.out_dirs is not None:
        data_split(args.root, args.out_dirs)
    else:
        print("Please input a valid root!")






