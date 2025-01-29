# velocity_emp_recorde
This project is an **Employee Record Management System** built to save and manage information of employees. It performs **CRUD** operations with **JWT Token** authentication, using **Django Rest Framework**. Additionally, it implements a **logger** to save responses in log files for tracking purposes.
## Description
The Employee Record Management System allows users to create, view, update, and delete employee records securely using JWT Token-based authentication. The API logs every request and response, ensuring all interactions with the system are captured for future reference.
## Technologies Used
- Python
- Django
- Django Rest Framework
- JWT Token Authentication
- Logging
- Middleware
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/nikhiljamdar/velocity_emp_recorde.git
## Usage
After the installation, you can interact with the API using tools like **Postman** Here's the step-by-step guide on how to use the API for registration, login, and performing CRUD operations on employee records.
### 1. **Register a User**
To register a user, send a `POST` request to the following URL with the required username and password:
**URL**: `POST /api/register/`

### 2. **Login and Generate JWT Tokens**
To log in and obtain the access and refresh tokens, you can use either of the following URLs:
- **URL**: `POST /api/login/` (Custom Login View)
- **OR**: `POST /api/token/` (Django REST Framework JWT view)

### 3. **Refresh Access Token**
To refresh the access token using the refresh token, you can use either of the following URLs:
**URL**: `POST /api/token/refresh/` (Standard refresh token URL)
- **OR**: `POST /api/custom_token/refresh/` (Custom refresh token view)

### 4. **Perform CRUD Operations on Employee Records**
We must include the access token in the `Authorization` header with the **Bearer Token** authentication scheme for all CRUD operations.

**Create a New Employee**
- **URL**: `POST /api/employees/`
**Example request body:**
```json
  {
        "name": "Nikhil Jamdar",
        "salary": "100000.00",
        "email": "nik@example.com",
        "phone_number": {
            "number": "9372998391"
        }
  }
  ```

