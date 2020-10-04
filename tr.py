import numpy as np
import matplotlib.pyplot as plt
import math 
import csv
from mpl_toolkits import mplot3d

radius=[1 ,2 ,3]   #radius of concentric spheres [sphere1 ,sphere2 ,sphere3]
centre=[1 ,1 ,1]   #cordinates of centre in concetric spheres [x ,y ,z]
r1=radius[0]
r2=radius[1]
r3=radius[2]
def sphere2cartesian(az, el, r):                 #function to convert data from spherical cordinates to cartesian cordinate system
  rcos_theta = r * np.cos(el)
  x = rcos_theta * np.cos(az)
  y = rcos_theta * np.sin(az)
  z = r * np.sin(el)
  return x+centre[0], y+centre[1], z+centre[2]   #return points on cartesian cordinate system

def writeToFile(cart1, cart2, cart3, r1, r2, r3):  #function to write the X,Y,Z cordinates and radius into CSV file
  fields = ['Number','X', 'Y', 'Z','Radius'] 
  with open('Datapoints.csv', 'w') as f1:
    line= str(fields[0])+','+str(fields[1])+','+str(fields[2])+','+str(fields[3])+','+str(fields[4])
    line=line+"\n"
    f1.write(line)
    for i in range (0,datapoints):
      line = str(i+1)
      line = line+','+str(cart1[0][i])+','+str(cart1[1][i])+','+str(cart1[2][i])+','+str(r1)
      line = line+"\n"
      f1.write(line)
    for j in range (0,datapoints):
      line = str(j+datapoints+1)
      line = line+','+str(cart2[0][j])+','+str(cart2[1][j])+','+str(cart2[2][j])+','+str(r2)
      line=line+"\n"
      f1.write(line)
    for k in range (0,datapoints):  
      line = str(k+2*datapoints+1)
      line = line+','+str(cart3[0][k])+','+str(cart3[1][k])+','+str(cart3[2][k])+','+str(r3)
      line=line+"\n"
      f1.write(line)


np.random.seed(0)
datapoints= 1000

pi=math.pi

#first data set
radius[0]=np.zeros(datapoints, dtype = float)+radius[0]             # assign radius (fixed)
azi1  = np.random.random(np.shape(radius[0])) * 2*pi        #random azimuth   [  0     2pi]
elev1 = (np.random.random( np.shape(radius[0]))* pi)-pi/2    # random elevation [-pi/2  pi/2]

#second data set 
radius[1]=np.zeros(datapoints, dtype = float)+radius[1]           # assign radius (fixed)
azi2  = np.random.random(np.shape(radius[1])) * 2*pi        #random azimuth   [  0     2pi]
elev2 = (np.random.random( np.shape(radius[1]))* pi)-pi/2    # random elevation [-pi/2  pi/2]

#third data set 
radius[2]=np.zeros(datapoints, dtype = float)+radius[2]            # assign radius (fixed)
azi3  = np.random.random(np.shape(radius[2])) * 2*pi        #random azimuth   [  0     2pi]
elev3 = (np.random.random( np.shape(radius[2]))* pi)-pi/2    # random elevation [-pi/2  pi/2]

#convert to cartesian
cart1 = sphere2cartesian(azi1,elev1,radius[0])
cart2 = sphere2cartesian(azi2,elev2,radius[1])
cart3 = sphere2cartesian(azi3,elev3,radius[2])

#plot the data using 3d plot
plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.scatter3D(cart1[0], cart1[1], cart1[2], marker='s',c=cart1[2], cmap='Reds',label='Datapoints on sphere with radius 1')
ax.scatter3D(cart2[0], cart2[1], cart2[2], marker='^',c=cart2[2], cmap='Greens',label='Datapoints on sphere with radius 2')
ax.scatter3D(cart3[0], cart3[1], cart3[2], marker='o',c=cart3[2], cmap='Blues',label='Datapoints on sphere with radius 3')
plt.title('Data generated')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.legend()
plt.show(block=False)
figure = plt.gcf()
figure.set_size_inches(8, 8)
plt.savefig('output.jpg',dpi=200)

writeToFile(cart1,cart2,cart3,r1,r2,r3 )       #write the X,Y,Z cordinates into a CSV file



