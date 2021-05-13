# detect language model
import fasttext
from pycountry import languages

PRETRAINED_MODEL_PATH = 'lid.176.bin'
LANGUAGE_LABEL_PREFIX = '__label__'

# load model
model = fasttext.load_model(PRETRAINED_MODEL_PATH)

# input sentences
sampleSentences = ['вот', 'hello', 'hola mi amigo']

# create prediction
language_model_predictions = model.predict(sampleSentences)

# parallel arrays
language_predictions = language_model_predictions[0]
language_prediction_certainties = language_model_predictions[1]

for i in range(0, len(sampleSentences)):
    language_prediction_certainty = language_prediction_certainties[i][0]
    language_prediction = language_predictions[i]
    test_result = language_prediction[0][len(LANGUAGE_LABEL_PREFIX):]
    language_prediction_result = languages.get(alpha_2=test_result)
    predicted_language_name = language_prediction_result.name
    print(f'Sentence "{sampleSentences[i]}" is in {predicted_language_name} with probability {language_prediction_certainty}')
