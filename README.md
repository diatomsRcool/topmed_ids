# topmed_ids

This repository contains the code and data sets for linking TOPMed resources to normalized phenotypes in an ontology.

The topmed_curies.tsv file contains mappings across several ontologies for each variable and included the variable_phv, data set url, and study url. It was produced by phv_to_pheno.py.

## File explanations

2018-10-05_1214_tagged_variables.txt: This file is from TOPMed. It maps each variable to a normalized phenotype term.

curie_table.tsv: This file is from the Haendel lab. It maps each of the normalized phenotype terms used in the tagged_variables file and maps them to ontology terms from MONDO, HPO, NCIT, OBA, etc.

topmed_urls.p: This is a pickled dictionary. The keys are variable_phv identifiers that correspond to the tagged_variables file from TOPMed. The values are the URLs for the splash pages in dbGAP for the data set and the study where the variable is located. The URLs are separated by |. The data set URL is first.
