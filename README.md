# Personal Comfort Models (PCM) for vehicle indoor 

### Participant details:
   
   |Serial|ID|Gender|Name|
   |-----|-----|:---:|:------:|
   |1| S01 | F | Anna Laura |
   |2| S02 | F | Carolina |
   |3| S03 | F | Chiara |
   |4| S04 | F | Claudia |
   |5| S05 | F | Ilaria |
   |6| S06 | M | Luca |
   |7| S07 | M | Mattia|
   |8| S08 | F | Silvia|

## Data description
    1. Physiological data
    2. Environmenatal data
    3. Living lab data

### Physiological data (source: Empatica E4)

    - (TEMP) Temperature Sensor (degree Cel.)
    - (EDA) Electrodermal activity sensor (micro seimens)
    - (BVP) Photoplethysmograph (BVP)
    - (ACC) Accelerometer 3-axis sensor (ACC)
    - (IBI) Time of each heart beat and the duration between consecutive heart beats
    - (HR) Average heart rate extracted from the BVP signal, heart beat (BVP)
    - (TAGS) Event mark times

*CSV files in this archive are in the following format:*

> The first row is the initial time of the session expressed as unix timestamp in UTC. These timestamps represent the time at which each data point was recorded. Each value is in seconds since the Unix epoch (January 1, 1970).

> The second row is the sample rate expressed in Hz. Second row in each data file indicates the sample rate of data collection, except IBI. 

- *TEMP.csv:* Data from temperature sensor expressed degrees on the Celsius (°C) scale.

- *EDA.csv:* Data from the electrodermal activity sensor expressed as microsiemens (μS).

- *BVP.csv:* Data from photoplethysmograph.

- *ACC.csv:* Data from 3-axis accelerometer sensor. The accelerometer is configured to measure acceleration in the range [-2g, 2g]. Therefore the unit in this file is 1/64g. Data from x, y, and z axis are respectively in first, second, and third column.

- *IBI.csv:* Inter-Beat Interval, Time between individuals heart beats extracted from the BVP signal. No sample rate is needed for this file. The first column is the time (respect to the initial time) of the detected inter-beat interval expressed in seconds (s). The second column is the duration in seconds of the detected inter-beat interval (i.e., the distance in seconds from the previous beat).

- *HR.csv:* Average heart rate extracted from the BVP signal.The first row is the initial time of the session expressed as unix timestamp in UTC.
The second row is the sample rate expressed in Hz.

- *tags.csv:* Event mark times. Each row corresponds to a physical button press on the device; the same time as the status LED is first illuminated. The time is expressed as a unix timestamp in UTC and it is synchronized with initial time of the session indicated in the related data files from the corresponding session.

### Environmental data (source: Thermohygrometer)
| Node | Placed | Parameters |
|:-----:|-----|------|
| N1 | vehicle (front ac) | Air-Temp, Humidity, Dew-point |
| N2 | vehicle (front seat) | Air-Temp, Humidity, Dew-point |
| N3 | vehicle (rear seat) | Air-Temp, Humidity, Dew-point |
| N4 | vehicle (front seat) | Air-Temp, Humidity, Dew-point |
| N5 | office desk | Air-Temp, Humidity, Dew-point |


### Living Lab data (source: )

| LL Nr.| Node id | Parameters | Participant id |
|-------|:--------:|-----|:-----------:|
| LL 15 | 19F798E   | air-temp, illuminance, electricity, door, window    | S01 |
| LL 16 | 19F7993, 19FD06D| air temp, illuminance, electricity, door window, C02, relative humidity, globe temp  | x  |
| LL 17 | 1A057E5, 1A00DC1|air temp, illuminance, electricity, door window , C02, relative humidity, globe temp| S04, S07 |
| LL 18 | 1A00DBE, 1A057DF|air temp, illuminance, electricity, door window , C02, relative humidity, globe temp | S03, S05 |
| LL 19 | 1A057E0 | air-temp, illuminance, electricity, door, window  | x   |
| RO 1  |   --   | air temp, globe temp, relative humidity, air velocity  | S02, S08  |
| RO 2  |   --   | air temp, globe temp, relative humidity, air velocity | S06       |


*Living lab designation:*

|Living Lab |Participant ID | Parameters |
|-------|---------|---------|
| $LL_a$ | S01      | air-temp, illuminance, electricity, door, window |
| $LL_b$ | S02, S08 | air temp, globe temp, relative humidity, air velocity |
| $LL_c$ | S03, S05 | air temp, illuminance, electricity, door window , C02, relative humidity, globe temp |
| $LL_d$ | S04, S07 | air temp, illuminance, electricity, door window , C02, relative humidity, globe temp |
| $LL_e$ | S06      | air temp, globe temp, relative humidity, air velocity |


