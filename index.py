import argparse
from nltk.corpus import reuters

#python3 index.py -i /Users/magz/nltk_data/corpora/reuters/training -d dictionary-file -p postings-file

#-i directory-of-documents -d dictionary-file -p postings-file
def main():
    args = parse_user_args()
    print (args.input)

def parse_user_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-i', '--input', required=True,
                            help='directory-of-documents')
    arg_parser.add_argument('-d', '--dictionary', required=True,
                            help='dictionary-file')
    arg_parser.add_argument('-p', '--posting', required=True,
                            help='postings-file')
    return arg_parser.parse_args()


if __name__ == '__main__':
    main()
