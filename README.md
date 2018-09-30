# Project HeartBeat

***This repository contains the code for the project "Project HeartBeat". This project contains three main parts:***

## 1. User Information:

In this step, the user is first asked to enter their Name, Gender [M/F] and Age. As the user submits this information, this information is stored in a text file for the current user. This information is later used in the last step to generate user's "Medical Report".

## 2. Collect User Heart Rate Data:

In this step, the user clicks on the "Start Reading Data" Button which starts reading the data from the "PulseSensor" connected to Arduino and to laptop over Serial Port. The button press triggers two functions:

**a) save_and_plot:** In this, the data is collected for upto 3 to 4 minutes and is saved into a CSV file along with Timestamp. Then we pre-process the data using Pandas to provide column names and organize the data in a better way. 

**b) plotHeartBeat:** Once the data collection is complete, this function is called to load the data from the CSV file and a Heart Rate plot is generated for the user and saved as a png file.

## 3. Get User Data Analytics:

In this step, the user clicks on the "Get Data Summary" button which in turn invokes three functions:

**a) getUserImage:** In this, we use OpenCV to take an image of the user whose data is being collected and crop and resize it according to our report requirements. This image is saved and is used to personalize the user Helth Report.

**b) get_data_analytics:** In this, we read the data using Pandas as a DataFrame. This data has two features: "Heart_Rate" and "Time". We read in the "Heart_Rate" data and find the rolling mean average of the heart rate data and plot it. Along with this, we find the peaks between two heart rate plots, the difference between which gives us the "Beats per Minute". We take in the data for all the peaks in the plot of heart rate data and find the "Average Beats per Minute" using that.

**c) save_report:** In this, we take all the data that we have collected till now i.e. Name, Age, Gender, user Image, Current Date, Average BPM, Heart Rate ECG plots, Heart Rate plots with moving averages and peaks and generate a single Medical Report for the user as a PDF file.

# Requirements:

**1. Python 3.5 or above**

**2. OpenCV [latest]**

**3. Flask**
```
pip3 install flask
```

**4. Numpy**
```
pip3 install numpy
```

**5. Pandas**
```
pip3 install pandas
```

**6. Matplotlib**
```
pip3 install matplotlib
```

**7. Serial**
```
pip3 install -U pySerial
```

**8. ReportLab**
```
pip3 install reportlab
```

# Results

**1. Flask Dashboard:**

![Output a1](Images/flask-page.png?raw=true "Output a1")

**2. Heart Rate Reading and it's Plot:**

![Output a1](Images/sample_heartRate.png?raw=true "Output a1")

**3. Data Analysis:**

![Output a1](Images/sample_user_cropped_image.png?raw=true "Output a1")

**4. Final PDF Report:**

You can download or view the sample generated PDF report [here](https://github.com/AashiDutt/Project_HeartBeat/blob/master/Images/sample_report.pdf).
