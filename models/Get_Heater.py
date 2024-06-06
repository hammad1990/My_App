import math
from flask import flash


elem1=[1,1.5,2,2.5,3,4,5,6]
length1 = len(elem1)
elem2=[1,2,2.5,3,4,5,6]
length2 = len(elem2)

class heat11:
    def __init__(self,eh,st,volt):
        self.eh=eh
        self.x=float(self.eh)
        self.st=st
        self.volt=volt
        
        self.st1=[0,0,0,0,0,0,0,0,0]
        self.st2=[0,0,0,0,0,0,0,0,0]
        self.st3=[0,0,0,0,0,0,0,0,0]
        self.st4=[0,0,0,0,0,0,0,0,0]
        self.st5=[0,0,0,0,0,0,0,0,0]
        self.st6=[0,0,0,0,0,0,0,0,0]
        self.cal()
    def cal(self):
        
        
        y=math.floor(self.x)
        y=y+0.5

        if y-self.x==0:
            pass
        elif y-self.x==0.5:
            pass
        elif y-self.x>0:
            self.x=y
        else:
            y-self.x<0
            self.x=y+.5

        self.eh=self.x
        # print(self.eh)
        if self.st==1 and self.eh<=3:
            self.eh=3
        if self.st==2 and self.eh<=6:
            self.eh=6
        if self.st==3 and self.eh<=9:
            self.eh=9
        if self.st==4 and self.eh<=12:
            self.eh=12
        if self.st==5 and self.eh<=15:
            self.eh=15
        if self.st==6 and self.eh<=18:
            self.eh=18
        # print(self.eh)
        
        count=self.st
        z=0

        ################## 220v #########################
        if self.volt==220:
            if self.st==1: ############ stage 1################
                if self.eh>54:
                    flash('MAX Heater cap for 1 stage: 54KW', "error")
                    # return(self.st1)
                else:
                    while self.st1[z]==self.st1[z+3]==self.st1[z+6] ==0:
                        for i in range(0,length1):    #try 1
                            self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem1[i]
                            # print(sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6))
                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                break
                            if i==7 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                for e in range(0,len(self.st1)):
                                    self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0 
                                for i in range(0,length1):  #try 2
                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                            break
                                    for q in range(0,length1):
                                        self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem1[q]
                                        self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem1[i]
                                        # print(sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)+self.st1[z+1]+self.st1[z+4]+self.st1[z+7])
                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                            break
                                        if i==7 and q==7 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                            for e in range(0,len(self.st1)):
                                                self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                            for i in range(0,length1):   #try 3
                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                    break
                                                for q in range(0,length1):
                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                        break
                                                    for w in range(0,length1):
                                                        self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem1[w]
                                                        self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem1[q]
                                                        self.st1[z+2]=self.st1[z+5]=self.st1[z+8]=elem1[i]
                                                        
                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                            break
                                                        if i==7 and q==7 and w==7 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                            for e in range(0,len(self.st1)):
                                                                self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                            self.eh+=0.5
                    self.eh=sum(self.st1)
                    # print(self.eh)
                    
                    

####################### end stage1 ######################
 ###################### stage 2##########################
            elif self.st==2: 
                if self.eh>108:
                    flash('MAX Heater cap for 2 stage: 108KW', "error")
                    print("MAX Heater cap for 2 stage: 108KW")
                else:
                    
                    while self.st1[z]==self.st1[z+3]==self.st1[z+6]==self.st2[z]==self.st2[z+3]==self.st2[z+6] ==0:
                        self.st2[z]=self.st2[z+3]=self.st2[z+6]=1
                        for i in range(0,length1):    ####################try 1
                            
                            self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem1[i]
                            # print(self.st1)
                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                break
                            else:
                                self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem1[i] 
                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                    break
                            
                            
                                if i==7 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                    for e in range(0,len(self.st1)):
                                        self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                    self.st2[z]=self.st2[z+3]=self.st2[z+6]=1
                                    for i1 in range(0,length1):  ####################try 2
                                    
                                    
                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                             break
                                        for q1 in range(0,length1):
                                            self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem1[q1]
                                            self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem1[i1]

                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                break
                                            else:
                                                self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem1[q1]
                                                self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem1[i1]
##                                            
##                                            print(self.st2)
                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                    break
                            
                                                if i1==7 and q1==7 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                
                                                    for e in range(0,len(self.st1)):
                                                        self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                    self.st2[z]=self.st2[z+3]=self.st2[z+6]=1
                                                    for i2 in range(0,length1): ########################### #try 3
                                                      
                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                            break
                                                        for q2 in range(0,length1):
                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                break
                                                                
                                                            for w2 in range(0,length1):
                                                                self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem1[w2]
                                                                self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem1[q2]
                                                                self.st1[z+2]=self.st1[z+5]=self.st1[z+8]=elem1[i2]
##                                                                print(self.st1)
                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                    break
                                                                else:
                                                                    self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem1[w2]
                                                                    self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem1[q2]
                                                                    self.st2[z+2]=self.st2[z+5]=self.st2[z+8]=elem1[i2]
##                                                                    print(self.st2)
                                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                        break

                                                                    
                                                                    if i2==7 and q2==7 and w2==7 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                                        for e in range(0,len(self.st1)):
                                                                            self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0

##                                                                                     print(self.st1)
##                                                                                     print(self.st2)
                                                                        self.eh+=0.5
                                                                        # print(self.eh)
                                                                                  
                                                                                     
                    self.eh=sum(self.st1+self.st2)

                    # print(self.eh)
         #################### stage 3 #########################
            elif self.st==3: 
                if self.eh>162:
                    flash('MAX Heater cap for 3 stage: 162KW', "error")
                    print("MAX Heater cap for 3 stage: 162KW")
                else:
                    

                    while self.st1[z]==self.st1[z+3]==self.st1[z+6]==self.st2[z]==self.st2[z+3]==self.st2[z+6]==self.st3[z]==self.st3[z+3]==self.st3[z+6] ==0:
                        self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=1
                        for i in range(0,length1):    ####################try 1
                            
                            self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem1[i]
                            # print(self.st1)
                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                     break
                            elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem1[i] 
                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                     break
                                else:
                                    self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem1[i] 
                                    if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                        break

                            # print(self.st1[z]+self.st1[z+3]+self.st1[z+6])
                            
                                    if i==7 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                        for e in range(0,len(self.st1)):
                                            self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                    
                                        self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=1
                                        for i1 in range(0,length1):  ####################try 2
                                    
                                    
                                            if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                break
                                            for q1 in range(0,length1):
                                                self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem1[q1]
                                                self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem1[i1]
##                                        print(self.st1)
                                                if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                    break
                                                elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:

                                                    self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem1[q1]
                                                    self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem1[i1]

                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                        break
                                                    else:
                                                        self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem1[q1]
                                                        self.st3[z+1]=self.st3[z+4]=self.st3[z+7]=elem1[i1]
##                                            
##                                            print(self.st2)
                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                            break
                            
                                                        if i1==7 and q1==7 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                
                                                            for e in range(0,len(self.st1)):
                                                                self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                            self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=1
                                                            for i2 in range(0,length1): ########################### #try 3
##                                                        
                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                    break
                                                                for q2 in range(0,length1):
                                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                        break
                                                                
                                                                    for w2 in range(0,length1):
                                                                        self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem1[w2]
                                                                        self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem1[q2]
                                                                        self.st1[z+2]=self.st1[z+5]=self.st1[z+8]=elem1[i2]
##                                                                print(self.st1)
                                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                            break
                                                                        elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:

                                                                            self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem1[w2]
                                                                            self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem1[q2]
                                                                            self.st2[z+2]=self.st2[z+5]=self.st2[z+8]=elem1[i2]
