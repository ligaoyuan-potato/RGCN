#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: Potato
@E-mail: li_gaoy@foxmail.com
@Time:   2019/12/12 14:43
@File:   imshow.py 
"""

import cv2
import os


def readfile(root, label_file):
    f = open(label_file, 'r', encoding='utf-8')
    ims, labels = [], []
    for line in f.readlines():
        line = line.strip('\n').strip('\r')
        if line == '':
            continue
        jpg_index = line.find('jpg')
        img_name = line[0:jpg_index + 3]
        label_str = line[jpg_index + 4:]
        img_path = os.path.join(root, img_name)
        ims.append(img_path)
        labels.append(label_str)
    dic = {}
    for i, j in enumerate(ims):
        dic[ims[i]] = labels[i]
    return dic


def draw_corner(img, cors):
    x0, y0, x1, y1, x2, y2, x3, y3 = map(int, cors.split(','))
    v=4
    img[y0:y0+v, x0:x0+v] = (0, 0, 255)
    img[y1:y1+v, x1:x1+v] = (0, 255, 0)
    img[y2:y2+v, x2:x2+v] = (255, 0, 0)
    img[y3:y3+v, x3:x3+v] = (0, 255, 255)
    return img


if __name__ == '__main__':

    path = r'../data/images/'
    label = r'../data/label/val.txt'

    imdict = readfile(path, label)
    for name, label in imdict.items():
        print(name)
        print(label)
        img = cv2.imread(name)
        print(img.shape)
        img = draw_corner(img, label)
        if img.shape[1]>3000:
            size = img.shape
            img = cv2.resize(img, (int(size[1]/3), int(size[0]/3)), cv2.INTER_LINEAR)
        elif img.shape[1]>1800:
            size = img.shape
            img = cv2.resize(img, (int(size[1] / 2), int(size[0] / 2)), cv2.INTER_LINEAR)
        else:
            pass
        cv2.imshow('mubiao', img)
        cv2.waitKey(0)
        # break