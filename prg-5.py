from nltk import word_tokenize, pos_tag
s = input("Enter a sentence: ")
t = pos_tag(word_tokenize(s))
noun = []
pronoun = []
verb = []
adjective = []
adverb = []
for w, p in t:
    if p.startswith("NN"):
        noun.append(w)
    elif p.startswith("PRP"):
        pronoun.append(w)
    elif p.startswith("VB"):
        verb.append(w)
    elif p.startswith("JJ"):
        adjective.append(w)
    elif p.startswith("RB"):
        adverb.append(w)
print("Nouns:", noun)
print("Pronouns:", pronoun)
print("Verbs:", verb)
print("Adjectives:", adjective)
print("Adverbs:", adverb)
