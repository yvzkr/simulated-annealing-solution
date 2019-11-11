# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:42:00 2019

@author: yavuz
"""
from Read_lokasyon import NodeRead as lokasyonOku
from simulated_algo import SimulatedAnnealing

import statistics

def calculateStatic(data):
    print("Best:",min(data))
    print("Worst",max(data))
    print("Mean of the ",len(data), "results", statistics.mean(data))
    print("Median of the ",len(data),"results", statistics.median(data))
    


def main():
    
    '''param'''
    temp = 100000
    stopping_temp = 0.001
    alpha = 0.9999
    stopping_iter = 100000

    """Read location"""
    cities = lokasyonOku("dataset/krE100.txt").generate()
    
    results=[]
    for i in range(10):
        SimAnni = SimulatedAnnealing(cities, temp, alpha, stopping_temp, stopping_iter)
        SimAnni.anneal()
        results.append(SimAnni.min_weight)
        '''animate'''
        SimAnni.animateSolutions()
    
        '''show the improvement over time'''
        SimAnni.plotLearning()
        
        
    calculateStatic(results)



if __name__ == "__main__":
    main()
