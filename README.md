# deeppunct

Pre-trained models (trained on google news, wikipedia and tatoeba) are available at https://drive.google.com/open?id=1Yd8cJaqfQkrJMbRVWIWtuyo4obTDYu-e

Demo of the model trained on google news corpus is available at http://bpraneeth.com/projects

Usage:
```
from deeppunct import DeepPunct
punct_correct = DeepPunct('params_path', 'checkpoint_path')
punct_correct.punctuate('hey')
'Hey!'
```

# Installation:

pip install deeppunct

# Points to Note:

Max input and output lengths are 200

Segment text into sentences using https://github.com/bedapudi6788/deepsegment and run punctuation correction on each sentence seperately.
