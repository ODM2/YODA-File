YAML Observation Data Archive & Exchange (YODA) Format
===============

### Getting Started with YODA
YODA is an observational data encoding format using YAML.

* [Blank YODA Excel Templates](https://github.com/ODM2/YODA-File/tree/master/excel_templates) - Get blank templates and get started. The [Time Series template](https://github.com/ODM2/YODA-File/tree/master/excel_templates/time_series) is ready to use.
* [Example Excel Templates and YODA files](https://github.com/ODM2/YODA-File/tree/master/examples) - View examples that have been populated with data.
* [YODA Documentation](https://github.com/ODM2/YODA-File/tree/master/doc) - Read the YODA File Specification and other documentation.

### Goals
We developed the **YAML Observation Data Archive & Exchange (YODA) File Format** to serve as a specification for human-readable, machine-parseable, text-based data files that accommodate the full diversity of critical zone science data -- such as hydrological time series, soil profile geochemistry, biodiversity transects, etc. -- that can be organized with the [Observations Data Model v2 (ODM2)](https://github.com/ODM2/ODM2)  Specifically, we designed the YODA File format to meet the following requirements:

* **Easy for humans to read and use**. Anyone opening the file in a text editor or spreadsheet application should be able to intuitively understand the contents of the file's structured metadata header and comma-separated data table.
* **Easy for machines to parse and generate**.  The file should be very easy to parse and validate with the wide variety of software tools used by scientists.
* **Group results into a single data array** similar to how scientists most commonly view their data, but also conforming to the metadata requirements of an [ODM2](https://github.com/ODM2/ODM2) [Dataset](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/core_datasets.md).
* **Serve as a self-describing archival file format** that is readily accepted by earth and environmental science data repositories, such as [IEDA EarthChem Library](http://www.earthchem.org/library) or [Knowledge Network for Biocomplexity (KNB)](https://knb.ecoinformatics.org/)

### Design Vision
A YODA File follows the data serialization and interchange format of [YAML](http://en.wikipedia.org/wiki/YAML) ("YAML Ain't Markup Language"), a superset of [JSON](http://www.json.org/) (JavaScript Object Notation). YAML can be readily [parsed by any modern computer language](http://yaml.org/).

The key feature of a YODA file that distiguishes it from generic YAML is that a YODA file:
1. Organizes data into a comma-separated data array (e.g. a data table or DataFrame) with multiple columns and rows, and 
2. Provides all the metadata of an [ODM2](https://github.com/ODM2/ODM2) [Dataset](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/core_datasets.md) so that the data array can be parsed by software into an [ODM2](https://github.com/ODM2/ODM2) database instance.

[YODA Profiles](https://github.com/ODM2/YODA-File/blob/master/doc/YODA_profiles.md#yoda-profiles) have been developed for common dataset types to define expectations for the data array block and to facilitate data/metadata input forms/templates for the end-user.

A YODA File will be structurally validated against required and optional ODM2 fields and controlled vocabularies using [JSON Schema](http://json-schema.org/), which provides a means for documenting the YODA File Schema and set of software tools for validating any JSON file against our schema. This **work in progress** can be found in the [YODA-Tools repository](https://github.com/ODM2/YODA-Tools).

We are also developing the [YODA Tools](https://github.com/ODM2/YodaTools) library, which is built upon the [ODM2PythonAPI](https://github.com/ODM2/ODM2PythonAPI) to create YODA files from our [YODA Excel Templates](https://github.com/ODM2/YODA-File/tree/master/excel_templates) or from an ODM2 database and to import YODA Files into an ODM2 database. YODA Files will thus serve as an interchange format between components of the [ODM2 Software Ecosystem](http://www.odm2.org/).

### Specification
The [draft YODA File Specification](https://github.com/ODM2/YODA-File/blob/master/doc/YODAFile_Specification_Draft0.md) and [other YODA File documentation](https://github.com/ODM2/YODA-File/tree/master/doc) provide many design and implementation details, but are presently a *work in progress*.

### History
The YODA file format developed out of the effort to substantially extend the CZO Display File specfication. The original [CZO Display File](http://criticalzone.org/national/publications/pub/whitenack-et-al-2011-czo-display-file-specification/) format was developed in 2010-2011 as a means for [US Critical Zone Observatories](http://criticalzone.org/) to share data in a form that was both human readable and machine parsable. The header provides structured metadata that allows the comma-separated data to be ingested into an [Observations Data Model 1.1 (ODM1.1)](http://his.cuahsi.org/odmdatabases.html) database, such as a [CUAHSI HydroServer](http://his.cuahsi.org/hydroserver.html).

### Contribute
There are many ways to contribute:
* Help us develop the YODA File specification document.
* Help us develop the JSON-schema validation tools.
* Help us develop examples of valid YODA Files.
* Help us develop tools for generating valid YODA Files, such as:
  * MS Excel templates that contain some auto-validation features.
  * Python/R/Matlab scripts.

### Credits

This work was supported by National Science Foundation Grants [EAR-1224638](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1224638), [EAR-1332257](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1332257), and [ACI-1339834](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1339834). Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.
