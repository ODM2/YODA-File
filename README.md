CZO Display File v2 Specification
===============

###History
The [CZO Display File v1](http://criticalzone.org/national/publications/pub/whitenack-et-al-2011-czo-display-file-specification/) format was developed in 2010-2011 as a means for [US Critical Zone Observatories](http://criticalzone.org/) to share data in a form that was both human readable and machine parsable. The header provides metadata that allows the comma-separated data to be ingested into an [Observations Data Model 1.1 (ODM1.1)](http://his.cuahsi.org/odmdatabases.html) database, such as a [CUAHSI Hydroserver](http://his.cuahsi.org/hydroserver.html).

###Goals
Our goal for **CZO Display File v2** is to substantially extend the CZO Display File specification to accomodate the full diversity of critical zone science data -- such as hydrological time series, soil profile geochemistry, biodiversity transects, etc. -- that can be organized with the [Observations Data Model v2 (ODM2)](https://github.com/UCHIC/ODM2).  In addition, the CZO Display File v2 will meet the following requirements:
* *Easy for humans to read and write**. Anyone opening the file in a text editor or spreadsheet applicaiton should be able to quickly and intuitively understand the file contents and how to use the data.
* **Easy for machines to parse and generate**.  The file should be very easy to parse and validate with the wide variety of software tools used by scientists.
* **Conform to the metadata requirements of an [ODM2](https://github.com/UCHIC/ODM2) [Dataset](https://github.com/UCHIC/ODM2/blob/master/doc/ODM2Docs/core_datasets.md)**, and yet have the flexibility to utilize a variety of controlled vocabularies.
* **Serve as a self-describing archival file format** that is readily accepted by earth and environmental science data respositories, such as [IEDA EarthChem](http://www.earthchem.org/library) or [Knowledge Network for Biocomplexity (KNB)](https://knb.ecoinformatics.org/)

In addition, we aim to develop a number of tools to assist with the creation and parsing of CZO Display Files.

###Design
A CZO Display File v2 will follow the syntax of either [JSON](http://www.json.org/) (JavaScript Object Notation) or [YAML](http://en.wikipedia.org/wiki/YAML) ("YAML Ain't Markup Language"), which are lightweight data-interchange formats that can be readily parsed by any modern computer language.  In addition, by CZO Display File v2 convention, most data will be contained within a comma-separated data array block that can be easily parsed by a spreadsheet application into data columns.

A CZO Display File v2 will be structurally validated against required and optional ODM2 fields and controlled vocabularies using [JSON Schema](http://json-schema.org/), which provides a means for documenting the CZO Display File v2 Schema and set of software tools for validating any JSON file against our schema. 

###Contribute
There are many ways to contribute:
* Help us develop the CZO Display File v2 specification document.
* Help us develop the json-schema validation tools.
* Help us develop examples of valid CZO Display Files (v2).
* Help us develop tools for generating valid CZO Display Files (v2), such as:
  * MS Excel templates that contain some auto-validation features.
  * Python/R/Matlab scripts.

