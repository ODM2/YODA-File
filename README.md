YAML Observation Data Archive & Exchange (YODA) Format
===============

###Getting Started with YODA
YODA is an observational data encoding format using YAML. 
* [Blank YODA Excel Templates](https://github.com/ODM2/YODA-File/tree/master/excel_templates) - Get the blank templates and get started.
* [Example Excel Templates and YODA files](https://github.com/ODM2/YODA-File/tree/master/examples) - View examples that have been populated with data.

###Goals
Our goal for **YODA Files** is to substantially extend the original CZO Display File specification to accommodate the full diversity of critical zone science data -- such as hydrological time series, soil profile geochemistry, biodiversity transects, etc. -- that can be organized with the [Observations Data Model v2 (ODM2)](https://github.com/UCHIC/ODM2).  In addition, the YODA File will meet the following requirements:
* **Easy for humans to read and write**. Anyone opening the file in a text editor or spreadsheet application should be able to quickly and intuitively understand the file contents and how to use the data.
* **Easy for machines to parse and generate**.  The file should be very easy to parse and validate with the wide variety of software tools used by scientists.
* **Conform to the metadata requirements of an [ODM2](https://github.com/UCHIC/ODM2) [Dataset](https://github.com/UCHIC/ODM2/blob/master/doc/ODM2Docs/core_datasets.md)**, and yet have the flexibility to utilize a variety of controlled vocabularies.
* **Serve as a self-describing archival file format** that is readily accepted by earth and environmental science data repositories, such as [IEDA EarthChem](http://www.earthchem.org/library) or [Knowledge Network for Biocomplexity (KNB)](https://knb.ecoinformatics.org/)

In addition, we aim to develop a number of tools to assist with the creation and parsing of YODA Files.

###Design
A YODA File will follow the data serialization and interchange format of [YAML](http://en.wikipedia.org/wiki/YAML) ("YAML Ain't Markup Language"), a superset of [JSON](http://www.json.org/) (JavaScript Object Notation) which can be readily parsed by any modern computer language. In addition, by YODA File convention, most data will be contained within a comma-separated data array table that can be easily parsed by a spreadsheet application into data columns.

A YODA File will be structurally validated against required and optional ODM2 fields and controlled vocabularies using [JSON Schema](http://json-schema.org/), which provides a means for documenting the YODA File Schema and set of software tools for validating any JSON file against our schema. 

###History
The original [CZO Display File](http://criticalzone.org/national/publications/pub/whitenack-et-al-2011-czo-display-file-specification/) format was developed in 2010-2011 as a means for [US Critical Zone Observatories](http://criticalzone.org/) to share data in a form that was both human readable and machine parsable. The header provides structured metadata that allows the comma-separated data to be ingested into an [Observations Data Model 1.1 (ODM1.1)](http://his.cuahsi.org/odmdatabases.html) database, such as a [CUAHSI HydroServer](http://his.cuahsi.org/hydroserver.html).

###Contribute
There are many ways to contribute:
* Help us develop the YODA File specification document.
* Help us develop the JSON-schema validation tools.
* Help us develop examples of valid YODA Files.
* Help us develop tools for generating valid YODA Files, such as:
  * MS Excel templates that contain some auto-validation features.
  * Python/R/Matlab scripts.

### Credits

This work was supported by National Science Foundation Grants [EAR-1224638](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1224638), [EAR-1332257](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1332257), and [ACI-1339834](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1339834). Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.
