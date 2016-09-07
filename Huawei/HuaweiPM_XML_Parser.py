# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 14:46:03 2016

@author: Gerardo Alfredo Alarcon Rivas
"""
'''This function saves take a string and save this in a new line of the input file'''
def logger(cadena, file_):
         f = open(file_, 'a')
         f.write(cadena+"\n") # python will convert \n to os.linesep
         f.close()

'''The parser take on xml file and create a tree form this
the code write and output file in a tabular format with all the elements of the
initial file. THe code can parse the exported xml files from Huawei PM counters
from all the levels'''
def XML_Parser_PMHUAWEi(XML_FILE, OutPut_dir):
    import xml.etree.ElementTree as ET
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    header= ['fileFormatVersion','vendorName','elementType','beginTime','endTime','userLabel','Duration','MeasTypes','MeasInfoId','meas_objLdn','MeasResults']
    cade=[]
    fileFormatVersion,vendorName,elementType,beginTime,endTime,userLabel,Duration,MeasTypes,MeasInfoId,meas_objLdn,MeasResults="","","","","","","","","","",""
    logger('\t'.join(header),OutPut_dir)
    '''This block take the fileformat, vendorName,elementType and begin time'''
    for node in root.findall('{http://latest/nmc-omc/cmNrm.doc#measCollec}fileHeader'):
        fileFormatVersion=str(node.get('fileFormatVersion'))
        vendorName=str(node.get('vendorName'))
        for nr in node.findall('{http://latest/nmc-omc/cmNrm.doc#measCollec}fileSender'):
            elementType=str(nr.get('elementType'))
            
        for key in node.findall('{http://latest/nmc-omc/cmNrm.doc#measCollec}measCollec'):
            beginTime=str(key.get('beginTime'))
        #print temp_line
    '''This block take the end time of the xml'''
    for node in root.findall('{http://latest/nmc-omc/cmNrm.doc#measCollec}fileFooter'):
        for g in node.findall('{http://latest/nmc-omc/cmNrm.doc#measCollec}measCollec'):
                endTime=str(g.get("endTime"))
        #print '\t'.join(header)
        #print '\t'.join(temp_line)
    '''This block take the label of the element'''
    for node in root.findall('{http://latest/nmc-omc/cmNrm.doc#measCollec}measData'):
        #print node  
        for g in node.findall("{http://latest/nmc-omc/cmNrm.doc#measCollec}managedElement"):
            userLabel=str(g.get('userLabel'))
        #print '\t'.join(temp_line)
    
        for g in node.findall("{http://latest/nmc-omc/cmNrm.doc#measCollec}measInfo"):
                #print g.tag,"\n"
                                
            for po in g.findall("{http://latest/nmc-omc/cmNrm.doc#measCollec}granPeriod"):
                    Duration=str(po.get("duration"))
                    #print po.get('duration')
                
            for po in g.findall("{http://latest/nmc-omc/cmNrm.doc#measCollec}measTypes"):
                    MeasTypes=str(po.text)                 
                    #print po.text                
                    MeasInfoId=str(g.get('measInfoId'))
               
                
                
                
            for io in g.findall("{http://latest/nmc-omc/cmNrm.doc#measCollec}measValue"):
                   # print io.get("measObjLdn")
                    meas_objLdn=str(io.get("measObjLdn"))
                    for e in io.findall("{http://latest/nmc-omc/cmNrm.doc#measCollec}measResults"):
                        MeasResults=e.text
                        # header                        
                        #fileFormatVersion,#0
                        #vendorName,#1
                        #elementType,#2
                        #beginTime,#3
                        #endTime,#4
                        #userLabel,#5
                        #Duration,#6
                        #MeasTypes,#7
                        #MeasInfoId,#8
                        #meas_objLdn,#9
                        #MeasResults#10
                        cade=[fileFormatVersion,vendorName,elementType,beginTime,endTime,userLabel,Duration,MeasTypes,MeasInfoId,meas_objLdn,MeasResults]
                        logger( '\t'.join(cade),OutPut_dir)
                        
                        
            
    #print '\t'.join(header)
    #print '\t'.join(temp_line)
   
    tempo="dfsdf"
  
    return tempo

XML_Parser_PMHUAWEi('C:\Users\VervebaMX2\Documents\Projects\XML Parsing\XML Files\HuaweiPM\MBTS-HMEX0036\A20160725.2300-0500-0000-0500_MBTS-HMEX0036.xml','C:\Users\VervebaMX2\Documents\Projects\Python Scripts\CM&PM Parsers\HuaweiPM_XML_Parser\Logs\loggy2.txt')




