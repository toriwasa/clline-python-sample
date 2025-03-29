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
- Snake case for files, functions, and variables
- Camel case for class names
- Constants in uppercase snake case
- Function names must start with verbs
- Property names must start with nouns
- Literal values must be defined as constants at file start
- Functions with literal value arguments must use Literal type
- All functions require documentation comments
- Complex operations should be split into well-named variables
- All imports must be at file start
- Imports must use relative paths from src/cline-sample

### Function Visibility Rules
- Public functions in infrastructure/usecase layers for controller use
- Private functions prefixed with underscore (_)
- Private functions for internal layer use only

### DataFrame Class Standards
- Use _df for private DataFrame attributes
- Implement schema validation in constructors
- Provide DataFrame access through properties
- Include class documentation with field descriptions
- Calculable values exposed as properties

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
- Tests mirror source structure
- Follow Arrange-Act-Assert pattern
- Test names describe business rules in Japanese
- Test structure:
  1. Arrange: Define test inputs and expected values
  2. Act: Execute test target
  3. Assert: Verify results match expectations

### Documentation Patterns
- Function comments required
- DataFrame schema validation in constructors
- Property getters for DataFrame access
- Clear variable names for complex operations
- Class documentation includes data and property descriptions

### Architecture Implementation
- Domain models define data structures
- Infrastructure layer handles data conversion only
- Use cases implement pure business logic
- Controllers orchestrate operations
- CUI handlers manage command-line interaction

### Business Logic Patterns
- Pure functions without side effects
- Separate validation from business logic
- Explicit type hints for arguments and returns
- Domain model transformation focus