##                                                                    print(self.st2)
                                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                break
                                                                            else:
                                                                                self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem1[w2]
                                                                                self.st3[z+1]=self.st3[z+4]=self.st3[z+7]=elem1[q2]
                                                                                self.st3[z+2]=self.st3[z+5]=self.st3[z+8]=elem1[i2]

                                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                    break

                                                                    
                                                                                
                                                                                if i2==7 and q2==7 and w2==7 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                                
                                                                                    for e in range(0,len(self.st1)):
                                                                                        self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                                                      
                                                                                    self.eh+=0.5
                                                                                    # print(self.eh)
                                                                                     
                                                                                     


                           
                    self.eh=sum(self.st1+self.st2+self.st3)

                    # print(self.eh)           

          ############# stage 4 ##########
            elif self.st==4: 
                if self.eh>216:
                    flash('MAX Heater cap for 4 stage: 216KW', "error")
                    print("MAX Heater cap for 4 stage: 216KW")
                else:
                    

                    while self.st1[z]==self.st1[z+3]==self.st1[z+6]==self.st2[z]==self.st2[z+3]==self.st2[z+6]==self.st3[z]==self.st3[z+3]==self.st3[z+6]==self.st4[z]==self.st4[z+3]==self.st4[z+6] ==0:
                    
                        self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=self.st4[z]=self.st4[z+3]=self.st4[z+6]=1
                        for i in range(0,length1):    ####################try 1
                            
                            self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem1[i]
                            # print(self.st1)
                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                    break
                            elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem1[i] 
                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                    break
                                elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                    self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem1[i]
                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                        break
                                    else:
                                        self.st4[z]=self.st4[z+3]=self.st4[z+6]=elem1[i] 
                                        if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                            break

                            # print(self.st1[z]+self.st1[z+3]+self.st1[z+6])
                            
                                        if i==7 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                            for e in range(0,len(self.st1)):
                                                self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                    
                                            self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=self.st4[z]=self.st4[z+3]=self.st4[z+6]=1
                                            for i1 in range(0,length1):  ####################try 2
                                    
                                    
                                                if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                    break
                                                for q1 in range(0,length1):
                                                    self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem1[q1]
                                                    self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem1[i1]
                                        
                                                    if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                        break
                                                    elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:

                                                        self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem1[q1]
                                                        self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem1[i1]

                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                            break
                                                        elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                                            self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem1[q1]
                                                            self.st3[z+1]=self.st3[z+4]=self.st3[z+7]=elem1[i1]
                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                break
                                                            else:
                                                                self.st4[z]=self.st4[z+3]=self.st4[z+6]=elem1[q1]
                                                                self.st4[z+1]=self.st4[z+4]=self.st4[z+7]=elem1[i1]
                                            

                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                    break
                            
                                                                if i1==7 and q1==7 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                
                                                                    for e in range(0,len(self.st1)):
                                                                        self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                                    self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=self.st4[z]=self.st4[z+3]=self.st4[z+6]=1
                                                                    for i2 in range(0,length1): ########################### #try 3
                                                        
                                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                            break
                                                                        for q2 in range(0,length1):
                                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                break
                                                                
                                                                            for w2 in range(0,length1):
                                                                                self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem1[w2]
                                                                                self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem1[q2]
                                                                                self.st1[z+2]=self.st1[z+5]=self.st1[z+8]=elem1[i2]

                                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                    break
                                                                                elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:

                                                                                    self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem1[w2]
                                                                                    self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem1[q2]
                                                                                    self.st2[z+2]=self.st2[z+5]=self.st2[z+8]=elem1[i2]

                                                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                        break
                                                                                    elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:
                                                                                        self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem1[w2]
                                                                                        self.st3[z+1]=self.st3[z+4]=self.st3[z+7]=elem1[q2]
                                                                                        self.st3[z+2]=self.st3[z+5]=self.st3[z+8]=elem1[i2]
                                                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                            break
                                                                                        else:
                                                                                            self.st4[z]=self.st4[z+3]=self.st4[z+6]=elem1[w2]
                                                                                            self.st4[z+1]=self.st4[z+4]=self.st4[z+7]=elem1[q2]
                                                                                            self.st4[z+2]=self.st4[z+5]=self.st4[z+8]=elem1[i2]

                                                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                break

                                                                    
                                                                                
                                                                                            if i2==7 and q2==7 and w2==7 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                                
                                                                                                for e in range(0,len(self.st1)):
                                                                                                    self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                                                    
                                                                                                self.eh+=0.5
                                                                                                print(self.eh)
                                                                                    
                                                                                    


                        
                    self.eh=sum(self.st1+self.st2+self.st3+self.st4)

                    # print(self.eh)                     
        


        ############## end stage 4###########
        ################ stage 5##########
            elif self.st==5: 
                if self.eh>270:
                    flash('MAX Heater cap for 5 stage: 270KW', "error")
                    print("MAX Heater cap for 5 stage: 270KW")
                else:
                    

                    while self.st1[z]==self.st1[z+3]==self.st1[z+6]==self.st2[z]==self.st2[z+3]==self.st2[z+6]==self.st3[z]==self.st3[z+3]==self.st3[z+6]==self.st4[z]==self.st4[z+3]==self.st4[z+6]==self.st5[z]==self.st5[z+3]==self.st5[z+6] ==0:
                    
                        self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=self.st4[z]=self.st4[z+3]=self.st4[z+6]=self.st5[z]=self.st5[z+3]=self.st5[z+6]=1
                        for i in range(0,length1):    ####################try 1
                            
                            self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem1[i]
                            # print(self.st1)
                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                    break
                            elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem1[i] 
                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                    break
                                elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                    self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem1[i]
                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                        break
                                    elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                        self.st4[z]=self.st4[z+3]=self.st4[z+6]=elem1[i]
                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                            break

                                        else:
                                            self.st5[z]=self.st5[z+3]=self.st5[z+6]=elem1[i] 
                                            if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                break


                            
                                            if i==7 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                for e in range(0,len(self.st1)):
                                                    self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                    
                                                self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=self.st4[z]=self.st4[z+3]=self.st4[z+6]=self.st5[z]=self.st5[z+3]=self.st5[z+6]=1
                                                for i1 in range(0,length1):  ####################try 2
                                    
                                    
                                                    if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                        break
                                                    for q1 in range(0,length1):
                                                        self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem1[q1]
                                                        self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem1[i1]
                                        
                                                        if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                            break
                                                        elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:

                                                            self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem1[q1]
                                                            self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem1[i1]

                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                break
                                                            elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                                                self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem1[q1]
                                                                self.st3[z+1]=self.st3[z+4]=self.st3[z+7]=elem1[i1]
                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                    break

                                                                elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                                                    self.st4[z]=self.st4[z+3]=self.st4[z+6]=elem1[q1]
                                                                    self.st4[z+1]=self.st4[z+4]=self.st4[z+7]=elem1[i1]
                                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                        break

                                                                    else:
                                                                        self.st5[z]=self.st5[z+3]=self.st5[z+6]=elem1[q1]
                                                                        self.st5[z+1]=self.st5[z+4]=self.st5[z+7]=elem1[i1]
                                            

                                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                            break
                            
                                                                        if i1==7 and q1==7 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                
                                                                            for e in range(0,len(self.st1)):
                                                                                self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                                            self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=self.st4[z]=self.st4[z+3]=self.st4[z+6]=1
                                                                            for i2 in range(0,length1): ########################### #try 3
                                                        
                                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                    break
                                                                                for q2 in range(0,length1):
                                                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                        break
                                                                
                                                                                    for w2 in range(0,length1):
                                                                                        self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem1[w2]
                                                                                        self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem1[q2]
                                                                                        self.st1[z+2]=self.st1[z+5]=self.st1[z+8]=elem1[i2]

                                                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                            break
                                                                                        elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:

                                                                                            self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem1[w2]
                                                                                            self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem1[q2]
                                                                                            self.st2[z+2]=self.st2[z+5]=self.st2[z+8]=elem1[i2]

                                                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                break
                                                                                            elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:
                                                                                                self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem1[w2]
                                                                                                self.st3[z+1]=self.st3[z+4]=self.st3[z+7]=elem1[q2]
                                                                                                self.st3[z+2]=self.st3[z+5]=self.st3[z+8]=elem1[i2]
                                                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                    break
                                                                                                elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:
                                                                                                    self.st4[z]=self.st4[z+3]=self.st4[z+6]=elem1[w2]
                                                                                                    self.st4[z+1]=self.st4[z+4]=self.st4[z+7]=elem1[q2]
                                                                                                    self.st4[z+2]=self.st4[z+5]=self.st4[z+8]=elem1[i2]
                                                                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                        break
                                                                                                    else:
                                                                                                        self.st5[z]=self.st5[z+3]=self.st5[z+6]=elem1[w2]
                                                                                                        self.st5[z+1]=self.st5[z+4]=self.st5[z+7]=elem1[q2]
                                                                                                        self.st5[z+2]=self.st5[z+5]=self.st5[z+8]=elem1[i2]

                                                                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                            break

                                                                    
                                                                                
                                                                                                        if i2==7 and q2==7 and w2==7 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                                
                                                                                                            for e in range(0,len(self.st1)):
                                                                                                                self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                                                    
                                                                                                            self.eh+=0.5
                                                                                                            print(self.eh)
                                                                                    
                                                                                    


                        
                    self.eh=sum(self.st1+self.st2+self.st3+self.st4+self.st5)

                    # print(self.eh)                     
        
         ################# stage 6 ###########
            elif self.st==6: 
                if self.eh>324:
                    flash('MAX Heater cap for 6 stage: 324KW', "error")
                    print("MAX Heater cap for 6 stage: 324KW")
                else:
                    

                    while self.st1[z]==self.st1[z+3]==self.st1[z+6]==self.st2[z]==self.st2[z+3]==self.st2[z+6]==self.st3[z]==self.st3[z+3]==self.st3[z+6]==self.st4[z]==self.st4[z+3]==self.st4[z+6]==self.st5[z]==self.st5[z+3]==self.st5[z+6]==self.st6[z]==self.st6[z+3]==self.st6[z+6] ==0:
                    
                        self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=self.st4[z]=self.st4[z+3]=self.st4[z+6]=self.st5[z]=self.st5[z+3]=self.st5[z+6]=self.st6[z]=self.st6[z+3]=self.st6[z+6]=1
                        for i in range(0,length1):    ####################try 1
                            
                            self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem1[i]
                            # print(self.st1)
                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                    break
                            elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem1[i] 
                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                    break
                                elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                    self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem1[i]
                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                        break
                                    elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                        self.st4[z]=self.st4[z+3]=self.st4[z+6]=elem1[i]
                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                            break
                                        elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                            self.st5[z]=self.st5[z+3]=self.st5[z+6]=elem1[i]
                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                break

                                            else:
                                                self.st6[z]=self.st6[z+3]=self.st6[z+6]=elem1[i] 
                                                if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                    break


                            
                                                if i==7 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                    for e in range(0,len(self.st1)):
                                                        self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                    
                                                    self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=self.st4[z]=self.st4[z+3]=self.st4[z+6]=self.st5[z]=self.st5[z+3]=self.st5[z+6]=1
                                                    for i1 in range(0,length1):  ####################try 2
                                    
                                    
                                                        if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                            break
                                                        for q1 in range(0,length1):
                                                            self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem1[q1]
                                                            self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem1[i1]
                                        
                                                            if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                break
                                                            elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:

                                                                self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem1[q1]
                                                                self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem1[i1]

                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                    break
                                                                elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                                                    self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem1[q1]
                                                                    self.st3[z+1]=self.st3[z+4]=self.st3[z+7]=elem1[i1]
                                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                        break

                                                                    elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                                                        self.st4[z]=self.st4[z+3]=self.st4[z+6]=elem1[q1]
                                                                        self.st4[z+1]=self.st4[z+4]=self.st4[z+7]=elem1[i1]
                                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                            break
                                                                        elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                                                            self.st5[z]=self.st5[z+3]=self.st5[z+6]=elem1[q1]
                                                                            self.st5[z+1]=self.st5[z+4]=self.st5[z+7]=elem1[i1]
                                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                break

                                                                            else:
                                                                                self.st6[z]=self.st6[z+3]=self.st6[z+6]=elem1[q1]
                                                                                self.st6[z+1]=self.st6[z+4]=self.st6[z+7]=elem1[i1]
                                            

                                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                    break
                            
                                                                                if i1==7 and q1==7 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                
                                                                                    for e in range(0,len(self.st1)):
                                                                                        self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                                                    self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=self.st4[z]=self.st4[z+3]=self.st4[z+6]=1
                                                                                    for i2 in range(0,length1): ########################### #try 3
                                                        
                                                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                            break
                                                                                        for q2 in range(0,length1):
                                                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                break
                                                                
                                                                                            for w2 in range(0,length1):
                                                                                                self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem1[w2]
                                                                                                self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem1[q2]
                                                                                                self.st1[z+2]=self.st1[z+5]=self.st1[z+8]=elem1[i2]

                                                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                    break
                                                                                                elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:

                                                                                                    self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem1[w2]
                                                                                                    self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem1[q2]
                                                                                                    self.st2[z+2]=self.st2[z+5]=self.st2[z+8]=elem1[i2]

                                                                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                        break
                                                                                                    elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:
                                                                                                        self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem1[w2]
                                                                                                        self.st3[z+1]=self.st3[z+4]=self.st3[z+7]=elem1[q2]
                                                                                                        self.st3[z+2]=self.st3[z+5]=self.st3[z+8]=elem1[i2]
                                                                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                            break
                                                                                                        elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:
                                                                                                            self.st4[z]=self.st4[z+3]=self.st4[z+6]=elem1[w2]
                                                                                                            self.st4[z+1]=self.st4[z+4]=self.st4[z+7]=elem1[q2]
                                                                                                            self.st4[z+2]=self.st4[z+5]=self.st4[z+8]=elem1[i2]
                                                                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                                break
                                                                                                            elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:
                                                                                                                self.st5[z]=self.st5[z+3]=self.st5[z+6]=elem1[w2]
                                                                                                                self.st5[z+1]=self.st5[z+4]=self.st5[z+7]=elem1[q2]
                                                                                                                self.st5[z+2]=self.st5[z+5]=self.st5[z+8]=elem1[i2]
                                                                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                                    break
                                                                                                                else:
                                                                                                                    self.st6[z]=self.st6[z+3]=self.st6[z+6]=elem1[w2]
                                                                                                                    self.st6[z+1]=self.st6[z+4]=self.st6[z+7]=elem1[q2]
                                                                                                                    self.st6[z+2]=self.st6[z+5]=self.st6[z+8]=elem1[i2]

                                                                                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                                        break

                                                                    
                                                                                
                                                                                                                    if i2==7 and q2==7 and w2==7 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                                
                                                                                                                        for e in range(0,len(self.st1)):
                                                                                                                            self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                                                    
                                                                                                                        self.eh+=0.5
                                                                                                                        print(self.eh)
                                                                                    
                                                                                    


                        
                    self.eh=sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)

                    # print(self.eh) 

          ############## end 220v###########
          
          
          
         ################# 460v*****************       
        else :
            if self.st==1: ############ stage 1################
                if self.eh>54:
                    flash('MAX Heater cap for 1 stage: 54KW', "error")
                    print("MAX Heater cap for 1 stage: 54KW")
                else:
                    while self.st1[z]==self.st1[z+3]==self.st1[z+6] ==0:
                        for i in range(0,length2):    #try 1
                            self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem2[i]
                            # print(sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6))
                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                break
                            if i==6 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                for e in range(0,len(self.st1)):
                                    self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0 
                                for i in range(0,length2):  #try 2
                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                            break
                                    for q in range(0,length2):
                                        self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem2[q]
                                        self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem2[i]
                                        # print(sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)+self.st1[z+1]+self.st1[z+4]+self.st1[z+7])
                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                            break
                                        if i==6 and q==6 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                            for e in range(0,len(self.st1)):
                                                self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                            for i in range(0,length2):   #try 3
                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                    break
                                                for q in range(0,length2):
                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                        break
                                                    for w in range(0,length2):
                                                        self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem2[w]
                                                        self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem2[q]
                                                        self.st1[z+2]=self.st1[z+5]=self.st1[z+8]=elem2[i]
                                                        
                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                            break
                                                        if i==6 and q==6 and w==6 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                            for e in range(0,len(self.st1)):
                                                                self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                            self.eh+=0.5
                    self.eh=sum(self.st1)
                    # print(self.eh)
                    
                    

