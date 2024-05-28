# Patent-Fraud-Project

## Overview
This project focuses on detecting potential fraudulent activities by identifying similarities between company names using unstructured data analysis. The primary goal is to determine if patents are being transferred between main companies and their potential shell companies for tax benefits and regulatory protection.

## Description
The Python script uses regular expressions and string manipulation techniques to clean and compare company names from a dataset. It operates on a CSV file containing company names, cleaning unwanted characters and breaking down each name into components for detailed comparison.

## Features
- **Data Cleaning**: Removes punctuation and other non-essential characters from company names.
- **Name Comparison**: Splits names into words, converts them to lowercase, and compares them to identify matches or similarities.
- **Indicator Assignment**: Assigns indicators based on the type of match or mismatch found between two compared names, which helps in categorizing the type of relationship or discrepancy between the entities.

## Usage
1. Set the directory path where the CSV file is located.
2. Ensure the CSV file is named `final_sep1.csv` and is encoded in 'ISO-8859-1'.
3. Run the script to process the data. The script will output a new CSV file `Name_Matching6.csv` with an additional column 'Indicator' showing the result of the name comparisons.

