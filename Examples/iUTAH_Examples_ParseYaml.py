import yaml

longHeaderStream = file('iUTAH_MultiTimeSeriesExample_LongHeader.yaml', 'r')
longHeaderObject = yaml.load(longHeaderStream)

compactHeaderStream = file('iUTAH_MultiTimeSeriesExample_CompactHeader.yaml', 'r')
compactHeaderObject = yaml.load(compactHeaderStream)

nestedTableStream = file('iUTAH_SpecimenTimeSeriesExample_CompactHeader.yaml', 'r')
nestedTableObject = yaml.load(nestedTableStream)

print yaml.dump(nestedTableObject)