####################### end stage1 ######################
 ###################### stage 2##########################
            elif self.st==2: 
                if self.eh>108:
                    flash('MAX Heater cap for 2 stage: 108KW', "error")
                    print("MAX Heater cap for 2 stage: 108KW")
                else:
                    
                    while self.st1[z]==self.st1[z+3]==self.st1[z+6]==self.st2[z]==self.st2[z+3]==self.st2[z+6] ==0:
                        self.st2[z]=self.st2[z+3]=self.st2[z+6]=1
                        for i in range(0,length2):    ####################try 1
                            
                            self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem2[i]
                            # print(self.st1)
                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                break
                            else:
                                self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem2[i] 
                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                    break
                            
                            
                                if i==6 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                    for e in range(0,len(self.st1)):
                                        self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                    self.st2[z]=self.st2[z+3]=self.st2[z+6]=1
                                    for i1 in range(0,length2):  ####################try 2
                                    
                                    
                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                             break
                                        for q1 in range(0,length2):
                                            self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem2[q1]
                                            self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem2[i1]

                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                break
                                            else:
                                                self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem2[q1]
                                                self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem2[i1]
##                                            
##                                            print(self.st2)
                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                    break
                            
                                                if i1==6 and q1==6 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                
                                                    for e in range(0,len(self.st1)):
                                                        self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                    self.st2[z]=self.st2[z+3]=self.st2[z+6]=1
                                                    for i2 in range(0,length2): ########################### #try 3
                                                      
                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                            break
                                                        for q2 in range(0,length2):
                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                break
                                                                
                                                            for w2 in range(0,length2):
                                                                self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem2[w2]
                                                                self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem2[q2]
                                                                self.st1[z+2]=self.st1[z+5]=self.st1[z+8]=elem2[i2]
