# -*- coding: utf-8 -*-
"""
Created on Mon Aug 08 09:33:24 2016

@author: VervebaMX2
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 14:46:03 2016

@author: Gerardo Alfredo Alarcon Rivas
"""
import sys
def merge_dicts(*dict_args):
    '''
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result
'''This function saves take a string and save this in a new line of the input file'''
def logger(cadena, file_):
         f = open(file_, 'a')
         f.write(cadena+"\n") # python will convert \n to os.linesep
         f.close()

'''The parser take on xml file and create a tree form this
the code write and output file in a tabular format with all the elements of the
initial file. THe code can parse the exported xml files from Ericsson PM SGSN counters
from all the levels'''
def XML_Parser_PM_SGSN_Ericsson(XML_FILE, OutPut_dir):
    import xml.etree.ElementTree as ET
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    temp={}
    temp2={}
    temp3={}
    temp4={}
    header=[]
    lines=[]
    '''Main loop'''
    for node in root.iter("{http://www.3gpp.org/ftp/specs/archive/32_series/32.435#measCollec}fileHeader"):
        temp.update(dict(node.attrib))
        for child1 in node:
            temp.update((dict(child1.attrib)))
    for node in root.iter("{http://www.3gpp.org/ftp/specs/archive/32_series/32.435#measCollec}fileFooter"):
        for child1 in node:        
            temp.update( (dict( child1.attrib)))
    for node in root.iter("{http://www.3gpp.org/ftp/specs/archive/32_series/32.435#measCollec}measInfo"):
        header=[]
        temp3={}
        temp2={}
        temp2.update(dict(node.attrib))
        for child1 in node.findall("{http://www.3gpp.org/ftp/specs/archive/32_series/32.435#measCollec}job"):
                temp2.update(dict(child1.attrib)) 
        for child1 in node.findall("{http://www.3gpp.org/ftp/specs/archive/32_series/32.435#measCollec}granPeriod"):
                temp2.update(dict(child1.attrib))
        for child1 in node.findall("{http://www.3gpp.org/ftp/specs/archive/32_series/32.435#measCollec}repPeriod"):
                temp2.update(dict(child1.attrib))
        for child1 in node.findall("{http://www.3gpp.org/ftp/specs/archive/32_series/32.435#measCollec}measType"):
                temp3.update({dict(child1.attrib).get('p'):child1.text})
                #print temp2
        for key in temp:
            header.append(key)
        for key in temp2:
            header.append(key)
        for key in temp3:
            header.append(temp3.get(key))
        header.append('measObjLdn')
        logger('\t'.join(header),OutPut_dir)
        for child1 in node.findall("{http://www.3gpp.org/ftp/specs/archive/32_series/32.435#measCollec}measValue"):
                temp4={}                
                temp4.update(dict(child1.attrib))
                lines=[]
                for child2 in child1.findall("{http://www.3gpp.org/ftp/specs/archive/32_series/32.435#measCollec}r"):
                    temp4.update({ temp3.get(dict(child2.attrib).get('p')): child2.text})
                for key in header:
                    lines.append(merge_dicts(temp,temp2,temp4).get(key))
                logger('\t'.join(lines),OutPut_dir)
                
                
              
                
               
    
        

        
        
#XML_Parser_PM_SGSN_Ericsson('C:\Users\VervebaMX2\Documents\Projects\Python Scripts\CM&PM Parsers\CM-and-PM-ericsson-and-huawei-parsers\Ericsson\Test\A20160725.0000-0500-20160725.0015-0500_SubNetwork=ONRM_ROOT_MO,SubNetwork=SGSN_MME,MeContext=MX-GDL-M3-DATA-MME-1_statsfile.xml','C:\Users\VervebaMX2\Documents\Projects\Python Scripts\CM&PM Parsers\CM-and-PM-ericsson-and-huawei-parsers\Ericsson\Test\loggy2.txt')
first_arg = sys.argv[1]
second_arg = sys.argv[2]

if __name__ == "__main__":
    XML_Parser_PM_SGSN_Ericsson(first_arg,second_arg)