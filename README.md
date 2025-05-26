# Cornell Movie Dialogue Age Classification Visualization 🎬📊

An interactive web-based visualization system that analyzes Cornell Movie Dialogs Dataset to classify movies by age groups (Adult, Family, Children) using Natural Language Processing and presents insights through D3.js cloud packing, sunburst diagrams, and word cloud visualizations.

## 🎯 Project Overview

This project processes the Cornell Movie Dialogs Dataset using NLP techniques to extract dialogue features and classify movies into age-appropriate categories. The system generates interactive visualizations including word clouds for thematic analysis, sunburst diagrams for hierarchical data exploration, and cloud packing for entity relationship visualization.

## ✨ Key Features

### 🔍 Natural Language Processing Pipeline
- **Dialogue Text Processing** using NLTK for tokenization and cleaning
- **Named Entity Recognition (NER)** to extract characters, locations, and organizations
- **Age Group Classification** based on dialogue content analysis
- **Feature Extraction** including vocabulary complexity and thematic keywords
- **CSV Data Transformation** for structured analysis and visualization

### 📈 Interactive Visualizations

#### 1. Word Cloud Visualization
- **Dynamic Word Clouds** for each age category (Adult, Family, Children)
- **Interactive Filtering** by movie category and frequency thresholds
- **Hover Details** showing word frequency and context
- **Responsive Sizing** based on term importance and frequency

#### 2. Sunburst Diagram
- **Hierarchical Structure**: Age Groups → Movie Genres → Individual Movies
- **Interactive Navigation** with click-to-zoom functionality
- **Focus+Context Design** maintaining overview while exploring details
- **Color Coding** by age classification with smooth transitions
- **Breadcrumb Navigation** for easy traversal back to overview

#### 3. Cloud Packing Visualization
- **Circular Packing Layout** showing movie relationships and clustering
- **Size Encoding** representing dialogue volume or complexity metrics
- **Interactive Exploration** with zoom, pan, and selection capabilities
- **Entity Grouping** based on NER results and thematic similarity

### 🔗 Brushing & Linking Implementation
- **Cross-Visualization Selection** where clicking elements updates all views
- **Coordinated Filtering** across word cloud, sunburst, and cloud packing
- **Real-time Updates** with smooth animations between states
- **Synchronized Highlighting** of related elements across visualizations

## 🛠️ Technical Stack

### Backend Processing
- **Python** - Core data processing and NLP analysis
- **NLTK** - Natural Language Processing and NER
- **Pandas** - Data manipulation and CSV processing
- **Flask/Django** - Web framework for serving processed data
- **Scikit-learn** - Text vectorization and classification

### Frontend Visualization
- **D3.js** - Interactive data visualizations
- **HTML5/CSS3** - Structure and responsive styling
- **JavaScript** - Client-side interactions and data binding

### Data Processing Pipeline
```
Cornell Movie Dataset → Text Cleaning → NER Processing → 
Age Classification → CSV Export → JSON API → D3.js Visualizations
```

## 📊 Dataset Processing

### Cornell Movie Dialogs Dataset
- **220,579 conversational exchanges** between movie characters
- **617 movies** with metadata including genre and year
- **9,035 movie characters** with dialogue attribution
- **Custom Age Classification** based on dialogue content analysis

### Data Transformation Process

#### 1. Text Preprocessing
```python
# Clean and normalize dialogue text
# Remove special characters and standardize formatting
# Tokenize sentences and extract meaningful terms
```

#### 2. Named Entity Recognition
```python
# Extract entities: PERSON, LOCATION, ORGANIZATION
# Generate NER CSV with entity types and frequencies
# Create entity-movie relationship mappings
```

#### 3. Age Group Classification
- **Adult Movies**: Complex themes, mature language patterns
- **Family Movies**: Universal themes, moderate complexity
- **Children Movies**: Simple vocabulary, positive sentiment

#### 4. CSV Generation
- `movies_classified.csv` - Movie metadata with age classifications
- `dialogue_features.csv` - Extracted features per movie
- `ner_entities.csv` - Named entities with frequencies and types
- `word_frequencies.csv` - Term frequencies by age group

## 🎨 Visualization Details

### Word Cloud Implementation
```javascript
// D3.js word cloud with interactive features
// Size based on term frequency within age groups
// Color coding by age classification
// Interactive filtering and selection
```

**Features:**
- **Dynamic Generation** from processed dialogue data
- **Category Filtering** to show Adult/Family/Children-specific terms
- **Interactive Tooltips** with frequency and movie context
- **Responsive Layout** adapting to different screen sizes

### Sunburst Diagram Structure
```
Root
├── Adult Movies
│   ├── Action Genre
│   │   ├── Movie 1
│   │   └── Movie 2
│   └── Drama Genre
└── Family Movies
    ├── Adventure Genre
    └── Comedy Genre
```

**Interactive Features:**
- **Click-to-Zoom** for exploring movie hierarchies
- **Breadcrumb Navigation** showing current path
- **Smooth Transitions** between hierarchy levels
- **Context Preservation** with overview always visible

### Cloud Packing Layout
- **Hierarchical Circles** representing movie clusters by age group
- **Size Encoding** based on dialogue volume or complexity metrics
- **Interactive Zoom** for detailed exploration of clusters
- **Entity Highlighting** showing NER-based relationships

## 🚀 Installation & Setup

### Prerequisites
```bash
Python 3.8+
Flask/Django
Node.js (optional, for development server)
Modern web browser
```

