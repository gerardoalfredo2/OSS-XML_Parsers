# -*- coding: utf-8 -*-
"""
Created on Wednesday Aug 18 09:33:24 2016

@author: Gerardo Alfredo Alarcon Rivas
"""

'''This function saves take a string and save this in a new line of the input file'''
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
initial file. THe code can parse the exported xml files from Ericsson  PM counters por RNC
from all the levels'''
def XML_ParserEricsson_CM_RNC(XML_FILE, OutPut_dir):
    
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
    RNC_name=''
    
    
    
    '''This BLock ontain the RNC Info only'''
    #print '<<<<Writing RNC Info>>>>'
    for node in root.findall('{configData.xsd}configData'):
        #print 'root: ',node
        for child1 in node:
            #print 'child1: ',child1
            for child2 in child1:
                #print "child2: ",child2.tag,"\n"
                #print child2.attrib#RNC ID
                for child3 in child2:#MeContext
                    #print "child3: ",child3.tag,"\n"
                    RNC_name=(str(dict(child3.attrib).get('id')))
                    #print child3.attrib#RNC ID
                    
                    for child4 in child3.findall('{genericNrm.xsd}VsDataContainer'):
                        #print "child4: ",child4.tag,"\n"
                        for child5 in child4:
                            #print "child5: ",child5.tag,child5.text,"\n"
                            for child6 in child5:
                             #   print "child6: ",child6.tag,child6.text,"\n"
                                for child7 in child6:
                            #        print "child6: ",str(child7.tag).replace('{EricssonSpecificAttributes.15.25.xsd}',""),child7.text,"\n"
                                    temp.update({str(child7.tag).replace('{EricssonSpecificAttributes.15.25.xsd}',''):str(child7.text)})
                                    headers.append(str(child7.tag).replace('{EricssonSpecificAttributes.15.25.xsd}',''))
                                    lines.append(str(child7.text))
                                    
                                
                            headers.insert(0,'RNC_Name')
                            lines.insert(0,RNC_name)                                
                            logger('\t'.join(headers),OutPut_dir+RNC_name+'_RNC_Info.txt')
                            logger('\t'.join(lines),OutPut_dir+RNC_name+'_RNC_Info.txt')

                            #logger('\t'.join(list((temp.keys()))),OutPut_dir+RNC_name+'_RNC_Info.txt')
                            #logger('\t'.join(list((temp.values()))),OutPut_dir+RNC_name+'_RNC_Info.txt')
                                
                            #print(temp.values())
                            temp.clear()
                            headers=[]
                            lines=[]
                    
                    
                    #This block take the Utran cell information and the MO
                    #print '<<<<UtranCell Info>>>>'
                    
                    for child4 in child3.findall('{genericNrm.xsd}ManagedElement'):
                        #print "child4: ",child4.tag,"\n"
                        for child5 in child4.findall('{utranNrm.xsd}RncFunction'):
                            #print "child5: ",child5.tag,"\n"
                            
                            for child6 in child5.findall('{utranNrm.xsd}UtranCell'):
                                info['id']=str(dict(child6.attrib).get('id'))
                                #print child6.tag,child6.attrib
                               # print '\r '+info.get('id')
                                #print child6.tag
                                
                                #This block parse the Utran cells info
                                
                                for child7 in child6.findall('{utranNrm.xsd}attributes'):
                                    temp.update({'id':info.get('id')})                                    
                                    for child8 in child7:
                                        #print 'child8 :',child8.tag,child8.text
                                        temp.update({str(child8.tag).replace('{utranNrm.xsd}',''):str(child8.text)})
                                        headers.append(str(child8.tag).replace('{utranNrm.xsd}',''))
                                        lines.append(str(child8.text))
                                    if os.path.exists(OutPut_dir+RNC_name+"_Utran_Cells_"+".txt")==False:
                                        logger('\t'.join(info.keys()+headers),OutPut_dir+RNC_name+"_Utran_Cells_"+".txt")
                                    logger('\t'.join(info.values()+lines),OutPut_dir+RNC_name+"_Utran_Cells_"+".txt")
                                    
                                    #logger('\t'.join(temp.keys()),OutPut_dir+RNC_name+"_Utran_Cells_"+".txt")
                                    #logger('\t'.join(temp.values()),OutPut_dir+RNC_name+"_Utran_Cells_"+".txt")
                                    temp.clear()
                                    lines=[]
                                    headers=[]
                        
                                    
                                    
                                
                                    
                                #This block parse the other MO in cell level only vsDataMultiCarrier MO
                                #print '<<<<MO cell Level>>>>'
                                for child7 in child6.findall('{genericNrm.xsd}VsDataContainer'):
                                    #print 'child 7 ',child7.tag,child7.attrib
                                                                        
                                    temp1.update({'Id':str(info.get('id'))})                                     
                                    temp1.update({'Id_2':str(dict(child7.attrib).get('id'))})
                                    #print 'child7 :',child7.tag,child7.text
                                    #print temp
                                    #print '\r'+str(info.get('id'))
                                    for child8 in child7.findall('{genericNrm.xsd}VsDataContainer'):
                                        #print 'child8 :',child8.tag,child8.text
                                    
                                        for child9 in child8:
                                            #print 'child9:  ',child9.tag
                                            #print 'child9 :',child9.tag,child9.text
                                            for child10 in child9.findall('{genericNrm.xsd}attributes'):
                                                #print child10.tag,child10.text
                                                for child11 in child10:
                                                    #print 'child11:   ',child11.tag
                                                    temp.update({(str(child11.tag).replace('{genericNrm.xsd}','')).replace('{EricssonSpecificAttributes.15.25.xsd}',''):str(child11.text)})
                                                    headers.append((str(child11.tag).replace('{genericNrm.xsd}','')).replace('{EricssonSpecificAttributes.15.25.xsd}','')) 
                                                    lines.append(str(child11.text))
                                                    for child12 in child11:
                                                            temp.update({(str(child12.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','')).replace('{genericNrm.xsd}',''): str(child12.text)})
                                                            headers.append((str(child12.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','')).replace('{genericNrm.xsd}',''))
                                                            lines.append(str(child12.text))
                                  
                                    temp=merge_dicts(temp1,temp)
                                    #print temp
                                    if str(temp.get('vsDataType'))!='None':
                                        if os.path.exists(OutPut_dir+RNC_name+"_CellLevel_"+str(temp.get('vsDataType'))+".txt")==False:
                                            logger(str('\t'.join(list(temp1.keys()+headers))).replace('\n',''), OutPut_dir+RNC_name+"_CellLevel_"+str(temp.get('vsDataType'))+".txt")
                                        logger(str('\t'.join(list(temp1.values()+lines))).replace('\n',''), OutPut_dir+RNC_name+"_CellLevel_"+str(temp.get('vsDataType'))+".txt") 
                                    
                                    
    
                                    temp.clear()
                                    headers=[]
                                    lines=[]
                                    
                                
                                
                                
                                
                                         
                           #This block parse the other MO in cell level
                                for child7 in child6.findall('{genericNrm.xsd}VsDataContainer'):
                                    n=1
                                    #print 'child 7 ',child7.tag,child7.attrib
                                    temp1.update({'Id':str(info.get('id'))})                                     
                                    temp1.update({'Id_2':str(dict(child7.attrib).get('id'))})
                                    #print 'child7: ',child7.tag
                                    #print 'child7 :',child7.tag,child7.text
                                    for child8 in child7:
                                        #print 'child8: ',child8.tag
                                        for child9  in child8:
                                            temp.update({str(str(child9.tag).replace('{genericNrm.xsd}','')).replace('{EricssonSpecificAttributes.15.25.xsd}',''):str(child9.text).replace('\n','')})
                                            headers.append(str(str(child9.tag).replace('{genericNrm.xsd}','')).replace('{EricssonSpecificAttributes.15.25.xsd}',''))
                                            lines.append(str(child9.text).replace('\n',''))
                                           # print 'child9: ',child9.tag,child9.text
                                            for child10  in child9:
                                        
                                                if len(child10)>0:
                                                    temp2.clear() 
                                                    for child11 in child10.iter():
                                                        temp2.update({(str(child11.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','')).replace('{genericNrm.xsd}',''):str(child11.text).replace('\n','')})
                                                    temp.update({str(child10.tag).replace('{EricssonSpecificAttributes.15.25.xsd}',''):str(','.join(" %s=%r " % (key,val) for (key,val) in temp2.iteritems()))})
                                                    headers.append(str(child10.tag).replace('{EricssonSpecificAttributes.15.25.xsd}',''))
                                                    lines.append(str(','.join(" %s=%r " % (key,val) for (key,val) in temp2.iteritems())))
                                                else:    
                                                    if str(str(child10.tag).replace('{genericNrm.xsd}','')).replace('{EricssonSpecificAttributes.15.25.xsd}','') in temp.keys():
                                                        temps.append(str(child10.text).replace('\n',''))                                                        
                                                        temp.update({str(str(child10.tag).replace('{genericNrm.xsd}','')).replace('{EricssonSpecificAttributes.15.25.xsd}','')+'_'+str(n):str(child10.text).replace('\n','')})                                            
                                                        n=n+1
                                                        headers2=str(str(child10.tag).replace('{genericNrm.xsd}','')).replace('{EricssonSpecificAttributes.15.25.xsd}','')
                                                        #print temps
                                                    else:
                                                        #print len(temps)
                                                        if len(temps)>0:
                                                            headers.append(headers2)
                                                            lines.append(' : '.join(temps))
                                                        else:
                                                            temp.update({str(str(child10.tag).replace('{genericNrm.xsd}','')).replace('{EricssonSpecificAttributes.15.25.xsd}',''):str(child10.text).replace('\n','')})                                            
                                                            headers.append(str(str(child10.tag).replace('{genericNrm.xsd}','')).replace('{EricssonSpecificAttributes.15.25.xsd}',''))
                                                            lines.append(str(child10.text).replace('\n',''))
                                                    temps=[]
                                    temp=merge_dicts(temp1,temp)
                                    if os.path.exists(OutPut_dir+RNC_name+"_CellLevel_"+str(temp.get('vsDataType'))+".txt")==False:
                                        logger('\t'.join(temp1.keys()+headers).replace('\n',''),OutPut_dir+RNC_name+"_CellLevel_"+str(temp.get('vsDataType'))+".txt")
                                    logger('\t'.join(temp1.values()+lines).replace('\n',''),OutPut_dir+RNC_name+"_CellLevel_"+str(temp.get('vsDataType'))+".txt")
                                    
                                    headers=[]
                                    lines=[]
                                    #print temp
                          
                                    #logger('\t'.join(list(temp.keys())).replace('\n',''),OutPut_dir+RNC_name+"_"+str(temp.get('vsDataType'))+".txt")
                                    #logger('\t'.join(list(temp.values())).replace('\n',''),OutPut_dir+RNC_name+"_"+str(temp.get('vsDataType'))+".txt")
                                    #print temp.get('{genericNrm.xsd}vsDataType')
                                    temp.clear()     
                                    

                                    

                            #THis block parse the utran neighbors
                                #print '<<<<utran neighbors>>>>'
                                    
                                for child7 in child6.findall('{utranNrm.xsd}UtranRelation'):
                                    #print child7.tag
                                    temp1={}
                                    #print 'child 7 ',child7.tag,child7.attrib
                                    temp1.update({'Id':str(info.get('id'))})                                     
                                    temp1.update({'Id_2':str(dict(child7.attrib).get('id'))})
                                    #print 'child7: ',child7.tag
                                    #print 'child7 :',child7.tag,child7.text
                                    for child8 in child7.iter():
                                        #print 'child8: ',child8.tag
                                        for child9  in child8:
                                            temp.update({str(str(child9.tag).replace('{genericNrm.xsd}','')).replace('{EricssonSpecificAttributes.15.25.xsd}',''):str(child9.text).replace('\n','')})
                                            headers.append(str(str(child9.tag).replace('{genericNrm.xsd}','')).replace('{EricssonSpecificAttributes.15.25.xsd}',''))
                                            lines.append(str(child9.text).replace('\n',''))
                                           # print 'child9: ',child9.tag,child9.text
                                            
                                            
                                    temp=merge_dicts(temp1,temp)
                                    headers.insert(0,str('Id_2'))
                                    headers.insert(0,str('Id'))
                                    lines.insert(0,str(temp1.get('id_2')))
                                    lines.insert(0,str(temp1.get('id')))
                                    if os.path.exists(OutPut_dir+RNC_name+"_CellLevel_"+str(temp.get('vsDataType'))+".txt")==False:
                                        logger('\t'.join(headers).replace('\n',''),OutPut_dir+RNC_name+"_CellLevel_"+str(temp.get('vsDataType'))+".txt")
                                    logger('\t'.join(lines).replace('\n',''),OutPut_dir+RNC_name+"_CellLevel_"+str(temp.get('vsDataType'))+".txt")
                                    
                                    headers=[]
                                    lines=[]
                                    #print temp
                                   
                                #print '<<<<GSM neighbors>>>>'    
                            #This block parse the GSM relations
                                for child7 in child6.findall('{geranNrm.xsd}GsmRelation'):
                                    temp1={}
                                    #print child7.tag
                                    #print 'child 7 ',child7.tag,child7.attrib
                                    temp1.update({'Id':str(info.get('id'))})                                     
                                    temp1.update({'Id_2':str(dict(child7.attrib).get('id'))})
                                    #print 'child7: ',child7.tag
                                    #print 'child7 :',child7.tag,child7.text
                                    for child8 in child7.iter():
                                        #print 'child8: ',child8.tag
                                        for child9  in child8:
                                            temp.update({str(str(child9.tag).replace('{genericNrm.xsd}','')).replace('{EricssonSpecificAttributes.15.25.xsd}',''):str(child9.text).replace('\n','')})
                                            headers.append(str(str(child9.tag).replace('{genericNrm.xsd}','')).replace('{EricssonSpecificAttributes.15.25.xsd}',''))
                                            lines.append(str(child9.text).replace('\n',''))
                                           # print 'child9: ',child9.tag,child9.text
                                            
                                            
                                    temp=merge_dicts(temp1,temp)
                                    headers.insert(0,'Id_2')
                                    headers.insert(0,'Id')
                                    lines.insert(0,str(temp1.get('id_2')))
                                    lines.insert(0,str(temp1.get('id')))
                                    if os.path.exists(OutPut_dir+RNC_name+"_CellLevel_"+str(temp.get('vsDataType'))+".txt")==False:
                                        logger(str('\t'.join(headers)).replace('\n',''),OutPut_dir+RNC_name+"_CellLevel_"+str(temp.get('vsDataType'))+".txt")
                                    logger(str('\t'.join(lines)).replace('\n',''),OutPut_dir+RNC_name+"_CellLevel_"+str(temp.get('vsDataType'))+".txt")
                                    
                                    headers=[]
                                    lines=[]
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                            
                            
                                
                            #THis MO obtains Mo in RNC level
                                
                            #print '<<<<Mo in RNC level>>>>'
                            for child6 in child5.findall('{genericNrm.xsd}VsDataContainer'):
                                temp.update({'RNC_Name':RNC_name})                                
                                #print 'child6: ',child6.tag,
                               # print dict(child6.attrib).get('id')
                                temp.update({'id':str(dict(child6.attrib).get('id'))})
                                info['id']=str(dict(child6.attrib).get('id'))
                                for child7 in child6:
                                   # print '\r'+str(dict(child6.attrib).get('id'))
                                    #print 'child7: ',child7.tag
                                    for child8 in child7:
                                        #print 'child8: ',child8.tag
                                        temp.update({(str(child8.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','')).replace('{genericNrm.xsd}',''):str(child8.text).replace('\n','')})                                        
                                        headers.append((str(child8.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','')).replace('{genericNrm.xsd}',''))
                                        lines.append(str(child8.text).replace('\n',''))                                        
                                        for child9 in child8:
                                            #print 'child9: ',child9.tag
                                           
                                            #print len(child9)    
                                            if len(child9)>0:
                                                te={}
                                                for child11 in child9:
                                                    te.update({(str(child11.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','')).replace('{genericNrm.xsd}',''):str(child11.text).replace('\n','')})
                                               
                                                temp.update({(str(child9.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','')).replace('{genericNrm.xsd}',''):str(','.join("%s=%r" % (key,val) for (key,val) in te.iteritems()))})
                                                headers.append((str(child9.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','')).replace('{genericNrm.xsd}',''))
                                                lines.append(str(','.join("%s=%r" % (key,val) for (key,val) in te.iteritems())))                                                
                                               # print 'child9: ',child9.tag
                                               # print "good"
                                            else:
                                                 temp.update({(str(child9.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','')).replace('{genericNrm.xsd}',''):str(child9.text).replace('\n','')})
                                                 headers.append((str(child9.tag).replace('{EricssonSpecificAttributes.15.25.xsd}','')).replace('{genericNrm.xsd}',''))
                                                 lines.append(str(child9.text).replace('\n',''))
                                #print temp
                                headers.insert(0,'RNC_name')
                                headers.insert(0,'id')
                                lines.insert(0,RNC_name)
                                lines.insert(0,info.get('id'))
                                if 'vsDataIurLink' in headers:pass#Evalua if this value exist in the current list
                                else:
                                    if os.path.exists(OutPut_dir+RNC_name+"_RNCLevel_"+str(temp.get('vsDataType'))+".txt")==False:#Evaluate if exist the file to decide if is needed print the headers
                                        logger('\t'.join(headers).replace('\n',''),OutPut_dir+RNC_name+"_RNCLevel_"+str(temp.get('vsDataType'))+".txt")
                                    logger('\t'.join(lines).replace('\n',''),OutPut_dir+RNC_name+"_RNCLevel_"+str(temp.get('vsDataType'))+".txt")
                                
                                #logger('\t'.join(list(temp.keys())).replace('\n',''),OutPut_dir+RNC_name+"_RNCLevel_"+str(temp.get('vsDataType'))+".txt")
                                #logger('\t'.join(list(temp.values())).replace('\n',''),OutPut_dir+RNC_name+"_RNCLevel_"+str(temp.get('vsDataType'))+".txt")
                                temp.clear()
                                headers=[]
                                lines=[]
                               
    print "Done....."                            
XML_ParserEricsson_CM_RNC('C:\Users\VervebaMX2\Documents\Projects\XML_Parsing\TEst\Test_allEricssonXML3G\XML\X20160826CM_RNC210.xml','C:\\Users\\VervebaMX2\\Documents\\Projects\\XML_Parsing\\TEst\\Test_allEricssonXML3G\\Results\\')
