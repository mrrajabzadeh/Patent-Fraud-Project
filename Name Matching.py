# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 11:16:08 2023

@author: mraja
"""

import pandas as pd
import os
import re

# Set the working directory and load the CSV file into a pandas DataFrame
new_directory = r"C:\Users\mraja\OneDrive\Desktop\Name Matching\Sixth"
os.chdir(new_directory)
df = pd.read_csv('final_sep1.csv', encoding='ISO-8859-1')

# Create a new column to store the Indicators
df['Indicator'] = 1

def clean_word(word):
    # Clean unwanted characters from a word using regular expressions
    cleaned_word = re.sub(r'[(),/\'".?]', '', word)
    return cleaned_word if cleaned_word else None  # Return None if the cleaned word is empty

words_col1_lists = []
words_col2_lists = []

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Clean and split words in the 'clean_company' column
    words_col1 = [clean_word(w) for w in re.split(r'[ ]', row['clean_company']) if clean_word(w) is not None]
    # Clean and split words in the 'Alleged Infringer' column
    words_col2 = [clean_word(w) for w in re.split(r'[ ]', row['defendant_original_name']) if clean_word(w) is not None]

    # Convert words to lowercase for comparison
    words_col1_lower = [w.lower() for w in words_col1]
    words_col2_lower = [w.lower() for w in words_col2]
    
    words_col1_lists.append(words_col1_lower)
    words_col2_lists.append(words_col2_lower)
    
    matched = True
    
    # Sum the first and second words of either column
    if len(words_col1_lower) >= 2:
        col1_sum = ''.join(words_col1_lower[:2])
    if len(words_col2_lower) >= 2:
        col2_sum = ''.join(words_col2_lower[:2])    
    
    min_length = min(len(words_col1_lower), len(words_col2_lower))
    
        
    # Check for specific words in the first word of either column
    if words_col1_lower[0] in ['corp', 'inc', 'llc', 'sa', 'ltd', 'gmbh', 'ag', 'co', 'lp', 'na'] or words_col2_lower[0] in ['corp', 'inc', 'llc', 'sa', 'ltd', 'gmbh', 'ag', 'co', 'lp', 'na']:
        matched = False
        df.at[index, 'Indicator'] = 0
        
    # Check for first word starting with "us" in either column
    elif words_col1_lower[0].startswith('us') or words_col2_lower[0].startswith('us'):
        matched = False
        df.at[index, 'Indicator'] = 4
         
    # Check if the concatenated words match the first word of the other column
    elif col1_sum == words_col2_lower[0]:
        matched = False
        df.at[index, 'Indicator'] = 4
    elif col2_sum == words_col1_lower[0]:
        matched = False
        df.at[index, 'Indicator'] = 4
                
     # Check for dash in the first word of either column
    elif '-' in words_col1_lower[0]:
        words_col1_cleaned = words_col1_lower[0].replace('-', '')
        if words_col1_cleaned == words_col2_lower[0] or words_col1_cleaned == ''.join(words_col2_lower[:2]) or words_col1_cleaned == ''.join(words_col2_lower[:3]):
            matched = False
            df.at[index, 'Indicator'] = 1
        else:
            matched = False
            df.at[index, 'Indicator'] = 0
    elif '-' in words_col2_lower[0]:
        words_col2_cleaned = words_col2_lower[0].replace('-', '')
        if words_col2_cleaned == words_col1_lower[0] or words_col2_cleaned == ''.join(words_col1_lower[:2]) or words_col2_cleaned == ''.join(words_col1_lower[:3]):
            matched = False
            df.at[index, 'Indicator'] = 1
        else:
            matched = False
            df.at[index, 'Indicator'] = 0
      
    # Check matching of first words
    elif words_col1_lower[0] != words_col2_lower[0]:
        matched = False
        df.at[index, 'Indicator'] = 0
    
    if matched:
        for i in range(1, min_length):
            # Check for specific words in both columns
            if (words_col1_lower[i] in ['corp', 'inc', 'llc', 'sa', 'ltd', 'gmbh', 'ag', 'co', 'lp','na']) or (words_col2_lower[i] in ['corp', 'inc', 'llc', 'sa', 'ltd', 'gmbh', 'ag', 'co', 'lp','na']):
                if words_col1_lower[i] != words_col2_lower[i]:
                    df.at[index, 'Indicator'] = 2
                    break
            
            # Check matching of remaining words
            elif words_col1_lower[i] != words_col2_lower[i]:
                df.at[index, 'Indicator'] = 3
                break
            

# Save the modified DataFrame to a new CSV file
df.to_csv('Name_Matching6.csv', index=False)
