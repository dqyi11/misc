import argparse
import os, sys
import numpy as np
import matplotlib.pyplot as plt

if __name__=='__main__':

    parser=argparse.ArgumentParser(description='')
    parser.add_argument('filename',
            type=str,
            help='Filename to load')
    parser.add_argument('-d','--dimension',
            type=int,
            default=6,
            help='Dimension of trajectory')
    args = parser.parse_args()

    with open(args.filename, 'r') as f:
        data = np.loadtxt(f, delimiter=',', skiprows=1)
        #print str(data.shape)

        assert data.shape[1] == 1+args.dimension*2
        dataNum = data.shape[0]

        T = data[:,0]
        #print str(T.shape)

        POS = data[:,1]
        VEL = data[:,2]
        for i in range(1, args.dimension):
            POS = np.vstack((POS, data[:,i*2+1]))
            VEL = np.vstack((VEL, data[:,i*2+2]))

        #print str(POS.shape)
        #print str(VEL.shape)

        f, axarr = plt.subplots(args.dimension, sharex=True)
        twinxs = []
        for i in range(args.dimension):
            axarr[i].plot(T, POS[i,:], '-r')
            axarr[i].set_xlabel('time')
            axarr[i].set_ylabel('POS', color='r')
            axarr[i].tick_params('y', colors='r')
            twinxs.append( axarr[i].twinx() )
            twinxs[i].plot(T, VEL[i,:], '-b')
            twinxs[i].set_ylabel('VEL', color='b')
            twinxs[i].tick_params('y', colors='b')

        f.tight_layout()
        plt.show()

