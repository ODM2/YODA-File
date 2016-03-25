Excel Templates
===============
The folders in this directory hold blank Microsoft Excel templates for generating valid YODA files. Each Excel templates has been developed to serve a single YODA profile for common dataset types, to ease data and metadata input by the end-user.

Each YODA profile is defined by the expectations and constraints within the data array block for the [ODM2 ResultTypes](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_results.md), for SamplingFeatures (i.e. sites, specimens), for the row index and for each data column.

Excel templates exist for the following YODA profiles:

**Time Series**: Use this template if you are creating a YODA file for observations derived from in-situ sensors or other regularly spaced time series data (e.g., your input data are formatted similar to a datalogger output file with one date/time column and multiple data columns where each data column represents a different variable).

* *ODM2 ResultTypes*: [Time Series Coverage Results](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_results_timeseries.md) ([diagrams](http://odm2.github.io/ODM2/schemas/ODM2_Current/diagrams/ODM2Results.html))
* *Sampling Features*: entire data array refers to one or more SamplingFeatures, all of which have to be of type "Site"
* *Row index*: DateTime (+ UTCOffset)
* *Column*: Method, Result attributes (i.e. VariableName, UnitsName) and SamplingFeature are constant over the entire column

**Specimens** (under development):  Use this template if you are creating a YODA file for observations derived from physical specimens and your data conform to a cross tabulated format (e.g., one date/time column with multiple data columns where each data column represents a different variable).

* *ODM2 ResultTypes*: [MeasurementResults](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_results_measurement.md), [CategoricalResults](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_results_categorical.md) ([diagrams](http://odm2.github.io/ODM2/schemas/ODM2_Current/diagrams/ODM2Results.html))
* *Sampling Features*: sites and specimens can vary by row
* *Row index*: DateTime (+ UTCOffset) + SamplingFeatureID
* *Column*: Method, Result attributes (i.e. VariableName, UnitsName)

**Specimen Time Series**(under development):  Use this template if you are creating a YODA file for observations derived from physical specimens and your data are in a serial format (e.g., one date/time column and one data value column where each row in the table represents an observation of a particular variable).

* *ODM2 ResultTypes*: [MeasurementResults](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_results_measurement.md), [CategoricalResults](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_results_categorical.md) ([diagrams](http://odm2.github.io/ODM2/schemas/ODM2_Current/diagrams/ODM2Results.html))
* *Sampling Features*: entire data array refers to a single site, but specimens can vary by row
* *Row index*: DateTime (+ UTCOffset) + SamplingFeatureID for specimens
* *Column*: Method, Result attributes (i.e. VariableName, UnitsName) and Site.SamplingFeature are constant over the entire column

For example implementations, see the [examples folder](https://github.com/ODM2/YODA-File/tree/master/examples).

The **Old Prototypes** folder contains older versions of the templates.  These should not be used, but we have kept them in case we need to refer back to them.
