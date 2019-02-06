import pickle
import re

#opening input files and dictionaries
infile = open('2018-12-28_1202_tagged_variables.txt', 'r')
#url_dict = pickle.load(open('topmed_urls.p', 'rb'))
curies = open('curie_table.tsv', 'r')

#create output file
out_file = open('topmed_curies.tsv', 'w')
#add column headers to output file
out_file.write('variable_phv	tag_id	ncit	hpo	mondo	efo	oba	data_set	study\n')

next(infile)
for line in infile: #iterate over infile
	row = line.split('\t')
	tag_id = row[0]
	variable_phv = row[2]
	variable_acc = row[3]
	set_acc = row[4]
	m = re.match('\w\w\w[\d]+', set_acc)
	set_id = m[0][-4:]
	study_acc = row[5]
	set_url = 'https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=' + study_acc 
	study_url = 'https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/dataset.cgi?study_id=' + study_acc + '&pht=' + set_id
	curies.seek(0)	
	for line in curies: #look for phenotype in ontology map
		row = line.split('\t')
		topmed_id = row[3]
		if topmed_id == tag_id: #when phenotype found, grab ontology terms
			ncit = row[4]
			hpo = row[7]
			mondo = row[10]
			efo = row[13]
			oba = row[16]
			out_file.write('\t'.join([variable_phv,tag_id,ncit,hpo,mondo,efo,oba,set_url,study_url]) + '\n') #output mapping
		else:
			continue