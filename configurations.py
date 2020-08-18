import os, argparse, sys

while True:
    try:

        parser = argparse.ArgumentParser(add_help=False, description='Runs Autodock Vina multi-ligand docking!')

        ## Add the arguments:
        parser.add_argument('-c', '--configProteinName',
                            type=str,
                            help="->> python vina_runner.py -c [Configuration File Name Here] <<- "
                                 "Here is the example of a command. "
                                 "You must type correct protein name to run the docking! ")

        ## Optional Arguments:
        parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                            help="In the command line you need to type the name of a protein correctly (after the "
                                 "'python3 vina_runner.py') to let the script start the docking with Autodock Vina. "
                                 "Command line command example ==> "
                                 "python vina_runner.py -c [Configuration File Name Here] -o C:/Program1/TSRI/vina/test/ "
                                 "(-o path can be optional). "
                                 "The written protein name represents the conf_PROTEIN.txt config file which should "
                                 "be located in the same directory as 'vina_runner.py' and it also should be set up "
                                 "properly for docking. Have a happy docking!")

        parser.add_argument('-o', "--output", help="# output_dir path must be written with ending '/' "
                                                   "(ex: C:/Program1/TSRI/vina/test2/ <= last '/' must be presented!). "
                                                   "Output directory path is optional argument, "
                                                   "default path for output directory should be already mentioned "
                                                   "in conf_[PROTEIN].txt file, by user.", action="store", type=str)

        ## Execute the parse_args() method:
        args = parser.parse_args()

        pName = args.configProteinName

        conf_name = pName    ## conf_[PROTEIN__FILE_NAME].txt must be located in the same directory as
                                                ## configuration.py and vina_runner.py
        with open(conf_name) as file_in:
            lines = []
            for line in file_in:
                lines.append(line)

        ## Slicing each line of data:

        ## Directory were all ligands area located for docking:
        ligpath = lines[1][10:].rstrip()
        ## Protein file name:
        receptor = lines[2][11:].rstrip()
        ## Protein file full path:
        freceptor = lines[3][12:].rstrip()
        ## vina.exe directory:
        vina_dir = lines[4][11:].rstrip()

        ## Accepts output directory from command -o [out_dir]:
        if args.output is not None:
            print("\nSetting up output_dir path manually...")
            output_dir = args.output

            ## Checks if the manually created path exists, if not creates one.
            if args.output[1:].startswith(":"):
                output_dir = args.output
            ## If user mentioned just a name of a directory but not the full path the output directory will be created
            ## in the vina.exe directory folder
            elif not args.output[1:].startswith(":"):
                output_dir = lines[4][11:-9].rstrip() + args.output + "/"




        ## If from command line output_dir is not set, it uses default option from config_[PROTEIN].txt file:
        else:
            print("\nUsing default output_dir path from " + "[" + conf_name + "].")
            output_dir = lines[5][13:].rstrip()
        ## Checks if conf_[PROTEIN].txt file exists.
        if os.path.isfile(conf_name) is True:
            print("\nConfig file name is correct!")
        ## Checks if directory already exists, if not creates one:
        if not os.path.isdir(output_dir):
            os.mkdir(output_dir)
        else:
            output_dir = output_dir

        ## Autodock Vina's configuration details that user have set-up in conf_[PROTEIN].txt file:
        strcenter_x = lines[6][14:].rstrip()
        strcenter_y = lines[7][14:].rstrip()
        strcenter_z = lines[8][14:].rstrip()
        strsize_x = lines[9][12:].rstrip()
        strsize_y = lines[10][12:].rstrip()
        strsize_z = lines[11][12:].rstrip()
        strcpu = lines[12][9:].rstrip()
        strexhaustiveness = lines[13][20:].rstrip()
        strnum_modes = lines[14][15:].rstrip()

        ## Breaks out of while loop if try-ing if the script was working
        break

    except FileNotFoundError:
        print("\nWrong protein name! Script cannot find the config file! type -> python vina_runner.py --help")
        ## Breaks out of while loop if script was crashed for 'FileNotFoundError'
        break
