# Tech Context

## Technologies Used

### Core Technologies
- Python (>=3.11) - Primary programming language
- Apache Spark (>=3.5.5) - Data processing framework for DataFrame operations with Window functions
- pandas (>=2.2.3) - Used alongside Spark for data operations
- Ruff (>=0.11.2) - Code linting and formatting tool
- pyright (>=1.1.398) - Static type checking
- pytest (>=8.3.5) - Unit testing framework with Spark session fixtures
- faker (>=37.1.0) - Test data generation

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
- Source code must reside in src/cline_sample/
- Tests must reside in tests/cline_sample/
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
- Imports must use relative paths from src/cline_sample

### Function Visibility Rules
- Public functions in infrastructure/usecase layers for controller use
- Private functions prefixed with underscore (_)
- Private functions for internal layer use only

### DataFrame Class Standards
- ✅ Use _df for private DataFrame attributes (implemented in UserActionDataFrame)
- ✅ Implement schema validation in constructors using StructType/StructField:
  ```python
  SCHEMA = StructType([
      StructField("id", IntegerType(), True),
      StructField("username", StringType(), True),
      StructField("user_machine_id", StringType(), True),
      StructField("action_name", StringType(), True),
      StructField("action_time", TimestampType(), True)
  ])
  ```
- ✅ Provide DataFrame access through properties (df property)
- ✅ Include class documentation with field descriptions and types
- ✅ Implement companion @dataclass for pure data representation (UserAction)

## Dependencies

### Core Dependencies
- Python 3.11+ runtime
- Apache Spark 3.5.5+ for DataFrame operations
- pandas 2.2.3+ for data manipulation
- Ruff 0.11.2+ for code quality
- pyright 1.1.398+ for type checking
- pytest 8.3.5+ for testing framework
- faker 37.1.0+ for test data generation

### Infrastructure Dependencies
- S3 integration capabilities (pending)
- Database integration capabilities:
  - ✅ SQLite for local storage (implemented)
  - ✅ DataFrame operations with Apache Spark (implemented)
  - ✅ TSV file reading capabilities (implemented)
  - ✅ UserActionDataFrame with schema validation (implemented)

## Tool Usage Patterns

### Code Organization
- Domain models in domain/models/:
  - ✅ user_action.py - Contains UserAction and UserActionDataFrame
- Infrastructure code in infrastructure/:
  - ✅ file/user_action_reader.py - TSV file reading
  - ✅ db/sqlite_user_action.py - SQLite operations
- Business logic in usecase/:
  - ✅ get_latest_user_actions.py - Window function based filtering
- Controller layer (pending)
- Handler layer (pending)

### Testing Patterns
- Test files prefixed with test_
- Tests mirror source structure in tests/ directory
- Follow Arrange-Act-Assert pattern with clear section comments
- Test names describe business rules in Japanese
- SparkSession fixture used for DataFrame testing
- Test structure:
  1. Arrange:
     - Constants class for test data
     - SparkSession.createDataFrame with Row objects
     - Clear input and expected output setup
  2. Act: Execute test target function
  3. Assert: Compare DataFrames using collect()

### Data Generation Tools
- ✅ tool/create_sample_data.py:
  - Generates sample user action data in TSV format
  - Uses faker for realistic test data
  - Configurable data volume
- ✅ tool/write_tsv_to_sqlite.py:
  - Imports TSV data into SQLite database
  - Maintains schema consistency
  - Handles data type conversion

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

### Business Logic Implementation
- Pure functions without side effects
- Separate validation from business logic
- Explicit type hints for arguments and returns
- Domain model transformation focus
- Examples:
  ```python
  def get_latest_user_actions(user_actions: UserActionDataFrame) -> UserActionDataFrame:
      """Get the latest actions for each user."""
      window_spec = Window.partitionBy("username").orderBy(desc("action_time"))
      filtered_df = user_actions.df.withColumn("row_number", row_number().over(window_spec))
      return UserActionDataFrame(filtered_df.where(col("row_number") == 1).drop("row_number"))
  ```

### Infrastructure Implementation
- Environment-aware connections
- Literal type for environment selection:
  ```python
  Env = Literal["dev", "stg", "prod"]
  ```
- Match expression for environment routing:
  ```python
  def _get_connection(env: Env) -> Connection:
      match env:
          case "dev":
              return create_dev_connection()
          case "stg":
              return create_stg_connection()
          case "prod":
              return create_prod_connection()
