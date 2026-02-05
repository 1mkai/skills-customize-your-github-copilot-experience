# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build scalable REST APIs using the FastAPI framework. You'll create a web service that handles HTTP requests, manages data models, and implements proper routing with validation, developing real-world API development skills.

## 📝 Tasks

### 🛠️ Create a Basic API Endpoint

#### Description
Set up a FastAPI application with basic GET and POST endpoints. Create a simple API that can handle requests and return JSON responses.

#### Requirements
Completed program should:

- Initialize a FastAPI application
- Create at least one GET endpoint that returns JSON data
- Create at least one POST endpoint that accepts data
- Use appropriate HTTP status codes for responses
- Include basic error handling for invalid requests


### 🛠️ Implement Data Validation with Pydantic

#### Description
Define data models using Pydantic to validate incoming request data. Ensure that all API inputs are properly validated before processing.

#### Requirements
Completed program should:

- Create at least one Pydantic model for request/response data
- Use type hints in Pydantic models
- Handle validation errors gracefully
- Return meaningful error messages when validation fails


### 🛠️ Build a Complete CRUD API

#### Description
Extend your API to support full CRUD (Create, Read, Update, Delete) operations. Implement endpoints for managing a collection of resources with an in-memory data store.

#### Requirements
Completed program should:

- Implement GET endpoints to retrieve all items and a single item by ID
- Implement POST endpoint to create new items
- Implement PUT endpoint to update existing items
- Implement DELETE endpoint to remove items
- Use proper HTTP methods and status codes for each operation
- Maintain data persistence during the application runtime
