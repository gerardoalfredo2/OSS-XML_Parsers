# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 11:15:45 2016

@author: Gerardo Alfredo Alarcon Rivas
"""
import sys
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
    
def get_files(directory,exte):
 files_name=[]
 import glob
 print directory+exte
 files_name= glob.glob(directory+exte)
 return files_name
 
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
                   CellId=str(dict(child3.attrib).get('id'))
                   
                   for child4 in child3.findall('{genericNrm.xsd}VsDataContainer'):
                        headers.append('dateTime')                        
                        headers.append('Area_Name')
                        lines.append(Date)                        
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
                        if os.path.exists(OutPut_dir+Table_name+'.txt')!=True:
                            logger('\t'.join(headers).replace('\n',''),OutPut_dir+Table_name+'.txt')
                        #print '\t'.join(headers).replace('\n','')
                        logger('\t'.join(lines).replace('\n',''),OutPut_dir+Table_name+'.txt')
                        #print '\t'.join(lines).replace('\n','')
                        headers=[]
                        lines=[]
                         
                        
                   # This block fill the information of the MO NodeB       
                   
                   for child4 in child3.findall('{genericNrm.xsd}ManagedElement'):
                        Id2=str(dict(child4.attrib).get('id'))
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
                               #print str(child6.tag).replace('{genericNrm.xsd}',''),child6.text
                        if os.path.exists(OutPut_dir+'EnodeBInfo.txt')!=True:
                            logger('\t'.join(headers).replace('\n',''),OutPut_dir+'EnodeBInfo.txt')
                        #print '\t'.join(headers).replace('\n','')
                        logger('\t'.join(lines).replace('\n',''),OutPut_dir+'EnodeBInfo.txt')
                        #print '\t'.join(lines).replace('\n','')
                        headers=[]
                        lines=[]
                      
                        
                        #This block take the other mo
                   # This block fill the information of the MO NodeB       
                   
                   for child4 in child3.findall('{genericNrm.xsd}ManagedElement'):
                      # print child4.attrib
                        
                        for child5 in child4.findall('{genericNrm.xsd}VsDataContainer'):
                            #print '----->child5',child5.tag,child5.attrib,child5.text
                            for child6 in child5.findall('{genericNrm.xsd}attributes'):
                                # print '-------->child6: ',str(child6.tag).replace('{EricssonSpecificAttributes.15.25.xsd}',''),child6.attrib
                                 headers.append('DateTime')
                                 lines.append(Date)
                                 headers.append("AreaName")
                                 lines.append(Area_name)
                                 headers.append("EnodeBId")
                                 lines.append(CellId)
                                 headers.append('Id2')
                                 lines.append(Id2)
                                 for child7 in child6:
                                    if str(child7.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','').replace('{genericNrm.xsd}','')=='vsDataType':
                                        Table_name=str(child7.text)
                                    headers.append(str(child7.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','').replace('{genericNrm.xsd}',''))
                                    lines.append(str(child7.text))
                                   # print '------------>child7: ',child7.text
                                    for child8 in child7:
                                     
                                        if len(child8)>0:
                                            temp2={}
                                            for child9 in child8.iter():
                                                temp2.update({(str(child9.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','')).replace('{genericNrm.xsd}',''):str(child9.text).replace('\n','')})
                                            headers.append(str(child8.tag).replace('{EricssonSpecificAttributes.15.25.xsd}',''))
                                            lines.append(str(','.join(" %s=%r " % (key,val) for (key,val) in temp2.iteritems()))) 
                                        else:
                                            headers.append(str(child8.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','').replace('{genericNrm.xsd}',''))
                                            lines.append(str(child8.text))
                                          #  print '--------------->child8: ',str(child8.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','').replace('{genericNrm.xsd}',''),child8.text
                                 #print "Table_name:",Table_name
                                 if os.path.exists(OutPut_dir+Table_name+'.txt')!=True:
                                     logger('\t'.join(headers).replace('\n',''),OutPut_dir+Table_name+'.txt')
                                 logger('\t'.join(lines).replace('\n',''),OutPut_dir+Table_name+'.txt')
                                 lines=[]
                                 headers=[]                                    
                   
                   
                   #
                   for child4 in child3.findall('{genericNrm.xsd}ManagedElement'):
                      # print child4.attrib
                        Id2=str(dict(child4.attrib).get('id'))
                        for child5 in child4.findall('{genericNrm.xsd}VsDataContainer'):
                            #print '----->child5',child5.tag,child5.attrib,child5.text
                            for child6 in child5.findall('{genericNrm.xsd}VsDataContainer'):
                                 Id3=str(dict(child6.attrib).get('id'))
                                 #print '-------->child6: ',str(child6.tag).replace('{EricssonSpecificAttributes.15.25.xsd}',''),child6.attrib
                                 headers.append('DateTime')
                                 lines.append(Date)
                                 headers.append("AreaName")
                                 lines.append(Area_name)
                                 headers.append("EnodeBId")
                                 lines.append(CellId)
                                 headers.append('Id2')
                                 lines.append(Id2)
                                 headers.append('Id3')
                                 lines.append(Id3)
                                 for child7 in child6.findall('{genericNrm.xsd}attributes'):
                                   #print child7.tag,child7.attrib 
                                   for child8 in child7:
                                       #print child8.tag,child8.text
                                       headers.append(str(child8.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','').replace('{genericNrm.xsd}',''))
                                       lines.append(str(child8.text))
                                       #print str(child8.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','').replace('{genericNrm.xsd}',''),child8.text
                                       if str(child8.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','').replace('{genericNrm.xsd}','')=='vsDataType':
                                               Table_name=str(child8.text).replace('{genericNrm.xsd}','')
                                        #       print Table_name
                                       for child9 in child8:
                                           #print str(child9.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','').replace('{genericNrm.xsd}',''),child9.text
                                           
                                           #headers.append(str(child9.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','').replace('{genericNrm.xsd}',''))
                                           #lines.append(str(child9.text))
                                           #print '------------>child7: ',child7.text
                                          
                                           if len(child9)>0:
                                                     temp2={}
                                                     for child10 in child9:
                                                         temp2.update({(str(child10.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','')).replace('{genericNrm.xsd}',''):str(child10.text)})
                                                     headers.append(str(child9.tag).replace('{EricssonSpecificAttributes.15.25.xsd}',''))
                                                     lines.append(str(','.join(" %s=%r " % (key,val) for (key,val) in temp2.iteritems()))) 
                                           else:
                                                     headers.append(str(child9.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','').replace('{genericNrm.xsd}',''))
                                                     lines.append(str(child9.text))
                                            # print '--------------->child9: ',str(child9.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','').replace('{genericNrm.xsd}',''),child9.text
                                       #print "Table_name:",Table_name
                                   if os.path.exists(OutPut_dir+Table_name+'.txt')!=True:
                                          logger('\t'.join(headers).replace('\n',''),OutPut_dir+Table_name+'.txt')
                                   logger('\t'.join(lines).replace('\n',''),OutPut_dir+Table_name+'.txt')
                                   lines=[]
                                   headers=[] 
                                   
                                   
                                   
                                   
                   for child4 in child3.findall('{genericNrm.xsd}ManagedElement'):
                      # print child4.attrib
                        Id2=str(dict(child4.attrib).get('id'))
                        for child5 in child4.findall('{genericNrm.xsd}VsDataContainer'):
                            #print '----->child5',child5.tag,child5.attrib,child5.text
                            for child6 in child5.findall('{genericNrm.xsd}VsDataContainer'):
                                 Id3=str(dict(child6.attrib).get('id'))
                                 #print '-------->child6: ',str(child6.tag).replace('{EricssonSpecificAttributes.15.25.xsd}',''),child6.attrib
                                
                                 for child7 in child6.findall('{genericNrm.xsd}VsDataContainer'):
                                   Id4=dict(child7.attrib).get('id')
                                 
                                   #print "Child7:  ",child7.tag,child7.attrib 
                                   for child8 in child7.findall('{genericNrm.xsd}attributes'):
                                       #print "child8: ",child8.tag,child8.text
                                       for child9 in child8:
                                           headers.append(str(child9.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','').replace('{genericNrm.xsd}',''))
                                           lines.append(str(child9.text))
                                           #print "child9: ",child9.tag,child9.text
                                           if str(child9.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','').replace('{genericNrm.xsd}','')=='vsDataType':
                                                       Table_name=str(child9.text).replace('{genericNrm.xsd}','')
                                                      # print Table_name
                                           for child10 in child9:
                                              # print "child10: ",child10.tag.replace('{EricssonSpecificAttributes.15.25.xsd}','').replace('{genericNrm.xsd}',''),child10.text
                                               #headers.append(str(child10.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','').replace('{genericNrm.xsd}',''))
                                               #lines.append(str(child10.text))
                                               
                                               if len(child10)>0:
                                                         temp2={}
                                                         for child11 in child10:
                                                             temp2.update({(str(child11.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','')).replace('{genericNrm.xsd}',''):str(child11.text)})
                                                         headers.append(str(child10.tag).replace('{EricssonSpecificAttributes.15.25.xsd}',''))
                                                         lines.append(str(','.join(" %s=%r " % (key,val) for (key,val) in temp2.iteritems()))) 
                                               else:
                                                         headers.append(str(child10.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','').replace('{genericNrm.xsd}',''))
                                                         lines.append(str(child10.text))
                                               #print '--------------->child9: ',str(child9.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','').replace('{genericNrm.xsd}',''),child9.text
                                           #print "Table_name:",Table_name
                                   
                                   
                                   headers.insert(0,'Id4')
                                   lines.insert(0,Id4)
                                   headers.insert(0,'Id3')
                                   lines.insert(0,Id3)
                                   headers.insert(0,'Id2')
                                   lines.insert(0,Id2)
                                   headers.insert(0,"EnodeBId")
                                   lines.insert(0,CellId)
                                   headers.insert(0,"AreaName")
                                   lines.insert(0,Area_name)
                                   headers.insert(0,'DateTime')
                                   lines.insert(0,Date)
                                   
                                   
                                   
                                   
                                   
                                   
                                   if os.path.exists(OutPut_dir+Table_name+'.txt')!=True:
                                              logger('\t'.join(headers).replace('\n',''),OutPut_dir+Table_name+'.txt')
                                   logger('\t'.join(lines).replace('\n',''),OutPut_dir+Table_name+'.txt')
                                   lines=[]
                                   headers=[] 
                                   
                                   
                                   
                                   
                                   

                                            
                             
                                    
                        
         #   pass
            
         
            
    print "Parse Done....."             
#XML_ParserEricsson_CM_LTEFUll('C:\Users\VervebaMX2\Documents\Projects\XML_Parsing\TEst\LTE\cm_exp_20160831_LTE_ALL\cm_exp_20160831_LTE_BAJACSUR_ALL.xml','C:/Users/VervebaMX2/Documents/Projects/XML_Parsing/TEst/LTE/cm_exp_20160831_LTE_ALL/Test/')
                               
def main_process(directory_in,directory_out):
    files=[]
    files=list(get_files(directory_in,"*.xml"))
    for file_ in files:
        print 'Processing:'+directory_in+file_
        XML_ParserEricsson_CM_LTEFUll(file_,directory_out)
        print 'Result in : '+directory_out
first_arg = sys.argv[1]
second_arg = sys.argv[2]

if __name__ == "__main__":
    main_process(first_arg,second_arg)