# Python-Database-OBS-RFID
Brief implementation on how to build a system of nested functions in Python for data analysis on OBS and RFID Dataset
The data set contains observational and wearable sensors data collected in a group of 20 Guinea baboons living in an enclosure of a Primate Center in France, between June 13th 2019 and July 10th 2019. These data were analyzed and published in the paper V. Gelardi, J. Godard, D. Paleressompoulle, N. Claidière, A. Barrat, “Measuring social networks in primates: wearable sensors vs. direct observations”, Proc. R. Soc. A 476:20190737 (2020).
## OBS DATA
The file OBS_data.txt contains all the behavioral events registered by an observer, with 7 columns:
– DateTime = Time stamp of the event, namely the moment the observed behavior was registered. In case of STATE events (events with duration > 0), it refers to the beginning of the behavior;
– Actor = The name of the actor;
– Recipient = The name of the individual the Actor is acting upon;
– Behavior = The behavior the Actor. 14 types of behaviors are registered:’Resting’, ‘Grooming’, ‘Presenting’,’Playing with’, ‘Grunting-Lipsmacking’, ‘Supplanting’,’Threatening’, ‘Submission’, ‘Touching’, ‘Avoiding’, ‘Attacking’,’Carrying’, ‘Embracing’, ‘Mounting’, ‘Copulating’, ‘Chasing’. In addition two other categories were included: ‘Invisible’ and ‘Other’;
– Category = The classification of the behavior. It can be ‘Affiliative’, ‘Agonistic’, ‘Other’;
– Duration = Duration of the observed behavior. POINT events have no duration;
– Point = indicates if the event is a POINT event (YES) or a STATE event (NO).
## SENSOR DATA
The file RFID_data.txt contains contacts data recorded in the same period by the SocioPatterns infrastructure. The proximity sensors were worn by 13 of the 20 individuals cited above.
The data file consists of 4 columns:
– t = time of the beginning of the contact in Epoch format (Unix timestamps);
– i = Name of the first individual;
– j = Name of the second individual;
– DateTime
