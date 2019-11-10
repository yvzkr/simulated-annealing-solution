# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:42:00 2019

@author: yavuz
"""
from Read_lokasyon import NodeRead as lokasyonOku
from simulated_algo import SimulatedAnnealing

def main():
    '''parametreler'''
    T = 100000
    stopping_T = 0.0001
    colling_faktor = 0.9995
    stopping_iter = 10000000

    """Read location"""
    cities = lokasyonOku("dataset/krB100.tsp.txt").generate()
    
    SimAnni = SimulatedAnnealing(cities, T, colling_faktor, stopping_T, stopping_iter)



if __name__ == "__main__":
    main()
