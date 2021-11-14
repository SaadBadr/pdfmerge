# Import module
from merge_pdf import merge
import os, sys, getopt

def mergeFolder(folderPath, output_file):
    merge.Merge(output_file, debug=True).merge_folder (folderPath)


def main(argv):
    inputpath =  os.curdir
    outputpath = os.path.join(os.curdir, 'output.pdf')

    try:
        opts, args = getopt.getopt(argv,"i:o:x:")
    except getopt.GetoptError:
        print('pdfmerge -i <inputpath> -o <outputpath>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-i':
            inputpath = arg
        elif opt == '-o':
            outputpath = arg
        elif opt == '-x':
            inputpath = arg
            outputpath = os.path.join(arg, 'output.pdf')

    mergeFolder(inputpath, outputpath)







if __name__ == '__main__':
    main(sys.argv[1:])