# Station Configuration via YAML
Station initialization can be configured in a YAML configuration file. YAML is similar to JSON in that it is a human-readable data format. 

Documentation at [QC-Docs/YAML](http://microsoft.github.io/Qcodes/examples/Station.html#Configuring-the-Station-by-using-a-YAML-configuration-file)

Configures initialization of multiple instruments and parameters. Provide access by initializing station with config file, `station = qcodes.Station(config.yaml)`

**Examples**
1. [sweep_station.yaml](/QCoDeS/src/qcodes_testing/sweep_station.yaml) and [qc_sweep_yaml](/QCoDeS/src/qcodes_testing/qc_sweep_yaml.py) to see how custom drivers can be initialized. Note that the sweep here uses the do1d module as opposed to the measurement context in [qc_sweep](/QCoDeS/src/qcodes_testing/qc_sweep.py)