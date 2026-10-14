# 5-LOX Salt-Bridge Locations

Interactive visualization of salt-bridge locations identified from the molecular dynamics simulations of human 5-lipoxygenase.

## Interactive 3D viewer

👉 **[Open the interactive 5-LOX salt-bridge viewer](https://najla23.github.io/Molecular-dynamics-simulations-of-human-5-lipoxygenase/)**

The viewer allows interactive rotation, zooming, inspection of individual residue pairs, and visualization of the different salt-bridge comparison scenes.

### Condition labels

- **WT** = ATP-free system
- **CRYO** = original cryo-EM PDB structure with ATP bound (**ATP+**)
- **ATP** = system in which ATP was initially placed outside the protein (**ATP+out**)



### Really important note

Salt bridges in this viewer are shown only to map the relevant residue pairs onto a single static 5-LOX structure. The quantitative results reported in the manuscript were obtained from the dynamic MD trajectories, not from this static structure.

Therefore, distances visible here do not represent the distances sampled during the simulations and should not be interpreted as measures of salt-bridge occupancy, persistence, or interaction strength.



The PyMOL session is also available in this directory:

`5LOX_salt_bridge_locations.pse`
