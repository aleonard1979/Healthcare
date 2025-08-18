## Health care


```python
#import needed libraries
import pandas as pd
import numpy as np
import datetime
```


```python
df = pd.read_csv(r'C:\Users\Antonio\Downloads\healthcare_dataset.csv')
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Blood Type</th>
      <th>Medical Condition</th>
      <th>Date of Admission</th>
      <th>Doctor</th>
      <th>Hospital</th>
      <th>Insurance Provider</th>
      <th>Billing Amount</th>
      <th>Room Number</th>
      <th>Admission Type</th>
      <th>Discharge Date</th>
      <th>Medication</th>
      <th>Test Results</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bobby JacksOn</td>
      <td>30</td>
      <td>Male</td>
      <td>B-</td>
      <td>Cancer</td>
      <td>1/31/2024</td>
      <td>Matthew Smith</td>
      <td>Sons and Miller</td>
      <td>Blue Cross</td>
      <td>18856.28131</td>
      <td>328</td>
      <td>Urgent</td>
      <td>2/2/2024</td>
      <td>Paracetamol</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1</th>
      <td>LesLie TErRy</td>
      <td>62</td>
      <td>Male</td>
      <td>A+</td>
      <td>Obesity</td>
      <td>8/20/2019</td>
      <td>Samantha Davies</td>
      <td>Kim Inc</td>
      <td>Medicare</td>
      <td>33643.32729</td>
      <td>265</td>
      <td>Emergency</td>
      <td>8/26/2019</td>
      <td>Ibuprofen</td>
      <td>Inconclusive</td>
    </tr>
    <tr>
      <th>2</th>
      <td>DaNnY sMitH</td>
      <td>76</td>
      <td>Female</td>
      <td>A-</td>
      <td>Obesity</td>
      <td>9/22/2022</td>
      <td>Tiffany Mitchell</td>
      <td>Cook PLC</td>
      <td>Aetna</td>
      <td>27955.09608</td>
      <td>205</td>
      <td>Emergency</td>
      <td>10/7/2022</td>
      <td>Aspirin</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>3</th>
      <td>andrEw waTtS</td>
      <td>28</td>
      <td>Female</td>
      <td>O+</td>
      <td>Diabetes</td>
      <td>11/18/2020</td>
      <td>Kevin Wells</td>
      <td>Hernandez Rogers and Vang,</td>
      <td>Medicare</td>
      <td>37909.78241</td>
      <td>450</td>
      <td>Elective</td>
      <td>12/18/2020</td>
      <td>Ibuprofen</td>
      <td>Abnormal</td>
    </tr>
    <tr>
      <th>4</th>
      <td>adrIENNE bEll</td>
      <td>43</td>
      <td>Female</td>
      <td>AB+</td>
      <td>Cancer</td>
      <td>9/19/2022</td>
      <td>Kathleen Hanna</td>
      <td>White-White</td>
      <td>Aetna</td>
      <td>14238.31781</td>
      <td>458</td>
      <td>Urgent</td>
      <td>10/9/2022</td>
      <td>Penicillin</td>
      <td>Abnormal</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 55500 entries, 0 to 55499
    Data columns (total 15 columns):
     #   Column              Non-Null Count  Dtype  
    ---  ------              --------------  -----  
     0   Name                55500 non-null  object 
     1   Age                 55500 non-null  int64  
     2   Gender              55500 non-null  object 
     3   Blood Type          55500 non-null  object 
     4   Medical Condition   55500 non-null  object 
     5   Date of Admission   55500 non-null  object 
     6   Doctor              55500 non-null  object 
     7   Hospital            55500 non-null  object 
     8   Insurance Provider  55500 non-null  object 
     9   Billing Amount      55500 non-null  float64
     10  Room Number         55500 non-null  int64  
     11  Admission Type      55500 non-null  object 
     12  Discharge Date      55500 non-null  object 
     13  Medication          55500 non-null  object 
     14  Test Results        55500 non-null  object 
    dtypes: float64(1), int64(2), object(12)
    memory usage: 6.4+ MB
    


```python
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])
```


```python
df.dtypes
```




    Name                          object
    Age                            int64
    Gender                        object
    Blood Type                    object
    Medical Condition             object
    Date of Admission     datetime64[ns]
    Doctor                        object
    Hospital                      object
    Insurance Provider            object
    Billing Amount               float64
    Room Number                    int64
    Admission Type                object
    Discharge Date        datetime64[ns]
    Medication                    object
    Test Results                  object
    dtype: object




```python
df.drop_duplicates()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Blood Type</th>
      <th>Medical Condition</th>
      <th>Date of Admission</th>
      <th>Doctor</th>
      <th>Hospital</th>
      <th>Insurance Provider</th>
      <th>Billing Amount</th>
      <th>Room Number</th>
      <th>Admission Type</th>
      <th>Discharge Date</th>
      <th>Medication</th>
      <th>Test Results</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bobby JacksOn</td>
      <td>30</td>
      <td>Male</td>
      <td>B-</td>
      <td>Cancer</td>
      <td>2024-01-31</td>
      <td>Matthew Smith</td>
      <td>Sons and Miller</td>
      <td>Blue Cross</td>
      <td>18856.281310</td>
      <td>328</td>
      <td>Urgent</td>
      <td>2024-02-02</td>
      <td>Paracetamol</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1</th>
      <td>LesLie TErRy</td>
      <td>62</td>
      <td>Male</td>
      <td>A+</td>
      <td>Obesity</td>
      <td>2019-08-20</td>
      <td>Samantha Davies</td>
      <td>Kim Inc</td>
      <td>Medicare</td>
      <td>33643.327290</td>
      <td>265</td>
      <td>Emergency</td>
      <td>2019-08-26</td>
      <td>Ibuprofen</td>
      <td>Inconclusive</td>
    </tr>
    <tr>
      <th>2</th>
      <td>DaNnY sMitH</td>
      <td>76</td>
      <td>Female</td>
      <td>A-</td>
      <td>Obesity</td>
      <td>2022-09-22</td>
      <td>Tiffany Mitchell</td>
      <td>Cook PLC</td>
      <td>Aetna</td>
      <td>27955.096080</td>
      <td>205</td>
      <td>Emergency</td>
      <td>2022-10-07</td>
      <td>Aspirin</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>3</th>
      <td>andrEw waTtS</td>
      <td>28</td>
      <td>Female</td>
      <td>O+</td>
      <td>Diabetes</td>
      <td>2020-11-18</td>
      <td>Kevin Wells</td>
      <td>Hernandez Rogers and Vang,</td>
      <td>Medicare</td>
      <td>37909.782410</td>
      <td>450</td>
      <td>Elective</td>
      <td>2020-12-18</td>
      <td>Ibuprofen</td>
      <td>Abnormal</td>
    </tr>
    <tr>
      <th>4</th>
      <td>adrIENNE bEll</td>
      <td>43</td>
      <td>Female</td>
      <td>AB+</td>
      <td>Cancer</td>
      <td>2022-09-19</td>
      <td>Kathleen Hanna</td>
      <td>White-White</td>
      <td>Aetna</td>
      <td>14238.317810</td>
      <td>458</td>
      <td>Urgent</td>
      <td>2022-10-09</td>
      <td>Penicillin</td>
      <td>Abnormal</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>55495</th>
      <td>eLIZABeTH jaCkSOn</td>
      <td>42</td>
      <td>Female</td>
      <td>O+</td>
      <td>Asthma</td>
      <td>2020-08-16</td>
      <td>Joshua Jarvis</td>
      <td>Jones-Thompson</td>
      <td>Blue Cross</td>
      <td>2650.714952</td>
      <td>417</td>
      <td>Elective</td>
      <td>2020-09-15</td>
      <td>Penicillin</td>
      <td>Abnormal</td>
    </tr>
    <tr>
      <th>55496</th>
      <td>KYle pEREz</td>
      <td>61</td>
      <td>Female</td>
      <td>AB-</td>
      <td>Obesity</td>
      <td>2020-01-23</td>
      <td>Taylor Sullivan</td>
      <td>Tucker-Moyer</td>
      <td>Cigna</td>
      <td>31457.797310</td>
      <td>316</td>
      <td>Elective</td>
      <td>2020-02-01</td>
      <td>Aspirin</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>55497</th>
      <td>HEATher WaNG</td>
      <td>38</td>
      <td>Female</td>
      <td>B+</td>
      <td>Hypertension</td>
      <td>2020-07-13</td>
      <td>Joe Jacobs DVM</td>
      <td>and Mahoney Johnson Vasquez,</td>
      <td>UnitedHealthcare</td>
      <td>27620.764720</td>
      <td>347</td>
      <td>Urgent</td>
      <td>2020-08-10</td>
      <td>Ibuprofen</td>
      <td>Abnormal</td>
    </tr>
    <tr>
      <th>55498</th>
      <td>JENniFER JOneS</td>
      <td>43</td>
      <td>Male</td>
      <td>O-</td>
      <td>Arthritis</td>
      <td>2019-05-25</td>
      <td>Kimberly Curry</td>
      <td>Jackson Todd and Castro,</td>
      <td>Medicare</td>
      <td>32451.092360</td>
      <td>321</td>
      <td>Elective</td>
      <td>2019-05-31</td>
      <td>Ibuprofen</td>
      <td>Abnormal</td>
    </tr>
    <tr>
      <th>55499</th>
      <td>jAMES GARCiA</td>
      <td>53</td>
      <td>Female</td>
      <td>O+</td>
      <td>Arthritis</td>
      <td>2024-04-02</td>
      <td>Dennis Warren</td>
      <td>Henry Sons and</td>
      <td>Aetna</td>
      <td>4010.134172</td>
      <td>448</td>
      <td>Urgent</td>
      <td>2024-04-29</td>
      <td>Ibuprofen</td>
      <td>Abnormal</td>
    </tr>
  </tbody>
