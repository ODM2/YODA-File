**Documentation of the YODA Specimen Time Series Template**

This template is designed for specimens collected in the field and analyzed in the laboratory. 

*People and Organizations:*
 - Generates Organizations, People, and Affiliations blocks.

*DataSet Citation:*
 - Generates DataSets, Citations, AuthorLists, and DataSetCitations blocks.

*Methods:*
 - Generates Methods block.
 - The only permitted methods are of type "Specimen collection" and "Specimen analysis".

*Variables:* 
 - Generates Variables block.

*Sites and Specimens:*
 - The SamplingFeatures block is generated from both the Sites and Specimens tabs.
 - The Sites tab generates SamplingFeatures of type "Site".
 - The Specimens tab generates SamplingFeatures of type "Specimen".
 - The Specimens block is generated from the Specimens tab.
 - The Sites block is generated from the Sites tab.
 - The RelatedFeatures block is generated to represent the relationships between Sites and Specimens. These relationships are all of the type "Was collected at".
 - The Specimens tab generates Actions of type "Specimen collection".
 - The Specimens tab generates FeatureActions relating Sites to the "Specimen collection" Actions. 
 - The Specimens tab generates records in the ActionBy block for the "Specimen collection" Actions.

*Units:* 
 - Generates Units block.

*Annotations:*
 - All Annotations should be of type "Measurement Result Value".

*Processing Levels:*
 - Generates ProcessingLevels block.

*Analysis_Results:*
 - Generates Actions of type "Specimen analysis".
 - Generates FeatureActions relating Specimens to the "Specimen analysis" Actions.
 - Generates RelatedActions relating the "Specimen analysis" actions to the associated "Specimen collection" actions. These RelatedActions are all of type "Is child of".
 - Generates records in the ActionBy block for the "Specimen analysis" Actions.
 - Generates Results of type "Measurement". Each line corresponds to a single Result.
 - Generates MeasurementResults block.
 - Generates MeasurementResultValues block.
 - Generates DataSetResults block.
 - Generates MeasurementResultValueAnnotations block. The template permits up to five Annotations for each Result.

*Other Notes:*
 - Each Result must include information about the Collection Action and Analysis Action of the Specimen. This means that each Collection and Analysis Action must have a person associated with it as well as a datetime when it occurred. If the person or the datetime are unknown, then a generic name or date should be used.
 - This template does not allow for inputs of details about Actions and Feature actions.  All actions will be coded as Specimen Collection and Specimen Analysis actions.
