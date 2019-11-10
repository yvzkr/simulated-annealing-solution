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
    stopping_T = 0.001
    colling_faktor = 0.99
    stopping_iter = 1000

    """Read location"""
    cities = lokasyonOku("dataset/bier127.txt").generate()
    
    SimAnni = SimulatedAnnealing(cities, T, colling_faktor, stopping_T, stopping_iter)



if __name__ == "__main__":
    main()
