# Tech Context

## Technologies Used

### Core Technologies
- Python (>=3.11) - Primary programming language
- Apache Spark (>=3.5.5) - Data processing framework for DataFrame operations
- pandas (>=2.2.3) - Used alongside Spark for data operations
- Ruff (>=0.11.2) - Code linting and formatting tool
- pyright (>=1.1.398) - Static type checking
- pytest - Unit testing framework

## Development Setup

### Package Management
- uv - Package manager and virtual environment tool
- Python 3.11+ (specified in .python-version)
- Development dependencies managed in pyproject.toml:
  - Core: pyspark, pandas
  - Dev: faker, pyright, ruff

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
- ✅ Use _df for private DataFrame attributes (UserActionDataFrame)
- ✅ Implement schema validation in constructors (with StructType schema)
- ✅ Provide DataFrame access through properties (df property)
- ✅ Include class documentation with field descriptions
- ✅ Schema definition with StructField types:
  - IntegerType for numeric IDs
  - StringType for text fields
  - TimestampType for datetime fields

## Dependencies

### Core Dependencies
- Python 3.11+ runtime
- Apache Spark 3.5.5+ for DataFrame operations
- pandas 2.2.3+ for data manipulation
- Ruff 0.11.2+ for code quality
- pyright 1.1.398+ for type checking
- faker 37.1.0+ for test data generation

### Infrastructure Dependencies
- S3 integration capabilities (pending)
- Database integration capabilities:
  - SQLite for local storage (implemented)
  - DataFrame operations with Apache Spark (implemented)
  - TSV file reading capabilities (implemented)
  - UserActionDataFrame with schema validation (implemented)

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
- Domain models define data structures:
  - UserAction for core data (implemented)
  - UserActionDataFrame with Spark DataFrame operations (implemented)
- Infrastructure layer handles data conversion only:
  - TSV file reading with schema validation (implemented)
  - SQLite data access with Iterator pattern (implemented)
  - Environment-aware connections (dev/stg/prod)
- Use cases implement pure business logic (pending)
- Controllers orchestrate operations (pending)
- CUI handlers manage command-line interaction (pending)

### Development Environment Setup
```bash
# Install dependencies
uv pip install --upgrade pip
uv pip install -e .
uv pip install -e ".[dev]"

# Create sample data (using faker)
python tool/create_sample_data.py

# Import TSV data to SQLite
python tool/write_tsv_to_sqlite.py
```

### Business Logic Patterns
- Pure functions without side effects
- Separate validation from business logic
- Explicit type hints for arguments and returns
- Domain model transformation focus
