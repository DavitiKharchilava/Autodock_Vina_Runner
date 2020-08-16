#AutoDock Vina docker

\
####Runs Autodock Vina multi-ligand docking!

In the command line you need to type the name of a protein correctly (after the 'python3 vina_runner.py ') \
to let the script start the docking with Autodock Vina. \
The written protein name represents the conf_PROTEIN.txt config file which should be located \
in the same directory as 'vina_runner.py' and it also should be set up properly for docking. \
Have a happy docking!

\
####USER MANUAL:
- Both ligands and proteins must be prepared for docking and converted in .pdbqt format.
- For each protein docking new conf_PROTEIN.txt configuration file must be created.
- There must not be deleted or modified any variable's name above.
- After each "=" 1 blank space must be made(" "), as it is done for "vina_dir" variable.
- for the receptor there needs to be written receptor file name (NAME.pdbqt).
- "vina_dir" can be changed only from configuration.py file.
- All the directories can be written with single "\".
- After configuring this config file, it must be renamed after a protein name (conf_PROTEIN.txt)
for which this config is created.
It should be located in the same directory as "vina_docker.py".
- If the docking is re-running with same ligand and protein, but there is changed only grid box parameters,
be aware that in the
output directory older version of output file will be replaced with the newer one,
or change the next output directory to avoid such result.