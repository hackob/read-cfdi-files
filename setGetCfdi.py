#!/usr/bin/python

import xml.etree.ElementTree as ET
import os, sys, magic

def getFileType(filename):
#    cmd = shlex.split('file --mime-type {0}'.format(filename))
#    mime_type = subprocess.check_output(cmd).split()[-1]
#    return mime_type
    return magic.from_file(filename)

def main(argv):

    if len(argv) >= 1:

        xmlFile = argv[0]

        if getFileType(xmlFile).upper().find('XML') != -1:
            xmlTree = ET.parse(xmlFile)
            xml = xmlTree.getroot()

            fecha          = xml.get('fecha').replace("-","").replace("T","_").replace(":","")
            noCertificado  = xml.get('noCertificado')
            subTotal       = xml.get('subTotal')
            total          = xml.get('total')
            emisorRFC      = xml.find('{http://www.sat.gob.mx/cfd/3}Emisor').get('rfc')
            emisorNombre   = xml.find('{http://www.sat.gob.mx/cfd/3}Emisor').get('nombre')
            receptorRFC    = xml.find('{http://www.sat.gob.mx/cfd/3}Receptor').get('rfc')
            receptorNombre = xml.find('{http://www.sat.gob.mx/cfd/3}Receptor').get('nombre')
            impuestos      = xml.find('{http://www.sat.gob.mx/cfd/3}Impuestos').get('totalImpuestosTrasladados')
       
            newFileName = "%s_%s_%s_%s_%s_%s_%s" % (fecha, noCertificado, emisorRFC, receptorRFC, subTotal, impuestos, total)
            print newFileName
        else:
            print "Debe especificarse un archivo en formato XML"
    else:
        print "Debe especificarse el nombre del archivo de entrada"
        print "$ setGetCfdi.py archivo.xml"

if __name__ == "__main__":
   main(sys.argv[1:])
