import json
p='Projekt.ipynb'
with open(p,'r',encoding='utf-8') as f:
    nb=json.load(f)
for cell in nb.get('cells',[]):
    if cell.get('cell_type')=='code':
        cell['outputs']=[]
        cell['execution_count']=None
with open(p,'w',encoding='utf-8') as f:
    json.dump(nb,f,ensure_ascii=False,indent=1)
print('Cleared outputs')
