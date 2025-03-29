# Tech Context

## Technologies Used

### Core Technologies
- Python - Primary programming language
- Apache Spark - Data processing framework for DataFrame operations
- pytest - Unit testing framework
- Ruff - Code linting and formatting tool
- pyright - Static type checking

## Development Setup

### Package Management
- uv - Package manager and virtual environment tool
- Python version specified in .python-version

### Code Quality Tools
```bash
# Linting
uv run ruff check --fix

# Formatting
uv run ruff format

# Type Checking
uv run pyright
```

## Technical Constraints

### Code Structure
- Source code must reside in src/cline-sample/
- Tests must reside in tests/cline-sample/
- Follow domain-driven design architecture
- Strict separation of concerns across layers

### Coding Standards
- Snake case for functions and variables
- Camel case for class names
- Constants in uppercase snake case
- Function names must start with verbs
- Property names must start with nouns
- Literal values must be defined as constants

## Dependencies

### Core Dependencies
- Python runtime
- Apache Spark for DataFrame operations
- pytest for testing
- Ruff for code quality
- pyright for type checking

### Infrastructure Dependencies
- S3 integration capabilities
- Database integration capabilities

## Tool Usage Patterns

### Code Organization
- Domain models in domain/models/
- Infrastructure code in infrastructure/
- Business logic in usecase/
- Controllers in controller/
- CUI handlers in handler/cui/

### Testing Patterns
- Test files prefixed with test_
- Tests organized to mirror source structure
- Follow Arrange-Act-Assert pattern
- Test descriptions in Japanese for business rules

### Documentation Patterns
- Function comments required
- DataFrame schema validation in constructors
- Property getters for DataFrame access
- Clear variable names for complex operations
