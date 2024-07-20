from spellchecker import SpellChecker
import nltk
nltk.download('punkt')


def num_sentences(essay_text):
    sentences = nltk.sent_tokenize(essay_text)
    return len(sentences)


def spelling_mistakes(essay_text):
    spell = SpellChecker()
    words = nltk.word_tokenize(essay_text)
    misspelled = spell.unknown(words)
    return len(misspelled)

