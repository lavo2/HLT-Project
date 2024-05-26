import stanza
import pandas as pd
import re
from tqdm import tqdm

def clean_text(s):
    s = s.lower()
    # if you encounter a - or ' (or something else) in the text, replace it with a space
    #TODO: right?
    s1 = re.sub(r'[^a-z\s]', ' ', s)
    s1 = ' '.join([w for w in s1.split() if len(w) > 2])
    # remove multiple spaces and starting and ending spaces
    s2 = re.sub(r'\s+', ' ', s1).strip()
    return s2

def clean_vocabulary(df):
    df['ingredients'] = df['ingredients'].apply(clean_text)
    df = df.drop_duplicates()
    df = df[df['ingredients'] != '']

    nlp = stanza.Pipeline(lang='en', processors='tokenize, mwt, pos, lemma', use_gpu=True)
    
    # definition of new dictionary
    cleaned_ingredients = []

    with tqdm(total=len(df)) as pbar:
        for ingredient in  df['ingredients']:
            # Process ingredient through the pipeline
            doc = nlp(ingredient)
            
            # Extract tokenized forms, part-of-speech tags, and lemmatized forms
            tokens = [word.text for sent in doc.sentences for word in sent.words]
            pos_tags = [word.upos for sent in doc.sentences for word in sent.words]
            lemmas = [word.lemma for sent in doc.sentences for word in sent.words]
            
            ### NOTICE THAT WE ARE USING `lemmas` INSTEAD OF `tokens`, so we will define our clean dictionary with the pure form of the words (their lemmatization!!!) ###
            # eliminate the tokens in `tokens` that are ADJ in `pos_tags`
            tokens = [lemmas[i] for i in range(len(tokens)) if pos_tags[i] != 'ADJ' and pos_tags[i] != 'PROPN' and pos_tags[i] != 'VERB']

            # reconvert tokens to a string
            cleaned_ingredient = ' '.join(tokens)

            # append to the list
            cleaned_ingredients.append(cleaned_ingredient)
            pbar.update(1)

    cleaned_df = pd.DataFrame(cleaned_ingredients, columns=['ingredients'])
    cleaned_df = cleaned_df.drop_duplicates()
    cleaned_df = cleaned_df[cleaned_df['ingredients'] != '']
    return cleaned_df


def clean_ingredients_list(df):
    ingredients = []
    for i in range(len(df)):
        ing = (df['ingredients'][i].split(','))
        ingredients.append(ing)
    ingredients[0]
    df = pd.DataFrame(ingredients)
    df = df.map(lambda x: x if x is not None else '')
    df = df.map(clean_text)
    nlp = stanza.Pipeline(lang='en', processors='tokenize, mwt, pos, lemma', use_gpu=True)
   

    ingredients_l = df.values.tolist()

    cleaned_ingredients = []

    with tqdm(total=len(df)) as pbar:
        for row in ingredients_l:
            cleaned_row = []
            for ingredient in row:
                # Process ingredient through the pipeline
                doc = nlp(ingredient)
                
                # Extract tokenized forms, part-of-speech tags, and lemmatized forms
                tokens = [word.text for sent in doc.sentences for word in sent.words]
                pos_tags = [word.upos for sent in doc.sentences for word in sent.words]
                lemmas = [word.lemma for sent in doc.sentences for word in sent.words]
                
                ### NOTICE THAT WE ARE USING `lemmas` INSTEAD OF `tokens`, so we will define our clean dictionary with the pure form of the words (their lemmatization!!!) ###
                # eliminate the tokens in `tokens` that are ADJ in `pos_tags`
                tokens = [lemmas[i] for i in range(len(tokens)) if pos_tags[i] != 'ADJ' and pos_tags[i] != 'PROPN' and pos_tags[i] != 'VERB']

                # reconvert tokens to a string
                cleaned_ingredient = ' '.join(tokens)

                # append to the list
                cleaned_row.append(cleaned_ingredient)

            cleaned_ingredients.append(cleaned_row)
            pbar.update(1)

    # remove duplicates
    for i in range(len(cleaned_ingredients)):
        cleaned_ingredients[i] = list(set(cleaned_ingredients[i]))

    # remove empty strings
    cleaned_ingredients = [[x for x in row if x != ''] for row in cleaned_ingredients]

    cleaned_df = pd.DataFrame(cleaned_ingredients)

    return cleaned_df