### Physiological Variables details

#### Empatica E4 - a wrist worn wearable device

> Empatica wearable technology is designed to monitor various physiological parameters and gather biometric data for health and research applications. 
> *Empatica E4 Physiological Monitoring:* The device is equipped with various sensors to monitor a range of physiological parameters, including:

- *Electrodermal Activity (EDA):* Measures the electrical conductance of the skin, often associated with stress, emotional arousal, and sweat gland activity.
- *Heart Rate (HR):* Monitors the wearer's heart rate, which can provide insights into physical and emotional states.
- *Temperature:* Measures the wearer's skin temperature, which can be indicative of changes in the autonomic nervous system.
- *Acceleration:* Captures motion and activity data, useful for tracking physical activity and movement.
- *Blood Volume Pulse (BVP):* Monitors changes in blood volume in the skin, which is related to cardiovascular activity.

#### Here are some key aspects of the generated data:
> Electrodermal Activity (EDA):
> - Skin Conductance Level (SCL): The baseline level of electrical conductance of the skin.
> - Skin Conductance Response (SCR): Momentary increases in conductance often linked to emotional arousal or stress.

> Heart Rate (HR):
> - Heart Rate Variability (HRV): The variation in time between successive heartbeats, which can be used to assess stress, relaxation, and autonomic nervous system balance.

> Temperature:
> - Skin Temperature: Continuous measurements of skin temperature, which may show fluctuations related to the wearer's state.

> Acceleration:
> - Activity Data: Information about the wearer's physical movements and activity levels, which can be used for physical activity tracking and posture analysis.

> Blood Volume Pulse (BVP):
> - Pulse Rate: Information about the wearer's pulse or heart rate, derived from changes in blood volume in the skin.

**Acceleration Data:**
> The following rows contain three sets of values, which represent the acceleration data along three axes (typically X, Y, and Z):
> - The first row with values like "32.000000, 32.000000, 32.000000" represents the raw acceleration data along the X, Y, and Z axes, respectively.
> - The subsequent rows contain numerical values in three columns, where each column represents the acceleration along the X, Y, and Z axes.
For example, in the row with values "-55, 45, 25":
> - "-55" corresponds to the acceleration along the X-axis.
> - "45" corresponds to the acceleration along the Y-axis.
> - "25" corresponds to the acceleration along the Z-axis.

*Data Interpretation:*
> The values in each row represent the acceleration of an object or device at a specific time point. The unit of acceleration typically depends on the hardware and configuration but is often measured in meters per second squared (m/s²).

> Sample data:
> - At timestamp 1693895582.000000, the acceleration along the X, Y, and Z axes is approximately 32.000000 m/s² for each axis.
> - Subsequent rows represent the acceleration values at different time points. For example, at timestamp 1693895583.000000 (one second later), the acceleration along each axis might have changed, as indicated by the corresponding numerical values.
> - The data allows you to track how acceleration changes over time along three different axes. This can be useful for various applications, such as monitoring the motion or vibrations of a device or tracking the movement of an object. Analysis of this data can provide insights into patterns, trends, or events related to the object's motion.

**Blood Volume Pulse (BVP) sensor:**
> BVP sensor from an Empatica wearable device is a measure of the variation in blood volume in a specific area, typically obtained from the wrist using a photoplethysmogram (PPG) sensor. BVP data is often used to monitor heart rate, heart rate variability, and other physiological parameters related to cardiovascular health.

*Data Interpretation:*
> - Unix Timestamp: The first value, '1693895582.00', appears to be a Unix timestamp, which represents the time in seconds since January 1, 1970. It indicates when the BVP measurements were taken.
> - The second row with the value "4.000000" indicates the sample rate of the Electrodermal Activity (EDA) data, expressed in Hertz (Hz). In the context of EDA data, the sample rate represents how many data points are recorded per second.
> - Subsequent Values: The subsequent numeric values represent the amplitude or intensity of the blood volume pulse signal at different points in time. These values are typically measured in arbitrary units or have been scaled or normalized. The specific units may vary depending on the device and the data processing applied.
> - Heart Rate: BVP data can be used to derive heart rate information. The variations in blood volume are often associated with the heartbeats, so the peaks in the BVP signal can be used to calculate heart rate. The frequency of these peaks corresponds to the heart rate.
> - Heart Rate Variability (HRV): BVP data can also be used to calculate heart rate variability, which is the variation in time between successive heartbeats. HRV is associated with the autonomic nervous system and can provide insights into stress, physical fitness, and other factors.
> - Pulse Waveform: BVP data may also contain information about the shape and characteristics of the pulse waveform, which can be used to assess the health of the cardiovascular system.

