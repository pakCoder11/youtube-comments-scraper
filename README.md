# YouTube Comments Scraper

## Overview
The YouTube Comments Scraper is a Python-based tool designed to extract comments from YouTube videos using browser automation. It utilizes the `selenium-driverless` library for headless browsing and `pyautogui` for smooth automation on Windows OS, enabling the collection of large volumes of comments without requiring the YouTube Data API.

## Features
- Scrapes comments and replies from a specified YouTube video.
- Handles large-scale comment extraction through automation.
- Exports comments to CSV format.
- No API key required; relies entirely on browser automation.
- Configurable to scroll and load dynamic comments on YouTube pages.

## Prerequisites
- Windows OS
- Python 3.8+
- Chrome browser (for compatibility with `selenium-driverless`)
- Required Python packages (listed in `requirements.txt`):
  - `selenium-driverless`
  - `pyautogui`
  - `pandas` (for CSV export)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/youtube-comments-scraper.git
   cd youtube-comments-scraper
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure Chrome browser is installed on your Windows system.

## Output
- The script generates a `Youtube-comments-data.xlsx` file with the following fields:
  - `username`: Unique ID of the comment (if available).
  - `comment`: Comment text.
  - `time`: Timestamp of the comment (if available).

## Notes
- The script uses `selenium-driverless` for headless Chrome automation, which may require a stable internet connection to load comments dynamically.
- `pyautogui` ensures smooth automation on Windows but may require adjustments for screen resolution or system performance.
- Be mindful of YouTube's terms of service when scraping large amounts of data.
- Performance may vary depending on the number of comments and system resources.
