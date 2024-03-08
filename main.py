
import matplotlib.pyplot as plt
import mne
import get_erp_func

# Load your EEG data here (update with your data path and format)
raw = mne.io.read_raw_brainvision('data/oddball_pilot_001_1.vhdr', preload=True)

# Update channel locations (update with your montage file if needed)
raw.set_montage('standard_1020')

# Resample
raw.resample(250)

# Filter
raw.filter(1, 40)

# ICA for artifact removal (adjust parameters as needed)
ica = mne.preprocessing.ICA(n_components=None, random_state=97, max_iter=800)
# Then proceed with component inspection and exclusion

ica.fit(raw)
ica.exclude = [0]  # Update this to exclude components representing eye artifacts
ica.apply(raw)

# Re-reference (update this if you have specific reference channels)
raw.set_eeg_reference('average', projection=True)

# Define your conditions and event_id here
epoch_twd = (-200, 1000)
baseline_twd = (-200, 0)
markers = ['S 21', 'S 22']
# event_id = {'S 21': 1, 'S 22': 2}

# print(raw.ch_names)
# print(event_id)
# Extract ERPs
ERPs = get_erp_func.get_erp_func(raw, epoch_twd, baseline_twd, markers)

plt.figure()
pz_index = mne.pick_channels(raw.info['ch_names'], ['Pz'])[0]
plt.plot(ERPs['t_axis'], ERPs['ERPs']['S 21'][pz_index], label='S 21')
plt.plot(ERPs['t_axis'], ERPs['ERPs']['S 22'][pz_index], label='S 22')
plt.xlabel('Time after stimulus (ms)')
plt.ylabel('Amplitude (μV)')
plt.title('Brain response pattern')
plt.show()
