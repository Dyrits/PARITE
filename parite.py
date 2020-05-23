#! /usr/bin/env python3
# coding: utf-8

import analysis.csv as c_an
import analysis.xml as x_an
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "-ext", "--extension", 
                        help = """Type of file to analyse. Is it a CSV or an XML?""")
    parser.add_argument("-d", "-data", "--datafile",
                        help= """File containing pieces of information about the members of parliament""")
    parser.add_argument("-p", "--byparty", action='store_true', help="""Displays a piechart for each political party""")
    parser.add_argument("-i", "--info", action='store_true', help="""Information about the size of the file""")
    return parser.parse_args()


def main():
    args = parse_arguments()
    datafile = args.datafile
    if datafile:
        # The following conditions were made using a regular expression search in the original project:
        if datafile.endswith(".xml", args.byparty, args.info):
            x_an.launch_analysis(datafile)
        elif datafile.endswith(".csv", args.byparty, args.info):
            c_an.launch_analysis(datafile, args.byparty, args.info)
    else: #The default datafiles are used according to the specified extension.
        if args.extension == 'xml':
            x_an.launch_analysis('SyceronBrut.xml')
        elif args.extension == 'csv':
            c_an.launch_analysis('current_mps.csv', args.byparty, args.info)
        
        
if __name__ == '__main__':
    main()