##                                                                print(self.st1)
                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                    break
                                                                else:
                                                                    self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem2[w2]
                                                                    self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem2[q2]
                                                                    self.st2[z+2]=self.st2[z+5]=self.st2[z+8]=elem2[i2]
##                                                                    print(self.st2)
                                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                        break

                                                                    
                                                                    if i2==6 and q2==6 and w2==6 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                                        for e in range(0,len(self.st1)):
                                                                            self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0

##                                                                                     print(self.st1)
##                                                                                     print(self.st2)
                                                                        self.eh+=0.5
                                                                        # print(self.eh)
                                                                                  
                                                                                     
                    self.eh=sum(self.st1+self.st2)

                    # print(self.eh)
         #################### stage 3 #########################
            elif self.st==3: 
                if self.eh>162:
                    flash('MAX Heater cap for 3 stage: 162KW', "error")
                    print("MAX Heater cap for 3 stage: 162KW")
                else:
                    

                    while self.st1[z]==self.st1[z+3]==self.st1[z+6]==self.st2[z]==self.st2[z+3]==self.st2[z+6]==self.st3[z]==self.st3[z+3]==self.st3[z+6] ==0:
                        self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=1
                        for i in range(0,length2):    ####################try 1
                            
                            self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem2[i]
                            # print(self.st1)
                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                     break
                            elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem2[i] 
                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                     break
                                else:
                                    self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem2[i] 
                                    if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                        break

                            # print(self.st1[z]+self.st1[z+3]+self.st1[z+6])
                            
                                    if i==6 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                        for e in range(0,len(self.st1)):
                                            self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                    
                                        self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=1
                                        for i1 in range(0,length2):  ####################try 2
                                    
                                    
                                            if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                break
                                            for q1 in range(0,length2):
                                                self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem2[q1]
                                                self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem2[i1]
##                                        print(self.st1)
                                                if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                    break
                                                elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:

                                                    self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem2[q1]
                                                    self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem2[i1]

                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                        break
                                                    else:
                                                        self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem2[q1]
                                                        self.st3[z+1]=self.st3[z+4]=self.st3[z+7]=elem2[i1]
##                                            
##                                            print(self.st2)
                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                            break
                            
                                                        if i1==6 and q1==6 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                
                                                            for e in range(0,len(self.st1)):
                                                                self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                            self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=1
                                                            for i2 in range(0,length2): ########################### #try 3
##                                                        
                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                    break
                                                                for q2 in range(0,length2):
                                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                        break
                                                                
                                                                    for w2 in range(0,length2):
                                                                        self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem2[w2]
                                                                        self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem2[q2]
                                                                        self.st1[z+2]=self.st1[z+5]=self.st1[z+8]=elem2[i2]
##                                                                print(self.st1)
                                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                            break
                                                                        elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:

                                                                            self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem2[w2]
                                                                            self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem2[q2]
                                                                            self.st2[z+2]=self.st2[z+5]=self.st2[z+8]=elem2[i2]
