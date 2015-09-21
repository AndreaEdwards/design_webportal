from tornado.web import RequestHandler
from src.pdb import (PDBFromUniprot, 
	CIFFromUniprot, LigandBindingSite, EditPDB, 
	SurfaceResidues, Rosetta, MutantListMaker,
	DDGMonomer)


class ProteinHandler(RequestHandler):

    def get(self):
        self.render("protein.html", step='0', uniprot_id='', genbank='', pdb_codes=[])

    def post(self):
    	#print step
    	#if step == '0':
    	accession = self.get_argument("uniprot")
    	# Search PDB for codes matching uniprot id
    	uniprot_id = accession
    	queryText = ("<orgPdbQuery>" +
    				 	"<queryType>org.pdb.query.simple.UpAccessionIdQuery</queryType>" +
    						"<description>Simple query for a list of Uniprot Accession IDs: " + uniprot_id + " </description>" +
    						"<accessionIdList>" + uniprot_id + "</accessionIdList>" +
    					"</orgPdbQuery>")
    	pdb_from_uniprot = PDBFromUniprot()
    	pdb_codes = pdb_from_uniprot.get_pdb_id(queryText)
    	if pdb_codes != []:
    		step = '1'
    		self.render("protein.html", step=step, uniprot_id=uniprot_id, pdb_codes=pdb_codes)
    		#print pdb_codes
    	else:
    		print "No structures found in Protien Data Bank"
    	#elif step == '1':
    	#pdb_getter = PDBFromUniprot()
    	#pdb_code = '2XGE'
    	#pdb_getter.fetch_pdb(pdb_code)



    	#	# Download .pdb using pdb_id
    	#	# THIS WORKS. DO NOT CHANGE
    	#	pdb_getter = PDBFromUniprot()
    	#	pdb_code = '2XGE'
    	#	pdb_getter.fetch_pdb(pdb_code)
    	#	cif_getter = CIFFromUniprot()
    	#	cif_getter.fetch_mmCIF(pdb_code, pdb_dir)

#    def post(self):
#    	seletect_organism = self.get_argument("usage_table")
#    	if seletect_organism in organism_mapping:
#    		sorted_dict = util.BuildUsageDict(organism_mapping[seletect_organism])
#    		organism_name = organism_names[seletect_organism]
#    	else:
#    		pass
#    	rules_dict, inverse_dict = util.BuildRulesDict('rules.txt')
#    	if self.get_argument("keep_or_remove") == 'remove':
#            remove_aa = self.get_arguments('aa')
#        else:
#            selected_aa = self.get_arguments('aa')
#            remove_aa = list(aa.difference(selected_aa))
#    	filtered_dict = util.EditUsageDict(remove_aa, sorted_dict)
#    	selection = self.get_argument("compression_method")
#    	if selection == 'rank':
#    	    print selection
#    	    threshold = 2
#    	    new_dict = RemoveCodonByRank(threshold, filtered_dict)
#    	else:
#    	    print selection
#    	    threshold = 0.04
#    	    new_dict = RemoveCodonByUsage(threshold, filtered_dict)
#
#    	codon_order = new_dict.keys()
#
#    	codon_count = BuildCodonCount(new_dict, codon_order)
#
#    	redundancy = 0
#
#    	best_result = start_multiprocessing(new_dict,rules_dict,codon_count, redundancy, processes = 3)
#    	self.render("dynamcc_0_results.html", organism=organism_name, remove_aa=remove_aa, best_result=best_result)
#
#
#class DynamccRHandler(RequestHandler):
#    def get(self):
#        self.render("dynamcc_R.html")
#
#    def post(self):
#    	seletect_organism = self.get_argument("usage_table")
#        if seletect_organism in organism_mapping:
#    		sorted_dict = util.BuildUsageDict(organism_mapping[seletect_organism])
#    		organism_name = organism_names[seletect_organism]
#    	else:
#    		pass
#    	rules_dict, inverse_dict = util.BuildRulesDict('rules.txt')
#    	if self.get_argument("keep_or_remove") == 'remove':
#            remove_aa = self.get_arguments('aa')
#        else:
#            selected_aa = self.get_arguments('aa')
#            remove_aa = list(aa.difference(selected_aa))
#    	filtered_dict = util.EditUsageDict(remove_aa, sorted_dict)
#    	InUse_dict = ReformatUsageDict(filtered_dict)
#    	codon_list = BestList(filtered_dict)
#    	in_use = FlagInUse(codon_list, InUse_dict)
#    	best_compression = execute_algorithm(codon_list,in_use,rules_dict,inverse_dict)
#    	#print 'Maximally compressed list,', best_compression, ', Length: %i' % len(best_compression)
#    	self.render("dynamcc_R_results.html", organism=organism_name, remove_aa=remove_aa, best_compression=best_compression, length=len(best_compression))










