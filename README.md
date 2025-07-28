# Spotify Historycal Data Visualization Project
- **This is all my data listening history**
A comprehensive Python-based toolkit for analyzing and visualizing personal Spotify streaming history data. This project provides multiple approaches to explore your music listening patterns through interactive dashboards, static visualizations, and data search capabilities.

## 📊 Project Overview

This repository contains a collection of Python scripts designed to transform raw Spotify streaming data (JSON format) into meaningful insights and beautiful visualizations.  The project offers three main approaches to data analysis:

1. **Interactive Web Applications** - Streamlit dashboard and Panel-based search interface
2. **Static Visualizations** - Matplotlib and Seaborn charts with enhanced aesthetics  
3. **Interactive Plots** - Plotly-powered charts with hover functionality and zoom capabilities

The analysis focuses on temporal patterns, artist preferences, track popularity, and listening behavior across different time periods. All scripts are designed to work with Spotify's official data export format, making it easy to analyze your personal listening history.

## 🚀 Features

- **Multi-format Visualization Support**: Static plots (Matplotlib/Seaborn), interactive charts (Plotly), and web dashboards (Streamlit)
- **Temporal Analysis**: Monthly listening trends, daily patterns, and yearly comparisons
- **Artist & Track Analytics**: Top artists and tracks by listening time with detailed breakdowns
- **Interactive Filtering**: Year-based filtering and artist search capabilities
- **Data Export**: CSV export functionality for further analysis
- **Enhanced Aesthetics**: Multiple color schemes and improved visual design
- **Responsive Design**: Web-based dashboards that work across devices

## 📋 Requirements

```python
pandas
matplotlib
seaborn
plotly
streamlit
panel
mplcursors
json
os
```

## 📁 File Structure and Functionality

### Core Visualization Scripts


#### `dmain.py` - Comprehensive Data Visualization Suite

The primary visualization script that creates a complete set of static and interactive charts for Spotify data analysis. This script serves as the foundation for understanding your listening patterns through multiple visualization types.

**Key Visualizations Created:**
- **Monthly Listening Time Series**: A line plot showing total listening hours per month over time, helping identify seasonal patterns and long-term trends in your music consumption
- **Daily Listening Heatmap**: A color-coded matrix displaying listening intensity across days of the week and hours of the day, revealing your daily listening habits
- **Monthly Activity Heatmap**: An annual overview showing total listening hours for each month, useful for identifying peak listening periods throughout the year
- **Top 30 Tracks Bar Chart**: Horizontal bar chart ranking your most-played tracks by total listening time
- **Top 50 Artists Bar Chart**: Similar ranking for artists, showing your musical preferences and loyalty patterns
- **Interactive Artist Scatter Plot**: A Plotly-powered scatter plot of your top 101 artists with hover functionality, color-coded by listening time using the viridis color scheme

**Technical Implementation:**
The script processes JSON files from your Spotify data export, converts timestamps to datetime objects, and calculates listening time in hours. It uses seaborn's "whitegrid" style for consistent aesthetics across matplotlib plots, while the interactive scatter plot leverages Plotly Express for enhanced user interaction.

#### `gmain.py` - Enhanced Visualization with Interactive Features

An improved version of `dmain.py` that focuses on visual aesthetics and interactivity. This script represents the evolution of the basic visualization approach, incorporating advanced styling and user interaction capabilities.

**Enhanced Features:**
- **Improved Color Schemes**: Utilizes sophisticated color palettes including plasma, magma, coolwarm, and viridis for better visual appeal and data distinction
- **Interactive Tooltips**: Implements mplcursors for hover functionality on matplotlib plots, providing detailed information when hovering over data points
- **Enhanced Typography**: Improved font sizes, weights, and positioning for better readability
- **Artist Name Annotations**: Strategically positioned artist names on scatter plots with intelligent placement algorithms to avoid overlap
- **Advanced Styling**: Dark backgrounds for contrast, custom grid settings, and optimized layout parameters

