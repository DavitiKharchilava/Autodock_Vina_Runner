#AutoDock Vina docker


####Runs Autodock Vina multi-ligand docking!

In the command line you need to type the name of a protein correctly (after the 'python3 vina_runner.py ') \
to let the script start the docking with Autodock Vina. \
The written protein name represents the conf_PROTEIN.txt config file which should be located \
in the same directory as 'vina_runner.py' and it also should be set up properly for docking. \
Output directory path is an optional argument, default path for output directory should be already mentioned in conf_[PROTEIN].txt file, by user. \


####USER MANUAL:

USER MANUAL:

ligpath => Directory of a ligands which are going to be docked to a protein

receptor => File name of a protein macromolecule (PROTEIN.pdbqt)

freceptor => Full directory path for protein file

vina_dir = r"C:\Program1\TSRI\Vina\vina.exe" => Autodock Vina installed directory

output_dir => Docking output directory by default (can be changed manually from command line)

\
Autodock Vina docking grid box parameters:
                
strcenter_x 

strcenter_y 

strcenter_z 

strsize_x   

strsize_y   

strsize_z   

\
strcpu => Number of CPUs used for docking process (by default it's 8)

strexhaustiveness => Level of being more accurate (by default it's 8)

strnum_modes => Number of Autodock Vina runs (by default it's 9)

\
- Both ligands and proteins must be prepared for docking and converted in .pdbqt format.
- For each protein docking new conf_PROTEIN.txt configuration file must be created.
- There must not be deleted or modified any variables' names above.
- After each "=" 1 blank space must be made(" "), as it is done for "vina_dir" variable.
- "vina_dir" can be changed only from configuration.py file.
- for the receptor there needs to be written receptor file name (NAME.pdbqt).
- All the directories can be written with single "\".
- After configuring this config file, it must be renamed after a protein name (conf_PROTEIN.txt)
for which this config is created. It should be located in the same directory as "vina_docker.py".
- If the docking is re-running with same ligand and protein, but there is changed only grid box parameters,
be aware that in the output directory older version of output file will be replaced with the newer one,
or change the next output directory to avoid such result.
- script will use output_dir line as a default docking output directory, from the command line this directory can be 
changed manually. Either way if the output_dir does not exists there will be created one.

Have a happy docking!
