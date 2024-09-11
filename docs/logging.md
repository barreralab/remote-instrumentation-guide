# Logging 
Doesn't work as intended outside of IPython, see [Issue 3](#issues). Offloads to standard logger python library. Read documentation there to understand. Still, implement logging when creating drivers.  
To enable logging, put 
```python
from qcodes.logger import start_all_logging
start_all_logging()
```
at top of your programming. Log files are stored in the `/.qcodes/logs` folder in your home directory. You can export them to pandas df for better viewing via 

**TODO** Show how to view





<!-- 

### Background
- [Station config via YAML](http://microsoft.github.io/Qcodes/examples/Station.html)

### Qcodes Impoortant Examples
- [Instrument Group config](http://microsoft.github.io/Qcodes/examples/driver_examples/QCoDeS%20example%20with%20InstrumentGroup%20and%20DelegateInstrument.html)
- [Qcodes example with DelegateInstrument driver](http://microsoft.github.io/Qcodes/examples/driver_examples/QCoDeS%20example%20with%20DelegateInstrument.html)
- 
 -->
