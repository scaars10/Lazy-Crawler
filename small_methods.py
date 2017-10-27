import os

# directory_manage checks if a directory exists or not if not then it creates it itself


def directory_manage(relative_location):

	base_path = os.path.dirname(os.path.realpath(__file__))

	if not os.path.exists(os.path.join(base_path, relative_location)):
		os.makedirs(os.path.join(base_path, relative_location))


