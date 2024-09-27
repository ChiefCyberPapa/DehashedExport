# DehashedExport
This Python script uses the Dehashed API to retrieve a list of email addresses associated with a specific domain. It exports the results into a CSV file. The script also includes color-coded prompts for user input and a friendly success message. This has only been tested in Linux.

## Prerequisites

You must have an API key purchses from dehashed.com to interface with their API. Before using this script, ensure you have the following prerequisites installed:

1. **Python 3.x**: You need Python 3.x to run this script. You can check if Python is installed on your system by running:

   ```bash
   python3 --version

   If Python is not installed, install it using the following command for Ubuntu/Debian-based systems:

   ```bash
   sudo apt update

   ```bash
   sudo apt install python3 python3-pip


2. This script uses the colorama package to display colored text in the terminal. Install it by running:

   ```bash
   pip3 install colorama

## Installation

1. Open the terminal and navigate to the directory where you want to store the script.

2. Use the git clone command to clone the repository:

   ```bash
   git clone https://github.com/ChiefCyberPapa/DehashedExport.git

4. Navigate to the cloned directory:

   ```bash
   cd DehashedExport
   
## Usage

1. To run the script, follow these steps:

    In the terminal, navigate to the directory where the script is stored:

   ```bash

    cd path_to_directory/DehashedExport

2. Run the Python script:

   ```bash

    python3 DehashedExport.py

3. The script will prompt you to input the following details:

    Email associated with your Dehashed API key.
    Your Dehashed API key.
    The domain you wish to search (e.g., example.com).

4. Once the script retrieves the data, it will automatically export the results into a CSV file named dehashed_results_<domain>.csv.

5. After successful completion, you will see a friendly message:

   Wow...that was easy!

   Thank you for using the DehashedExport script, used to dump a list of emails by domain from Dehashed.com.

   You can buy me a coffee if you like this or send complaints and improvements to ChiefCyberPapa@proton.me.

6. Use the exported CSV and compare it with a list of emails you have compiled as a CSV with the DehashedCompare tool found here: https://github.com/ChiefCyberPapa/DehashedCompare/tree/main
