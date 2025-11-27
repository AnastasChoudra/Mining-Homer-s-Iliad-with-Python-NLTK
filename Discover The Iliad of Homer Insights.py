# run this in a console / cell / scratch file
import nltk
#nltk.download('punkt')
#nltk.download('punkt_tab')   
#nltk.download('averaged_perceptron_tagger')
#nltk.download('averaged_perceptron_tagger_eng')
#nltk.download('popular')
from nltk import pos_tag, RegexpParser
import import_ipynb
from tokenize_words import word_sentence_tokenize
from chunk_counters import np_chunk_counter, vp_chunk_counter

# import text
text = open("the_iliad.txt",encoding='utf-8').read().lower()

# sentence and word tokenize text here
word_tokenized_text = word_sentence_tokenize(text)

# store and print any word tokenized sentence here
single_word_tokenized_sentence = word_tokenized_text[100]
print('Single Word-Tokenized Sentence (sentence #100):','\n')
print(single_word_tokenized_sentence,'\n')

# create a list to hold part-of-speech tagged sentences here
pos_tagged_text = list()

# create a for loop through each word tokenized sentence here
for word_tokenized_sentence in word_tokenized_text:
    # part-of-speech tag each sentence and append to list of pos-tagged sentences here
    pos_tagged_text.append(pos_tag(word_tokenized_sentence))

# store and print any part-of-speech tagged sentence here
single_pos_sentence = pos_tagged_text[100]
print('POS-Tags for the Same Sentence:','\n')
print(single_pos_sentence,'\n')

# define noun phrase chunk grammar here
np_chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"

# create noun phrase RegexpParser object here
np_chunk_parser = RegexpParser(np_chunk_grammar)

# define verb phrase chunk grammar here
vp_chunk_grammar = "VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}"

# create verb phrase RegexpParser object here
vp_chunk_parser = RegexpParser(vp_chunk_grammar)

# create a list to hold noun phrase chunked sentences and a list to hold verb phrase chunked sentences here
np_chunked_text = list()
vp_chunked_text = list()

# create a for loop through each pos-tagged sentence here
for pos_tagged_sentence in pos_tagged_text:
    # chunk each sentence and append to list here
    np_chunked_text.append(np_chunk_parser.parse(pos_tagged_sentence))
    vp_chunked_text.append(vp_chunk_parser.parse(pos_tagged_sentence))

# store and print the most common NP-chunks here
most_common_np_chunks = np_chunk_counter(np_chunked_text)
print('Most Common Noun Phrase (NP) Chunks:','\n')
print(most_common_np_chunks,'\n')

# store and print the most common VP-chunks here
most_common_vp_chunks = vp_chunk_counter(vp_chunked_text)
print('Most Common Verb Phrase (VP) Chunks:','\n')
print(most_common_vp_chunks)
