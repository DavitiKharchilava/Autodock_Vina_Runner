import os, subprocess, configurations, argparse, sys
from texttable import Texttable

while True:
    try:
        # CALLING VINA

        lignames = []
        for file in os.listdir(configurations.ligpath):
            if file.endswith(".pdbqt"):
                lignames.append(file)

        for i in range(len(lignames)):
            fligand = str('"' + configurations.ligpath + "\\" + lignames[i] + '"')

            # print_path = ''
            # for i in range(len(configurations.output_dir)):
            #     if configurations.output_dir[i] == "\\" and configurations.output_dir[i+1] == "\\":
            #         print_path = configurations.output_dir[:i] \
            #                      + configurations.output_dir[i] \
            #                      + configurations.output_dir[i+1:0]

            print("\nNow will be docked ligand "
                  + lignames[i][:-6] + " to a protein "
                  + configurations.receptor[:-6]
                  + ". Output directory for docking will be -->> " + configurations.output_dir)

            subprocess.call(
                configurations.vina_dir + " --receptor " + configurations.freceptor + " --ligand " + fligand \
                + " --center_x " + configurations.strcenter_x \
                + " --center_y " + configurations.strcenter_y \
                + " --center_z " + configurations.strcenter_z \
                + " --size_x " + configurations.strsize_x \
                + " --size_y " + configurations.strsize_y \
                + " --size_z " + configurations.strsize_z \
                + " --cpu " + configurations.strcpu \
                + " --exhaustiveness " + configurations.strexhaustiveness \
                + " --num_modes " + configurations.strnum_modes \
                + " --out " + configurations.output_dir + lignames[i][:-6] + "_" + configurations.receptor[:-6]
                + "_" + "out" + ".pdbqt")
            i += 1

            path_lig, dirs_lig, files_lig = next(os.walk(configurations.ligpath))
            file_count_lig = str(len(files_lig))
            print("\n" + "The number of ligand(s) in the ligand(s)' directory: " + file_count_lig)

            path_out, dirs_out, files_out = next(os.walk(configurations.output_dir))
            file_count_out = str(len(files_out))
            print("The number of successfully docked ligands: " + file_count_out)

            """_________________________________________________________"""
            """For sorting Autodock Vina outputs"""

            print("\n\nSorted docking output with binding energies from highest to low:")
            try:
                # from texttable import Texttable

                # macromolecule = input("Please enter the name of a protein: ").lower()

                # output_path = "C:/Program1/TSRI/vina/test2"  # + macromolecule

                """ If you choose to save the output in .txt file [all data.txt] too, the comments "#" need to be removed in lines where 
                the text_file is mentioned """

                # text_file = open(output_path + "/all data.txt", mode="a")

                list_pdbqt = []

                for filename in os.listdir(configurations.output_dir):
                    if filename.endswith(".pdbqt"):  # "out" should be deleted if we sort with filenames
                        pdbqt_file = open(configurations.output_dir + "/" + filename, mode="r")
                        pdbqt_file.readline()
                        new_content = pdbqt_file.readline()
                        list_pdbqt.append((filename, new_content))
                    else:
                        print("sorting was not successful, ")

                list_pdbqt = sorted(list_pdbqt, key=lambda f: float(f[1].split()[3]))
                # filename: filename -for sorting with names
                # f: float(f[1].split()[3]) -for sorting with energy

                t = Texttable()

                for (filename, new_content) in list_pdbqt:
                    # text_file.write(filename)

                    # x = PrettyTable()
                    # x.field_names = ["Docked Ligand Output Name", "Binding Energy", "Output Directory Path"]
                    # x.add_row([filename, new_content.split()[3], configurations.output_dir])
                    # print(x)

                    # text_file.write("\n")
                    # text_file.write(new_content)
                    # text_file.write("\n")
                    t.add_rows([['Output file name', 'The strongest binding energy', 'Output Directory Path'],
                                [filename, new_content.split()[3], configurations.output_dir]])

                    # text_file.flush()
                print(t.draw())
            except:
                list_pdbqt = []

                for filename in os.listdir(configurations.output_dir):
                    if filename.endswith(".pdbqt"):  # "out" should be deleted if we sort with filenames
                        pdbqt_file = open(configurations.output_dir + "/" + filename, mode="r")
                        pdbqt_file.readline()
                        new_content = pdbqt_file.readline()
                        list_pdbqt.append((filename, new_content))
                    else:
                        print("sorting was not successful, ")

                list_pdbqt = sorted(list_pdbqt, key=lambda f: float(f[1].split()[3]))
                print("Something went wrong while sorting output files ! Introducing alternative sorted output:\n")
                print("\nOutput file name || The strongest binding energy || Output Directory Path")
                for (filename, new_content) in list_pdbqt:
                    print("\n" + filename + " || " + new_content.split()[3] + " || " + configurations.output_dir + "\n")
                """_________________________________________________________"""

        break
    except:
        print("\n\n'vinna_runner.py' stopped working!\n")
        break