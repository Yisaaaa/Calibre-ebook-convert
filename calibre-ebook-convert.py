import subprocess
import os
import argparse

# Rename to your own path
path = '/sdcard/Download/'
func = lambda li: ['--'+x for x in li]

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-c,', '--convert', dest='CONVERT_TYPE', help='filetype to convert to')
parser.add_argument('-op', '--option', nargs='*',dest='OPTION', help="add 'O' before option e.g Ooutput-profile tablet")
parser.add_argument('-t', '--type', dest='TYPE', help='file type you are converting')
ARGS = parser.parse_args()

def convert_to_other_ebook_format(input_ebook, output_format, option):
    #print(option)
    # book.epub to [converted]book.pdf for example
    output_ebook = '[converted]' + input_ebook.split('.epub')[0] + '.' + output_format.replace('.', '')
    if option is not None:
        process = subprocess.Popen(['ebook-convert', input_ebook, output_ebook] + option)
    else:
        process = subprocess.Popen(['ebook-convert', input_ebook, output_ebook])        
    process.wait()

if __name__ == '__main__':
    if ARGS.TYPE == 'epub':
        books = [epub for epub in os.listdir(path) if epub.endswith('.epub')]
    elif ARGS.TYPE == 'mobi':
        books = [mobi for mobi in os.listdir(path) if mobi.endswith('.mobi')]
    
    # These are just my default option
    if ARGS.OPTION is not None:
        if 'mobi' in ARGS.OPTION:
            ARGS.OPTION = ['Opretty-print', 'Odont-compress', 'Omobi-keep-original-images', 'Odisable-font-rescaling']
        elif 'epub' in ARGS.OPTION:
            ARGS.OPTION.extend(['Odisable-font-rescaling', 'Opreserve-cover-aspect-ratio', 'Opretty-print'])
            ARGS.OPTION.remove('epub')
    # ---- #
        
        ARGS.OPTION = [x.replace('O', '--') if x.startswith('O') else x for x in ARGS.OPTION]
    print(ARGS.OPTION)
        
    for book in books:
        convert_to_other_ebook_format(book, ARGS.CONVERT_TYPE, ARGS.OPTION)