import subprocess
import os
import argparse

# Rename to your own path
path = '/sdcard/Download/'
func = lambda li: ['--'+x for x in li]

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-c,', '--convert', dest='CONVERT_TYPE', help='filetype to convert to')
parser.add_argument('-op', '--option', nargs='+',dest='OPTION',help='option output')
ARGS = parser.parse_args()

def convert_to_other_ebook_format(input_ebook, output_format, option):
    # book.epub to [converted]book.pdf for example
    output_ebook = '[converted]' + input_ebook.split('.epub')[0] + '.' + output_format.replace('.', '')
    process = subprocess.Popen(['ebook-convert', input_ebook, output_ebook] + option)
    process.wait()

if __name__ == '__main__':
    epub_books = [epub for epub in os.listdir(path) if epub.endswith('.epub')]
    
    ARGS.OPTION = func(ARGS.OPTION)
    
    # Automatically set output profile to tablet
    ARGS.OPTION.append('output-profile')
    ARGS.OPTION.append('tablet')
    
    for book in epub_books:
        convert_to_other_ebook_format(book, ARGS.CONVERT_TYPE, ARGS.OPTION)