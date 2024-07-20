import nltk
from nltk.tag import PerceptronTagger
from nltk import word_tokenize

# Ensure the necessary components are downloaded
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

# Initialize the tagger
tagger = PerceptronTagger()

def verb(tokens):
    tagged = tagger.tag(tokens)
    errors = 0
    for i in range(len(tagged) - 1):
        current_word, current_tag = tagged[i]
        next_word, next_tag = tagged[i + 1]

        # Incorrect use of past tense instead of infinitive
        if current_tag == 'TO' and next_tag != 'VB':
            errors += 1

        # Continuous without auxiliary (he cooking quickly)
        if current_tag in ['NN', 'PRP'] and next_tag == 'VBG':
            errors += 1

        # "To be" followed by an inappropriate tag
        if current_tag in ['VBZ', 'VBP', 'VBD', 'VB'] and current_word.lower() in ['is', 'are', 'was', 'were', 'be']:
            if next_tag not in ['VBG', 'VBN']:
                errors += 1

        # Adverb consistency
        if current_tag == 'WRB' and next_tag not in ['VB', 'VBD', 'VBG']:
            errors += 1

    return errors

def agreement(tokens):
    tagged = tagger.tag(tokens)
    errors = 0
    for i in range(len(tagged) - 1):
        current_word, current_tag = tagged[i]
        next_word, next_tag = tagged[i + 1]

        # Singular subject with plural verb and vice versa
        if (current_tag in ['NN', 'NNP'] and next_tag == 'VBP') or \
           (current_tag in ['NNS', 'NNPS'] and next_tag == 'VBZ'):
            errors += 1

    return errors
