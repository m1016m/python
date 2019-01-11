#pprint module pprint()印出好看的結果 2016/2/8
from pprint import pprint
from collections import OrderedDict
quotes=OrderedDict([('Moe','A wise guy'),('Larry','Ow!'),('Curly','Nyuk nyuk'),])
print(quotes)
pprint(quotes)

food_list=['apple','eggs','cake','water']
print(food_list)
pprint(food_list)

#??????? 