**Electrodermal Activity (EDA) sensor:**
> EDA measures the electrical conductance of the skin, which can be influenced by factors such as sweat gland activity, arousal, and emotional responses.

*Data interpretition*
> - Unix Timestamp: The first value, '1694010873.000000', is a Unix timestamp representing the time in seconds since January 1, 1970. It indicates when the EDA measurements were taken.
> - Sample Rate: The second value, '4.000000', represents the sample rate, which is the rate at which EDA measurements are recorded. In this case, it's 4 Hz, meaning there are four measurements taken every second.
> - EDA Amplitude: The subsequent numeric values represent the amplitude or magnitude of the EDA signal at different points in time. These values are typically measured in microsiemens (μS) or micro-microsiemens (μμS) and reflect the skin's electrical conductance.
> - Baseline: The initial values often serve as the baseline EDA levels. These levels can vary between individuals and are influenced by factors like skin moisture, temperature, and individual differences.
> - Phasic Changes: The values following the baseline represent phasic changes in EDA. Phasic changes indicate deviations from the baseline and are often associated with physiological responses to stimuli, such as increased EDA in response to stress or arousal.
> - Arousal and Emotional Responses: EDA data is frequently used to assess emotional states, arousal, and stress. An increase in EDA can indicate arousal or emotional responses, such as excitement, anxiety, or stress.

**IBI (Inter-Beat Interval) sensor:**
>  The IBI data records the time of each heart beat (or inter-beat interval) and the duration between consecutive heart beats. This data can be used for various physiological and cardiovascular analyses, such as heart rate variability, and can provide insights into the functioning of the cardiovascular system. The time column allows you to understand when these measurements occurred, and the duration column provides information about the time intervals between beats.

*Data Interpretation:*
> - Time (in seconds): The first column represents the time, which is expressed in seconds (s) and is relative to the initial time. This time value is the time at which each inter-beat interval (IBI) measurement was taken. It tells you when each IBI measurement occurred.

> - Duration of IBI (in seconds): The second column represents the duration in seconds (s) of the detected inter-beat interval. It is the time interval (duration) between the current beat and the previous beat. In other words, it measures the time it took for the heart to beat again after the previous beat. This duration provides information about the heart rate variability and can be used to analyze aspects of the cardiovascular system's performance.

**Heart rate (HR) Sensor:**
> Heart rate is a measure of the number of times the heart beats per minute and is often used as an indicator of a person's cardiovascular health and physical fitness.
---


### Implementation
*Follow the steps to reproduce the paper results*

**Step 1:**
Run script_E4_features for physiological data
>`python3 script_E4_features.py --data /path/to/E4_data/ --output /path/to/output/dir/`  
> Ex. python script_E4_features.py --data /path/datasets/VIC_summer2023/ --output ../output/E4_features/

**Step 2:**
Run script_tinytag_data for environmental data
>`python3 script_tinytag.py --data /path/to/tinytag/data --output /path/to/output/dir/  
> Ex. python script_tinytag_data.py --data /path/datasets/VIC_summer2023/ --output /path/output/tinytag_data/

**Step 3:**
Run script_select_features for selecting physiological features
>`python3 script_select_E4_features.py --features /path/to/dir/ --output /path/to/output/dir/`  
> Ex. python script_select_E4_features.py --features /path/output/E4_features/ --output /path/output/selected_E4_features/

**Step 4:**
Run script_living_lab for processing living lab data
>`python3 script_living_lab.py`

**Step 5:**
Run script_process_data for cleaning, interpolation, instances-labeling and merging phy-env data 
> `python3 script_process_data.py`

**Step 6:**




## Results

**S01**
| ID_instance | Duration (min) |
|-------------|:--------------:|
| S01_1       | 36.0        |
| S01_2       | 46.6        |
| S01_3       | 29.0        |
| S01_4       | 27.7        |
| S01_5       | 33.5        |
| S01_6       | 52.3        |
| S01_8       | 14.2        |
| S01_10      | 39.7        |
| S01_11      | 34.7        |
| S01_12      | 16.8        |
| S01_13      | 22.7        |
| S01_14      | 44.9        |
| S01_16      | 35.0        |
| S01_17      | 19.7        |
| S01_18      | 28.8        |
| S01_19      | 12.0        |
| S01_20      | 8.0         |
| S01_21      | 24.8        |
| **Total**   | **503.54**      |


**S02**