# import_package_data.py

import pymongo
from pymongo import MongoClient
from pymongo.errors import PyMongoError
import json

import pymongo.errors
from package_lookup_table import (
    PACKAGE_LOOKUP_TABLE,
)

# --- 1. Your Data ---
# This is the full dataset you provided.
data = PACKAGE_LOOKUP_TABLE


# --- 2. MongoDB Configuration ---
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "electronics_db"
COLLECTION_NAME = "component_packages"


# --- 3. The Main Function ---
def import_to_mongodb():
    """Connects to MongoDB, cleans the data, and inserts it into a collection."""

    client = None  # Initialize client to None
    try:
        # Establish connection to MongoDB
        client = MongoClient(
            MONGO_URI, serverSelectionTimeoutMS=5000
        )  # 5-second timeout
        # The ismaster command is cheap and does not require auth.
        client.admin.command("ismaster")
        print(f"Successfully connected to MongoDB at {MONGO_URI}")

        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]

        # --- Data Cleaning Step ---
        # Convert string representations of lists into actual arrays for proper storage.
        cleaned_data = []
        for item in PACKAGE_LOOKUP_TABLE:
            # Create a copy to modify
            new_item = item.copy()
            # Clean the 'Typical_Pins' field
            try:
                # Safely parse the string into a Python list
                new_item["Typical_Pins"] = json.loads(new_item["Typical_Pins"])
            except (json.JSONDecodeError, TypeError):
                # If it's not a valid list (e.g., "Variable"), keep the original string
                pass

            # Clean the 'Pitch' field
            try:
                new_item["Pitch"] = json.loads(new_item["Pitch"])
            except (json.JSONDecodeError, TypeError):
                pass

            cleaned_data.append(new_item)
        print("Data cleaning complete. Converted string-lists to arrays.")

        # Optional: Clear the collection before inserting to prevent duplicates on re-runs
        if collection.count_documents({}) > 0:
            print(
                f"Collection '{COLLECTION_NAME}' is not empty. Clearing it before new import..."
            )
            collection.delete_many({})
            print("Collection cleared.")

        # --- Bulk Insert Operation ---
        if cleaned_data:
            result = collection.insert_many(cleaned_data)
            print(f"\nSuccess! Inserted {len(result.inserted_ids)} documents into:")
            print(f"  - Database:   '{DATABASE_NAME}'")
            print(f"  - Collection: '{COLLECTION_NAME}'")
        else:
            print("No data to insert.")
    except pymongo.errors.ConnectionFailure as e:
        print(f"\nError: Could not connect to MongoDB.")
        print("Please ensure your MongoDB server is running and accessible.")
        print(f"Details: {e}")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

    finally:
        # Ensure the client connection is closed
        if client:
            client.close()
            print("\nMongoDB connection closed.")


# --- 4. Run the Script ---
if __name__ == "__main__":
    import_to_mongodb()
