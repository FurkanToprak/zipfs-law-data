import wikipedia
from pycountry import languages
import random
from collections import Counter
from itertools import chain
from string import punctuation
import operator

NUMBER_OF_ARTICLES = 10000

removePunctuation = str.maketrans('', '', punctuation)

wikipedia_languages = wikipedia.languages()

long_used_name = []
used = []
no_translation = []

for wikipedia_language in wikipedia_languages:
    language_obj = languages.get(alpha_2=wikipedia_language)
    if language_obj is None:
        no_translation.append(wikipedia_language)
    else:
        long_language_name = language_obj.name
        long_used_name.append(long_language_name)
        used.append(wikipedia_language)

# print("------")
# print("USED:", len(used))
# print(used)
# print(long_used_name)
# print("-----")
# print("NOT USED:", len(not_used))
# print(not_used)
# print("NO TRANSLATION:", len(no_translation))
# print(no_translation)

for i in range(min(1, len(used))):
    language = used[i]
    long_language = long_used_name[i]
    wikipedia.set_lang(language)
    # article_samples = []
    language_histogram = dict()
    for i in range(0, NUMBER_OF_ARTICLES // 10):
        random_articles = wikipedia.random(pages=10)
        for random_article in random_articles:
            try:
                try:
                    wiki_page_obj = wikipedia.page(title=random_article)
                # Wikipedia isn't sure what the title is referring to
                except wikipedia.DisambiguationError as amb_err:
                    continue
                    # random_page = random.choice(amb_err.options)
                    # # print(amb_err.options)
                    # try:
                    #     wiki_page_obj = wikipedia.page(title=random_page)
                    # # sometimes there is no fix to ambiguity
                    # except wikipedia.DisambiguationError as amb_err_2:
                    #     continue # if no fix, skip

                wiki_page_content = wiki_page_obj.content
                # stripped and case-insensitive
                preprocessed_wiki_page_words = wiki_page_content.translate(
                    removePunctuation).lower().split()
                # print(preprocessed_wiki_page_words)
                for preprocessed_wiki_page_word in preprocessed_wiki_page_words:
                    if preprocessed_wiki_page_word in language_histogram:
                        language_histogram[preprocessed_wiki_page_word] += 1
                    else:
                        language_histogram[preprocessed_wiki_page_word] = 1

            except wikipedia.exceptions.PageError as no_such_random_page_error:
                pass

    output_file = open(f'word-freq-{wikipedia_language}.csv', 'w')
    # sort words by prevelance
    ordered_histogram = sorted(
        language_histogram.items(), key=lambda kv: kv[1], reverse=True)
    datapoints = 0
    for datum in ordered_histogram:
        output_file.write(f'{datum[0]},{datum[1]}\n')
    output_file.close()
    print("Done with ", long_language)
