import argparse

def is_valid(word,new_word,list):
    if (new_word in list):
        return False
    i=1
    while (len(word)>0 and len(new_word)>0 and i>-1):
        i= word.find(new_word[0])
        if (i==-1):
            break
        word=word.replace(new_word[0],'',1)
        new_word=new_word.replace(new_word[0],'',1)
    return len(new_word)==0


def generate_words(word,new_word,list):
    if (len(new_word)==len(word)):
        print(new_word)
        list.append(new_word)
        return
    for w in word:
        if (is_valid(word,new_word + w,list)):
            new_word= new_word + w
            generate_words(word,new_word,list)
            new_word= new_word[:-1]

parser= argparse.ArgumentParser(prog='Script for generate anagrams from a pivot word')
parser.add_argument('-w','--word',required=True,help='pivot word')
args= vars(parser.parse_args())

word= args['word']
list=[]

generate_words(word,'',list)