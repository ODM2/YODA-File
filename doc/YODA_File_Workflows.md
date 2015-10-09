The YODA File Work Flows
========================
**Case 1: Create YODA File for New Dataset**
User creates a new YODA file for a Dataset for the first time using one of the Excel Templates.

1. User downloads the blank Excel template file
2. User types or copies and pastes metadata into the template
3. User copies and pastes data values into the template
4. User types UUIDs into the template OR uses the code in the template to generate them for the first time
5. User generates the YODA file using the template

**Case 2: Add New or Additional Data to a Dataset for which a YODA File Already Exists**
User wants to add additional data to the same Dataset or Result for which an existing YODA file has been created.  The same same UUIDs will be used for SamplingFeatures, Results, and Dataset. User creates a new YODA template file by copying an existing YODA template file. Most of the metadata can stay the same, but the data **MUST** be different.

1. User copies the existing YODA Excel Template to a new file
2. User deletes the data from the DataValues tab
3. User pastes new data into the DataValues tab
4. User generates the YODA file using the template 

**Case 3: Create New Version of an Existing YODA File**
User wants to create a new version of an existing YODA file. In this case there is likely a problem with the data stored in the existing file or the metadata description is wrong, needs to be updated, or is incomplete.

1. User creates a new YODA file by copying an existing YODA template file. 
2. User modifies the metadata description 
3. User modifies the data content of the file

Rules for YODA Files
====================
Based on the above workflows, the following rules emerge for YODA files:

1. Loading the data contents of a YODA file to an ODM2 database is atomic - it should be all or nothing (all of the data values load or none of them load)
2. No two YODA files should contain the same data values. Versioning may be an exception.  However, the idea is that new files for the same Dataset/Result would pick up where another YODA file leaves off.  New data would not be appended to an existing YODA file. Instead an entirely new file would be created that contains the next "chunk" of data.

What to do When Loading A YODA File into ODM2
=============================================
When loading a YODA file to an ODM2 database, we will have to do the following:

Case 1 and 2 above:

1. Check to see if the SamplingFeature already exists (by UUID) - if not, load
2. Check to see if the Result already exists (by UUID) - if not, load
3. Check to see if the Dataset already exists (by UUID) - if not, load
4. Check to see if the Method already exists (by unique columns) - if not, load

Case 3 above:

1.  Do we delete the existing Dataset from the ODM2 database and add the new version, or leave the old version and create a new version of the existing dataset in the database????


