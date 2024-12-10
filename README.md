# Authentication & RBAC System

## Setup Instructions
1. Clone the repository.
2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python run.py
   ```

## Endpoints
1. `/register` - Register a new user.
2. `/login` - Authenticate and get a token.
3. `/protected` - Access a protected route (requires token).