##                                                                    print(self.st2)
                                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                break
                                                                            else:
                                                                                self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem2[w2]
                                                                                self.st3[z+1]=self.st3[z+4]=self.st3[z+7]=elem2[q2]
                                                                                self.st3[z+2]=self.st3[z+5]=self.st3[z+8]=elem2[i2]

                                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                    break

                                                                    
                                                                                
                                                                                if i2==6 and q2==6 and w2==6 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                                
                                                                                    for e in range(0,len(self.st1)):
                                                                                        self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                                                      
                                                                                    self.eh+=0.5
                                                                                    # print(self.eh)
                                                                                     
                                                                                     


                           
                    self.eh=sum(self.st1+self.st2+self.st3)

                    # print(self.eh)           

          ############# stage 4 ##########
            elif self.st==4: 
                if self.eh>216:
                    flash('MAX Heater cap for 4 stage: 216KW', "error")
                    print("MAX Heater cap for 4 stage: 216KW")
                else:
                    

                    while self.st1[z]==self.st1[z+3]==self.st1[z+6]==self.st2[z]==self.st2[z+3]==self.st2[z+6]==self.st3[z]==self.st3[z+3]==self.st3[z+6]==self.st4[z]==self.st4[z+3]==self.st4[z+6] ==0:
                    
                        self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=self.st4[z]=self.st4[z+3]=self.st4[z+6]=1
                        for i in range(0,length2):    ####################try 1
                            
                            self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem2[i]
                            # print(self.st1)
                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                    break
                            elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem2[i] 
                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                    break
                                elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                    self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem2[i]
                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                        break
                                    else:
                                        self.st4[z]=self.st4[z+3]=self.st4[z+6]=elem2[i] 
                                        if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                            break

                            # print(self.st1[z]+self.st1[z+3]+self.st1[z+6])
                            
                                        if i==6 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                            for e in range(0,len(self.st1)):
                                                self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                    
                                            self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=self.st4[z]=self.st4[z+3]=self.st4[z+6]=1
                                            for i1 in range(0,length2):  ####################try 2
                                    
                                    
                                                if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                    break
                                                for q1 in range(0,length2):
                                                    self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem2[q1]
                                                    self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem2[i1]
                                        
                                                    if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                        break
                                                    elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:

                                                        self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem2[q1]
                                                        self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem2[i1]

                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                            break
                                                        elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                                            self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem2[q1]
                                                            self.st3[z+1]=self.st3[z+4]=self.st3[z+7]=elem2[i1]
                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                break
                                                            else:
                                                                self.st4[z]=self.st4[z+3]=self.st4[z+6]=elem2[q1]
                                                                self.st4[z+1]=self.st4[z+4]=self.st4[z+7]=elem2[i1]
                                            

                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                    break
                            
                                                                if i1==6 and q1==6 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                
                                                                    for e in range(0,len(self.st1)):
                                                                        self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                                    self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=self.st4[z]=self.st4[z+3]=self.st4[z+6]=1
                                                                    for i2 in range(0,length2): ########################### #try 3
                                                        
                                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                            break
                                                                        for q2 in range(0,length2):
                                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                break
                                                                
                                                                            for w2 in range(0,length2):
                                                                                self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem2[w2]
                                                                                self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem2[q2]
                                                                                self.st1[z+2]=self.st1[z+5]=self.st1[z+8]=elem2[i2]

                                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                    break
                                                                                elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:

                                                                                    self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem2[w2]
                                                                                    self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem2[q2]
                                                                                    self.st2[z+2]=self.st2[z+5]=self.st2[z+8]=elem2[i2]

                                                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                        break
                                                                                    elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:
                                                                                        self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem2[w2]
                                                                                        self.st3[z+1]=self.st3[z+4]=self.st3[z+7]=elem2[q2]
                                                                                        self.st3[z+2]=self.st3[z+5]=self.st3[z+8]=elem2[i2]
                                                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                            break
                                                                                        else:
                                                                                            self.st4[z]=self.st4[z+3]=self.st4[z+6]=elem2[w2]
                                                                                            self.st4[z+1]=self.st4[z+4]=self.st4[z+7]=elem2[q2]
                                                                                            self.st4[z+2]=self.st4[z+5]=self.st4[z+8]=elem2[i2]

                                                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                break

                                                                    
                                                                                
                                                                                            if i2==6 and q2==6 and w2==6 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                                
                                                                                                for e in range(0,len(self.st1)):
                                                                                                    self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                                                    
                                                                                                self.eh+=0.5
                                                                                                # print(self.eh)
                                                                                    
                                                                                    


                        
                    self.eh=sum(self.st1+self.st2+self.st3+self.st4)

                    # print(self.eh)                     
        


        ############## end stage 4###########
        ################ stage 5##########
            elif self.st==5: 
                if self.eh>270:
                    flash('MAX Heater cap for 5 stage: 270KW', "error")
                    print("MAX Heater cap for 5 stage: 270KW")
                else:
                    

                    while self.st1[z]==self.st1[z+3]==self.st1[z+6]==self.st2[z]==self.st2[z+3]==self.st2[z+6]==self.st3[z]==self.st3[z+3]==self.st3[z+6]==self.st4[z]==self.st4[z+3]==self.st4[z+6]==self.st5[z]==self.st5[z+3]==self.st5[z+6] ==0:
                    
                        self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=self.st4[z]=self.st4[z+3]=self.st4[z+6]=self.st5[z]=self.st5[z+3]=self.st5[z+6]=1
                        for i in range(0,length2):    ####################try 1
                            
                            self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem2[i]
                            # print(self.st1)
                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                    break
                            elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem2[i] 
                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                    break
                                elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                    self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem2[i]
                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                        break
                                    elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                        self.st4[z]=self.st4[z+3]=self.st4[z+6]=elem2[i]
                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                            break

                                        else:
                                            self.st5[z]=self.st5[z+3]=self.st5[z+6]=elem2[i] 
                                            if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                break


                            
                                            if i==6 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                for e in range(0,len(self.st1)):
                                                    self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                    
                                                self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=self.st4[z]=self.st4[z+3]=self.st4[z+6]=self.st5[z]=self.st5[z+3]=self.st5[z+6]=1
                                                for i1 in range(0,length2):  ####################try 2
                                    
                                    
                                                    if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                        break
                                                    for q1 in range(0,length2):
                                                        self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem2[q1]
                                                        self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem2[i1]
                                        
                                                        if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                            break
                                                        elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:

                                                            self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem2[q1]
                                                            self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem2[i1]

                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                break
                                                            elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                                                self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem2[q1]
                                                                self.st3[z+1]=self.st3[z+4]=self.st3[z+7]=elem2[i1]
                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                    break

                                                                elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                                                    self.st4[z]=self.st4[z+3]=self.st4[z+6]=elem2[q1]
                                                                    self.st4[z+1]=self.st4[z+4]=self.st4[z+7]=elem2[i1]
                                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                        break

                                                                    else:
                                                                        self.st5[z]=self.st5[z+3]=self.st5[z+6]=elem2[q1]
                                                                        self.st5[z+1]=self.st5[z+4]=self.st5[z+7]=elem2[i1]
                                            

                                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                            break
                            
                                                                        if i1==6 and q1==6 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                
                                                                            for e in range(0,len(self.st1)):
                                                                                self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                                            self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=self.st4[z]=self.st4[z+3]=self.st4[z+6]=1
                                                                            for i2 in range(0,length2): ########################### #try 3
                                                        
                                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                    break
                                                                                for q2 in range(0,length2):
                                                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                        break
                                                                
                                                                                    for w2 in range(0,length2):
                                                                                        self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem2[w2]
                                                                                        self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem2[q2]
                                                                                        self.st1[z+2]=self.st1[z+5]=self.st1[z+8]=elem2[i2]

                                                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                            break
                                                                                        elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:

                                                                                            self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem2[w2]
                                                                                            self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem2[q2]
                                                                                            self.st2[z+2]=self.st2[z+5]=self.st2[z+8]=elem2[i2]

                                                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                break
                                                                                            elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:
                                                                                                self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem2[w2]
                                                                                                self.st3[z+1]=self.st3[z+4]=self.st3[z+7]=elem2[q2]
                                                                                                self.st3[z+2]=self.st3[z+5]=self.st3[z+8]=elem2[i2]
                                                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                    break
                                                                                                elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:
                                                                                                    self.st4[z]=self.st4[z+3]=self.st4[z+6]=elem2[w2]
                                                                                                    self.st4[z+1]=self.st4[z+4]=self.st4[z+7]=elem2[q2]
                                                                                                    self.st4[z+2]=self.st4[z+5]=self.st4[z+8]=elem2[i2]
                                                                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                        break
                                                                                                    else:
                                                                                                        self.st5[z]=self.st5[z+3]=self.st5[z+6]=elem2[w2]
                                                                                                        self.st5[z+1]=self.st5[z+4]=self.st5[z+7]=elem2[q2]
                                                                                                        self.st5[z+2]=self.st5[z+5]=self.st5[z+8]=elem2[i2]

                                                                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                            break

                                                                    
                                                                                
                                                                                                        if i2==6 and q2==6 and w2==6 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                                
                                                                                                            for e in range(0,len(self.st1)):
                                                                                                                self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                                                    
                                                                                                            self.eh+=0.5
                                                                                                            # print(self.eh)
                                                                                    
                                                                                    


                        
                    self.eh=sum(self.st1+self.st2+self.st3+self.st4+self.st5)

                    # print(self.eh)                     
        
         ################# stage 6 ###########
            elif self.st==6: 
                if self.eh>324:
                    flash('MAX Heater cap for 6 stage: 324KW', "error")
                    print("MAX Heater cap for 6 stage: 324KW")
                else:
                    

                    while self.st1[z]==self.st1[z+3]==self.st1[z+6]==self.st2[z]==self.st2[z+3]==self.st2[z+6]==self.st3[z]==self.st3[z+3]==self.st3[z+6]==self.st4[z]==self.st4[z+3]==self.st4[z+6]==self.st5[z]==self.st5[z+3]==self.st5[z+6]==self.st6[z]==self.st6[z+3]==self.st6[z+6] ==0:
                    
                        self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=self.st4[z]=self.st4[z+3]=self.st4[z+6]=self.st5[z]=self.st5[z+3]=self.st5[z+6]=self.st6[z]=self.st6[z+3]=self.st6[z+6]=1
                        for i in range(0,length2):    ####################try 1
                            
                            self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem2[i]
                            # print(self.st1)
                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                    break
                            elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem2[i] 
                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                    break
                                elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                    self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem2[i]
                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                        break
                                    elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                        self.st4[z]=self.st4[z+3]=self.st4[z+6]=elem2[i]
                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                            break
                                        elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                            self.st5[z]=self.st5[z+3]=self.st5[z+6]=elem2[i]
                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                break

                                            else:
                                                self.st6[z]=self.st6[z+3]=self.st6[z+6]=elem2[i] 
                                                if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                    break


                            
                                                if i==6 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                    for e in range(0,len(self.st1)):
                                                        self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                    
                                                    self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=self.st4[z]=self.st4[z+3]=self.st4[z+6]=self.st5[z]=self.st5[z+3]=self.st5[z+6]=1
                                                    for i1 in range(0,length2):  ####################try 2
                                    
                                    
                                                        if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                            break
                                                        for q1 in range(0,length2):
                                                            self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem2[q1]
                                                            self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem2[i1]
                                        
                                                            if  sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                break
                                                            elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:

                                                                self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem2[q1]
                                                                self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem2[i1]

                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                    break
                                                                elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                                                    self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem2[q1]
                                                                    self.st3[z+1]=self.st3[z+4]=self.st3[z+7]=elem2[i1]
                                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                        break

                                                                    elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                                                        self.st4[z]=self.st4[z+3]=self.st4[z+6]=elem2[q1]
                                                                        self.st4[z+1]=self.st4[z+4]=self.st4[z+7]=elem2[i1]
                                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                            break
                                                                        elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!=self.eh:
                                                                            self.st5[z]=self.st5[z+3]=self.st5[z+6]=elem2[q1]
                                                                            self.st5[z+1]=self.st5[z+4]=self.st5[z+7]=elem2[i1]
                                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                break

                                                                            else:
                                                                                self.st6[z]=self.st6[z+3]=self.st6[z+6]=elem2[q1]
                                                                                self.st6[z+1]=self.st6[z+4]=self.st6[z+7]=elem2[i1]
                                            

                                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                    break
                            
                                                                                if i1==6 and q1==6 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                
                                                                                    for e in range(0,len(self.st1)):
                                                                                        self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                                                    self.st2[z]=self.st2[z+3]=self.st2[z+6]=self.st3[z]=self.st3[z+3]=self.st3[z+6]=self.st4[z]=self.st4[z+3]=self.st4[z+6]=1
                                                                                    for i2 in range(0,length2): ########################### #try 3
                                                        
                                                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                            break
                                                                                        for q2 in range(0,length2):
                                                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                break
                                                                
                                                                                            for w2 in range(0,length2):
                                                                                                self.st1[z]=self.st1[z+3]=self.st1[z+6]=elem2[w2]
                                                                                                self.st1[z+1]=self.st1[z+4]=self.st1[z+7]=elem2[q2]
                                                                                                self.st1[z+2]=self.st1[z+5]=self.st1[z+8]=elem2[i2]

                                                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                    break
                                                                                                elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:

                                                                                                    self.st2[z]=self.st2[z+3]=self.st2[z+6]=elem2[w2]
                                                                                                    self.st2[z+1]=self.st2[z+4]=self.st2[z+7]=elem2[q2]
                                                                                                    self.st2[z+2]=self.st2[z+5]=self.st2[z+8]=elem2[i2]

                                                                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                        break
                                                                                                    elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:
                                                                                                        self.st3[z]=self.st3[z+3]=self.st3[z+6]=elem2[w2]
                                                                                                        self.st3[z+1]=self.st3[z+4]=self.st3[z+7]=elem2[q2]
                                                                                                        self.st3[z+2]=self.st3[z+5]=self.st3[z+8]=elem2[i2]
                                                                                                        if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                            break
                                                                                                        elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:
                                                                                                            self.st4[z]=self.st4[z+3]=self.st4[z+6]=elem2[w2]
                                                                                                            self.st4[z+1]=self.st4[z+4]=self.st4[z+7]=elem2[q2]
                                                                                                            self.st4[z+2]=self.st4[z+5]=self.st4[z+8]=elem2[i2]
                                                                                                            if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                                break
                                                                                                            elif sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6) !=self.eh:
                                                                                                                self.st5[z]=self.st5[z+3]=self.st5[z+6]=elem2[w2]
                                                                                                                self.st5[z+1]=self.st5[z+4]=self.st5[z+7]=elem2[q2]
                                                                                                                self.st5[z+2]=self.st5[z+5]=self.st5[z+8]=elem2[i2]
                                                                                                                if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                                    break
                                                                                                                else:
                                                                                                                    self.st6[z]=self.st6[z+3]=self.st6[z+6]=elem2[w2]
                                                                                                                    self.st6[z+1]=self.st6[z+4]=self.st6[z+7]=elem2[q2]
                                                                                                                    self.st6[z+2]=self.st6[z+5]=self.st6[z+8]=elem2[i2]

                                                                                                                    if sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)== self.eh:
                                                                                                                        break

                                                                    
                                                                                
                                                                                                                    if i2==6 and q2==6 and w2==6 and sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)!= self.eh :
                                                                
                                                                                                                        for e in range(0,len(self.st1)):
                                                                                                                            self.st1[e] = self.st2[e] = self.st3[e] = self.st4[e]= self.st5[e] = self.st6[e]=0
                                                                                    
                                                                                                                        self.eh+=0.5
                                                                                                                        # print(self.eh)

                        
                    self.eh=sum(self.st1+self.st2+self.st3+self.st4+self.st5+self.st6)

                    # print(self.eh)


        ############# end 460v############
        a=self.st1[0]
        b=self.st1[1]
        c=self.st1[2]
        if a>=b and a>=c:
            if b>=c:
            
                self.st1[0]=a
                self.st1[1]=b
                self.st1[2]=c
            else:
                self.st1[0]=a
                self.st1[1]=c
                self.st1[2]=b
        if b>=a and b>=c:
            if a>=c:
                self.st1[0]=b
                self.st1[1]=a
                self.st1[2]=c
            else:
                self.st1[0]=b
                self.st1[1]=c
                self.st1[2]=a
        if c>=a and c>=b:
            if b>=a:
                self.st1[0]=c
                self.st1[1]=b
                self.st1[2]=a
            else:
                self.st1[0]=c
                self.st1[1]=a
                self.st1[2]=b
                
    
