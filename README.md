# FRDF

## About
FRDF is a module for knowledge extraction based on Frame-semantic parsing.

## prerequisite
* `python 3`

## How to use
**Install**
```
git clone https://github.com/machinereading/FRDF.git
```

### Input
A list of annotations. This is an output of [KAIST-frame-parser](https://github.com/machinereading/KAIST_frame_parser)
```
[
  [
    ['헤밍웨이는', '1899년', '7월', '21일', '미국', '일리노이에서', '태어났고,', '62세에', '자살로', '사망했다.'], 
    ['_', '_', '_', '_', '_', '_', '태어나다.v', '_', '_', '_'], 
    ['_', '_', '_', '_', '_', '_', 'Being_born', '_', '_', '_'], 
    ['B-Child', 'B-Time', 'I-Time', 'I-Time', 'B-Place', 'I-Place', 'O', 'O', 'O', 'O']
  ], 
  ...
]
```

### Usage with [KAIST-frame-parser](https://github.com/machinereading/KAIST_frame_parser)

**Import modules**
```
from KAIST_frame_parser import srl_based_parser
from FRDF import frdf
```

**Load modules (i.e. parser and FRDF module)**
```
model_dir = {your_model_path}
FRDF = frdf.frame2RDF()
parser = srl_based_parser.SRLbasedParser(model_dir=model_dir)
```

**Run parser, then inputs it to FRDF**
```
text  = '헤밍웨이는 1899년 7월 21일 미국 일리노이에서 태어났고, 62세에 자살로 사망했다.'
parsed = parser.parser(text)
triples = FRDF.frame2dbo(parsed['conll'])
pprint(triples)
```

```
[
  ('헤밍웨이는', 'dbo:birthDate', '1899년 7월 21일'),
  ('헤밍웨이는', 'dbo:birthPlace', '미국 일리노이에서'),
  ('헤밍웨이는', 'dbo:deathDate', '62세에'),
  ('헤밍웨이는', 'frdf:Death-Manner', '자살로')
]
```


## Licenses
* `CC BY-NC-SA` [Attribution-NonCommercial-ShareAlike](https://creativecommons.org/licenses/by-nc-sa/2.0/)
* If you want to commercialize this resource, [please contact to us](http://mrlab.kaist.ac.kr/contact)

## Publisher
[Machine Reading Lab](http://mrlab.kaist.ac.kr/) @ KAIST

## Contact
Younggyun Hahm. `hahmyg@kaist.ac.kr`, `hahmyg@gmail.com`

## Acknowledgement
This work was supported by Institute for Information & communications Technology Promotion(IITP) grant funded by the Korea government(MSIT) (2013-0-00109, WiseKB: Big data based self-evolving knowledge base and reasoning platform)
