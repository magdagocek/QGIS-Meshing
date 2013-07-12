class MeshData(object):
	"""class the data about the mesh file that will be used for testing"""

	node_dict = {}
	elems_list = []
	number_of_nodes = 0
	number_of_elems = 0


	def __init__(self, file_path):

		self.file_path = file_path

	def parse(self) :

		input_file = open(self.file_path, "r")

		current_line = input_file.readline()

		while current_line != "$Nodes\n" :
			# keep reading...
			current_line = input_file.readline()

		# delete "$Nodes" line
		current_line = input_file.readline()
		self.number_of_nodes = current_line
		current_line = input_file.readline()

		while current_line != "$EndNodes\n" :
			# keep adding to the dictionary
			current_line_as_list = current_line.split() # split into words

			# insert into dictionary
			self.node_dict[current_line_as_list[1]] =  current_line_as_list[2]
			current_line = input_file.readline()


		# reached end of nodes data
		current_line = input_file.readline()
		current_line = input_file.readline()
		self.number_of_elems = current_line
		current_line = input_file.readline()

		while current_line != "$EndElements\n" :
			# add to list of elems as tuples
			current_line_as_list = current_line.split() # split into words
			del(current_line_as_list[0])

			# store the values as a list of tuples. last 2 values of each line will
			# be the first 2 elements  of the tuple, a list of all the others will
			# be the last elem of the tuple
			last_value = current_line_as_list.pop()
			second_last_value = current_line_as_list.pop()

			self.elems_list.append((second_last_value, last_value, current_line_as_list))

			current_line = input_file.readline()

		input_file.close()


#mesh = MeshData("ref.msh")

#mesh.parse()

#print "No of nodes:" + str(mesh.number_of_nodes)
#print "No of elems:" + str(mesh.number_of_elems)
#print "Nodes:\n"
#print mesh.node_dict
#print "Elems:\n"
#print mesh.elems_list
