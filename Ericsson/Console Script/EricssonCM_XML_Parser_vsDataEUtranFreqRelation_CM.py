# -*- coding: utf-8 -*-
"""
Created on Thursday september 01 14:46:03 2016

@author: Gerardo Alfredo Alarcon Rivas
Load the XML Dump of Ericsson(vsDataEUtranCellFreqRelation) and return the information in tabular format 
"""
import time
import sys
import pandas as pd

def update_progress_bar():
    print '\b.',sys.stdout.flush()

def EricssonCMParser(XML_FILE,OutPut_dir):
  print 'Starting ',sys.stdout.flush()

  import xml.etree.ElementTree as ET
  tree = ET.parse(XML_FILE)
  root = tree.getroot()
  header= ['Region','ENodeBname','CellName','EUtranFrequency','eutranFreqToQciProfileRelation','blackListEntryIdleMode','cellReselectionPriority','pMax','qRxLevMin','tReselectionEutra','tReselectionEutraSfHigh','tReselectionEutraSfMedium','userLabel','allowedMeasBandwidth','presenceAntennaPort1','qOffsetFreq','threshXHigh','threshXLow','allowedPlmnList1','allowedPlmnList2','allowedPlmnList3','adjacentFreq','connectedModeMobilityPrio','createdBy','lastModification','mobilityAction','timeOfCreation','timeOfLastModification','qQualMin','threshXHighQ','threshXLowQ','neighCellConfig','voicePrio','blackListEntry','interFreqMeasType','lbBnrPolicy','lbActivationThreshold','anrMeasOn','caTriggeredRedirectionActive','arpPrio','nonPlannedPhysCellIdRange','nonPlannedPciTargetIdType','nonPlannedPhysCellId','nonPlannedPciCIO','a5Thr1RsrqFreqOffset','a5Thr1RsrpFreqOffset','a5Thr2RsrpFreqOffset','a5Thr2RsrqFreqOffset','candNeighborRel']  
  data={}
  temp={}
  df = pd.DataFrame()
  for i in header:
      data.update({str(i):''})
  time.sleep(1)
  update_progress_bar()
  '''This block take the fileformat, vendorName,elementType and begin time'''
  # Assign head
                                      
  for node in root.findall('{configData.xsd}configData'):
      print 'node: ',node.tag 
      for child1 in node:
          
           print 'child1: ',child1.tag
           for child2 in child1:
              data['Region']=str(child2.get('id'))
               
              print 'child2     '+child2.get('id')
              #print new_line
              for child3 in child2:
                  
                  #print 'child 3  '+str(child3.get('id'))
                  #new_line.append(str(child3.get('id'))) 
                  #print new_line+new_line2
                  data['ENodeBname']=str(child3.get('id'))
                  for child4 in child3:
                      
                      for child5 in child4.findall('{genericNrm.xsd}VsDataContainer'):
                          
                          for child6 in child5.findall('{genericNrm.xsd}VsDataContainer'):
                            
                             data['CellName']=str(child6.get('id'))
                            
                             
                             for child7 in child6.findall('{genericNrm.xsd}VsDataContainer'):
                                 #print 'child7   ' +str(child7.get('id'))
                                 data['EUtranFrequency']=str(child7.get('id'))
                                 for child8 in child7.iter('{genericNrm.xsd}VsDataContainer'):
                                     #print 'child8:  '+str(child8.tag)
                                     for child9 in child8:
                                         for child10 in child9:
                                             l=1
                                             
                                             for child11 in child10:
                                                 if str(child11.tag).replace("{EricssonSpecificAttributes.15.25.xsd}",'')=="allowedPlmnList":
                                                     for child12 in child11:
                                                         temp.update({str(child12.tag).replace("{EricssonSpecificAttributes.15.25.xsd}",''):child12.text})
                                                     data["allowedPlmnList"+ str(l)]=str(' '.join("%s=%r" % (key,val) for (key,val) in temp.iteritems()))    
                                                     
                                                     l=l+1
                                                 else:
                                                     data[str(child11.tag).replace("{EricssonSpecificAttributes.15.25.xsd}",'')]=str(child11.text)
                                         df = df.append(data, ignore_index=True)
                  df.to_csv(OutPut_dir, sep='\t')
  print ' Done!'
                                                 
                                 
                                
                                 
#EricssonCMParser('C:\Users\VervebaMX2\Documents\Projects\XML Parsing\TEst\LTE\4gEUTranFreqRelation\cm_exp_20160831_LTE_BAJACSUR_EUtranFreqRelation.xml','C:\Users\VervebaMX2\Documents\Projects\XML Parsing\TEst\LTE\4gEUTranFreqRelation\cm_exp_20160831_LTE_BAJACSUR_EUtranFreqRelation.txt')
first_arg = sys.argv[1]
second_arg = sys.argv[2]

if __name__ == "__main__":
    EricssonCMParser(first_arg,second_arg)