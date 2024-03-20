# HELPER FUNCTIONS
# Use these functions to quickly get your inputs from your input file,
# and write your outputs to an output file.

# The name of your input file.
file_input_name = "input.txt"
# The name of your output file.
file_output_name = "output.txt"

IGNORE_ME_file_input = open(file_input_name, 'r')
IGNORE_ME_file_output = open(file_output_name, 'w')
IGNORE_ME_file_output_storage = []

# Get the next line from your input file.
# You may optionally pass a string argument for debug print statements. This parameter can be skipped.
# Example:
# cases = input()
# length = input("Length of the box")
def input(ignored=None):
    if ignored != None:
        print("Reading {}".format(ignored))
    return IGNORE_ME_file_input.readline().strip()

# Write a string to your output file.
# You must pass a string argument to be written to the file.
# Example:
# output("Case #{}: {}".format(case, result))
def output(output):
    print("Writing line: {}".format(output))
    IGNORE_ME_file_output_storage.append(output + "\n")

# Saves your output file and makes it ready for submission.
# You must put this at the end of your code.
# Do not pass any arguments.
def submit():
    IGNORE_ME_file_output_storage[-1] = IGNORE_ME_file_output_storage[-1].strip()
    IGNORE_ME_file_output.writelines(IGNORE_ME_file_output_storage)
    IGNORE_ME_file_output.close()
    print("Saved and finished! Send your output file called {}".format(file_output_name))