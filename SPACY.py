from spacy.tokens import Span
import spacy
nlp = spacy.load("en_core_web_sm")
# Create a Doc object
doc = nlp("I live in New York")
# Span for "New York" with label GPE (geopolitical)
span = Span(doc, 3, 5, label="GPE")
print(span.text)
# 'New York'


doc = nlp("Larry Page founded Google")
# Text and label of named entity span
print([(ent.text, ent.label_) for ent in doc.ents])
# [('Larry Page', 'PERSON'), ('Google', 'ORG')]

from spacy import displacy

doc = nlp("Larry Page founded Google")
displacy.render(doc, style="ent")
#displacy.serve(doc, style="ent")

nlp = spacy.load("en_core_web_sm")
doc = nlp("The 4 tools I used to teach myself data science without spending a dollar.")
displacy.serve(doc, style="dep")