**Unique Visualizations:**
The script creates the same core visualizations as `dmain.py` but with significant aesthetic improvements. The scatter plot includes artist name labels positioned using conditional logic to ensure readability, and the color schemes are specifically chosen to enhance data interpretation and visual appeal.

#### `gapp.py` - Interactive Streamlit Dashboard

A modern web-based dashboard built with Streamlit that provides an intuitive interface for exploring your Spotify data. This application represents the most user-friendly approach to data analysis in the repository.

**Dashboard Components:**
- **Header Section**: Clean title with musical note emoji and professional styling
- **Interactive Sidebar**: Multi-select year filter allowing users to focus on specific time periods
- **Top Artists Chart**: Dynamic horizontal bar chart that updates based on selected filters
- **Listening Patterns Heatmap**: Interactive heatmap showing listening activity by day of week and hour, with hover tooltips displaying exact values

**User Experience Features:**
The dashboard automatically updates all visualizations when filters are changed, providing real-time data exploration. The interface is responsive and works well on both desktop and mobile devices. All charts are built with Plotly, ensuring smooth interactions and professional appearance.

**Technical Architecture:**
The application loads JSON data on startup, processes it into a pandas DataFrame, and maintains state across user interactions. The filtering system is implemented using Streamlit's multiselect widget, which triggers automatic recomputation of visualizations when selections change.

#### `appsearch2.py` - Artist Search and Export Tool

A specialized Panel-based web application designed for searching and exporting specific artist data from your Spotify listening history. This tool is particularly useful for detailed analysis of individual artists or for creating custom datasets.

**Core Functionality:**
- **Artist Search Interface**: Text input field with case-insensitive and partial matching capabilities
- **Real-time Results**: Instant display of search results in a tabular format
- **Data Export**: One-click CSV export functionality for filtered results
- **Error Handling**: Comprehensive error messages for empty results or invalid searches

**Search Algorithm:**
The search functionality uses pandas string methods to perform case-insensitive partial matching on artist names. Results are automatically grouped by track name and aggregated by total listening time, providing a clean summary of the artist's tracks in your listening history.

**Export Features:**
When exporting data, the application creates CSV files with the naming convention "{artist}_listening_history.csv", making it easy to organize and identify exported datasets. The export includes all relevant metadata such as track names, album information, and calculated listening hours.

### Supporting Scripts

#### `main.py`, `main0.py`, `main2.py`, `main3.py`

These files represent various iterations and experimental versions of the core visualization scripts. They contain similar functionality to `dmain.py` and `gmain.py` but may include different styling approaches, alternative visualization types, or experimental features.

**Common Features Across Scripts:**
- JSON data loading and preprocessing
- Time-based feature extraction (hour, day of week, month, year)
- Conversion from milliseconds to hours for listening time
- Basic visualization creation using matplotlib and seaborn
- Data aggregation and grouping operations

These scripts serve as development versions and alternative implementations, allowing users to experiment with different visualization approaches or to understand the evolution of the project's codebase.

## 📈 Visualization Gallery

The following section describes the key visualizations created by the scripts, with references to the provided screenshots that demonstrate the actual output.


### Interactive Artist Analysis - Top 101 Artists Scatter Plot

**Generated by:** `dmain.py` or `gmain.py`  
**Screenshot Reference:** `Screenshot2025-07-01at16.41.40.png` and `Screenshot2025-07-01at16.41.29.png`

This sophisticated scatter plot represents one of the most comprehensive visualizations in the project, displaying your top 101 artists ranked by total listening time. The visualization demonstrates the power of interactive data exploration through several key features:

**Visual Design Elements:**
- **X-axis**: Hours played (ranging from 0 to 100+ hours)
- **Y-axis**: Artist names, arranged vertically for easy reading
- **Color Coding**: Viridis color scale representing listening intensity, with darker colors indicating higher listening times
- **Interactive Tooltips**: Hover functionality revealing exact listening hours and artist names

