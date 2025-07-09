import json
import pandas as pd
import re
import os

def clean_data(df):
    # Drop rows where all values are null
    cleaned_df = df.dropna()

    return cleaned_df

    # Save the cleaned DataFrame to a file
    # cleaned_df.to_excel(output_file, index=False)  # Change the filename and format as needed

def store_to_json(dict_data, file_path):
    # Open the file in append mode
    with open(file_path, 'a') as f:
        # Use json.dump to write the dictionary to the file
        json.dump(dict_data, f)
        # Write a newline character after each dictionary
        f.write('\n')

def read_dicts_from_json(file_path):
    dicts = []
    with open(file_path, 'r') as f:
        for line in f:
            dicts.append(json.loads(line))
    return dicts


def json_to_excel(json_file_path, excel_file_path):
    # Read the JSON file into a DataFrame
    df = pd.read_json(json_file_path, lines=True)

    # Write the DataFrame to an Excel file
    df.to_excel(excel_file_path, index=False)


def data_storage(main_list):
    # Convert list of lists into a single list
    single_list = [item for sublist in main_list for item in sublist]
    
    # Create a DataFrame from the list
    df = pd.DataFrame(single_list)
    # main_df = clean_data(df)
    
    # Save the DataFrame to an Excel file
    df.to_excel('insta-viral-posts-data.xlsx', index=False)

def save_data_to_excel(output_file_name):

    # Check if data.json exists and is not empty
    if os.path.exists("data.json") and os.path.getsize("data.json") > 0:
        with open('data.json', 'r') as f:
            data = [json.loads(line) for line in f.readlines()]

        # Create a DataFrame from the data
        df = pd.DataFrame(data)

        # Save the DataFrame to an Excel file
        df.to_excel(output_file_name, index=False)

        # Delete the original data.json file
        os.remove("data.json")

    else:
        print("data.json does not exist or is empty.")




# Your main_list

# Call the function with your main_list
# data_storage(main_list)

# for i in range(0,100):
#     store_to_json(dict1,'data.json')

# json_to_excel('data.json','data.xlsx')
    

def url_cleaners():
    # Define a regular expression pattern for URLs
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    # Open the input file and the output file
    with open('data.txt', 'r', encoding='utf-8') as infile, open('output.txt', 'w',encoding='utf-8') as outfile:
        for line in infile:
            # If the line is blank, write 'NaN' to the output file
            if line.strip() == '':
                outfile.write('NaN\n')
            else:
                # Remove URLs from the line and write it to the output file
                cleaned_line = re.sub(url_pattern, '', line)
                outfile.write(cleaned_line)


def process_social_links():
    # Read the Excel file
    df = pd.read_excel('New Arrival main file.xlsx')

    # Create new columns for each social media platform
    platforms = ['Instagram', 'Linkedin', 'Youtube', 'TikTok', 'Facebook', 'Twitter', 'Snapchat']
    for platform in platforms:
        df[platform + ' URL'] = None

    # Process the 'Social Links' column
    for i, link in enumerate(df['Social Links']):
        if pd.isnull(link):
            continue
        for platform in platforms:
            if platform.lower() in link.lower():
                df.loc[i, platform + ' URL'] = link

    # Save the DataFrame to a new Excel file
    df.to_excel('output.xlsx', index=False)

# Call the function
# process_social_links()

# Call the function
# Call the function
# url_cleaner()
# D = read_dicts_from_json('data.json')
# data_storage(D)
# url_cleaners() #clean the txt 
# process_social_links()

# save_data_to_excel('Instagram Business Data1.xlsx') 