############## maximize#################
        a1=self.st1[3]
        b1=self.st1[4]
        c1=self.st1[5]
        if a1>=b1 and a1>=c1:
            if b1>=c1:
            
                self.st1[3]=a1
                self.st1[4]=b1
                self.st1[5]=c1
            else:
                self.st1[3]=a1
                self.st1[4]=c1
                self.st1[5]=b1
        if b1>=a1 and b1>=c1:
            if a1>=c1:
                self.st1[3]=b1
                self.st1[4]=a1
                self.st1[5]=c1
            else:
                self.st1[3]=b1
                self.st1[4]=c1
                self.st1[5]=a1

        if c1>=a1 and c1>=b1:
            if b1>=a1:
                self.st1[3]=c1
                self.st1[4]=b1
                self.st1[5]=a1
            else:
                self.st1[3]=c1
                self.st1[4]=a1
                self.st1[5]=b1
            
############## maximize#################

        a2=self.st1[6]
        b2=self.st1[7]
        c2=self.st1[8]
        if a2>=b2 and a2>=c2:
            if b2>=c2:
            
                self.st1[6]=a2
                self.st1[7]=b2
                self.st1[8]=c2
            else:
                self.st1[6]=a2
                self.st1[7]=c2
                self.st1[8]=b2
        if b2>=a2 and b2>=c2:
            if a2>=c2:
                self.st1[6]=b2
                self.st1[7]=a2
                self.st1[8]=c2
            else:
                self.st1[6]=b2
                self.st1[7]=c2
                self.st1[8]=a2

        
        if c2>=a2 and c2>=b2:
            if b2>=a2:
                self.st1[6]=c2
                self.st1[7]=b2
                self.st1[8]=a2
            else:
                self.st1[6]=c2
                self.st1[7]=a2
                self.st1[8]=b2

        ############## stage 2#################
        a3=self.st2[0]
        b3=self.st2[1]
        c3=self.st2[2]
        if a3>=b3 and a3>=c3:
            if b3>=c3:
            
                self.st2[0]=a3
                self.st2[1]=b3
                self.st2[2]=c3
            else:
                self.st2[0]=a3
                self.st2[1]=c3
                self.st2[2]=b3
        if b3>=a3 and b3>=c3:
            if a3>=c3:
                self.st2[0]=b3
                self.st2[1]=a3
                self.st2[2]=c3
            else:
                self.st2[0]=b3
                self.st2[1]=c3
                self.st2[2]=a3
        if c3>=a3 and c3>=b3:
            if b3>=a3:
                self.st2[0]=c3
                self.st2[1]=b3
                self.st2[2]=a3
            else:
                self.st2[0]=c3
                self.st2[1]=a3
                self.st2[2]=b3
                
    
