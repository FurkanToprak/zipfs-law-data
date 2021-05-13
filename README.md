# zipf-data

A repository that generates [Zipf's Law](https://en.wikipedia.org/wiki/Zipf%27s_law) data on many languages.

The exact number is to be determined.

## Languages Analyzed: 122

```
['Afrikaans', 'Amharic', 'Aragonese', 'Arabic', 'Assamese', 'Avaric', 'Azerbaijani', 'Bashkir', 'Belarusian', 'Bulgarian', 'Bengali', 'Tibetan', 'Breton', 'Bosnian', 'Catalan', 'Chechen', 'Corsican', 'Czech', 'Chuvash', 'Welsh', 'Danish', 'German', 'Dhivehi', 'Modern Greek (1453-)', 'English', 'Esperanto', 'Spanish', 'Estonian', 'Basque', 'Persian', 'Finnish', 'French', 'Western Frisian', 'Irish', 'Scottish Gaelic', 'Galician', 'Guarani', 'Gujarati', 'Manx', 'Hebrew', 'Hindi', 'Croatian', 'Haitian', 'Hungarian', 'Armenian', 'Interlingua (International Auxiliary Language Association)', 'Indonesian', 'Interlingue', 'Ido', 'Icelandic', 'Italian', 'Japanese', 'Javanese', 'Georgian', 'Kazakh', 'Central Khmer', 'Kannada', 'Korean', 'Kurdish', 'Komi', 'Cornish', 'Kirghiz', 'Latin', 'Luxembourgish', 'Limburgan', 'Lao', 'Lithuanian', 'Latvian', 'Malagasy', 'Macedonian', 'Malayalam', 'Mongolian', 'Marathi', 'Malay (macrolanguage)', 'Maltese', 'Burmese', 'Nepali (macrolanguage)', 'Dutch', 'Norwegian Nynorsk', 'Norwegian', 'Occitan (post 1500)', 'Oriya (macrolanguage)', 'Ossetian', 'Panjabi', 'Polish', 'Pushto', 'Portuguese', 'Quechua', 'Romansh', 'Romanian', 'Russian', 'Sanskrit', 'Sardinian', 'Sindhi', 'Serbo-Croatian', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Albanian', 'Serbian', 'Sundanese', 'Swedish', 'Swahili (macrolanguage)', 'Tamil', 'Telugu', 'Tajik', 'Thai', 'Turkmen', 'Tagalog', 'Turkish', 'Tatar', 'Uighur', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Volapük', 'Walloon', 'Yiddish', 'Yoruba', 'Chinese']
```

## Language Model

From facebookresearch's pretrained model lid.176.bin - [download here](https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin).

## Install Dependencies

```
python3 -m venv ./venv
source /venv/bin/activate
pip3 install -r requirements.txt
```

## Run Program

```
python3 main.py
```
