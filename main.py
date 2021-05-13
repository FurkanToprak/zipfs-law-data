# detect language model
import fasttext
from pycountry import languages

PRETRAINED_MODEL_PATH = 'lid.176.bin'
LANGUAGE_LABEL_PREFIX = '__label__'


sampleSentence = ['вот', 'hello']
model = fasttext.load_model(PRETRAINED_MODEL_PATH)
language_model_prediction = model.predict(sampleSentence)
print(language_model_prediction)
language_prediction_certainty = language_model_prediction[1][0]
test_result = language_model_prediction[0][0][len():]
language_prediction_result = languages.get(alpha_2=test_result)
predicted_language_name = language_prediction_result.name

print(predicted_language_name, language_prediction_certainty)
