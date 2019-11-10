# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 20:59:18 2019

@author: yavuz
"""

import random
import numpy as np


class NodeGenerator:
    def __init__(self,path):
        x=[]
        y=[]
        p=[0]
        p,x,y=self.lokasyon_oku(p,x,y,path)
        self.width = x
        self.height = y
        self.nodesNumber = p

    def generate(self):
        xs = self.width
        ys = self.height
        return np.column_stack((xs, ys))

    def lokasyon_oku(self,p,X,Y,path):
        sehirler=[]
        with open(path) as b:
            locations = b.read()
            for location in locations.split("NODE_COORD_SECTION")[1:]:
                sehirler=(location.splitlines()[1:-1])
        p=[0]
        X=[]
        Y=[]
        for i in sehirler:
            p.append(int(i.split(" ")[0]))
            X.append(float(i.split(" ")[1]))
            Y.append(float(i.split(" ")[2]))
        return p[:-1],X,Y
