while True:
    try:
        import os, subprocess, configurations, argparse, sys

        # texttable package should be installed for better looking output results:
        from texttable import Texttable

        ## Looping through the names of a ligands located to the ligands directory and saving them in a list 'lignames':
        lignames = []
        for file in os.listdir(configurations.ligpath):
            if file.endswith(".pdbqt"):
                lignames.append(file)

        ## Looping through each 'lignames' list member and preparing command for Autodock Vina docking:
        for i in range(len(lignames)):
            fligand = str('"' + configurations.ligpath + "\\" + lignames[i] + '"')

            ## Telling the names of a ligand and a protein which are going to be docked, output directory is mentioned too:
            print("\nNow will be docked ligand "
                  + "[" + lignames[i][:-6] + "]" + " to a protein "
                  + "[" + configurations.receptor[:-6] + "]"
                  + ". \nOutput directory for docking will be -->> " + configurations.output_dir)

            ## CALLING VINA AND ADDING ALL THE CONFIGURATIONS:
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

            ## Telling how many ligands are located in ligand(s)' directory:
            path_lig, dirs_lig, files_lig = next(os.walk(configurations.ligpath))
            file_count_lig = str(len(files_lig))
            print("\n" + "The number of ligand(s) in the ligand(s)' directory: " + file_count_lig)

            ## Telling how many dockings were successfully completed:
            path_out, dirs_out, files_out = next(os.walk(configurations.output_dir))
            file_count_out = str(len(files_out))
            print("The number of successfully docked ligands: " + file_count_out)

            """_________________________________________________________"""
            """For sorting Autodock Vina outputs"""

            print("\n\nSorted docking output with binding energies from highest to low:")
            while True:
                try:
                    ## If you choose to save the output in .txt file [all data.txt] too, the comments "#" need to be
                    ## removed in lines where the text_file is mentioned

                    # text_file = open(output_path + "/all data.txt", mode="a")

                    list_pdbqt = []
                    ## Gathers all the data in the 'list_pdbat', that is interesting for us, from all files that are
                    ## located in directory and ends with 'out.pdbqt'
                    for filename in os.listdir(configurations.output_dir):
                        if filename.endswith("out.pdbqt"):  # "out" should be deleted if we sort with filenames
                            pdbqt_file = open(configurations.output_dir + "/" + filename, mode="r")
                            pdbqt_file.readline()
                            new_content = pdbqt_file.readline()
                            list_pdbqt.append((filename, new_content))
                        else:
                            print("sorting was not successful, ")


                    ## Gathers the strongest binding energies from each output file and sorts them with that value.

                    list_pdbqt = sorted(list_pdbqt, key=lambda f: float(f[1].split()[3]))
                    ## filename: filename <- for sorting with names
                    ## f: float(f[1].split()[3]) <- for sorting with energy

                    t = Texttable()

                    for (filename, new_content) in list_pdbqt:
                        # text_file.write(filename)
                        # text_file.write("\n")
                        # text_file.write(new_content)
                        # text_file.write("\n")
                        # text_file.flush()

                        ## If you choose to see the output without texttable package:
                        # print(filename, "||", new_content.split()[3], "||", configurations.output_dir, "\n")

                        ## Reviewing sorted output with 'texttable' package:
                        t.add_rows([['Output file name', 'The strongest binding energy', 'Output Directory Path'],
                                    [filename, new_content.split()[3], configurations.output_dir]])

                    ## Printing output texttable:
                    print(t.draw())
                    break
                except:
                    print("'texttable' package is not installed properly. Sorting alternatively!")

                    ## Code is almost same as it was for 'texttable' option, but outputs the result in less pretty way...
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

                    for (filename, new_content) in list_pdbqt:
                        print(filename, "||", new_content.split()[3], "||", configurations.output_dir, "\n")
                    break
            """_________________________________________________________"""

        break
    except:
        ## In case 'vina_runner.py' crashes:
        print("\n\n'vinna_runner.py' stopped working!"
              "\ntype -> python vina_runner.py --help")
        break
