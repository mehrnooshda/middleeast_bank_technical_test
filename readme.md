# Data Pipeline Documentation
This documentation provides an overview of the data pipeline designed to collect, process, and store investment fund data. The pipeline gathers daily information from the Fipiran API endpoint, stores the raw data in a data lake, and transforms it into a structured format suitable for analysis. The pipeline is implemented using Python.

## Table of Contents
1. [Project Structure](#Project Structure)
2. [Dependencies](#Dependencies)
3. [Usage](#Usage)
4. [Configuration](#Configuration)
5. [Contributing](#Contributing)

## Project Structure
The project consists of the following files:
```
├── app
│   └── data_gatherer.py
│   └── daily_pipeline.py
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```
* `app/data_gatherer.py`: Contains functions for gathering and processing data.
* `main.py`: Entry point of the application, runs the data pipeline.
* `app/daily_pipeline.py`: Configuration file for Apache Airflow (unfinished).
* `README.md`: Documentation file (you are currently reading it!).
* `requirements.txt`: List of project dependencies.
* `.gitignore`: Specifies files and directories to be ignored by Git.
## Dependencies
To run the data pipeline, ensure that you have the following dependencies installed:

* certifi==2023.5.7
* charset-normalizer==3.1.0
* idna==3.4
* requests==2.31.0
* urllib3==2.0.3
* pandas==1.3.1

You can install the dependencies by running the following command:

```
pip install -r requirements.txt
```
## Usage
To execute the data pipeline, follow these steps:

1. Clone the project repository.
2. Install the project dependencies as mentioned in the Dependencies section.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the following command:
`python main.py`

The pipeline will perform the following steps:


1. Gather daily investment fund information from the Fipiran API endpoint.

    * The API endpoint URL: `https://fund.fipiran.ir/api/v1/fund/fundcompare`

    * The gathered data will be stored in its raw format.
2. Transform the raw data into a structured format suitable for analysis.

    * Extract relevant information from the response JSON (columns: 'regNo', 'name').
    * Save the extracted data as a CSV file named 'raw_data.csv'.
3. Print or process the extracted fund information as needed.

## Configuration
The project includes an unfinished configuration file named `daily_pipeline.py`, which is intended for configuring Apache Airflow. However, this file is not fully completed due to time constraints.

To configure and use Apache Airflow with the data pipeline, please refer to the official Apache Airflow documentation for detailed instructions.

## Contributing
If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the project's GitHub repository.



