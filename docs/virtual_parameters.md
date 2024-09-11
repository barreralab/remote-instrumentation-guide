# Virtual Parameters
QCoDeS supports the abstraction of existing parameters/instruments in a variety of ways.

## Delegate Parameter
Parameters whose setting/getting is offloaded to other underlying parameters in an instrument. Can be used to represent inferrable quantities that require conversion from other parameters. 



Also helpful for writing drivers. See implementation of source setting in [Custom YokogawaGS820 Driver](/QCoDeS/src/LabDrivers/Yokogawa_GS820.py)

## Parameters with Setpoints 
Useful for defining parameters based on arrays of existing values. See [QC-Docs/Params_with_setpoints](http://

microsoft.github.io/Qcodes/examples/Parameters/Simple-Example-of-ParameterWithSetpoints.html) and then [QC-Docs/Params_setpoints_on_other_instruments](http://microsoft.github.io/Qcodes/examples/Parameters/Parameter-With-Setpoints-defined-on-a-different-instrument.html)

## Delegate Instruments 
To create containers for parameters in different instruments. Most easily achieved via YAML configuration See [QC-Docs/YAML-Deleg](http://microsoft.github.io/Qcodes/examples/driver_examples/QCoDeS%20example%20with%20DelegateInstrument.html) for introductory information and [QC-Docs/YAML-InstrumentGroup](http://microsoft.github.io/Qcodes/examples/driver_examples/QCoDeS%20example%20with%20InstrumentGroup%20and%20DelegateInstrument.html) to see how this can approach can be used to model devices on a chip
