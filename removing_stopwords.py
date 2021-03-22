import nltk
default_wt = nltk.word_tokenize
nltk.download("stopwords")
stopwords_list = nltk.corpus.stopwords.words("english")

def removing_stopwords(text):
    tokens = default_wt(text)
    stripped_tokens = [token.strip() for token in tokens]
    filtered_tokens = [stripped_token for stripped_token in stripped_tokens 
                       if stripped_token not in stopwords_list]
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text
