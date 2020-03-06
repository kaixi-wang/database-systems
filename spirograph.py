import numpy as np
import matplotlib.pyplot as plt

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

#sgm123=34.021190, -118.289067
center_lat=-118.289067
center_lng=34.021190

#test print
lats=getlat(center_lat,x)
lngs=getlng(center_lng,y)
plt.plot(lats,lngs)
plt.show()


#print to file
coordinates=getLatLng(center_lat,center_lng,x,y)
fpath='output_filepath/'
with open(fpath+'spiro_coordinates_small.txt', 'a') as f:
    for c in coordinates:
        f.write(c[0])

