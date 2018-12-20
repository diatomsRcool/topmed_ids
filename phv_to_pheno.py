import pickle

infile = open('2018-10-05_1214_tagged_variables.txt', 'r')

url_dict = pickle.load(open('topmed_urls.p', 'rb'))

curies = open('curie_table.tsv', 'r')

out_file = open('topmed_curies.tsv', 'w')

out_file.write('variable_phv	tag_id	ncit	hpo	mondo	efo	oba	data_set	study\n')

next(infile)
for line in infile:
	row = line.split('\t')
	tag_id = row[0]
	variable_phv = row[2]
	if variable_phv in url_dict:
		x,y = url_dict[variable_phv].split('|')
	else:
		continue
	curies.seek(0)	
	for line in curies:
		row = line.split('\t')
		topmed_id = row[3]
		if topmed_id == tag_id:
			ncit = row[4]
			hpo = row[7]
			mondo = row[10]
			efo = row[13]
			oba = row[16]
			out_file.write('\t'.join([variable_phv,tag_id,ncit,hpo,mondo,efo,oba,x,y]) + '\n')
		else:
			continue