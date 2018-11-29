from txt2txt import build_model, infer


class DeepPunct():
    deeppunct_model = None
    def __init__(self, params_path, checkpoint_path):
        # loading the model
        DeepPunct.deeppunct_model = build_model(params_path)
        DeepPunct.deeppunct_model[0].load_weights(checkpoint_path)
    
    def punctuate(self, sentence):
        if not DeepPunct.deeppunct_model:
            print('Please load the model first')

        sentence = sentence.strip()
        sentence = infer(sentence, DeepPunct.deeppunct_model[0], DeepPunct.deeppunct_model[1])
        
        return sentence
