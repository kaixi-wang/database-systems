import numpy as np
import matplotlib.pyplot as plt


"""
Draws a spirograph over a map that is centered at the given latitude and longitude
"""
#x(t) = (R+r)*cos((r/R)*t) - a*cos((1+r/R)*t)
#y(t) = (R+r)*sin((r/R)*t) - a*sin((1+r/R)*t)

#Using the above equations, loop through t from 0.00 to n*Pi (eg. 2*Pi;
#  note that 'n' might need to be more than 2, for the curve to close on itself;
# and, t is in radians, not degrees), in steps of 0.01.
# That will give you the sequence of (x,y) points that make up the Spiro curve
R=8
r=1
a=4
n=16
def getX(R,r,a,n):
    xvals=[]
    for t in np.arange(0, n*np.pi,.01):
        x=(R+r)*np.cos((r/R)*t) - a*np.cos((1+r/R)*t)
        xvals.append(x)
    return xvals
def getY(R,r,a,n):
    yvals=[]
    for t in np.arange(0, n*np.pi,.01):
        y=(R+r)*np.sin((r/R)*t) - a*np.sin((1+r/R)*t)
        yvals.append(y)
    return yvals

def plotXY(x,y):
    x = getX(R, r, a, n)
    y = getY(R, r, a, n)
    plt.plot(x, y)
    plt.show()

def getLatLng(center_lat,center_lng,x,y):
    latlng=[]
    for i in range(len(x)):
        lat=x[i]/3600+center_lat
        lng=y[i]/3600+center_lng
        txt=' '*10+'{},{},0\n'.format(lat,lng)
        latlng.append([txt])
    return latlng

def getlat(center_lat,x):
    return [val/3600+center_lat for val in x]
def getlng(center_lng,y):
    return [val/3600+center_lng for val in y]

def main():
    import sys
    import os
    if len(sys.argv)<3:
        print("Incorrect number of arguments. Please call as \n python -m spirograph.py <lat> <lon> <optional: output_dir>" )
    else:
        center_lat=float(sys.argv[1])
        center_lng=float(sys.argv[2])

        #test print
        lats=getlat(center_lat,x)
        lngs=getlng(center_lng,y)
        plt.plot(lats,lngs)
        plt.show()

        #print to file
        coordinates=getLatLng(center_lat,center_lng,x,y)
        fpath='output_filepath/'
        if len(sys.argv)>3:
            fpath=sys.argv[3]
        output_filename=os.path.join(fpath, 'spiro_coordinates.txt')
        with open(output_filename, 'a') as f:
            print('Writing coordinates to {}'.format(output_filename))
            for c in coordinates:
                f.write(c[0])


if __name__ == "__main__":
    main()