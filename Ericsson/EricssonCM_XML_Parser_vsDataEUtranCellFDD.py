# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 14:46:03 2016

@author: Gerardo Alfredo Alarcon Rivas
Load the XML Dump of Ericsson(vsDataEUtranCellFDD) and return the information in tabular format 
"""
def logger(cadena,file_):
         f = open(file_,'a')
         f.write(cadena+"\n") # python will convert \n to os.linesep
         f.close()
#import timeit
def EricssonCMParser(XML_FILE,OutPut_dir):#
  import xml.etree.ElementTree as ET
  tree = ET.parse(XML_FILE)
  root = tree.getroot()
  header= ['fileFormatVersion','vendorName','DateTime','Sub network ID','Subnetwork Name','MeContext','Cell']  
  temp=[]
  new_line=[]
  diction={}
  cade=[]
  #fileFormatVersion,vendorName,elementType,beginTime,endTime,userLabel,Duration,MeasTypes,MeasInfoId,meas_objLdn,MeasResults="","","","","","","","","","",""
  #logger('\t'.join(header),OutPut_dir)
  '''This block take the fileformat, vendorName,elementType and begin time'''
  # Assign headers  

  
 
  for node in root.findall('{configData.xsd}configData'):
        #print node.attrib
      
        for child2 in node:
                new_line.append(child2.get('id'))# subnetwork id
                #print new_line
                for child3 in child2:
                    new_line.append(child3.get('id'))#subnetwork name
                    #print new_line
                    for child4 in child3:#Mecontext
                        #print child4.attrib
                        for child5 in child4:
                            #print child5.tag
                            for child6 in child5:
                                 #print child6.tag
                                 for child7 in child6:
                                    #print child7.attrib #cell                                         
                                    for child8 in child7:
                                         #print child8
                                         for child9 in child8:
                                             #print child9.tag
                                             for child10 in child9.iter('{EricssonSpecificAttributes.15.25.xsd}vsDataEUtranCellFDD'):
                                                #print child9.attrib
                                                for child11 in child10:#.findall('{EricssonSpecificAttributes.15.25.xsd}vsDataEUtranCellFDD'):
                                                     if str(child11.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','',1) in temp:
                                                         pass
                                                     else:
                                                         temp.append(str(child11.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','',1))
  
  
  logger( str('\t'.join(header+temp)).replace('\n',''),OutPut_dir )                                               #for child12 in child11:
  for n in (header+temp):
        diction.update({n:''})
        #print n
  new_line=list(header+temp)
  #print diction.viewitems()                                                
                                                      
  
  
  
  for node in root.findall('{configData.xsd}fileHeader'):
      
      diction['fileFormatVersion']=str(node.get('fileFormatVersion'))
      diction['vendorName']=str(node.get('vendorName'))
      #print new_line 
  
  for node in root.findall('{configData.xsd}fileFooter'):
        diction['DateTime']=str(node.get('dateTime'))
        #print new_line
  #logger("\t".join(header+temp),  OutPut_dir)                                      
  for node in root.findall('{configData.xsd}configData'):
      #print node.tag 
      for child1 in node:
           diction['Sub network ID']=str(child1.get('id'))
           #print new_line
           for child2 in child1:
              diction['Subnetwork Name']=str(child2.get('id')) 
              #print new_line
              for child3 in child2:
                  diction['MeContext']=str(child3.get('id'))
                  #print 'child 3  '+str(child3.get('id'))
                  #new_line.append(str(child3.get('id'))) 
                  #print new_line+new_line2
                  for child4 in child3:
                      
                      for child5 in child4.findall('{genericNrm.xsd}VsDataContainer'):
                          #print 'child5     '+child5.tag
                          for child6 in child5.findall('{genericNrm.xsd}VsDataContainer'):
                             #print child6.tag
                             diction['Cell']=str(child6.get('id'))
                             #print "child6  "+str(child6.get('id'))
                             cade=[]
                             for child7 in child6.iter('{EricssonSpecificAttributes.15.25.xsd}vsDataEUtranCellFDD'):
                                 for child8 in child7:
                                     diction[str(child8.tag).replace("{EricssonSpecificAttributes.15.25.xsd}",'')]=child8.text
                                     #print "child8  "+str(child8.tag).replace("{EricssonSpecificAttributes.15.25.xsd}",'')
                                 
                                 for g in new_line:
                                     cade.append(str(diction.get(g)))
                                     #print diction.get(g)
                                 #logger(str('\t'.join(diction.values())).replace('\n',''),OutPut_dir)
                                 logger(str('\t'.join(cade)).replace('\n',''),OutPut_dir)          
#EricssonCMParser('C:\Users\VervebaMX2\Documents\Projects\LTE XML OSS ERICSSON FILES\EUtranCellFDD\cm_exp_20160812_LTE_CHIHUAHUA.xml','C:\Users\VervebaMX2\Documents\Projects\Python Scripts\CM&PM Parsers\CM-and-PM-ericsson-and-huawei-parsers\Test Folder\Ericsson CM\Result\eutra.txt')

EricssonCMParser('C:\Users\VervebaMX2\Documents\Projects\XML Parsing\TEst\LTE\cm_exp_20160831_LTE_TIJUANA_EUTranCellFDD.xml','C:\Users\VervebaMX2\Documents\Projects\XML Parsing\TEst\LTE\cm_exp_20160831_LTE_BAJACSUR_EUTranCellFDD_.txt')                                 
