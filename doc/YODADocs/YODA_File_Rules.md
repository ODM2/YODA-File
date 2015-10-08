Rules for YODA Files
====================
1. Loading the data contents of a YODA file to an ODM2 database is atomic - its all or nothing (all of the data values load or none of them load)
2. No two YODA files should contain the same data values (versioning may be an exception)

What to do When Loading A YODA File into ODM2
=============================================
When loading a YODA file to an ODM2 database, we will have to do the following:

1. Check to see if the SamplingFeature already exists (by UUID) - if not, load
2. Check to see if the Result already exists (by UUID) - if not, load
3. Check to see if the Dataset already exists (by UUID) - if not, load
4. Check to see if the Method already exists (by unique columns) - if not, load


The YODA File Work Flows
========================
1. User creates a new YODA file for a Dataset for the first time using the Excel Template
	a. User downloads the blank Excel template file
    b. User types or copies and pastes metadata into the template
	c. User copies and pastes data values into the template
	d. User types UUIDs into the template OR uses the code in the template to generate them for the first time
	e. User generates the YODA file using the template 
2. User wants to add additional data to the same Dataset or Result for which an existing YODA file has been created.  The same same UUIDs will be used for SamplingFeatures, Results, and Dataset.
	a. User creates a new YODA file by copying an existing YODA template file. Most of the metadata can stay the same, but the data MUST be different.
        i. User copies the existing YODA Excel Template to a new file
        ii. User deletes the data from the DataValues tab
        iii. User pastes new data into the DataValues tab
        iv. User generates the YODA file using the template 
3. User wants to create a new version of an existing YODA file. In this case there is likely a problem with the data stored in the existing file or the metadata discription is wrong, needs to be updated, or is incomplete.
    a. User creates a new YODA file by copying an existing YODA template file. 
    b. User modifies the metadata description 
    c. User modifies the data content of the file
4.  

**NOTE: No two YODA files should contain the same data values.**

3.  User wants to create a new version of an existing YODA file