### Backend Setup
```bash
# Clone repository
git clone https://github.com/yourusername/cornell-movie-age-viz.git
cd cornell-movie-age-viz

# Install Python dependencies
pip install nltk pandas flask scikit-learn

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('named_entity_recognition')"

# Process Cornell dataset
python scripts/process_cornell_data.py
python scripts/extract_ner.py
python scripts/classify_age_groups.py

# Start Flask server
python app.py
```

### Data Processing Scripts
```bash
# Generate processed CSVs
python scripts/process_cornell_data.py    # Main data cleaning
python scripts/extract_ner.py            # Named entity recognition
python scripts/generate_features.csv     # Feature extraction
python scripts/export_for_d3.py          # JSON for visualizations
```

## 📁 Project Structure

```
cornell-movie-age-viz/
├── data/
│   ├── raw/
│   │   └── cornell_movie_dialogs/       # Original dataset
│   ├── processed/
│   │   ├── movies_classified.csv        # Movies with age classifications
│   │   ├── dialogue_features.csv        # Extracted dialogue features
│   │   ├── ner_entities.csv             # Named entities by movie
│   │   └── word_frequencies.csv         # Term frequencies by age group
│   └── json/
│       ├── sunburst_data.json           # Hierarchical data for sunburst
│       ├── wordcloud_data.json          # Word frequency data
│       └── cloudpack_data.json          # Clustering data
├── scripts/
│   ├── process_cornell_data.py          # Main data processing
│   ├── extract_ner.py                   # NER extraction
│   ├── classify_age_groups.py           # Age classification model
│   └── export_for_d3.py                 # JSON generation for D3
├── static/
│   ├── js/
│   │   ├── wordcloud-viz.js             # Word cloud implementation
│   │   ├── sunburst-viz.js              # Sunburst diagram
│   │   ├── cloudpack-viz.js             # Cloud packing visualization
│   │   └── interaction-manager.js       # Brushing & linking
│   └── css/
│       └── styles.css                   # Visualization styling
├── templates/
│   └── index.html                       # Main dashboard interface
├── app.py                               # Flask application
└── requirements.txt                     # Python dependencies
```

## 🧠 NLP & Classification Methodology

### Text Analysis Pipeline
1. **Dialogue Extraction** from Cornell dataset conversations
2. **Text Normalization** removing noise and standardizing format
3. **Named Entity Recognition** using NLTK's NER capabilities
4. **Feature Engineering** extracting vocabulary complexity metrics
5. **Age Classification** based on content analysis and thematic keywords

### Classification Criteria
- **Children Movies**: Simple vocabulary, educational themes, positive sentiment
- **Family Movies**: Universal themes, moderate complexity, inclusive content
- **Adult Movies**: Complex narratives, mature themes, sophisticated dialogue

### Generated CSV Files
- **movies_classified.csv**: Movie ID, Title, Year, Genre, Age_Group, Dialogue_Count
- **ner_entities.csv**: Movie_ID, Entity_Text, Entity_Type, Frequency
- **dialogue_features.csv**: Movie_ID, Avg_Word_Length, Vocabulary_Size, Sentiment_Score
- **word_frequencies.csv**: Age_Group, Word, Frequency, Context_Movies

## 🎯 Visualization Interactions

### Cross-Visualization Brushing & Linking
1. **Word Cloud Selection**: Clicking words filters sunburst and cloud packing
2. **Sunburst Navigation**: Selecting age groups updates word cloud terms
3. **Cloud Pack Interaction**: Hovering clusters highlights related elements
4. **Coordinated Filtering**: Age group filters apply across all visualizations

### Interactive Features
- **Hover Tooltips** with detailed information and context
- **Click Selection** for filtering and highlighting related data
- **Zoom Controls** for detailed exploration of complex visualizations
- **Animation Transitions** maintaining user context during updates

## 📊 Key Insights from Analysis

### Age Group Characteristics
- **Children Movies**: High frequency of words like "friend," "help," "magic"
- **Family Movies**: Balanced vocabulary with adventure and relationship themes
- **Adult Movies**: Complex emotional vocabulary and mature thematic elements

### Named Entity Patterns
- **Character Names**: Different naming patterns across age groups
- **Locations**: Adventure settings more common in family films
- **Organizations**: Adult movies feature more complex institutional references

## 🏆 Project Deliverables

### Technical Achievements
- ✅ **Complete NLP Pipeline** with Cornell dataset processing
- ✅ **Named Entity Recognition** with CSV export and analysis
- ✅ **Age Group Classification** based on dialogue content
- ✅ **Three Interactive D3.js Visualizations** (Word Cloud, Sunburst, Cloud Packing)
- ✅ **Brushing & Linking** across all visualization components
- ✅ **Focus+Context Design** maintaining overview during detailed exploration
- ✅ **Data Transformation Pipeline** from raw text to structured CSVs

### Data Processing Outputs
- Processed and classified 617 movies from Cornell dataset
- Generated comprehensive NER analysis with entity frequencies
- Created structured CSV files for visualization and further analysis
- Implemented robust age classification based on dialogue patterns

## 🔮 Future Enhancements

- **Advanced Classification Models** using machine learning for improved accuracy
- **Temporal Analysis** showing how movie dialogue has evolved over decades
- **Character Network Analysis** visualizing relationships within movies
- **Sentiment Analysis Integration** adding emotional context to age classifications
- **Interactive Data Export** allowing users to download filtered datasets

---

*This project demonstrates practical application of Natural Language Processing for content classification, combined with sophisticated interactive visualizations to explore patterns in cinematic dialogue across different age-appropriate movie categories.*