# -*- coding: utf-8 -*-
"""
Created on Wednesday Aug 18 09:33:24 2016

@author: Gerardo Alfredo Alarcon Rivas
"""
def file_tolist(file_name):
    array = []
    with open(file_name, "r") as f:
        for line in f:
            array.append(str(line.replace('\s','')))
    return array
    
'''This function saves take a string and save this in a new line of the input file'''

def logger(cadena, file_):
         f = open(file_, 'a')
         f.write(cadena+"\n") # python will convert \n to os.linesep
         f.close()

'''The parser take on xml file and create a tree form this
the code write and output file in a tabular format with all the elements of the
initial file. THe code can parse the exported xml files from Ericsson  PM counters por RNC
from all the levels'''
def XML_ParserEricsson_CM_RNC(XML_FILE, OutPut_dir,headers_utran):
    import xml.etree.ElementTree as ET
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    headers=[]
    lines= []
    file_name=''
    temp={}
    info={'id':''}
    RNC_name=''
    cade=''
    '''This block take the fileformat, vendorName,elementType and begin time'''
    for node in root.findall('{configData.xsd}configData'):
        print 'root: ',node
        for child1 in node:
            print 'child1: ',child1
            for child2 in child1:
                print "child2: ",child2.tag,"\n"
                print child2.attrib#RNC ID
                for child3 in child2:#MeContext
                    print "child3: ",child3.tag,"\n"
                    RNC_name=dict(child3.attrib).get('id')
                    print child3.attrib
                    '''#RNC ID
                    for child4 in child3.findall('{genericNrm.xsd}VsDataContainer'):
                        print "child4: ",child4.tag,"\n"
                        for child5 in child4:
                            print "child5: ",child5.tag,child5.text,"\n"
                            for child6 in child5:
                                print "child6: ",child6.tag,child6.text,"\n"
                                for child7 in child6:
                                    print "child6: ",str(child7.tag).replace('{EricssonSpecificAttributes.15.25.xsd}',""),child7.text,"\n"
                                    temp.update({str(child7.tag).replace('{EricssonSpecificAttributes.15.25.xsd}',''):str(child7.text)})                         
                                logger('\t'.join(list((temp.keys()))),OutPut_dir+RNC_name+'_RNC_nfo.txt')
                                logger('\t'.join(list((temp.values()))),OutPut_dir+RNC_name+'_RNC_nfo.txt')
                                print(temp.values())
                                temp.clear()'''
                    
                    headers=file_tolist(headers_utran)
                    for key in headers:
                        print key
                        temp.update({str(key).replace('\n',''):''})
                    for child4 in child3.findall('{genericNrm.xsd}ManagedElement'):
                        #print "child4: ",child4.tag,"\n"
                        for child5 in child4.findall('{utranNrm.xsd}RncFunction'):
                            #print "child5: ",child5.tag,"\n"
                            for child6 in child5.findall('{utranNrm.xsd}UtranCell'):
                                temp['UTRAN_CELL']=dict(child6.attrib).get('id')                            
                                logger('\t'.join(temp.keys()),OutPut_dir+'UtranCell_'+RNC_name+'.txt')
                                for child7 in child6.findall('{utranNrm.xsd}attributes'):
                                                                     
                                    for child8 in child7:
                                        #print 'child8 :',child8.tag,child8.text
                                        temp[str(child8.tag).replace('{utranNrm.xsd}','')]=str(child8.text)
                                        #temp.update({str(child8.tag).replace('{utranNrm.xsd}',''):str(child8.text)})
                                        print temp
                                    logger('\t'.join(temp.values()),OutPut_dir+'UtranCell_'+RNC_name+'.txt')
                                    #temp.clear()
                                '''
                                for child7 in child6.iter('{genericNrm.xsd}attributes'):
                                    #print 'child7 :',child7.tag,child7.text
                                    temp.update({'id':info.get('id')})
                                    
                                    for child8 in child7.iter():
                                        temp.update({str(child8.tag).replace('{EricssonSpecificAttributes.15.25.xsd}',''):str(child8.text)})
                                        #print "child8: ",str(child8.tag).replace('{EricssonSpecificAttributes.15.25.xsd}',''),child8.text
                                    cade=str('\t'.join(list(temp.keys()))).replace('\n','')
                                    logger(cade, OutPut_dir+RNC_name+"_"+str(temp.get('{genericNrm.xsd}vsDataType'))+".txt")
                                    cade=str('\t'.join(list(temp.values()))).replace('\n','')                                    
                                    logger(cade, OutPut_dir+RNC_name+"_"+str(temp.get('{genericNrm.xsd}vsDataType'))+".txt") 
                                    print temp.get('{genericNrm.xsd}vsDataType')
                                    temp.clear()
                                    
                            for child6 in child5.findall('{genericNrm.xsd}VsDataContainer'):
                                temp.update({'RNC_Name':RNC_name})                                
                                print child6
                                for child7 in child6.iter():
                                    temp.update({'RNC_Name':RNC_name})
                                    temp.update({str(child7.tag).replace('{EricssonSpecificAttributes.15.25.xsd}',''):str(child7.text)})
                                logger('\t'.join(list(temp.keys())).replace('\n',''),OutPut_dir+RNC_name+"_"+str(temp.get('{genericNrm.xsd}vsDataType'))+".txt")
                                logger('\t'.join(list(temp.values())).replace('\n',''),OutPut_dir+RNC_name+"_"+str(temp.get('{genericNrm.xsd}vsDataType'))+".txt")
                                temp.clear() 
                            
                            '''
        
        
XML_ParserEricsson_CM_RNC('C:\Users\VervebaMX2\Documents\Projects\XML Parsing\TEst\X20160826CM_RNC210.xml','C:\\Users\\VervebaMX2\\Documents\\Projects\\XML Parsing\\TEst\\Result\\','C:\Users\VervebaMX2\Documents\Projects\Python Scripts\CM&PM Parsers\CM-and-PM-ericsson-and-huawei-parsers\Ericsson\UtranCell_Headers.txt')
