import sys
import re
import time
from argparse import ArgumentParser

alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def split_into_sentences(text, lang):
	text = " " + text + "  "
	text = text.replace("\n"," ")
	text = re.sub(prefixes,"\\1<prd>",text)
	text = re.sub(websites,"<prd>\\1",text)
	if "Ph.D" in text: 
		text = text.replace("Ph.D.","Ph<prd>D<prd>")
	text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
	text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
	text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
	text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
	text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
	text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
	text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
	if "”" in text: text = text.replace(".”","”.")
	if "\"" in text: text = text.replace(".\"","\".")
	if "!" in text: text = text.replace("!\"","\"!")
	if "?" in text: text = text.replace("?\"","\"?")
	if(lang == "hin"):
		text = text.replace("।", "।<stop>")
	if(lang == "urd"):
		text = text.replace("؟","؟<stop>")
		text = text.replace("۔","۔<stop>")
	text = text.replace(".",".<stop>")
	text = text.replace("?","?<stop>")
	text = text.replace("!","!<stop>")
	text = text.replace("<prd>",".")
	sentences = text.split("<stop>")
	sentences = sentences[:-1]
	sentences = [s.strip() for s in sentences]
	return sentences


parser = ArgumentParser(description='This script will align source and target files\n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=input.txt -b=target.txt -s=eng -t=tel"
						)
parser.add_argument("-i", "--input", dest="inputfile",
					help="provide input file name",required=True)
parser.add_argument("-b", "--bilingualfile", dest="alignfile",
					help="provide file to be aligned with input file",required=True)
parser.add_argument("-s", "--srclang", dest="srclang",
					help="provide lang=eng/hin/tel of the input file",required=True)
parser.add_argument("-t", "--tgtlang", dest="tgtlang",
					help="provide lang=eng/hin/tel of the file to be aligned",required=True)

args = parser.parse_args()

input_file = args.inputfile
align_file = args.alignfile
src_lang = args.srclang
tgt_lang = args.tgtlang

#open file using open file mode
fp1 = open(input_file) # Open file on read mode -- input file
src_lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

#open file using open file mode
fp2 = open(align_file) # Open file on read mode -- input file
tgt_lines = fp2.read().split("\n") # Create a list containing all lines
fp2.close() # Close file

if(len(src_lines) != len(tgt_lines)):
	print("Source and Target files line number mismatched..Exiting")
	time.sleep(1.5)
	exit(0)

for s,t in zip(src_lines, tgt_lines):
	src_sentences = split_into_sentences(s, src_lang)
	tgt_sentences = split_into_sentences(t, tgt_lang)

	#print(src_sentences, tgt_sentences)
	src_sent_length = len(src_sentences)
	tgt_sent_length = len(tgt_sentences)

	if(src_sent_length == tgt_sent_length):
		for ss,ts in zip(src_sentences, tgt_sentences):
			print(ss, ts)
	if(src_sent_length > tgt_sent_length):
		i = 0
		for ss in src_sentences:
			try :
				tgt_sentences[i]
				try :
					tgt_sentences[i+1]
					print(ss, tgt_sentences[i])
				except:
					print(" ".join(src_sentences[i:]), tgt_sentences[i])
					break
					#print(ss, tgt_sentences[i])
			except:
				print(ss, " ")
			i = i + 1

	if(src_sent_length < tgt_sent_length):
		i = 0
		for tt in tgt_sentences:
			try :
				src_sentences[i]
				try:
					src_sentences[i+1]
					print(src_sentences[i], tt)
				except:
					print(src_sentences[i], " ".join(tgt_sentences[i:]))
					break
			except:
				print(" ", tt)
				#next
			i = i + 1


	#print(s,t)
