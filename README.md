# Python SQLite CRUD Scripts

A collection of Python scripts demonstrating basic CRUD (Create, Read, Update, Delete) operations using SQLite. This project serves as an introduction to interacting with SQLite databases through Python, covering essential database functions and data manipulation.

## Features

- **Create**: Add new records to an SQLite database.
- **Read**: Retrieve and display data.
- **Update**: Modify existing records.
- **Delete**: Remove records from the database.
- **SQLite Integration**: A lightweight database solution, ideal for local data storage.

## Requirements

- **Python 3.x**

### Libraries

The project relies on the standard Python library:
- `sqlite3`: Python’s built-in SQLite library, requiring no additional installation.

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shahramsamar/Python_sqllite_crude_Scripts.git
    cd Python_sqllite_crude_Scripts
    ```

2. **Run the Scripts:**

    Each script performs specific CRUD operations. Use:

    ```bash
    python <script_name>.py
    ```

3. **Database Setup:**

   Some scripts may create an SQLite database file (`.db`) if it doesn't already exist.

### Project Structure

- `create_record.py`: Script to add new entries.
- `read_records.py`: Script to display database records.
- `update_record.py`: Script to update existing records.
- `delete_record.py`: Script to remove records.
- `sample.db`: Sample SQLite database (optional).

## Contributing

Contributions are welcome! Feel free to submit pull requests with enhancements, bug fixes, or additional CRUD examples.

## License

This project is open-source and available for educational purposes.
