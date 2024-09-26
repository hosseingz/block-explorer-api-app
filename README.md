# Block Explorer API 📊

Welcome to the **Block Explorer API**! This is a Django-based RESTful API that allows users to explore blockchain blocks and transactions. It provides endpoints to retrieve block details, transaction information, and explore transactions based on specific addresses. The API is built using Django Rest Framework and supports user authentication, rate limiting, and pagination.

## Features ✨

- **User Registration**: Register new users and generate authentication tokens.
- **Explore Blockchain Data**: Retrieve blocks, transactions, and address-specific transaction history.
- **Django Admin Integration**: Export and manage blocks and transactions directly from the Django admin panel.
- **Rate Limiting**: Protect API endpoints with throttling to avoid abuse.
- **Token-based Authentication**: Secure API using token authentication.

## Table of Contents 📚

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Admin Integration](#admin-integration)
- [Data Model](#data-model)
- [License](#license)
## Installation 🛠️

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/block-explorer-api.git
   cd block-explorer-api
   ```

2. **Set up the virtual environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install PostgreSQL**:
   - For **Ubuntu**:
     ```bash
     sudo apt update
     sudo apt install postgresql postgresql-contrib
     ```
   - For **macOS** (using Homebrew):
     ```bash
     brew install postgresql
     brew services start postgresql
     ```
   - For **Windows**:
     Download the installer from the [official PostgreSQL website](https://www.postgresql.org/download/windows/) and follow the installation instructions.

5. **Create a PostgreSQL database**:
   - Access the PostgreSQL prompt:
     ```bash
     sudo -u postgres psql  # For Linux
     psql -U postgres       # For Windows and macOS
     ```
   - Create a new database and user:
     ```sql
     CREATE DATABASE your_database_name;
     CREATE USER your_username WITH PASSWORD 'your_password';
     ALTER ROLE your_username SET client_encoding TO 'utf8';
     ALTER ROLE your_username SET default_transaction_isolation TO 'read committed';
     ALTER ROLE your_username SET timezone TO 'UTC';
     GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_username;
     ```
   - Exit the PostgreSQL prompt:
     ```sql
     \q
     ```

6. **Set up environment variables**:
   Create a `.env` file in the root directory and configure the following:
   ```plaintext
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   DB_NAME="your_database_name"
   DB_USER="your_username"
   DB_PASSWORD="your_password"
   DB_HOST="localhost"
   ```

7. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

8. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## Sample Data 📄

Example blocks and transactions are provided in the `/dataset/` directory:
- `blocks.csv`: Contains sample block data.
- `transactions.csv`: Contains transaction data associated with the blocks.

1. Start your Django development server:
   ```bash
   python manage.py runserver
   ```

2. Navigate to the Django admin interface (typically at `http://127.0.0.1:8000/admin`).

3. Find and select the `Blocks` or `Transactions` section in the admin panel.

4. Click on the "Import" button (you should see this option using the `ImportExportModelAdmin` you set up).

5. Choose the corresponding CSV file (`blocks.csv` or `transactions.csv`) to import.

6. Follow the instructions to upload the CSV file. Once processed, the data will be imported into your database.


After completing the import, check your database to ensure the records have been added correctly. You can do this through the Django admin interface or directly using a database management tool.


## Usage 🚀

After setting up the project, you can start making requests to the API endpoints.

### API Endpoints:

- **User Registration**: 
  - `POST /api/signup/`
  - Request body: 
    ```json
    {
      "username": "your_username",
      "email": "your_email",
      "first_name": "First Name",
      "last_name": "Last Name",
      "password": "your_password"
    }
    ```

- **Get Block Details**:
  - `GET /api/get-block/<block_id>/`
  
- **Get Transaction Details**:
  - `GET /api/get-transaction/<txID>/`
  
- **Get Address Transactions**:
  - `GET /api/get-address-transactions/<address>/`

### Authentication 🔑
The API uses token-based authentication. Upon registering, users receive a token that must be included in the header of authenticated requests:
```bash
Authorization: Token <your_token>
```

## Admin Integration 🖥️

The project integrates with the Django Admin panel for easy management and export of blocks and transactions. You can access the admin interface at `/admin/`.

- Admin actions supported via `import_export.admin.ImportExportActionModelAdmin`.
- Export blocks and transactions in CSV, JSON, and other formats.

## Data Model 🗃️

### Block Model
Represents a blockchain block with the following fields:
- `block_id`: A unique identifier for the block.
- `timestamp`: The time at which the block was mined.

### Transactions Model
Represents a transaction within a block:
- `owner_address`: Address of the sender.
- `to_address`: Address of the receiver.
- `amount`: Transaction amount.
- `txID`: Unique transaction identifier.
- `block`: Foreign key relation to the `Block` model.

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to explore the API and contribute to its development! 😊