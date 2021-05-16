import string
import pymorphy2
from nltk import word_tokenize
from nltk.corpus import stopwords
from words import in_words

russian_stopwords = stopwords.words("russian")


def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars])


def format_message(text):
    text = text.lower()

    print(text)

    text = remove_chars_from_text(text, string.punctuation)
    text = remove_chars_from_text(text, string.digits)
    text_tokens = word_tokenize(text)

    for stop in russian_stopwords:
        if stop in text_tokens:
            text_tokens.remove(stop)

    morph = pymorphy2.MorphAnalyzer()

    for i in range(len(text_tokens)):
        if in_words(text_tokens[i]):
            text_tokens[i] = in_words(text_tokens[i])
        else:
            text_tokens[i] = morph.parse(text_tokens[i])[0].normal_form
    return text_tokens

print(format_message('Что такое самматив?'))

