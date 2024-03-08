# MNE Python to Generate ERP from vhdr file

- Python 12 & venv
## How to set up environment
```python
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


## Programme Result
Extracting parameters from data/oddball_pilot_001_1.vhdr...
Setting channel info structure...
Reading 0 ... 653149  =      0.000 ...   653.149 secs...
Filtering raw data in 1 contiguous segment
Setting up band-pass filter from 1 - 40 Hz

FIR filter parameters
---------------------
Designing a one-pass, zero-phase, non-causal bandpass filter:
- Windowed time-domain design (firwin) method
- Hamming window with 0.0194 passband ripple and 53 dB stopband attenuation
- Lower passband edge: 1.00
- Lower transition bandwidth: 1.00 Hz (-6 dB cutoff frequency: 0.50 Hz)
- Upper passband edge: 40.00 Hz
- Upper transition bandwidth: 10.00 Hz (-6 dB cutoff frequency: 45.00 Hz)
- Filter length: 825 samples (3.300 s)

Fitting ICA to data using 16 channels (please be patient, this may take a while)
Selecting by non-zero PCA components: 16 components
Fitting ICA took 2.4s.
Applying ICA to Raw instance
    Transforming to ICA space (16 components)
    Zeroing out 1 ICA component
    Projecting back using 16 PCA components
EEG channel type selected for re-referencing
Adding average EEG reference projection.
1 projection items deactivated
Average reference projection was added, but has not been applied yet. Use the apply_proj method to apply it.
Used Annotations descriptions: ['New Segment/', 'Stimulus/S 21', 'Stimulus/S 22', 'Stimulus/S 23']
Not setting metadata
93 matching events found
Applying baseline correction (mode: mean)
Created an SSP operator (subspace dimension = 1)
1 projection items activated
Using data from preloaded Raw for 93 events and 301 original time points ...
1 bad epochs dropped