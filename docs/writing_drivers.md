# Writing Drivers 
Creating drivers amounts to defining a subclass of some base Instrument class and writing out the declarations for the parameters you want to include. It is ***highly recommmended*** that you inherit from the VisaInstrument base class as it allows you to create a simulated instrument for your driver to test trivial functionality.  

**NOTE** The following template requires that you have qcodes 0.46.0 and up. With previous versions, `self.add_parameter()` did not return anything, leading to [Issues 4](#issues) whereas now it returns the created parameter, allowing it to be assigned to an attribute. 


The general template goes as 

```python title="Instrument Driver template"
from qcodes.instrument import VisaInstrument

# log messages outside of instrument 
log = logging.getLogger(__name__)

# Inherit From VisaInstrument class
class YourInstrument(VisaInstrument):
    def __init__(self, name:str, address:str, terminator:str = '\n', **kwargs: Any) -> None:
        # Setup connection and other higher level items with parent Constructor
        super().__init__(name, address, terminator, **kwargs)

        # Add parameters here. You can define helper methods in the class
        # for the get_cmds and set_cmds. Here's an example
        # *Important*: assign the new parameter to a class attribute 
        # to meet modern qcodes standard (helps intellisense in code editors) 

        # Here is the method I recommend you use to add parameters 
        self.current = self.add_parameter(
            name = "current",
            label="Current",
            # output of asks is a string, this ensures conversion to float
            # note, you can set this to a function if you want more 
            # complicated behaviour
            get_parser=float,
            get_cmd=...,
            set_cmd=...,
            vals=...)
        "Docstring for current here"


        # Not recommended since instrument=self is easy to forget
        self.voltage = Parameter(
            "voltage",
            label="Voltage",
            get_parser=float,
            get_cmd=...,
            set_cmd=...,
            vals=...,
            # requires this line
            instrument=self
        )
        "Docstring for voltage parameter here"


        # At the end of the init function, make this method call defined 
        # in the Instrument class to print a connection msg
        # IMPORTANT: your instrument must return a standard id string on 
        # a *IDN? query for this method to work. Else, override the get_idn()
        # method. See remarks below
        self.connect_message() 
```

**Arguments to `self.add_parameter(...)`**
1. name: TODO: look into 
2. label: TODO: what diff
3. get_parser (optional): on queries, the driver receives data from the instrument in the form of a string. Specifying a get_parser allows you to update/modify the string data. If set to a primitive data type like `int` or `float`, then conversion is made implicitly. You can alternatively pass in a custom function 

How do you query and write to the instrument when inside a driver? You can use these inherited methods defined in InstrumentBase
1. Query: `self.ask(cmd: str)`
2. Write: `self.write(cmd: str)`
You'll see these methods used often in the drivers you'll encounter. It may even be necessary to override them in some cases. See [Keithley_2600 Driver](http://microsoft.github.io/Qcodes/_modules/qcodes/instrument_drivers/Keithley/_Keithley_2600.html#Keithley2600). Also note that this instrument doesn't communicate using SCPI, but instead the TSP protocol. 

If you want to include a parameter that is only settable/gettable, assign the set_cmd/get_cmd to False, not None. None corresponds to a manual parameter. 

Note that when you inherit from the VisaInstrument class, you'll see that the class heirarchy goes as  

\[
\underbrace{\textrm{VisaInstrument}}_{\textrm{Sets up VISA  connection}} \longrightarrow \overbrace{\textrm{Instrument}}^{\textrm{adds IDN param and some methods}} \longrightarrow \underbrace{\textrm{InstrumentBase}}_{\textrm{defines add\_parameter, etc}}
\]

where $a \to b$ signifies that $a$ is a child of $b$. 
**Exercises**
It's instructive to peek through the curtains of the qcodes api and see how these lines of codes actually control the instrument. Try out the following exercises. 

1. With the hierarchy above in miind, probe the source code for this [Weinschel Instrument Driver](https://github.com/microsoft/Qcodes/blob/main/src/qcodes/instrument_drivers/weinschel/Weinschel_8320.py) to investigate the following questions. Note: you can either search for the class source code at the given link, or if you have qcodes installed, you can use your code editor to look into the source files with the help  of code navigation.
When inheriting from the VisaInstrument class, 
    1. How is the visa address and backend specified for the instrument and where is the connection initialized?
    2. What instrument parameter is added first?
2. If no additional parameters/functions are defined in an instrument that inherits from VisaInstrument, which of the following methods/parameters will be available?
    a. `self.close()`
    b. `self.reset()`                 
    c. `self.connect_message()`
    d. `self.model`

**Solutions**
<details>
<summary>Look at to verify</summary>

1. I explored source on vscode editor 
    1. VisaInstrument class **TODO** add solution 
    2. the IDN parameter
2. (b) and (d) are NOT defined. close and connect methods are inherited from InstrumentBase
</details>
 

**Examples**
1. [Custom YokogawaGS820 Driver](/QCoDeS/src/LabDrivers/Yokogawa_GS820.py): Molded from the YokogawaGS200 driver and components from several others with modernized code. Supports only sourcing capabilities of the yoko currently (no measurements possible). Each channel treated as an instrument itself. Variations in range settings for different models handled in base class. 
2. [Modified Keithley6500 Driver](/QCoDeS/src/LabDrivers/Keithley_6500_1.py): Modified from core Keithely6500 driver to include input_impedance parameter and continuous reading mode (not succesful). Required updating setter functions.  
3. [AC Box Driver](/QCoDeS/src/LabDrivers/AC_DAC.py): Driver for Barrera Lab's custom built AC-DAC AD9106 Waveform generator **TODO** Update link when file name changes
4. [DC Box Driver](/QCoDeS/src/LabDrivers/Barrera_DCDAC_57604.py): Driver for Barrera Lab's custom built DC-DAC AD5764 DC generator 

**Remarks/Cautions**
1. If you don't override the `get_idn()` method, then you have to ensure that your instrument supports the `*IDN?` SCPI query, and moreover, returns a string formatted as 

\[
\textrm{\{vendor\}[s]\{model\}[s]\{serial\}[s]\{firmware\}}
\]

where $[s]$ denotes a separator which is either a comma, colon, or semicolon. Comma is more standard. 

**Important** For Arduino controlled devices operating over the Serial bus, it should be noted that Ardunos reset themselves when opening a serial connection (a byproduct of making firmware programming accessible). The current fix is to sleep for 3 seconds in the init method of the driver before `self.connect_message()` is called. 

## Testing your Driver 
If you want to make a contribution to the qcodes community driver library, you'll have to implement some of their testing protocols. 

To test trivial functionality and ensure `continuous integration', instantiate a [Simulated Instrument]() of your driver and verify that connection is possible. This requires writing a yaml file for a pyvisa simulated instrument and then passing the file into your instrument. 

**Examples**
1. [BarreraDCDAC5764 Simulated Instrument](/QCoDeS/src/LabDrivers/Barrera_DCDAC_5764/sim_test.py) using [DCDAC_5764.yaml](/QCoDeS/src/LabDrivers/Barrera_DCDAC_5764/DCDAC_5764.yaml)

With the physical instrument on hand, you can use standard testing frameworks such as pytest, unittest, etc to verify parameter setting/getting and instrument communication works. 
**Examples** 
1. [yoko_pytest](/QCoDeS/src/LabDrivers/yokogs820_test.py)
2. [BarreraDCDAC5764 unittest](/QCoDeS/src/LabDrivers/Barrera_DCDAC_5764/dcdac_test.py)



## Pipeline for Custom Instruments
1. *Build Instrument with SCPI support over some bus*
    For Arduino-driven instruments, see **TODO:** add user guide. 
    Ensure that data is buffered out of instrument only on query commands or else you have to do a lot more post-processing on the driver end.  
2. *Use pyvisa to perform functional testing of remote access*
    Confirm connection and data transfer works as intended. Remember to account for terminator characters. 
3. *Build qcodes driver*
    Inherit from VisaInstrument class if possible (allows construction of virtual instrument) 
    If instrument is programmed properly, the qcodes driver only needs to know the command tree and expected in/outputs. So this step could be done in parallel with construction, assuming good planning. 
4. *Test integration with Virtual Instrument*
    Instantiate a virtual instrument of your driver to verify trivial functionality. 
5. *Comprehensive Testing*
    Test getting/setting of all parameters. Verify that snapshots are correct at each point in time. Benchmark performance
