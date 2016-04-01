YAML Observation Data Archive & Exchange (YODA) Format Specification
=======
Draft v0.1 (work in progress)

# Introduction

## Goals

We developed the **YAML Observation Data Archive & Exchange (YODA) File Format** to serve as a specification for human-readable, machine-parseable, text-based data files that accommodate the full diversity of critical zone science data -- such as hydrological time series, soil profile geochemistry, biodiversity transects, etc. -- that can be organized with the [Observations Data Model v2 (ODM2)](https://github.com/ODM2/ODM2). 

Specifically, we designed the YODA File format to meet the following requirements:

* **Easy for humans to read and use**. Anyone opening the file in a text editor or spreadsheet application should be able to intuitively understand the contents of the file's structured metadata header and comma-separated data table.

* **Easy for machines to parse and generate**. The file should be very easy to parse and validate with the wide variety of software tools used by scientists.

* **Group results into a single data array** similar to how scientists most commonly view their data, but also conforming to the metadata requirements of an [ODM2](https://github.com/ODM2/ODM2) [Dataset](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/core_datasets.md).

* **Serve as a self-describing archival file format** that is readily accepted by earth and environmental science data respositories, such as [IEDA EarthChem Library](http://www.earthchem.org/library) or [Knowledge Network for Biocomplexity (KNB)](https://knb.ecoinformatics.org/)

###Design Vision
A YODA File follows the data serialization and interchange format of [YAML](http://en.wikipedia.org/wiki/YAML) ("YAML Ain't Markup Language"), a superset of [JSON](http://www.json.org/) (JavaScript Object Notation). YAML can be readily [parsed by any modern computer language](http://yaml.org/). 

The key feature of a YODA file that distiguishes it from generic YAML is that a YODA file (1) organizes data into a comma-separated data array (e.g. a data table or DataFrame) with multiple columns and rows, and (2) provides all the metadata of an [ODM2](https://github.com/ODM2/ODM2) [Dataset](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/core_datasets.md) so that the data array can be parsed by software into an [ODM2](https://github.com/ODM2/ODM2) database instance.

[YODA Profiles](https://github.com/ODM2/YODA-File/blob/master/doc/YODA_profiles.md) have been developed for common dataset types to expectations for the data array block and to facilitate data/metadata input forms/templates for the end-user.

A YODA File will be structurally validated against required and optional ODM2 fields and controlled vocabularies using [JSON Schema](http://json-schema.org/), which provides a means for documenting the YODA File Schema and set of software tools for validating any JSON file against our schema. This **work in progress** can be found in the [YODA-Tools repository](https://github.com/ODM2/YODA-Tools).

We are also developing the [YODA Tools](https://github.com/ODM2/YodaTools) library, which is built upon the [ODM2PythonAPI](https://github.com/ODM2/ODM2PythonAPI) to create YODA files from our [YODA Excel Templates](https://github.com/ODM2/YODA-File/tree/master/excel_templates) or from an ODM2 database and to import YODA Files into an ODM2 database. YODA Files will thus serve as an interchange format between components of the [ODM2 Software Ecosystem](http://www.odm2.org/).

## History

The YODA file format developed out of the effort to substantially extend the CZO Display File specfication. The original [CZO Display File](http://criticalzone.org/national/publications/pub/whitenack-et-al-2011-czo-display-file-specification/) format was developed in 2010-2011 as a means for [US Critical Zone Observatories](http://criticalzone.org/) to share data in a form that was both human readable and machine parsable. The header provides structured metadata that allows the comma-separated data to be ingested into an [Observations Data Model 1.1 (ODM1.1)](http://his.cuahsi.org/odmdatabases.html) database, such as a [CUAHSI HydroServer](http://his.cuahsi.org/hydroserver.html).


# Overall Design

## Data Serialization Format

A YODA File follows the data serialization and interchange format of [YAML](http://en.wikipedia.org/wiki/YAML) ("YAML Ain't Markup Language"), a superset of [JSON](http://www.json.org/) (JavaScript Object Notation). YAML can be readily [parsed by any modern computer language](http://yaml.org/). 



# ==BELOW HERE IS INCOMPLETE==


## Block Structure

The YODA file will have information "blocks" which match 1:1 with the required tables in ODM2.0.  Each block will be titled with the name of the corresponding ODM2 table.  Within each block, there will be a YAML list containing the information for each field in the specified ODM2 table.  Any values that will be referenced by other records should be preceded by a YAML anchor.

After the last information block, there will be a single "result values" block consisting of two sub-blocks: ColumnDefinitions and Data.  The column definitions block defines all of the parameters unique to each column of data, the data block consists of comma-separated data columns.

All YODA files are required to have these **Info blocks**, in order

* YODA Header

* DataSets

* Organizations

* People

* Affiliations

* SamplingFeatures

* Methods

* Variables

* ProcessingLevels

* Actions

* FeatureActions

* ActionBy

* Results

* DataSetsResults

Any other table from the ODM2 structure can be added as another information block.  The order of each table is determined by the YAML requirement that an anchor must always precede a reference to that anchor.

## Syntax, Structure, and Examples of Some Required Information Blocks

All yaml files *must* begin with a series of 3 hyphens.  Period.  In a YODA file, after these hyphens will be a header with information about the file itself.  ie:

**************

YODA:

  - {Version: "1.0.0", Profile: “TimeSeries”, CreationTool: “Excel Template v1.0”, DateCreated: "2015-03-13", DateUpdated: "2015-03-13"}

**************

The version is the version of the YODA file.  If you are following this specification document, the version will be 1.0.0.

The profile determines the structure of the data table.  It must be one of the following options:  TimeSeries, SpecimenTimeSeries, or multiVariableSpecimenMeasurements.

The creation tool is the tool and version used to output the YODA file, ie, an excel template, a python script, or simply "manual" for a file created by hand.

The date created is the date the YODA file was created (not that the data was collected).

The date updated is the date the YODA file was updated, if this is not the original version of the file.

After the required header, the information blocks begin.  These general rules apply to the information blocks:

* Each block begins with an un-indented block title, followed by a colon (:).  The block title should be exactly matched with the corresponding ODM2 table.

* Each line within the block will begin with two spaces, a hyphen, and another space.  The dash and indentation clearly mark the following text as belonging to the specified block.  This is a YAML specification

* The first text after the dash will most often be a YAML anchor.  This serves as a pseudo-primary key for the table within the YODA file.  Each anchor begins with an ampersand (&) and then the name of the primary key of the table followed by #### where ### is the the number within the YODA file.  IE, the first organization in the organizations block will have the anchor "&OrganizationID0001" and the second “&OrganizationID0002.”

    * Tables in ODM2 with a primary key "BridgeID" should *not* be given anchors when written in a YODA file.

    * Other tables that should not be given anchors because they do not have their own primary keys: Sites, Specimens, MeasurementResults, CategoricalResults, TimeSeriesResults, ProfileResults, PointCoverageResults, SectionResults, TransectResults, TrajectoryResults, SpectralResults

* After the YAML anchor (if needed) a single row of data from the corresponding ODM2 table should be listed out in between curly braces.

    * The fields should be in the same order as they are in ODM2

    * Each field begins with a the field name followed by a colon (:)

    * Text and date fields will be surrounded by quotation marks

    * Empty fields will be filled with the word NULL.

    * Fields will be separated by commas.

    * The entire table worth of data will all be on a single line.  Do not use word wrapping!

    * Whether a field must be fill out or call be left null is determined by the specification of ODM2.

Organizations Block Example:

**************

Organizations:

   - &OrganizationID0001 {OrganizationTypeCV:  "University", OrganizationCode:  "USU", OrganizationName:  "Utah State University", OrganizationDescription:  NULL, OrganizationLink:  NULL}

   - &OrganizationID0002 {OrganizationTypeCV:  "Research institute", OrganizationCode:  "SWRC", OrganizationName:  "Stroud Water Research Center", OrganizationDescription:  NULL, OrganizationLink:  "www.stroudcenter.org"} 

**************

All YODA Format Files have their **data table** organized in **columns** that share:

* ODM2core.Actions.MethodID

* Variables

* Units

YODA format files are further specified by domain profiles. 

YODA Format Profiles are distinguished by:

* Allowable ResultTypes

* Specified row index

Examples:

YODA TimeSeries profile: (sensors only?)

* ResultTypes: TimeSeriesResult

* Row Index: ValueDateTime & ValueDateTimeUTCoffset

YODA SpecimenMeasurement profile:

* ResultTypes: MeasurementResult, CategoricalResult

* Row Index: SamplingFeatureCode

YODA SpecimenTimeSeries profile:

* ResultTypes: MeasurementResult, CategoricalResult

* Row Index: ValueDateTime, SamplingFeatureCode

