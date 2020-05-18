# Text_as_data

## Text Pre-processing
drop HTML markup, punctuation, numbers, capitalization, and stopwords
Normalize
remove terms rare terms





## Feature Selection
Method 1: bag word
Shortcoming: 1. Do not demonstrate the order of the word
2. High-demensional sparse feature matrix ---- HASHING

Method 2: N-grams

Method 3: TF-IDF term frequency- inverse document frequency
Strength: Highlight some specific question which does not occure that often
          down-weight terms that appear in many documents and could give better results.
