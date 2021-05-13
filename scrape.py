import wikipedia
from pycountry import languages

language_list_file = open("identifiable_languages_list.txt", "r")
language_list = language_list_file.read().split()
print(language_list)
wikipedia_languages = wikipedia.languages()

long_used_name = []
used = []
long_not_used_name = []
not_used = []
no_translation = []

for wikipedia_language in wikipedia_languages:
    language_obj = languages.get(alpha_2=wikipedia_language)
    if language_obj is None:
        no_translation.append(wikipedia_language)
    else:
        long_language_name = language_obj.name
        if wikipedia_language in language_list:
            long_used_name.append(long_language_name)
            used.append(wikipedia_language)
        else:
            long_not_used_name.append(long_language_name)
            not_used.append(wikipedia_language)

print("------")
print("USED:", len(used))
print(used)
print(long_used_name)
print("-----")
# print("NOT USED:", len(not_used))
# print(not_used)
# print("NO TRANSLATION:", len(no_translation))
# print(no_translation)
