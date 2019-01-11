#module_9_stdlib_pprint.py 2016.4.18
#pprint module pprint()印出好看的結果 
from pprint import pprint
from collections import OrderedDict
quotes=OrderedDict([('Moe','A wise guy'),('Larry','Ow!'),('Curly','Nyuk nyuk'),])
print(quotes)
pprint(quotes,width=40) 

#OrderedDict([('Moe', 'A wise guy'),
#            ('Larry', 'Ow!'),
#            ('Curly', 'Nyuk nyuk')])

food_list=['apple','eggs','cake','water']
print(food_list)
pprint(food_list,width=40)

