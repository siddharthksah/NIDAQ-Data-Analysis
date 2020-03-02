csv_file  = (
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/200128_whisker with heavy tip_vortex gun in water/1cm whisker_sweep_50psi_1k_sampling_along contact pad.csv")

txt_file = (
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/200128_whisker with heavy tip_vortex gun in water/1cm whisker_sweep_50psi_1k_sampling_along contact pad.txt")

import csv
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()

with open(txt_file, 'r') as fin:
    data = fin.read().splitlines(True)
with open(txt_file, 'w') as fout:
    fout.writelines(data[5: ])

print('Done')