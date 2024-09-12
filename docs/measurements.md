# Taking Measurements 
## Using a Measurement Context 
Follow The Measurement Context Manager section of [QC-Docs/15mintoQC](http://microsoft.github.io/Qcodes/examples/15_minutes_to_QCoDeS.html#Measurement-Context-Manager). 
Note that Measurement Contexts are initialized with a Station and Experiment. The context relies on the snapshot method from the station. 

User defines the dependent and independent parameters under study. 

See [QC-Docs/Dataset/MeasuringX(t)](http://microsoft.github.io/Qcodes/examples/DataSet/Measuring%20X%20as%20a%20function%20of%20time.html) for measurements of time parameters

## Using doNd
Measurement contexts allow for complete freedom in experiment design, however, for standard measurements such as linear sweeps, they are over exposed pieces of software.
QCoDeS provide highly optimized data handling for such measurements. 
[QC-Docs/DataSet/UsingDoND...](http://microsoft.github.io/Qcodes/examples/DataSet/Using_doNd_functions_in_comparison_to_Measurement_context_manager_for_performing_measurements.html) explores the capabilities of the module, which include 
- Support for multi channel sweeps over multiple independent parameters. Linear and logarithmic sweeps built-in
- Simultaneous 'Together plotting'. View at [qc_doNd_together_sweep.py](/QCoDeS/src/qcodes_testing/qc_dond_together_sweep.py)
- $n$ dimensional sweeps by feeding sweeps into each other

Calling the `doNd()` returns a tuple of objects. The first of which can be plotted via the plot function from `qcodes.utils.dataset.doNd`. 
If you are in an IPython environment, you can configure the doNd for auto plotting. Outside, the best choice is plottr.

!!! note
    plottr doesn't have integrated support for general $n$ dimensional plotting. See this [resource](https://en.wikipedia.org/wiki/Interstellar_(film)) for more info 

**Examples**
1. [qc_doNd_together_sweep.py](/QCoDeS/src/qcodes_testing/qc_dond_together_sweep.py) Both output channels of YokogawaGS820 linearly sweep over voltage while Keithley2400 and Keithley6500 take measurements. Plotted data shows recorded voltages over the linearly sweeped parameter space resulting in heatmap over diagonal with x and y axes being yoko voltages. Compare with [qc_sweep.py](/QCoDeS/src/qcodes_testing/qc_sweep.py) to appreciate the power of doNd. The Keithly2400 driver is provided by qcodes core driver library, but the script
**Requires** 
    1. in-house [YokogawaGs820 driver](/QCoDeS/src/LabDrivers/Yokogawa_GS820.py) 
    2. modified [Keithley6500 driver](/QCoDeS//src/LabDrivers/Keithley_6500_1.py).  


## Saving Data in Memory 
Can save data in memory instead of to SQLite3 database to save time. But, no protection against memory loss. If computer crashes during experiment, data is vanquished. **TODO**: Look at [Saving DataInMem](http://microsoft.github.io/Qcodes/examples/DataSet/InMemoryDataSet.html),  [OptimizingDataTime](http://microsoft.github.io/Qcodes/examples/DataSet/Performing-measurements-using-qcodes-parameters-and-dataset.html#Optimizing-measurement-time), [SavingDataInBG](http://microsoft.github.io/Qcodes/examples/DataSet/Saving_data_in_the_background.html)
