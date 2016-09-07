# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 14:46:03 2016

@author: Gerardo Alfredo Alarcon Rivas
Load the XML Dump of Ericsson(enodeb mnc) and return the information in tabular format 
"""
import sys
def logger(cadena,file_):
         f = open(file_,'a')
         f.write(cadena+"\n") # python will convert \n to os.linesep
         f.close()
#import timeit
def EricssonCMParser(XML_FILE,OutPut_dir):#
  import xml.etree.ElementTree as ET
  tree = ET.parse(XML_FILE)
  root = tree.getroot()
  header= ['fileFormatVersion','vendorName','DateTime','Sub network ID','Subnetwork Name','MeContext']  
  temp=[]
  new_line=[]
  new_line2=[]
  new_line3=[]
  #cade=[]
  #fileFormatVersion,vendorName,elementType,beginTime,endTime,userLabel,Duration,MeasTypes,MeasInfoId,meas_objLdn,MeasResults="","","","","","","","","","",""
  #logger('\t'.join(header),OutPut_dir)
  '''This block take the fileformat, vendorName,elementType and begin time'''
  # Assign headers  
 
  for node in root.findall('{configData.xsd}configData'):
        #print node.tag
      
        for child2 in node:
                #print child2.get('id')
                for child3 in child2:
                    #print child3.get('id')
                    for child4 in child3:#Mecontext
                        #print child4.tag
                        for child5 in child4:
                            #print child5.tag
                            for child6 in child5:
                                 #print child6.tag
                                 
                                  for child7 in child6:
                                    #print child7.tag                                           
                                            for child8 in child7.findall('{EricssonSpecificAttributes.15.25.xsd}vsDataENodeBFunction'):
                                                #print child8
                                                for child9 in child8:
                                                    if str(child9.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','',1) in temp :
                                                        pass
                                                    elif child9.tag!='eNodeBPlmnId':
                                                        if child9.tag!='eNodeBPlmnId':
                                                            temp.append(str(child9.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','',1))
                                    
                                                               
                                                                
                                                        
                                                    
                                                   
                                                    #print temp
                                            
                                        
                                           #  print str(child9.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','',1),child9.text
  
  temp.append('MCC')
  temp.append('MNC') 
  temp.append('MNCLenght')  
  logger("\t".join(header+temp),  OutPut_dir)                                      
  
  for node in root.findall('{configData.xsd}fileHeader'):
      new_line=[]
      new_line.append(str(node.get('fileFormatVersion')))
      new_line.append(str(node.get('vendorName')))
      #print new_line 
  for node in root.findall('{configData.xsd}fileFooter'):
      new_line.append(str(node.get('dateTime')))
      #print new_line
  for node in root.findall('{configData.xsd}configData'):
      #print node.tag 
      for child1 in node:
           new_line.append(str(child1.get('id')))
           #print new_line
           for child2 in child1:
              new_line.append(str(child2.get('id'))) 
              #print new_line
              for child3 in child2:
                    new_line2=[]
                    new_line2.append(str(child3.get('id')))
                    #print new_line+new_line2
                    for child4 in child3:#Mecontext
                        #print child4.tag
                        for child5 in child4:
                            #print child5.tag
                            for child6 in child5:
                                 #print child6.tag
                                 for child7 in child6.findall('{EricssonSpecificAttributes.15.25.xsd}vsDataENodeBFunction'):
                                     for child8 in child7:
                                                new_line3=[]
                                                new_line2.append(str(child8.text))
                                                for child9 in child8:
                                                        new_line3.append(str(child9.text))
                                                        temp=list(new_line3)              
                                     
                                     #print '\t'.join(temp)
                                     logger( ("\t".join(new_line+new_line2+temp).replace('\n','')),OutPut_dir)
                                            #for child9 in child8:
                                              #  if str(child9.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','',1) in temp:
                                                       # pass
                                               # else:
                                                #    temp.append(str(child9.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','',1))
                                                    

EricssonCMParser('C:\Users\VervebaMX2\Documents\Projects\LTE XML OSS ERICSSON FILES\ENodeBFunction\cm_exp_20160812_LTE.xml','C:\Users\VervebaMX2\Documents\Python Scripts\Compilados\Test.txt')
