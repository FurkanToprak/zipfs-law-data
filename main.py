# detect language model
import fasttext
from pycountry import languages

PRETRAINED_MODEL_PATH = 'lid.176.bin'
model = fasttext.load_model(PRETRAINED_MODEL_PATH)
sampleSentence = 'вот'
language_model_prediction = model.predict(sampleSentence)
language_prediction_certainty = language_model_prediction[1][0]
test_result = language_model_prediction[0][0][len('__label__'):]
yuck = languages.get(alpha_2=test_result)
converted_name = yuck.name
print(test_result, converted_name, language_prediction_certainty)
