CZO Display File v2 Specification
===============

##History
The [CZO Display File v1](http://criticalzone.org/national/publications/pub/whitenack-et-al-2011-czo-display-file-specification/) format was developed in 2010-2011 as a means for [US Critical Zone Observatories](http://criticalzone.org/) to share data in a form that was both human readable and machine parseable. The header provides metadata that allows the comma-separated data to be ingested into an [Observations Data Model 1.1 (ODM1.1)](http://his.cuahsi.org/odmdatabases.html) database, such as a [CUAHSI Hydroserver](http://his.cuahsi.org/hydroserver.html).

##Goals
Our goal for **CZO Display File v2** is to substantially extend the CZO Display File specification to meet the following requirements:
* Human readable
* Machine parseable
* Conform to the metadata requirements of an [ODM2](https://github.com/UCHIC/ODM2) [Dataset](https://github.com/UCHIC/ODM2/blob/master/doc/ODM2Docs/core_datasets.md)
* Serve as an archival file format that is self-describing and readily accepted by earth and environmental science data respositories, such as [IEDA EarthChem](http://www.earthchem.org/library) or [Knowledge Network for Biocomplexity (KNB)](https://knb.ecoinformatics.org/)

