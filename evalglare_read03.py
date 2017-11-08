import pandas as pd
import glob


path = "/Users/Susanne/Desktop/mp/python/pp/"
list_of_files = glob.glob('/Users/Susanne/Desktop/mp/python/pp/*.csv')

myFile = open("evalglare.txt","w")
for file in list_of_files:

    data = pd.read_csv(file, sep='\s+')
    Ldata = data.iloc[ : -1]

    #getting the number of maximum glare sources
    glare = Ldata.iloc[:,0:1]
    glare_source_max = float(glare.max())

    #if no glare source is to be found, some valiues as listed below should be set to their minimum
    if glare_source_max == 0:
       Ls       = Ldata.iloc[:,5:6]
       Omega    = Ldata.iloc[:,6:7]
       pIndex   = Ldata.iloc[:,7:8]
       Lt       = Ldata.iloc[:,9:10]
       E_vert   = Ldata.iloc[:,10:11]
       Edir     = Ldata.iloc[:,11:12]
       LsMax    = Ls.max()
       xdir     =0
       ydir     =0
       zdir     =0
   
       GlareVec =[xdir,ydir,zdir]
       DGP      =float(data.iloc[-1,1:2])
       La       =float(data.iloc[-1,2:3])
       Ev       =float(data.iloc[-1,3:4])
       Lb       =float(data.iloc[-1,4:5])
       DGI      =0
       UGP      =0
       UGR      =0
       VCP      =100
       CGI      =0
       DGPcontrast=0
   
       #Udvælgelse af værdier for omega, pIndex, La, x,y,z værdierne er udvalgt 
       #ud fra max værdien for Ls og den tilhørende glare source. 
   
       MaxValue = (Ldata.loc[Ldata['L_s'].idxmax()])
       M_Ls     = str(MaxValue.iloc[5])
       M_Omega  = str(MaxValue.iloc[6])
       M_pIndex = str(MaxValue.iloc[7])
       M_x      = str(0)
       M_y      = str(0)
       M_z      = str(0)
       M_La     = str(La)
   
   
    elif glare_source_max != 0: 
    
       Ls       = Ldata.iloc[:,5:6]
       Omega    = Ldata.iloc[:,6:7]
       pIndex   = Ldata.iloc[:,7:8]
       Lt       = Ldata.iloc[:,9:10]
       E_vert   = Ldata.iloc[:,10:11]
       Edir     = Ldata.iloc[:,11:12]
       LsMax    = Ls.max()
   
       xdir     = Ldata.iloc[:,14:15]
       ydir     = Ldata.iloc[:,15:16]
       zdir     = Ldata.iloc[:,16:17]
       GlareVec2= [xdir,ydir,zdir]
       DGP      = float(data.iloc[-1,1:2])
       La       = float(data.iloc[-1,2:3])
       Ev       = float(data.iloc[-1,3:4])
       Lb       = float(data.iloc[-1,4:5])
       EvDir    = float(data.iloc[-1,5:6])
       DGI      = float(data.iloc[-1,6:7])
       UGR      = float(data.iloc[-1,7:8])
       VCP      = float(data.iloc[-1,8:9])
       CGI      = float(data.iloc[-1,9:10])
  
       #Udvælgelse af værdier for omega, pIndex, La, x,y,z værdierne er udvalgt 
       #ud fra max værdien for Ls og den tilhørende glare source.   
   
       MaxValue = Ldata.loc[Ldata['L_s'].idxmax()]
       M_La     = str(La)
       M_Ls     = str(MaxValue.iloc[5])
       M_Omega  = str(MaxValue.iloc[6])
       M_pIndex = str(MaxValue.iloc[7])
       M_x      = str(MaxValue.iloc[14])
       M_y      = str(MaxValue.iloc[15])
       M_z      = str(MaxValue.iloc[16])
  


     
     
    #Export data   
    myFile.write(M_Ls+'\t'+M_La+'\t'+ M_Omega+'\t'+M_pIndex+'\t'+M_x+'\t'+M_y+'\t'+M_z+"\n") 
    
myFile.close()      