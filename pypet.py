print 'Welome to Pypet!'

cat = {
  'name': 'Mr Fluffy',
  'hungry': True,
  'weight': 9.5,
  'number_of_toys': 5,
  'photo': '(=^o.o^=)__',
}

mouse = {
  'name': 'Mouse',
  'hungry': False,
  'weight': 1.5,
  'number_of_toys': 6,
  'photo': '<:3 )~~~~',
}

pets = [cat, mouse]

def feed(cat):
	if cat['hungry']:
		cat['hungry'] = False
		cat['weight']+=1
	else:
		print 'The Pypet is not hungry!'

for pet in pets:
  feed(pet)
  print pet


