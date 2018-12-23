# deepcorrect

Pre-trained models for punctuation correction (trained on google news, wikipedia and tatoeba) are available at https://drive.google.com/open?id=1Yd8cJaqfQkrJMbRVWIWtuyo4obTDYu-e

Demo of the punctuation model trained on google news corpus is available at http://bpraneeth.com/projects

This repo uses a seq2seq model written by me in keras with tensorflow backend. The multi-purpose seq2seq model can be found at https://github.com/bedapudi6788/txt2txt/

Usage:
```
from deepcorrect import DeepCorrect
corrector = DeepCorrect('params_path', 'checkpoint_path')
corrector.correct('hey')
'Hey!'
```

# Installation:

pip install deepcorrect

# Points to Note:

Max input and output lengths are 200

Segment text into sentences using https://github.com/bedapudi6788/deepsegment and run punctuation correction on each sentence seperately.
