import csv
import numpy as np

with open('ud1.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    
data1 = csv.reader(open('ud1.csv', 'r').readlines()[1:-1], delimiter=' ')  
data2 = csv.reader(open('ud1.csv', 'r').readlines()[5: ], delimiter=' ') 

Ldata = list(zip(*data1))
VC = list(zip(*data2))

print(VC)

#getting the number of maximum glare sources
glare_source = Ldata[0]
glare_source_max = glare_source[-1]
print(glare_source_max)


#if no glare source is to be found, some valiues as listed below should be set to their minimum
if glare_source_max == 0:
     
   ls = list(Ldata[5])
   Omega = Ldata[6]
   PIndex = Ldata[7]
   E_vert = Ldata[10]
   E_dir = Ldata[11]
   Lt = Ldata[9]
#LsMax=max(max(Ls));
   xdir = 0
   ydir = 0
   zdir = 0
   GlareVec1=[xdir,ydir,zdir]

   DGP=VC[1]
   La=VC[2]
   La = Ldata[7] 
   Ev=VC[3]
   LB=VC[4]
   EvDir=VC[5]
   DGI=0
   UGR=0
   UGP=0
   VCP=100
   CGI=0  
   DGPcontrast=0
                 
elif glare_source_max != 0: 
   Ls = (Ldata[5])
   Omega = (Ldata[6])
   pIndex = (Ldata[7])
   E_vert = Ldata[10]
   E_dir = Ldata[11]
   Lt = Ldata[9]
#LsMax=max(max(Ls));
   xdir = Ldata[14] 
   ydir = Ldata[15] 
   #zdir = Ldata[16] 
   GlareVec2=[xdir,ydir]

   DGP=VC[1]
   La=VC[2]
   La = Ldata[7] 
   Ev=VC[3]
   LB=VC[4]
   EvDir=VC[5]
   DGI=0
   UGR=0
   UGP=0
   VCP=100
   CGI=0  
   DGPcontrast=0

gi=list(Ls + Omega)



