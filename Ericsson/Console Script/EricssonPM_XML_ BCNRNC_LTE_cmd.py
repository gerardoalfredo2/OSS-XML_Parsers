# -*- coding: utf-8 -*-
"""
Created on Wednesday Aug 18 09:33:24 2016

@author: Gerardo Alfredo Alarcon Rivas
"""

'''This function saves take a string and save this in a new line of the input file'''
import sys 
def logger(cadena, file_):
         f = open(file_, 'a')
         f.write(cadena+"\n") # python will convert \n to os.linesep
         f.close()

'''The parser take on xml file and create a tree form this
the code write and output file in a tabular format with all the elements of the
initial file. THe code can parse the exported xml files from Ericsson  PM counters por RNC
from all the levels'''
def XML_ParserEricsson_PM_BCNRNC(XML_FILE, OutPut_dir):
    import xml.etree.ElementTree as ET
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    headers=[]
    lines= []   
    '''This block take the fileformat, vendorName,elementType and begin time'''
    for node in root.findall('mfh'):
        #print node.tag
        for child1 in node:
            headers.append(str(child1.tag))
            lines.append(str(child1.text))
        logger('\t'.join(headers),OutPut_dir)
        logger('\t'.join(lines),OutPut_dir)
       
    for node in root.findall('md'):
        headers=[]
        lines= []
        lines2=[]
        for child1 in node.findall('neid'):
            for child2 in child1:
                headers.append(str(child2.tag))
                lines.append(str(child2.text))
        headers.append('moid')
        for child1 in node.findall('mi'):
            for child2 in child1.findall('mt'):
                headers.append(str(child2.text))
            logger( '\t'.join(headers),OutPut_dir)
            for child2 in child1.findall('mv'):
                lines2=[]
                for child3 in child2.findall('moid'):
                    lines2.append(str(child3.text))
                for child3 in child2.findall('r'):
                      lines2.append(str(child3.text))
                logger( '\t'.join(lines+lines2),OutPut_dir)
        
                    
            
    
        
        
#XML_ParserEricsson_PM_BCNRNC('C:\Users\VervebaMX2\Documents\Projects\Python Scripts\CM&PM Parsers\CM-and-PM-ericsson-and-huawei-parsers\Ericsson\Test\A20160725.0000-0700-0015-0700_SubNetwork=ONRM_ROOT_MO,SubNetwork=LTE,MeContext=LBCNMXC0046_statsfile.xml','C:\Users\VervebaMX2\Documents\Projects\Python Scripts\CM&PM Parsers\CM-and-PM-ericsson-and-huawei-parsers\Ericsson\Test\log.txt')
first_arg = sys.argv[1]
second_arg = sys.argv[2]

if __name__ == "__main__":
    XML_ParserEricsson_PM_BCNRNC(first_arg,second_arg)