# 🚀 Python to MongoDB Data Converter

**Automated data migration tool for seamlessly converting Python data structures to MongoDB collections**

## ✨ Overview

This powerful Python script provides an efficient, automated solution for converting structured data from Python files directly into MongoDB collections. Designed specifically for electronics component package data, it features intelligent data cleaning, robust error handling, and bulk operations for optimal performance.

## 🎯 Key Features

### 🔄 **Automated Data Conversion**
- Seamlessly converts Python lookup tables to MongoDB documents
- Intelligent parsing of string-formatted arrays into proper MongoDB arrays
- Automatic data type conversion and validation

### 🧹 **Smart Data Cleaning**
- Converts string representations of lists into actual arrays
- Handles JSON parsing with graceful fallback for invalid data
- Preserves original data when conversion isn't possible

### 🚀 **Efficient Bulk Operations**
- High-performance bulk insert operations
- Optional collection clearing to prevent duplicates
- Optimized for large datasets

### 🛡️ **Robust Error Handling**
- Connection timeout management (5-second default)
- Comprehensive exception handling for MongoDB errors
- Graceful connection cleanup and resource management

### 🌐 **Universal MongoDB Compatibility**
- **Compatible with any MongoDB instance** (local, remote, cloud)
- Configurable connection strings
- Works with MongoDB Atlas, self-hosted, and Docker containers

## 📦 What's Included

- **`app.py`** - Main conversion script with full automation
- **`package_lookup_table.py`** - Sample data structure (electronics components)
- **README.md** - Comprehensive documentation

## 🚀 Quick Start

### Prerequisites
```bash
pip install pymongo
```

### Configuration
1. Update MongoDB connection settings in `app.py`:
```python
MONGO_URI = "mongodb://localhost:27017/"  # Customize for your setup
DATABASE_NAME = "electronics_db"
COLLECTION_NAME = "component_packages"
```

### Usage
```bash
python app.py
```

## 📊 Sample Data Structure

The script handles complex data structures like:
```python
{
    "Package_Type": "DIP",
    "Typical_Pins": "[8, 14, 16, 20, 24, 28, 40]",  # Converted to array
    "Pitch": "2.54",
    "Description": "Dual In-line Package"
}
```

## 🔧 Customization

- **Data Source**: Replace `PACKAGE_LOOKUP_TABLE` with your own data
- **Database Config**: Modify connection settings for your MongoDB instance
- **Collection Management**: Enable/disable automatic collection clearing
- **Data Cleaning**: Customize parsing logic for your specific data format

## 🌟 Perfect For

- **Data Migration Projects** - Moving from Python data files to MongoDB
- **ETL Processes** - Extract, Transform, Load operations
- **Database Seeding** - Populating MongoDB with initial data
- **Development Workflows** - Quick data imports for testing

## 📈 Performance

- Bulk insert operations for maximum throughput
- Efficient memory usage with streaming data processing
- Connection pooling and timeout management
- Optimized for both small and large datasets

---

**Ready to supercharge your data migration? Clone this repository and start converting your Python data to MongoDB in minutes!** 🚀
