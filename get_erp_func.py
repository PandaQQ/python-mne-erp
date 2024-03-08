import numpy as np
import mne

def get_erp_func(raw, epoch_twd, baseline_twd, markers):
    """
    Extract ERPs from EEG data.

    Parameters:
    - raw: Instance of mne.io.Raw. The raw EEG data.
    - epoch_twd: tuple of (start, end) in milliseconds, e.g., (-200, 1000), for the epoch window relative to event.
    - baseline_twd: tuple of (start, end) in milliseconds, e.g., (-200, 0), for the baseline correction.
    - markers: List of markers to epoch, e.g., ['S 81', 'S 82'].
    - event_id: Dictionary mapping event markers to integers, e.g., {'S 81': 1, 'S 82': 2}.

    Returns:
    - A dictionary with keys 't_axis', 'ERPs', and 'ST' containing the time axis, ERP waveforms, and single trial data.
    """
    # Create events array from raw data
    events, event_id = mne.events_from_annotations(raw)

    # Define epochs
    epochs = mne.Epochs(raw, events, event_id=event_id, tmin=epoch_twd[0] / 1000.0, tmax=epoch_twd[1] / 1000.0,
                        baseline=(baseline_twd[0] / 1000.0, baseline_twd[1] / 1000.0), preload=True)

    # Store single trial data for each condition
    ST = {marker: epochs[marker]._data for marker in markers}

    # Calculate ERPs as the mean across trials for each condition
    ERPs = {marker: np.mean(ST[marker], axis=0) for marker in markers}

    # Time axis
    t_axis = epochs.times

    return {
        't_axis': t_axis,
        'ERPs': ERPs,
        'ST': ST
    }
