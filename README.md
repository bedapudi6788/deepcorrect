# deeppunct

Pre-trained models available at https://drive.google.com/open?id=1g3gWMppxAZ4TBACnc8ewN3yUzpPuAE_L

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

Demo available at bpraneeth.com/projects