</table>
<p>54966 rows × 15 columns</p>
</div>




```python
df['Name'] = df['Name'].str.title()
```


```python
name_split = df['Name'].str.split(" ", n=1,expand=True)
df['first_name'] = name_split[0]
df['last_name'] = name_split[1]

```


```python
df.rename(columns={'Name': 'Full_Name'}, inplace=True)
```


```python
df['Admission_Year'] = pd.DatetimeIndex(df['Date of Admission']).year
df['Admission_Month'] = pd.DatetimeIndex(df['Date of Admission']).month_name()
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Full_Name</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Blood Type</th>
      <th>Medical Condition</th>
      <th>Date of Admission</th>
      <th>Doctor</th>
      <th>Hospital</th>
      <th>Insurance Provider</th>
      <th>Billing Amount</th>
      <th>Room Number</th>
      <th>Admission Type</th>
      <th>Discharge Date</th>
      <th>Medication</th>
      <th>Test Results</th>
      <th>first_name</th>
      <th>last_name</th>
      <th>Admission_Year</th>
      <th>Admission_Month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bobby Jackson</td>
      <td>30</td>
      <td>Male</td>
      <td>B-</td>
      <td>Cancer</td>
      <td>2024-01-31</td>
      <td>Matthew Smith</td>
      <td>Sons and Miller</td>
      <td>Blue Cross</td>
      <td>18856.28131</td>
      <td>328</td>
      <td>Urgent</td>
      <td>2024-02-02</td>
      <td>Paracetamol</td>
      <td>Normal</td>
      <td>Bobby</td>
      <td>Jackson</td>
      <td>2024</td>
      <td>January</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Leslie Terry</td>
      <td>62</td>
      <td>Male</td>
      <td>A+</td>
      <td>Obesity</td>
      <td>2019-08-20</td>
      <td>Samantha Davies</td>
      <td>Kim Inc</td>
      <td>Medicare</td>
      <td>33643.32729</td>
      <td>265</td>
      <td>Emergency</td>
      <td>2019-08-26</td>
      <td>Ibuprofen</td>
      <td>Inconclusive</td>
      <td>Leslie</td>
      <td>Terry</td>
      <td>2019</td>
      <td>August</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Danny Smith</td>
      <td>76</td>
      <td>Female</td>
      <td>A-</td>
      <td>Obesity</td>
      <td>2022-09-22</td>
      <td>Tiffany Mitchell</td>
      <td>Cook PLC</td>
      <td>Aetna</td>
      <td>27955.09608</td>
      <td>205</td>
      <td>Emergency</td>
      <td>2022-10-07</td>
      <td>Aspirin</td>
      <td>Normal</td>
      <td>Danny</td>
      <td>Smith</td>
      <td>2022</td>
      <td>September</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Andrew Watts</td>
      <td>28</td>
      <td>Female</td>
      <td>O+</td>
      <td>Diabetes</td>
      <td>2020-11-18</td>
      <td>Kevin Wells</td>
      <td>Hernandez Rogers and Vang,</td>
      <td>Medicare</td>
      <td>37909.78241</td>
      <td>450</td>
      <td>Elective</td>
      <td>2020-12-18</td>
      <td>Ibuprofen</td>
      <td>Abnormal</td>
      <td>Andrew</td>
      <td>Watts</td>
      <td>2020</td>
      <td>November</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Adrienne Bell</td>
      <td>43</td>
      <td>Female</td>
      <td>AB+</td>
      <td>Cancer</td>
      <td>2022-09-19</td>
      <td>Kathleen Hanna</td>
      <td>White-White</td>
      <td>Aetna</td>
      <td>14238.31781</td>
      <td>458</td>
      <td>Urgent</td>
      <td>2022-10-09</td>
      <td>Penicillin</td>
      <td>Abnormal</td>
      <td>Adrienne</td>
      <td>Bell</td>
      <td>2022</td>
      <td>September</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Hospital_Stay_Length'] = df['Discharge Date'] - df['Date of Admission']
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Full_Name</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Blood Type</th>
      <th>Medical Condition</th>
      <th>Date of Admission</th>
      <th>Doctor</th>
      <th>Hospital</th>
      <th>Insurance Provider</th>
      <th>Billing Amount</th>
      <th>Room Number</th>
      <th>Admission Type</th>
      <th>Discharge Date</th>
      <th>Medication</th>
      <th>Test Results</th>
      <th>first_name</th>
      <th>last_name</th>
      <th>Admission_Year</th>
      <th>Admission_Month</th>
      <th>Hospital_Stay_Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bobby Jackson</td>
      <td>30</td>
      <td>Male</td>
      <td>B-</td>
      <td>Cancer</td>
      <td>2024-01-31</td>
      <td>Matthew Smith</td>
      <td>Sons and Miller</td>
      <td>Blue Cross</td>
      <td>18856.28131</td>
      <td>328</td>
      <td>Urgent</td>
      <td>2024-02-02</td>
      <td>Paracetamol</td>
      <td>Normal</td>
      <td>Bobby</td>
      <td>Jackson</td>
      <td>2024</td>
      <td>January</td>
      <td>2 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Leslie Terry</td>
      <td>62</td>
      <td>Male</td>
      <td>A+</td>
      <td>Obesity</td>
      <td>2019-08-20</td>
      <td>Samantha Davies</td>
      <td>Kim Inc</td>
      <td>Medicare</td>
      <td>33643.32729</td>
      <td>265</td>
      <td>Emergency</td>
      <td>2019-08-26</td>
      <td>Ibuprofen</td>
      <td>Inconclusive</td>
      <td>Leslie</td>
      <td>Terry</td>
      <td>2019</td>
      <td>August</td>
      <td>6 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Danny Smith</td>
      <td>76</td>
      <td>Female</td>
      <td>A-</td>
      <td>Obesity</td>
      <td>2022-09-22</td>
      <td>Tiffany Mitchell</td>
      <td>Cook PLC</td>
      <td>Aetna</td>
      <td>27955.09608</td>
      <td>205</td>
      <td>Emergency</td>
      <td>2022-10-07</td>
      <td>Aspirin</td>
      <td>Normal</td>
      <td>Danny</td>
      <td>Smith</td>
      <td>2022</td>
      <td>September</td>
      <td>15 days</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Andrew Watts</td>
      <td>28</td>
      <td>Female</td>
      <td>O+</td>
      <td>Diabetes</td>
      <td>2020-11-18</td>
      <td>Kevin Wells</td>
      <td>Hernandez Rogers and Vang,</td>
      <td>Medicare</td>
      <td>37909.78241</td>
      <td>450</td>
      <td>Elective</td>
      <td>2020-12-18</td>
      <td>Ibuprofen</td>
      <td>Abnormal</td>
      <td>Andrew</td>
      <td>Watts</td>
      <td>2020</td>
      <td>November</td>
      <td>30 days</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Adrienne Bell</td>
      <td>43</td>
      <td>Female</td>
      <td>AB+</td>
      <td>Cancer</td>
      <td>2022-09-19</td>
      <td>Kathleen Hanna</td>
      <td>White-White</td>
      <td>Aetna</td>
      <td>14238.31781</td>
      <td>458</td>
      <td>Urgent</td>
      <td>2022-10-09</td>
      <td>Penicillin</td>
      <td>Abnormal</td>
      <td>Adrienne</td>
      <td>Bell</td>
      <td>2022</td>
      <td>September</td>
      <td>20 days</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.to_csv(r"C:\Users\Antonio\Desktop\Temp\health.csv", index=False)
```


```python

```


```python

```


```python

```
