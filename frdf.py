
# coding: utf-8

# In[5]:


import os
import sys
sys.path.append('../')
from FRDF import kotimex 


# In[2]:


def gen_mapping(mapping_file):
    with open(mapping_file, 'r') as f:
        next(f)
        lines = f.readlines()
    mappings = {}
    for line in lines:
        line = line.strip().split(',')
        frame, fe, rel = line[0],line[1],line[2]
        if frame not in mappings:
            mapping = {}
        else:
            mapping = mappings[frame]
        mapping[fe] = rel
        mappings[frame] = mapping
    return mappings

def get_frame(frames):
    frame = False
    for f in frames:
        if f != '_':
            frame = f   
    return frame


# In[3]:


class frame2RDF():
    def __init__(self):
        try:
            this_dir = os.path.dirname(os.path.abspath( __file__ ))
        except:
            this_dir = '.'
        mapping_file = this_dir+'/frame_dbo_mapping.csv'
        self.mapping = gen_mapping(mapping_file)
        
    def fe2dbo(self, frame, fe):
        rel = False
        if frame in self.mapping:
            fe2dbo = self.mapping[frame]
            if fe in fe2dbo:
                if fe2dbo[fe] == 'S':
                    rel = fe2dbo[fe]                
                elif 'dbo' in fe2dbo[fe]:
                    rel = fe2dbo[fe]
        if rel == False:
            rel = 'frdf:'+frame+'-'+fe
        return rel
        
    def frame2dbo(self, frame_conll, sentence_id='sent_1'):
        triples = []
        for anno in frame_conll:
            tokens, lus, frames, args = anno[0],anno[1],anno[2],anno[3]
            frame = get_frame(frames)
            if frame:
                sbj = False
                pred_obj_tuples = []
                for idx in range(len(args)):
                    arg_tag = args[idx]
                    arg_tokens = []
                    if arg_tag.startswith('B'):
                        fe_tag = arg_tag.split('-')[1]
                        arg_tokens.append(tokens[idx])
                        next_idx = idx + 1
                        while next_idx < len(args) and args[next_idx] == 'I-'+fe_tag:
                            arg_tokens.append(tokens[next_idx])
                            next_idx +=1
                        arg_text = ' '.join(arg_tokens)
                        fe = fe_tag
                        
                        # string to xsd
                        if fe == 'Time':
                            arg_text = kotimex.time2xsd(arg_text)
                        else:
                            arg_text = '\"'+arg_text+'\"'+'^^xsd:string'
                        
                        rel = frame2RDF.fe2dbo(self, frame, fe)
                        
                        if rel == 'S':
                            pass
#                             sbj = arg_text
                        else:
                            p = rel
                            o = arg_text
                            pred_obj_tuples.append( (p,o) )
                
                for p, o in pred_obj_tuples:
                    if sbj:
                        s = sbj
                    else:
                        s = 'frame:'+frame+'-'+sentence_id
                    triple = (s, p, o)
                    triples.append(triple)
        return triples

