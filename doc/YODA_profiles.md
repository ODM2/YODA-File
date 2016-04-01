YODA Profiles
===============

A ***YODA profile*** is defined by the expectations and constraints within the data array block for the *[ODM2 ResultTypes](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_results.md)*, for *[SamplingFeatures](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_samplingfeatures.md)* (i.e. sites, specimens), for the *row index* (i.e. metadata that distinquishes one row from another) and for each *data column*.

The following YODA profiles have been developed for common dataset types to serve corresponding [Excel templates](https://github.com/ODM2/YODA-File/tree/master/excel_templates). Each Excel template for YODA serves a single YODA profile.


###YODA profiles developed for Excel Templates:

**Time Series**: Use this template if you are creating a YODA file for observations derived from in-situ sensors or other regularly spaced time series data (e.g., your input data are formatted similar to a datalogger output file with one date/time column and multiple data columns where each data column represents a different variable).

* *ODM2 ResultTypes*: [Time Series Coverage Results](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_results_timeseries.md) ([diagrams](http://odm2.github.io/ODM2/schemas/ODM2_Current/diagrams/ODM2Results.html))
* *Sampling Features*: all must be of type "[Site](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_samplingfeatures.md#sampling-features-that-are-sites)", and if more than one, they can ony vary by data column
* *Row index*: DateTime (+ UTCOffset)
* *Data Column*: [SamplingFeature for Sites](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_samplingfeatures.md#sampling-features-that-are-sites), [Method](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/core_methods.md) and other [Result](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/core_results.md) attributes (i.e. VariableName, Units, SampledMedium) are constant over each entire column


**Specimens** (under development):  Use this template if you are creating a YODA file for observations derived from physical specimens and your data conform to a *cross tabulated format* (e.g., one specimen ID column with multiple data columns where each data column represents a different variable).

* *ODM2 ResultTypes*: [MeasurementResults](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_results_measurement.md), [CategoricalResults](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_results_categorical.md) ([diagrams](http://odm2.github.io/ODM2/schemas/ODM2_Current/diagrams/ODM2Results.html))
* *Sampling Features*: Specimens vary by row. Specimens can be related to their parent Sites and other SamplingFeatures, including their SpatialOffsets (i.e. depths), in the header.
* *Row index*: [SamplingFeatureID for Specimens](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_samplingfeatures.md#sampling-features-that-are-specimens)
* *Data Column*: [Method](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/core_methods.md) and other [Result](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/core_results.md) attributes (i.e. VariableName, Units, SampledMedium) are constant over each entire column


**Specimen Time Series** (under development):  Use this template if you are creating a YODA file for observations derived from physical specimens and your data are in a *serial format* (e.g., one date/time column and one data value column where each row in the table represents an observation of a particular variable on a particular specimen). This template is particularly useful for datasets where specimens were analyzed, but there is not a set or standard set of analyses for each specimen.

* *ODM2 ResultTypes*: [Measurement Results](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_results_measurement.md), [Categorical Results](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_results_categorical.md) ([diagrams](http://odm2.github.io/ODM2/schemas/ODM2_Current/diagrams/ODM2Results.html))
* *Sampling Features*: Specimens vary by row. Specimens can be related to their parent Sites and other SamplingFeatures in the header.
* *Row index*: DateTime (+ UTCOffset) + [SamplingFeatureID for Specimens](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_samplingfeatures.md#sampling-features-that-are-specimens) + Result attributes (i.e., VariableName + Method + Units)
* *Data Column*: There is a single data value column. All data values go in this single column.

For example implementations, see the [examples folder](https://github.com/ODM2/YODA-File/tree/master/examples).

The **Old Prototypes** folder contains older versions of the templates.  These should not be used, but we have kept them in case we need to refer back to them.


###Other envisioned YODA profiles:

* Spectra for [ODM2 SpectraResults](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_results_spectra.md)
* SensorDepthProfile for [ODM2 ProfileResults](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_results_profile.md)
* SensorTransect for [ODM2 TransectResults](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_results_transect.md)
* SensorSection for [ODM2 SectionResults](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_results_section.md)
* SensorPointCoverage for [ODM2 PointCoverageResults](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_results_pointcoverage.md)
* SensorTrajectory for [ODM2 TrajectoryResults](https://github.com/ODM2/ODM2/blob/master/doc/ODM2Docs/ext_results_trajectory.md)
