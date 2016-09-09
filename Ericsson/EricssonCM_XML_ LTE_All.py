# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 11:15:45 2016

@author: Gerardo Alfredo Alarcon Rivas
"""

import os.path
import collections
def logger(cadena, file_):
         f = open(file_, 'a')
         f.write(cadena+"\n") # python will convert \n to os.linesep
         f.close()
def merge_dicts(*dict_args):
    '''
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result
'''The parser take on xml file and create a tree form this
the code write and output file in a tabular format with all the elements of the
initial file. THe code can parse the exported xml files from Ericsson  CM LTE parameters
from all the levels'''
def XML_ParserEricsson_CM_LTEFUll(XML_FILE, OutPut_dir):
    
    import xml.etree.ElementTree as ET
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    temps=[]    
    headers=[]
    headers2=""
    lines= []
    
    temp1=collections.OrderedDict()
    temp=collections.OrderedDict()
    temp2=collections.OrderedDict()
    info=collections.OrderedDict()
    info={'id':''}
    Area_name=''
    Table_name=''
    
    
    
    '''This BLock ontain the RNC Info only'''
    for node in root.findall('{configData.xsd}fileFooter'):
        Date=dict(node.attrib).get('dateTime')
            
    for node in root.findall('{configData.xsd}configData'):
        for child1 in node:  
            for child2 in child1.findall('{genericNrm.xsd}SubNetwork'):
                #print child2.tag,dict(child2.attrib).get('id')
                Area_name=str(dict(child2.attrib).get('id'))
                #print 'Area_Name',Area_name
                
                # This block fill the information of the NodeB
                for child3 in child2.findall('{genericNrm.xsd}MeContext'):
                   '''   
                   for child4 in child3.findall('{genericNrm.xsd}VsDataContainer'):
                        headers.append('dateTime')                        
                        headers.append('Area_Name')
                        lines.appen(Date)                        
                        lines.append(Area_name)
                        #print 'NodeB',dict(child3.attrib).get('id')
                        headers.append('CellId')
                        lines.append(str(dict(child3.attrib).get('id')))
                        #print child4.attrib
                        for child5 in child4.iter():
                            if str(str(child5.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','')).replace('{genericNrm.xsd}','')=='vsDataType':
                                 Table_name= str(child5.text)
                                
                           # print (str(child5.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','')).replace('{genericNrm.xsd}',''),child5.text
                            headers.append(str(str(child5.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','')).replace('{genericNrm.xsd}',''))
                            lines.append(str(child5.text))
                        if os.path.exists(OutPut_dir+Area_name+'_'+Table_name+'.txt')!=True:
                            logger('\t'.join(headers).replace('\n',''),OutPut_dir+Area_name+'_'+Table_name+'.txt')
                        #print '\t'.join(headers).replace('\n','')
                        logger('\t'.join(lines).replace('\n',''),OutPut_dir+Area_name+'_'+Table_name+'.txt')
                        #print '\t'.join(lines).replace('\n','')
                        headers=[]
                        lines=[]
                     '''        
                        
                   # This block fill the information of the MO NodeB       
                   
                   for child4 in child3.findall('{genericNrm.xsd}ManagedElement'):
                      # print child4.attrib
                        headers.append("dateTime")
                        headers.append('Area_Name')
                        lines.append(Date)
                        lines.append(Area_name)
                        #print 'NodeB',dict(child3.attrib).get('id')
                        headers.append('CellId')
                        lines.append(str(dict(child3.attrib).get('id')))
                        for child5 in child4.findall('{genericNrm.xsd}attributes'):
                           for child6 in child5:
                               headers.append(str(child6.tag).replace('{genericNrm.xsd}',''))
                               lines.append(str(child6.text))
                               print str(child6.tag).replace('{genericNrm.xsd}',''),child6.text
                        if os.path.exists(OutPut_dir+Area_name+'_EnodeBInfo.txt')!=True:
                            logger('\t'.join(headers).replace('\n',''),OutPut_dir+Area_name+'_EnodeBInfo.txt')
                        #print '\t'.join(headers).replace('\n','')
                        logger('\t'.join(lines).replace('\n',''),OutPut_dir+Area_name+'_EnodeBInfo.txt')
                        #print '\t'.join(lines).replace('\n','')
                        headers=[]
                        lines=[]
                
         #   pass
            
         
            
            
XML_ParserEricsson_CM_LTEFUll('C:\Users\VervebaMX2\Documents\Projects\XML_Parsing\TEst\LTE\cm_exp_20160831_LTE_ALL\cm_exp_20160831_LTE_BAJACSUR_ALL.xml','C:/Users/VervebaMX2/Documents/Projects/XML_Parsing/TEst/LTE/cm_exp_20160831_LTE_ALL/Test/')
