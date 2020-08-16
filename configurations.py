import os, argparse, sys

while True:
    try:

        parser = argparse.ArgumentParser(add_help=False, description='Runs Autodock Vina multi-ligand docking!')

        # Add the arguments
        parser.add_argument("inputProteinName",
                            type=str,
                            help="->> python3 vina_runner.py [Protein Name Here] <<- "
                                 "Here is the example of a command. "
                                 "You must type correct protein name to run the docking! ")

        parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                            help="In the command line you need to type the name of a protein correctly (after the "
                                 "'python3 vina_runner.py ') to let the script start the docking with Autodock Vina. "
                                 "The written protein name represents the conf_PROTEIN.txt config file which should "
                                 "be located in the same directory as 'vina_runner.py' and it also should be set up "
                                 "properly for docking. Have a happy docking!")
        # parser.add_argument('-o', action="store", type=str)

        # Execute the parse_args() method
        args = parser.parse_args()

        pName = args.inputProteinName

        conf_name = "conf_" + pName + ".txt"    # conf_[PROTEIN_NAME].txt should be located in the same directory as
                                                # configuration.py and vina_runner.py
        with open(conf_name) as file_in:
            lines = []
            for line in file_in:
                lines.append(line)

        # ligdir = lines[0][9:-1]
        ligpath = lines[1][10:].rstrip()
        receptor = lines[2][11:].rstrip()
        freceptor = lines[3][12:].rstrip()
        vina_dir = r"C:\Program1\TSRI\Vina\vina.exe"  # edit this line if vina.exe installation directory needs to be changed
        output_dir = lines[5][13:-1].rstrip()
        # output_dir = str(args)[38:-2]
        # if output_dir == '':
        #     output_dir = lines[5][13:-1].rstrip()


        strcenter_x = lines[6][14:].rstrip()
        strcenter_y = lines[7][14:].rstrip()
        strcenter_z = lines[8][14:].rstrip()
        strsize_x = lines[9][12:].rstrip()
        strsize_y = lines[10][12:].rstrip()
        strsize_z = lines[11][12:].rstrip()
        strcpu = lines[12][9:].rstrip()
        strexhaustiveness = lines[13][20:].rstrip()
        strnum_modes = lines[14][15:].rstrip()

        conf_path = lines[15][12:].rstrip() + conf_name

        # conf_path = "X:/Documents/Python/TurboVina-master/vina_runner/" + conf_name
        conf_file = open(conf_path)

        if os.path.isfile(conf_path) is True:
            print("Config file name is correct!")
        else:
            print('Wrong protein name!')
    #
    #     # ligdir = "C:\\Program1\\TSRI\\Vina\\Ligands\\ligs"  # should be changed for ligands directory
    #     # ligpath = "C:\\Program1\\TSRI\\Vina\\Ligands\\ligs"  # should be changed for ligands directory
    #     # receptor = "6m71.pdbqt"  # receptor file name
    #     # freceptor = str("C:\\Program1\\TSRI\\Vina\\" + receptor)  # contains receptor location + receptor file name
    #     # vina_dir = r"C:\Program1\TSRI\Vina\vina.exe"  # if the vina.exe installed directory needs to be changed, change only r'YOUR_DIRECTORY'.
    #     # output = "C:\\Program1\\TSRI\\Vina\\test2\\"  # defines docking output directory
    #     #
    #     # # Autodock Vina docking parameters:
    #     # strcenter_x = str(146)
    #     # strcenter_y = str(124)
    #     # strcenter_z = str(91)
    #     # strsize_x = str(17)
    #     # strsize_y = str(13)
    #     # strsize_z = str(13)
    #     # strcpu = str(4)
    #     # strexhaustiveness = str(8)
    #     # strnum_modes = str(9)
        break
    except FileNotFoundError:
        print("\nWrong protein name! Script cannot find the config file! type -> python3 vina_runner.py --help")
        break