############## maximize#################
        a4=self.st2[3]
        b4=self.st2[4]
        c4=self.st2[5]
        if a4>=b4 and a4>=c4:
            if b4>=c4:
            
                self.st2[3]=a4
                self.st2[4]=b4
                self.st2[5]=c4
            else:
                self.st2[3]=a4
                self.st2[4]=c4
                self.st2[5]=b4
        if b4>=a4 and b4>=c4:
            if a4>=c4:
                self.st2[3]=b4
                self.st2[4]=a4
                self.st2[5]=c4
            else:
                self.st2[3]=b4
                self.st2[4]=c4
                self.st2[5]=a4

        if c3>=a4 and c4>=b4:
            if b4>=a4:
                self.st2[3]=c4
                self.st2[4]=b4
                self.st2[5]=a4
            else:
                self.st2[3]=c4
                self.st2[4]=a4
                self.st2[5]=b4
            
############## maximize#################

        a5=self.st2[6]
        b5=self.st2[7]
        c5=self.st2[8]
        if a5>=b5 and a5>=c5:
            if b2>=c5:
            
                self.st2[6]=a5
                self.st2[7]=b5
                self.st2[8]=c5
            else:
                self.st2[6]=a5
                self.st2[7]=c5
                self.st2[8]=b5
        if b2>=a5 and b2>=c5:
            if a5>=c5:
                self.st2[6]=b5
                self.st2[7]=a5
                self.st2[8]=c5
            else:
                self.st2[6]=b5
                self.st2[7]=c5
                self.st2[8]=a5

        
        if c5>=a5 and c5>=b5:
            if b5>=a5:
                self.st2[6]=c5
                self.st2[7]=b5
                self.st2[8]=a5
            else:
                self.st2[6]=c5
                self.st2[7]=a5
                self.st2[8]=b5
        ###############stage3############

        a6=self.st3[0]
        b6=self.st3[1]
        c6=self.st3[2]
        if a6>=b6 and a6>=c6:
            if b6>=c6:
            
                self.st3[0]=a6
                self.st3[1]=b6
                self.st3[2]=c6
            else:
                self.st3[0]=a6
                self.st3[1]=c6
                self.st3[2]=b6
        if b6>=a6 and b6>=c6:
            if a6>=c6:
                self.st3[0]=b6
                self.st3[1]=a6
                self.st3[2]=c6
            else:
                self.st3[0]=b6
                self.st3[1]=c6
                self.st3[2]=a6
        if c6>=a6 and c6>=b6:
            if b6>=a6:
                self.st3[0]=c6
                self.st3[1]=b6
                self.st3[2]=a6
            else:
                self.st3[0]=c6
                self.st3[1]=a6
                self.st3[2]=b6
                
    
############## maximize#################
        a7=self.st3[3]
        b7=self.st3[4]
        c7=self.st3[5]
        if a7>=b7 and a7>=c7:
            if b7>=c7:
            
                self.st3[3]=a7
                self.st3[4]=b7
                self.st3[5]=c7
            else:
                self.st3[3]=a7
                self.st3[4]=c7
                self.st3[5]=b7
        if b7>=a7 and b7>=c7:
            if a7>=c7:
                self.st3[3]=b7
                self.st3[4]=a7
                self.st3[5]=c7
            else:
                self.st3[3]=b7
                self.st3[4]=c7
                self.st3[5]=a7

        if c7>=a7 and c7>=b7:
            if b7>=a7:
                self.st3[3]=c7
                self.st3[4]=b7
                self.st3[5]=a7
            else:
                self.st3[3]=c7
                self.st3[4]=a7
                self.st3[5]=b7
            
############## maximize#################

        a8=self.st3[6]
        b8=self.st3[7]
        c8=self.st3[8]
        if a8>=b8 and a8>=c8:
            if b8>=c8:
            
                self.st3[6]=a8
                self.st3[7]=b8
                self.st3[8]=c8
            else:
                self.st3[6]=a8
                self.st3[7]=c8
                self.st3[8]=b8
        if b8>=a8 and b8>=c8:
            if a8>=c8:
                self.st3[6]=b8
                self.st3[7]=a8
                self.st3[8]=c8
            else:
                self.st3[6]=b8
                self.st3[7]=c8
                self.st3[8]=a8

        
        if c8>=a8 and c8>=b8:
            if b5>=a8:
                self.st3[6]=c8
                self.st3[7]=b8
                self.st3[8]=a8
            else:
                self.st3[6]=c8
                self.st3[7]=a8
                self.st3[8]=b8
        ############ stage 4#################
        a9=self.st4[0]
        b9=self.st4[1]
        c9=self.st4[2]
        if a9>=b9 and a9>=c9:
            if b9>=c9:
            
                self.st4[0]=a9
                self.st4[1]=b9
                self.st4[2]=c9
            else:
                self.st4[0]=a9
                self.st4[1]=c9
                self.st4[2]=b9
        if b9>=a9 and b9>=c9:
            if a9>=c9:
                self.st4[0]=b9
                self.st4[1]=a9
                self.st4[2]=c9
            else:
                self.st4[0]=b9
                self.st4[1]=c9
                self.st4[2]=a9
        if c9>=a9 and c9>=b9:
            if b9>=a9:
                self.st4[0]=c9
                self.st4[1]=b9
                self.st4[2]=a9
            else:
                self.st4[0]=c9
                self.st4[1]=a9
                self.st4[2]=b9
                
    
