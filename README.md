## **Heart Disease Prediction using Random Forest Algorithm**

### Overview

This project is a web application built using Flask, a Python micro web framework. It uses the Random Forest Algorithm to predict the likelihood of heart disease in patients based on their medical history and test results.

### Dataset Features

The dataset used for this project includes the following features:

- **Age**: The age of the patient.
- **Sex**: The sex of the patient (Male/Female).
- **Chest Pain Type**: The type of chest pain experienced by the patient:
  - Angina
  - Acute coronary syndrome
  - Pericarditis
  - Aortic dissection
- **Blood Pressure**: The resting blood pressure of the patient.
- **Cholestoral**: The cholesterol level of the patient.
- **Fasting Blood Sugar**: Whether the patient has fasting blood sugar (Yes/No).
- **Electrocardiographic**: The results of electrocardiographic tests:
  - Resting ECG
  - Holter monitoring
  - Stress ECG
- **Heart Rate**: The maximum heart rate achieved.
- **Angina**: Whether the patient has angina (Yes/No).
- **Oldpeak**: The old peak value:
  - OP < 0.1 mm
  - 0.1 mm ≤ OP < 0.5 mm
  - 0.5 mm ≤ OP < 1.0 mm
  - 1.0 mm ≤ OP < 1.5 mm
  - 1.5 mm ≤ OP < 2.0 mm
  - 2.0 mm ≤ OP < 2.5 mm
  - OP ≥ 2.5 mm
- **ST Segment Slope**: The ST segment slope:
  - Upsloping
  - Flat
  - Downsloping
- **Coronary angiography**: The results of coronary angiography:
  - Stenosis Severity
  - Lesion Length
  - Thrombus Burden
  - Collateral Circulation
- **Thalassemia**: The type of thalassemia:
  - Alpha thalassemia
  - Beta thalassemia
  - Thalassemia trait
  - Cooley's anemia

### Installation

To run the application, follow these steps:

#### Step 1: Create a Virtual Environment

Open your terminal or command prompt and navigate to the project directory. Run the following command to create a new virtual environment:

```bash
python -m venv venv
```

#### Step 2: Activate the Virtual Environment

Activate the virtual environment by running the following command:

```bash
.\venv\Scripts\activate.bat
```

On Unix/Linux systems, use the following command:

```bash
source venv/bin/activate
```

#### Step 3: Install Dependencies

Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

#### Step 4: Run the Application

Run the application by executing the following command:

```bash
python app.py
```

### Usage

Once the application is running, open a web browser and navigate to `http://localhost:5000`. The application's homepage will display a form with fields for inputting patient data.

Enter the patient's data into the form fields and submit the form to generate a prediction.

### Algorithm

This project uses the Random Forest Algorithm to predict the likelihood of heart disease. The algorithm is trained on a dataset of patient records and uses the features listed above to make predictions.

### Mapping Strings to Numerical Values

To preprocess the data, we map the string values to numerical values. The mapping is as follows:

- **Chest Pain Type**:
  - Angina: 0
  - Acute coronary syndrome: 1
  - Pericarditis: 2
  - Aortic dissection: 3
- **Electrocardiographic**:
  - Resting ECG: 0
  - Holter monitoring: 1
  - Stress ECG: 2
- **Oldpeak**:
  - OP < 0.1 mm: 0
  - 0.1 mm ≤ OP < 0.5 mm: 1
  - 0.5 mm ≤ OP < 1.0 mm: 2
  - 1.0 mm ≤ OP < 1.5 mm: 3
  - 1.5 mm ≤ OP < 2.0 mm: 4
  - 2.0 mm ≤ OP < 2.5 mm: 5
  - OP ≥ 2.5 mm: 6
- **ST Segment Slope**:
  - Upsloping: 0
  - Flat: 1
  - Downsloping: 2
- **Thalassemia**:
  - Alpha thalassemia: 0
  - Beta thalassemia: 1
  - Thalassemia trait: 2
  - Cooley's anemia: 3

### Notes

- This project uses a simple dataset for demonstration purposes only. The accuracy of the predictions may not be reliable with this dataset.
- In a real-world application, a larger and more diverse dataset would be necessary for accurate predictions.
- This project does not include any error handling or validation for user input. In a real-world application, these features would be essential for ensuring the accuracy and reliability of the predictions.
