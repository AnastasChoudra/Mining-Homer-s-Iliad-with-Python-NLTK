**A compact, end-to-end Natural-Language-Processing project that ingests the full text of Homer’s Iliad, extracts every sentence, tags each word with its part-of-speech, and surfaces the 30 most frequent noun phrases and verb phrases that drive the epic’s narrative.**

*Tech stack & libraries*
- Python 3.12
- NLTK – sentence splitter (Punkt), word tokenizer, Perceptron POS-tagger, and RegexpParser for custom chunk grammars
- Collections.Counter – lightning-fast frequency counts
- Zero external APIs or paid services – 100 % open-source stack.

*What the code actually does*
- Cleans & lower-cases the raw Project-Gutenberg file (the_iliad.txt).
- Sentence-tokenises → word-tokenises → POS-tags the entire epic.
- Applies two hand-crafted regular-grammar patterns:
- NP: optional determiner + any adjectives + noun (<DT>?<JJ>*<NN>)
- VP: NP followed by a verb and optional adverb (<DT>?<JJ>*<NN><VB.*><RB.?>?)
- Counts every matching chunk across ~15 k sentences and returns the top-30 lists.
- Prints results to console – ready for downstream visualisation or résumé bullet points.

