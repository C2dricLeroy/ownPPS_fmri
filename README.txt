Ownership_scr_PT1.py : Main task, trigger after instructions, 1 pause at the middle 

Ownership_treinos.py : Training session 


note : instructions are in portuguese


_______________________ For the Main task ___________________________________

1_ Dialog box

- Code of the participant
- Counterbalancing of keys (indicate the Key corresponding to the "reachable" response - the other will correspond to "non reachable")
- Color choosen for ownership 
- Individual boundary of the peripersonnal space (previously computed)


The task can take a few seconds to launch


------------------------------------------------------------------
2.fMRI trigger

Trigger need to be called at the beggining of the screen displaying instructions.
Please make sure that the dialog box is closed before calling the trigger.

Before running, change the "COM" number in file depending on the plugged device.
If no device connected, press "s" to simulate trigger.




____________________________Experiment design_______________________________________


- 4 blocks of 60 trials : 2 Spaces (PPS-EPS) * 2 Ownership (Self-Other) * 12 repetitions (3 distances * 6 repetitions) + 12 fillers (6 BOUNDARY space + 6 responses)

- In sum : 4 measures groups (2 space * 2 ownership) & 240 trials (192 test, 48 fillers) ; 

- In each block, 12 measure per measure group; 48 measure per measure group overall


- Fast-event related design

- Pseudo-random jitter computed with OptSeq for mask

- Duration : 27 min

-------------------------------------------------------------------

Response keys


- For now, A & B keys are used to answer. They can be modified to fit the device but answers need to be done only with the !! LEFT HAND !!