############## maximize#################
        a10=self.st4[3]
        b10=self.st4[4]
        c10=self.st4[5]
        if a10>=b10 and a10>=c10:
            if b10>=c10:
            
                self.st4[3]=a10
                self.st4[4]=b10
                self.st4[5]=c10
            else:
                self.st4[3]=a10
                self.st4[4]=c10
                self.st4[5]=b10
        if b10>=a10 and b10>=c10:
            if a10>=c10:
                self.st4[3]=b10
                self.st4[4]=a10
                self.st4[5]=c10
            else:
                self.st4[3]=b10
                self.st4[4]=c10
                self.st4[5]=a10

        if c10>=a10 and c10>=b10:
            if b10>=a10:
                self.st4[3]=c10
                self.st4[4]=b10
                self.st4[5]=a10
            else:
                self.st4[3]=c10
                self.st4[4]=a10
                self.st4[5]=b10
            
############## maximize#################

        a11=self.st4[6]
        b11=self.st4[7]
        c11=self.st4[8]
        if a11>=b11 and a11>=c11:
            if b11>=c11:
            
                self.st4[6]=a11
                self.st4[7]=b11
                self.st4[8]=c11
            else:
                self.st4[6]=a11
                self.st4[7]=c11
                self.st4[8]=b11
        if b11>=a11 and b11>=c11:
            if a11>=c11:
                self.st4[6]=b11
                self.st4[7]=a11
                self.st4[8]=c11
            else:
                self.st4[6]=b11
                self.st4[7]=c11
                self.st4[8]=a11

        
        if c11>=a11 and c11>=b11:
            if b11>=a11:
                self.st4[6]=c11
                self.st4[7]=b11
                self.st4[8]=a11
            else:
                self.st4[6]=c11
                self.st4[7]=a11
                self.st4[8]=b11
        ####### stage5##################
        a12=self.st5[0]
        b12=self.st5[1]
        c12=self.st5[2]
        if a12>=b12 and a12>=c12:
            if b12>=c12:
            
                self.st5[0]=a12
                self.st5[1]=b12
                self.st5[2]=c12
            else:
                self.st5[0]=a12
                self.st5[1]=c12
                self.st5[2]=b12
        if b12>=a12 and b12>=c12:
            if a12>=c12:
                self.st5[0]=b12
                self.st5[1]=a12
                self.st5[2]=c12
            else:
                self.st5[0]=b12
                self.st5[1]=c12
                self.st5[2]=a12
        if c12>=a12 and c12>=b12:
            if b12>=a12:
                self.st5[0]=c12
                self.st5[1]=b12
                self.st5[2]=a12
            else:
                self.st5[0]=c12
                self.st5[1]=a12
                self.st5[2]=b12
                
    
############## maximize#################
        a13=self.st5[3]
        b13=self.st5[4]
        c13=self.st5[5]
        if a13>=b13 and a13>=c13:
            if b13>=c13:
            
                self.st5[3]=a13
                self.st5[4]=b13
                self.st5[5]=c13
            else:
                self.st5[3]=a13
                self.st5[4]=c13
                self.st5[5]=b13
        if b13>=a13 and b13>=c13:
            if a13>=c13:
                self.st5[3]=b13
                self.st5[4]=a13
                self.st5[5]=c13
            else:
                self.st5[3]=b13
                self.st5[4]=c13
                self.st5[5]=a13

        if c13>=a13 and c13>=b13:
            if b13>=a13:
                self.st5[3]=c13
                self.st5[4]=b13
                self.st5[5]=a13
            else:
                self.st5[3]=c13
                self.st5[4]=a13
                self.st5[5]=b13
            
############## maximize#################

        a14=self.st5[6]
        b14=self.st5[7]
        c14=self.st5[8]
        if a14>=b14 and a14>=c14:
            if b14>=c14:
            
                self.st5[6]=a14
                self.st5[7]=b14
                self.st5[8]=c14
            else:
                self.st5[6]=a14
                self.st5[7]=c14
                self.st5[8]=b14
        if b14>=a14 and b14>=c14:
            if a14>=c14:
                self.st5[6]=b14
                self.st5[7]=a14
                self.st5[8]=c14
            else:
                self.st5[6]=b14
                self.st5[7]=c14
                self.st5[8]=a14

        
        if c14>=a14 and c14>=b14:
            if b14>=a14:
                self.st5[6]=c14
                self.st5[7]=b14
                self.st5[8]=a14
            else:
                self.st5[6]=c14
                self.st5[7]=a14
                self.st5[8]=b14
        #################### stage 6######################

        a15=self.st6[0]
        b15=self.st6[1]
        c15=self.st6[2]
        if a15>=b15 and a15>=c15:
            if b15>=c15:
            
                self.st6[0]=a15
                self.st6[1]=b15
                self.st6[2]=c15
            else:
                self.st6[0]=a15
                self.st6[1]=c15
                self.st6[2]=b15
        if b15>=a15 and b15>=c15:
            if a15>=c15:
                self.st6[0]=b15
                self.st6[1]=a15
                self.st6[2]=c15
            else:
                self.st6[0]=b15
                self.st6[1]=c15
                self.st6[2]=a15
        if c15>=a15 and c15>=b15:
            if b15>=a15:
                self.st6[0]=c15
                self.st6[1]=b15
                self.st6[2]=a15
            else:
                self.st6[0]=c15
                self.st6[1]=a15
                self.st6[2]=b15
                
    
############## maximize#################
        a16=self.st6[3]
        b16=self.st6[4]
        c16=self.st6[5]
        if a16>=b16 and a16>=c16:
            if b16>=c16:
            
                self.st6[3]=a16
                self.st6[4]=b16
                self.st6[5]=c16
            else:
                self.st6[3]=a16
                self.st6[4]=c16
                self.st6[5]=b16
        if b16>=a16 and b16>=c16:
            if a16>=c16:
                self.st6[3]=b16
                self.st6[4]=a16
                self.st6[5]=c16
            else:
                self.st6[3]=b16
                self.st6[4]=c16
                self.st6[5]=a16

        if c16>=a16 and c16>=b16:
            if b16>=a16:
                self.st6[3]=c16
                self.st6[4]=b16
                self.st6[5]=a16
            else:
                self.st6[3]=c16
                self.st6[4]=a16
                self.st6[5]=b16
            
############## maximize#################

        a17=self.st6[6]
        b17=self.st6[7]
        c17=self.st6[8]
        if a17>=b17 and a17>=c17:
            if b17>=c17:
            
                self.st6[6]=a17
                self.st6[7]=b17
                self.st6[8]=c17
            else:
                self.st6[6]=a17
                self.st6[7]=c17
                self.st6[8]=b17
        if b17>=a17 and b17>=c17:
            if a17>=c17:
                self.st6[6]=b17
                self.st6[7]=a17
                self.st6[8]=c17
            else:
                self.st6[6]=b17
                self.st6[7]=c17
                self.st6[8]=a17

        
        if c17>=a17 and c17>=b17:
            if b17>=a17:
                self.st6[6]=c17
                self.st6[7]=b17
                self.st6[8]=a17
            else:
                self.st6[6]=c17
                self.st6[7]=a17
                self.st6[8]=b17




        return(self.st1,self.st2,self.st3,self.st4,self.st5,self.st6)

                                        
                                   
if __name__=='__main__':
    eh=float(input("enter capacity"+" "))
    st=int (input("enter stages"+" "))
    volt=int (input("enter volt"+" "))
    heat=heat11(eh,st,volt)                                                                    
    print(heat.st1,heat.st2,heat.st3,heat.st4,heat.st5,heat.st6)
    print(heat.st1)
    print(heat.st2)
    print(heat.st3)
    print(heat.st4)
    print(heat.st5)
    print(heat.st6)


    

    

                