**Data Insights Revealed:**
The scatter plot clearly shows the distribution of listening preferences, with classical composers like Johann Sebastian Bach and Pyotr Ilyich Tchaikovsky appearing as top artists with over 100 hours of listening time. The visualization reveals a long tail distribution typical of music listening habits, where a small number of artists account for a large portion of total listening time.

**Technical Implementation:**
Created using Plotly Express, this visualization leverages the library's interactive capabilities to provide smooth zooming, panning, and hover interactions. The color scale is carefully chosen to provide clear visual distinction between different listening levels while maintaining aesthetic appeal.

### Streamlit Dashboard - Comprehensive Listening Analysis

**Generated by:** `gapp.py`  
**Screenshot Reference:** `Screenshot2025-07-01at16.44.35.png`

The Streamlit dashboard represents the pinnacle of user-friendly data exploration in this project. The interface combines multiple visualization types into a cohesive, interactive experience that allows for real-time data filtering and analysis.

**Dashboard Layout and Components:**

**Header Section:**
The dashboard opens with a clean, professional header featuring the title "🎵 Spotify Streaming History Dashboard" that immediately communicates the purpose and adds visual appeal through the musical note emoji.

**Interactive Filters Panel:**
Located in the sidebar, the filters section provides year-based data filtering with a multi-select interface. Users can choose from years 2012 through 2023, allowing for focused analysis of specific time periods. The interface shows selected years as colored tags (2018, 2020, 2022, 2023, 2019, 2013, 2014, 2021, 2017, 2015, 2016, 2012), demonstrating the comprehensive nature of the dataset.

**Top 10 Artists Visualization:**
The main content area features a horizontal bar chart displaying the top 10 artists by listening time. The chart shows:
- **Pyotr Ilyich Tchaikovsky**: Leading with approximately 100+ hours
- **Johann Sebastian Bach**: Close second with similar listening time
- **Vangelis**: Significant listening time in the 60-80 hour range
- **Cocteau Twins**: Moderate listening time
- **Ludwig van Beethoven**: Classical music representation
- **Depeche Mode**: Electronic/alternative music presence
- **Moby**: Electronic music representation
- **U2**: Rock music inclusion
- **Groove Armada**: Electronic/dance music
- **Wolfgang Amadeus Mozart**: Classical music completion

**Listening Patterns Heatmap:**
Below the artist chart, the dashboard displays a sophisticated heatmap showing listening patterns across different dimensions:
- **Y-axis**: Days of the week (Monday through Friday visible)
- **X-axis**: Time periods or hours
- **Color Scale**: Intensity from 0 to 100 using a viridis-style color scheme
- **Interactive Elements**: Hover tooltips and zoom capabilities

**User Experience Design:**
The dashboard demonstrates excellent UX principles through its clean layout, intuitive navigation, and responsive design. The color scheme is consistent across all elements, and the spacing provides clear visual separation between different components.

### Temporal Analysis Visualizations

**Generated by:** Multiple scripts (`dmain.py`, `gmain.py`, `main.py` variations)

While not directly shown in the provided screenshots, the codebase reveals several temporal analysis visualizations that provide crucial insights into listening behavior over time:

**Monthly Listening Time Series:**
This visualization tracks total listening hours across months, revealing seasonal patterns and long-term trends. The implementation includes:
- Line plots with enhanced styling using seaborn themes
- Custom tick labels showing month/year combinations
- Value annotations for peak listening periods
- Color gradients reflecting listening intensity

**Daily Activity Heatmaps:**
These heatmaps reveal when you're most likely to listen to music throughout the week and day:
- 7x24 grid showing days of week versus hours of day
- Color intensity representing listening activity
- Clear identification of peak listening times
- Weekend versus weekday pattern analysis

