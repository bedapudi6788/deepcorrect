import pydload
import os
import logging
from txt2txt import build_model, infer, infer_greedy

model_links = {
    'en_punct': {
        'checkpoint': '..',
        'params': '..'
    }
}

class DeepCorrect():
    deepcorrect_model = None
    def __init__(self, model_name):
        if model_name not in model_links:
            print("DeepSegment doesn't support '" + model_name + "' yet.")
            print("Please raise a issue at https://github.com/bedapudi6788/deepsegment to add this language into future checklist.")
            return None

        # loading the model
        home = os.path.expanduser("~")
        lang_path = os.path.join(home, '.DeepCorrect_' + model_name)
        checkpoint_path = os.path.join(lang_path, 'checkpoint')
        params_path = os.path.join(lang_path, 'params')
        
        if not os.path.exists(lang_path):
            os.mkdir(lang_path)

        if not os.path.exists(checkpoint_path):
            print('Downloading checkpoint', model_links[model_name]['checkpoint'], 'to', checkpoint_path)
            pydload.dload(url=model_links[model_name]['checkpoint'], save_to_path=checkpoint_path, max_time=None)

        if not os.path.exists(params_path):
            print('Downloading preprocessing utils', model_links[model_name]['utils'], 'to', params_path)
            pydload.dload(url=model_links[model_name]['utils'], save_to_path=params_path, max_time=None)


        DeepCorrect.deepcorrect_model = build_model(params_path)
        DeepCorrect.deepcorrect_model[0].load_weights(checkpoint_path)
    
    def correct(self, sentence, beam_size = 1):
        if not DeepCorrect.deepcorrect_model:
            print('Please load the model first')

        sentence = sentence.strip()

        if beam_size == 1:
            sentence = infer_greedy(sentence, DeepCorrect.deepcorrect_model[0], DeepCorrect.deepcorrect_model[1])
        
        elif beam_size > 1:
            sentence = infer(sentence, DeepCorrect.deepcorrect_model[0], DeepCorrect.deepcorrect_model[1], beam_size = beam_size)
        
        return sentence
