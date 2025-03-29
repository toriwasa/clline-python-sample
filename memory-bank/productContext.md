# Product Context

## Why This Project Exists

### Primary Objectives
- Enable efficient data processing with Spark DataFrames
- Provide a robust CLI-based data processing system
- Ensure data integrity through strict validation
- Maintain high code quality and maintainability

### Problem Space
- Complex data processing requirements
- Need for robust data validation
- Requirements for S3 and database integration
- Command-line based workflow automation

## How It Should Work

### User Interaction
1. Users interact through command-line interface
2. Commands processed with clear parameter validation
3. Business logic executed through use case layer
4. Results processed through appropriate infrastructure
5. Feedback provided through CLI

### Data Flow
1. Input data validated at domain model level
2. Business rules applied through use cases
3. Data persistence handled by infrastructure
4. Results returned through controller layer
5. Output presented via CLI handler

### Error Handling
- Clear validation error messages
- Proper business rule violation reporting
- Infrastructure error handling
- User-friendly CLI feedback

## User Experience Goals

### Command Line Interface
- Clear and intuitive commands
- Helpful error messages in Japanese
- Predictable behavior
- Efficient execution

### Data Processing
- Reliable data validation
- Consistent error handling
- Efficient processing of large datasets
- Clear operation feedback

### Code Maintenance
- Well-documented functions
- Clear separation of concerns
- Easy to test and modify
- Consistent coding patterns

### System Reliability
- Robust error handling
- Data integrity protection
- Clear operational feedback
- Predictable behavior patterns
