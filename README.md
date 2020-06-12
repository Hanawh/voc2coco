# voc2coco
 voc to coco data set for object detection

# First step

Run `data_split.py` to split voc annatation(xml) and images to following directory according to .txt in YOUR_ROOT

```python
sudo python data_split.py --root VOC_ROOT --out_dirs YOUR_ROOT
# eg. sudo python data_split.py --root /home/wh/VOC2007 --out_dirs /home/wh/data
```

Then you will find several files `*_xml, *_data etc` in YOUR_ROOT. We will base on `*_xml` to creat json file. 

#  Second step
```python
sudo python xml2json.py YOUR_ROOT/train_xml YOUR_ROOT/train.json
sudo python xml2json.py YOUR_ROOT/val_xml YOUR_ROOT/val.json
sudo python xml2json.py YOUR_ROOT/test_xml YOUR_ROOT/test.json
```
