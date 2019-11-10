# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:42:00 2019

@author: yavuz
"""
from Read_lokasyon import NodeRead as lokasyonOku
from simulated_algo import SimulatedAnnealing


def main():
    '''parametreler'''
    temp = 1000
    stopping_temp = 0.00000001
    alpha = 0.9995
    stopping_iter = 10000000

    """Read location"""
    cities = lokasyonOku("dataset/krB100.tsp.txt").generate()
    
    SimAnni = SimulatedAnnealing(cities, temp, alpha, stopping_temp, stopping_iter)
    SimAnni.anneal()
    '''animate'''
    SimAnni.animateSolutions()

    '''show the improvement over time'''
    SimAnni.plotLearning()


if __name__ == "__main__":
    main()