**Annual Overview Heatmaps:**
Yearly summaries showing listening patterns across months:
- 12-month overview with total hours per month
- Year-over-year comparison capabilities
- Seasonal trend identification
- Holiday and vacation period analysis

## 🛠️ Installation and Setup

### Prerequisites

Ensure you have Python 3.7 or higher installed on your system. The project has been tested with Python 3.8+ for optimal compatibility.

### Required Libraries Installation

```bash
pip install pandas matplotlib seaborn plotly streamlit panel mplcursors
```

### Spotify Data Export Setup

1. **Request Your Data**: Visit [Spotify Privacy Settings](https://www.spotify.com/account/privacy/) and request your extended streaming history
2. **Download Process**: Spotify will email you when your data is ready (typically 5-30 days)
3. **File Preparation**: Extract the downloaded ZIP file and locate the JSON files containing your streaming history
4. **Directory Setup**: Create a directory structure and place your JSON files in a folder accessible to the scripts

### Configuration

Update the `json_dir` variable in each script to point to your Spotify data directory:

```python
json_dir = '/path/to/your/spotify/data/'
```


## 🚀 Usage Instructions

### Running the Streamlit Dashboard

The most user-friendly way to explore your data is through the Streamlit dashboard:

```bash
streamlit run gapp.py
```

This will launch a web browser with the interactive dashboard where you can:
- Filter data by year using the sidebar controls
- Explore top artists through the interactive bar chart
- Analyze listening patterns via the heatmap visualization
- Export specific views or data subsets

### Generating Static Visualizations

For comprehensive static analysis, run the main visualization script:

```bash
python dmain.py
```

This will generate multiple matplotlib/seaborn plots including:
- Time series analysis of monthly listening trends
- Heatmaps showing daily and monthly listening patterns
- Bar charts for top tracks and artists
- Interactive Plotly scatter plot for detailed artist analysis

### Enhanced Visualizations with Interactivity

For improved aesthetics and interactive features:

```bash
python gmain.py
```

This enhanced version provides:
- Superior color schemes and visual design
- Interactive tooltips using mplcursors
- Artist name annotations on scatter plots
- Improved typography and layout

### Artist Search and Data Export

To search for specific artists and export their data:

```bash
python appsearch2.py
```

This launches a Panel-based web application where you can:
- Search for artists using partial name matching
- View filtered results in real-time
- Export artist-specific data to CSV files
- Perform bulk data extraction for multiple artists

## 📊 Data Format and Structure

### Input Data Requirements

The scripts expect Spotify JSON data files with the following structure:

```json
{
  "ts": "2023-01-01T12:00:00Z",
  "ms_played": 240000,
  "master_metadata_track_name": "Track Name",
  "master_metadata_album_artist_name": "Artist Name",
  "master_metadata_album_album_name": "Album Name"
}
```

### Key Data Fields Processed

- **ts**: Timestamp of when the track was played
- **ms_played**: Duration listened in milliseconds
- **master_metadata_track_name**: Track title
- **master_metadata_album_artist_name**: Artist name
- **master_metadata_album_album_name**: Album name

### Data Processing Pipeline

1. **JSON Loading**: All JSON files in the specified directory are loaded and concatenated
2. **Timestamp Conversion**: String timestamps are converted to pandas datetime objects
3. **Duration Calculation**: Milliseconds are converted to hours for easier interpretation
4. **Feature Extraction**: Time-based features (hour, day of week, month, year) are extracted
5. **Data Aggregation**: Listening data is grouped by various dimensions for analysis
6. **Filtering and Cleaning**: Invalid or incomplete records are removed

## 🎨 Customization Options

### Color Scheme Modifications

The scripts use various color palettes that can be easily customized:

```python
# In gmain.py - modify color schemes
cmap='plasma'  # Options: viridis, plasma, magma, coolwarm
palette="coolwarm"  # Seaborn palette options
color_continuous_scale='viridis'  # Plotly color scales
```

### Visualization Parameters

Key parameters that can be adjusted:

```python
# Figure sizes
plt.figure(figsize=(12, 8))

# Font sizes
fontsize=14, fontweight='bold'

# Number of top items to display
top_tracks = df.groupby('track_name')['hours_played'].sum().nlargest(30)
top_artists = df.groupby('artist_name')['hours_played'].sum().nlargest(50)
```

### Dashboard Customization

Streamlit dashboard elements can be modified:

```python
# Page configuration
st.set_page_config(page_title="Your Custom Title")

# Sidebar styling
st.sidebar.header("Custom Filter Title")

# Chart titles and labels
fig.update_layout(title="Your Custom Chart Title")
```

## 📈 Advanced Analytics Features

### Statistical Analysis

The scripts provide several statistical insights:
- **Listening Distribution**: Analysis of how listening time is distributed across artists and tracks
- **Temporal Patterns**: Identification of peak listening hours, days, and months
- **Diversity Metrics**: Calculation of musical diversity through artist and genre distribution
- **Trend Analysis**: Long-term trends in listening behavior and preferences

### Export Capabilities

Multiple export formats are supported:
- **CSV Export**: Detailed listening data for further analysis
- **Image Export**: High-resolution plots for presentations or reports
- **Interactive HTML**: Plotly charts can be saved as standalone HTML files

### Performance Optimization

For large datasets, the scripts include optimization features:
- **Efficient Data Loading**: Pandas optimizations for large JSON files
- **Memory Management**: Chunked processing for very large datasets
- **Caching**: Streamlit caching for improved dashboard performance

## 🔧 Troubleshooting

### Common Issues and Solutions

**Issue**: "FileNotFoundError: No JSON files found"
**Solution**: Verify the `json_dir` path is correct and contains Spotify JSON files

**Issue**: "Memory Error when loading data"
**Solution**: Process files in smaller batches or increase system memory

**Issue**: "Empty visualizations or no data"
**Solution**: Check that JSON files contain valid streaming data with required fields

**Issue**: "Streamlit dashboard not loading"
**Solution**: Ensure all required libraries are installed and ports are available

### Data Quality Checks

The scripts include several data validation steps:
- Verification of required JSON fields
- Removal of tracks with zero or negative play time
- Handling of missing artist or track information
- Timezone conversion for accurate temporal analysis

## 🤝 Contributing

This project welcomes contributions in several areas:

### Enhancement Opportunities

- **Additional Visualization Types**: New chart types or analysis methods
- **Performance Improvements**: Optimization for larger datasets
- **UI/UX Enhancements**: Improved dashboard design and user experience
- **Export Features**: Additional export formats or data processing options

### Code Quality

- **Documentation**: Improved code comments and documentation
- **Testing**: Unit tests for data processing functions
- **Error Handling**: More robust error handling and user feedback
- **Code Organization**: Refactoring for better modularity and reusability

## 📄 License

This project is open source and available under the MIT License. Feel free to use, modify, and distribute the code according to the license terms.

## 🙏 Acknowledgments

- **Spotify**: For providing comprehensive data export capabilities
- **Python Community**: For the excellent libraries that make this analysis possible
- **Visualization Libraries**: Matplotlib, Seaborn, and Plotly for powerful charting capabilities
- **Web Frameworks**: Streamlit and Panel for enabling interactive web applications

## 📞 Support

For questions, issues, or suggestions:
- Review the troubleshooting section above
- Check existing issues in the repository
- Create a new issue with detailed information about your problem
- Include sample data (anonymized) and error messages when reporting bugs

---

**Author**: Roberto with prompt assistance from Manus AI  
**Last Updated**: January 2025  
**Version**: 1.0.0

This README provides comprehensive documentation for the Spotify Data Visualization Project. The combination of static visualizations, interactive dashboards, and data export capabilities makes this toolkit suitable for both casual exploration and detailed analysis of personal music listening patterns.

