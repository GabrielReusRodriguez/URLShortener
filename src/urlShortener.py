#!/usr/bin/python3

"""
    @Author:    Gabriel Reus
    @Links:     https://github.com/GabrielReusRodriguez/URLShortener 
"""

import pyshorteners
import sys
import getopt

#https://pyshorteners.readthedocs.io/en/latest/apis/pyshorteners.shorteners.html#module-pyshorteners.shorteners.cuttly

#Funciones
#******************
def printHelp():
    print("Url Shortener: programa para generar una url acortada (El acortador default es tinyURL)\n")
    print("Uso de la aplicación:\n")
    print("UrlShortener [OPTIONS] <url>")
    print("\tOPTIONS:\n")
    print("\t--chilpit: \t acortador chilpit\n")
    print("\t--clckru: \t acortador clckru\n")
    print("\t--dagd: \t acortador dagd\n")
    print("\t--gitio: \t acortador gitio\n")
    print("\t--isgd: \t acortador isgd\n")
#    print("\t--nullpointer: \t acortador nullpointer\n")
    print("\t--tinyUrl: \t acortador tinyUrl (default)\n")
    print("\t--osdb: \t acortador osdb\n")
#    print("\t--owly: \t acortador owly\n")
#    print("\t--qpsru: \t acortador qpsru\n")
    print("\t-h, --help muestra esta ayuda\n")


#Programa principal
#*******************

shortener = None
long_url = None

if len(sys.argv) == 1:
    long_url = input("Introduce la URL para acortar: ")
    shortener = pyshorteners.Shortener().tinyurl
elif len(sys.argv) == 2:
    long_url = sys.argv[1]
    shortener = pyshorteners.Shortener().tinyurl
else:
    try:
        options, args  = getopt.getopt(sys.argv[1:], "h",
                               ["chilpit",
                               "clckru",
                               "dagd",
                               "gitio",
                               "isgd",
                               "nullpointer",
                               "tinyUrl",
                               "osdb",
                               "owly",
                               "qpsru",
                                "help"])
        for name, value in options:
            if name  in ['-h', '--help']:
                printHelp()
                exit(1)
            elif name in ['--chilpit']:
                shortener = pyshorteners.Shortener().chilpit
            elif name in ['--clckru']:
                shortener = pyshorteners.Shortener().clckru
            elif name in ['--dagd']:
                shortener = pyshorteners.Shortener().dagd
            elif name in ['--gitio']:
                shortener = pyshorteners.Shortener().gitio
            elif name in ['--isgd']:
                shortener = pyshorteners.Shortener().isgd
 #           elif name in ['--nullpointer']:
 #               shortener = pyshorteners.Shortener().nullpointer
            elif name in ['--tinyUrl']:
                shortener = pyshorteners.Shortener().tinyurl
            elif name in ['--osdb']:
                shortener = pyshorteners.Shortener().osdb
#            elif name in ['--owly']:
#                shortener = pyshorteners.Shortener().owly
#            elif name in ['--qpsru']:
#                shortener = pyshorteners.Shortener().qpsru

    except getopt.GetoptError as err:
        print("Error al procesar los parámetros ",err)
        exit (1)
    long_url = sys.argv[len(sys.argv) - 1]


if shortener is None:
    print("ERRROR  , no se ha inicializado el 'acortador'\n")
    exit(1)

##TinyURL shortener service
#type_tiny = pyshorteners.Shortener()
#short_url = type_tiny.tinyurl.short(long_url)
try:
    short_url = shortener.short(long_url)
except ShorteningErrorException  as err:
    print("ERROR al acortar la url del proveedor: ",err)
    exit(1)

print(short_url)