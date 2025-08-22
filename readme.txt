**README.TXT**

Heart Disease Prediction using Random Forest Algorithm
=====================================================

Overview
--------

This project is a web application built using Flask, a Python micro web framework. It uses the Random Forest Algorithm to predict the likelihood of heart disease in patients based on their medical history and test results.

Installation and Usage
--------------------

1.  Create a virtual environment by running the command `python -m venv venv` in your terminal or command prompt.
2.  Activate the virtual environment by running the command `.\venv\Scripts\activate` (on Windows) or `source venv/bin/activate` (on Unix/Linux systems).
3.  Install the required dependencies by running the command `pip install -r requirements.txt.
4.  Run the application by executing the command `python app.py`.
5.  Open a web browser and navigate to `http://localhost:5000` to access the application's homepage.

Troubleshooting
--------------

For help with installation or usage issues, refer to the detailed instructions in the INSTALLATION section of the README.md file.

Algorithm and Mapping
---------------------

The Random Forest Algorithm is used to predict the likelihood of heart disease. The algorithm is trained on a dataset of patient records and uses the following features:

*   Chest Pain Type
*   Electrocardiographic
*   Oldpeak
*   ST Segment Slope
*   Thalassemia

String values are mapped to numerical values as follows:

*   Chest Pain Type:
	*   Angina: 0
	*   Acute coronary syndrome: 1
	*   Pericarditis: 2
	*   Aortic dissection: 3
*   Electrocardiographic:
	*   Resting ECG: 0
	*   Holter monitoring: 1
	*   Stress ECG: 2
*   Oldpeak:
	*   OP < 0.1 mm: 0
	*   0.1 mm ≤ OP < 0.5 mm: 1
	*   0.5 mm ≤ OP < 1.0 mm: 2
	*   1.0 mm ≤ OP < 1.5 mm: 3
	*   1.5 mm ≤ OP < 2.0 mm: 4
	*   2.0 mm ≤ OP < 2.5 mm: 5
	*   OP ≥ 2.5 mm: 6
*   ST Segment Slope:
	*   Upsloping: 0
	*   Flat: 1
	*   Downsloping: 2
*   Thalassemia:
	*   Alpha thalassemia: 0
	*   Beta thalassemia: 1
	*   Thalassemia trait: 2
	*   Cooley's anemia: 3

Note
----

*   This project uses a simple dataset for demonstration purposes only. The accuracy of the predictions may not be reliable with this dataset.
*   In a real-world application, a larger and more diverse dataset would be necessary for accurate predictions.
*   This project does not include any error handling or validation for user input. In a real-world application, these features would be essential for ensuring the accuracy and reliability of the predictions.