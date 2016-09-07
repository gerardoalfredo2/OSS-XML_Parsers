# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 10:21:46 2016
This is the first version

@author: Gerardo Alfredo Alarcon Rivas
"""
import timeit
import re
import sys
"""This function clean the xml file due the dumps from huawei had a wrong char
        -Use filename as input of the file(this one include directory and filename) of
        the file that need to be repaired
"""
def remove_duplicates(li):
    my_set = set()
    res = []
    for e in li:
        if e not in my_set:
            res.append(e)
            my_set.add(e)
    #
    return res

def clean(filename_):
    filedata = None
    with open(filename_, 'r') as file :
        filedata = file.read()

# Replace the target string
    filedata = filedata.replace('\a', '|')

# Write the file out again
    with open(filename_, 'w') as file:
        file.write(filedata)
"""This function create a new file(file_) or open this if is existent and and a new line at the end
    -Use file_ as filename input(this one use directory and filename).
    -Use cadena as a input to write this at the end of the file """
def logger(cadena,file_):
         f = open(file_,'a')
         f.write(cadena+"\n") # python will convert \n to os.linesep
         f.close()
'''Loads a file and return a dictionary with the contents'''
def txt_reader(filenamess):
    #with open(filenamess) as f:
        #lines = f.read().splitlines()
    RNC_data={}
    contents={}
    linea=[]
    encabe=[]
    datos=[]
    with open(filenamess, "r") as ins:
        lines = []
        for line in ins:
            lines.append(liine)# This variable has all the lines of the parsed file
    #print lines
    for p in list(lines[0:15]):
                linea=list(p.split('\t'))
                RNC_data.update({linea[0]:linea[1]})
    #print RNC_data
    for g in RNC_data:
        encabe.append(g)
        datos.append(RNC_data[g])
    #print RNC_data['name']
    contents.update({'BSC Info':RNC_data})

    line=[]
    headers=[]# this list save all the headers
    for po in lines:
        if po.find("MODEL	ELEMENT	fdn")!=-1:
            headers.append(str(po).replace('\n',''))

        #print headers
    headers=remove_duplicates(headers)
    head=''

    for p in headers:# fill the diccionary with the available headers
         contents.update({p:[]})

    for r in contents.keys():
        temporal=[]
        fla=0
        for op in lines:
            if (''.join(e for e in r if e.isalnum()))==''.join(e for e in op if e.isalnum()):

                if len(temporal)>0:
                    #  pass
                    contents[head]=temporal
                temporal=[]

                head=str(r).replace('\n',"")
                fla=1
                #print head,r
            elif fla==1:
               # pass
                temporal.append(op)
                #print temporal



        #print head
        #break
    #print '\n'.join(contents.keys())




    for keys,values in contents.items():
        #logger(str(keys),'C:\Users\VervebaMX2\Documents\Projects\Python Scripts\CM&PM Parsers\HuaweiCM_XML_Parser\Logs\headers.txt')
        logger("".join(values),'C:\Users\VervebaMX2\Documents\Projects\Python Scripts\CM&PM Parsers\HuaweiCM_XML_Parser\Logs\headers.txt')
    #print contents.values()
    #for k in headers:
     #   logger(k,'C:\Users\VervebaMX2\Documents\Projects\Python Scripts\CM&PM Parsers\HuaweiCM_XML_Parser\Logs\headers.txt')
    return headers

'''
This is the main function, this is doing all the parse tasks.
    -XML_FILE is the name of the xml file to be parsed including the directory.
    -OutPut_dir is the name of the file and directory where the parsed file will be saved.
'''
def HWCMParser(XML_FILE,OutPut_dir):#
    start_time = timeit.default_timer()
    print "Start Time:",start_time
    clean(XML_FILE)# clean the file of one wrong character in the xml file
    dictionario=[]
    encabezados=[]
    import xml.etree.ElementTree as ET# Create the xml parse object as ET
    filename= XML_FILE
    tree = ET.parse(filename)# Load the xml file in the ET object
    root = tree.getroot()  #THis take the root element and save this in root variable
    compara=""# variable used to do comparison whit the headers
    for child_of_root in root:# THis start to explore the root childs and save in child_of_root

        for child_of_child in child_of_root:#we start to take the elements of Child_of_root

            elementos=[]
            for l in child_of_child.attrib:
                elementos.append(str(child_of_child.attrib[l]).replace('\n',''))# this save all the
                #_ elements of child_of_child dictionary as a list named elementos



            dictionario=[]
            encabezados=['MODEL','ELEMENT']# We add this two list strings to fill the first two columns of the header

            for next_level in child_of_child:
                dictionario.append(next_level.text)# we save the elements of the dictionary next_level.text in dictionario
                encabezados.append( next_level.attrib['name'] )# we save the elements of the dict next_level.attrib in encabezados


            if re.match("[\s]", child_of_child.text):# this if evaluate if we have a spave or tab symbol due we don't need use this in our list
                if compara!=" ".join(encabezados):# this line compare if we are changing the name of the headers(if is true this write this in the output file)
                    logger("\t".join(encabezados),OutPut_dir)
                cadena=('\t'.join(elementos))+"\t"+"\t".join(dictionario)
            else:
                cadena=('\t'.join(elementos))+"\t"+child_of_child.text+"\t"+"\t".join(dictionario)

            logger(cadena,OutPut_dir)
            compara=" ".join(encabezados) #we save actual value of the encabezados listto compare in the next iteration
            elementos=[]
    elapsed = timeit.default_timer() - start_time
    print"Elapsed Timer:",elapsed
    filestreamer=txt_reader(OutPut_dir)
    #print filestreamer
    return root

print(HWCMParser('C:\Users\VervebaMX2\Documents\Projects\XML Parsing\XML Files\HuaweiCM\CMExport_PUERNC170_10.150.6.20_2016072505.xml','C:\Users\VervebaMX2\Documents\Projects\Python Scripts\CM&PM Parsers\HuaweiCM_XML_Parser\logs\logo.txt'))