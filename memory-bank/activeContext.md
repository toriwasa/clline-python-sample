# Active Context

## Current Work Focus

### Project Initialization
- ✅ Memory bank setup and documentation
- ✅ Project structure establishment
- ✅ Core architectural patterns documentation

### Development Environment
- ✅ Python environment with uv
- ✅ Code quality tools configuration
- ✅ Testing framework setup

## Recent Changes

### Implementation Progress
- ✅ Created UserAction domain model with DataFrame support
- ✅ Implemented TSV and SQLite data readers
- ✅ Added get_latest_user_actions use case with tests
- ✅ Set up initial testing infrastructure

### Documentation
- ✅ Established memory bank structure
- ✅ Documented architectural patterns
- ✅ Established technical context

### Project Structure
- ✅ Set up core directory structure
- ✅ Configured development tools
- ✅ Defined coding standards

## Next Steps

### Immediate Tasks
1. ✅ Implement base domain model structure (UserAction)
2. ✅ Set up DataFrame validation patterns (UserActionDataFrame)
3. ✅ Create infrastructure layer foundations (TSV/SQLite readers)
4. ✅ Establish testing framework with Spark session fixtures

### Technical Setup
1. ✅ Configure Ruff for linting and formatting (configured in pyproject.toml)
2. ✅ Set up pyright type checking (configured in pyproject.toml)
3. ✅ Initialize pytest testing structure (tests/cline_sample/usecase contains first tests)
4. ✅ Set up Spark environment (implemented in UserActionDataFrame)

## Active Decisions and Considerations

### Recent Implementations
- ✅ UserActionDataFrame with schema validation
- ✅ TSV file reader with Spark DataFrame support
- ✅ SQLite iterator-based data reader
- ✅ Window function-based latest action filtering
- ✅ Initial test structure with Spark fixtures

### Architecture Decisions
- ✅ Using Spark DataFrame as primary data structure (implemented in UserActionDataFrame)
- ✅ Implementing strict validation in domain models (schema validation in constructors)
- ✅ Separating business logic from infrastructure (TSV/SQLite readers only handle data conversion)
- Maintaining functional purity in use cases (initial implementation in get_latest_user_actions)
- ✅ Supporting multiple data sources (TSV files and SQLite database)

### Code Quality Focus
- ✅ Strict type checking with pyright (configured)
- ✅ Consistent code formatting with Ruff (configured)
- ✅ Clear naming conventions (implemented)
- ✅ Comprehensive documentation (added to all components)

## Important Patterns and Preferences

### Coding Style
- Snake case for functions and variables
- Camel case for classes
- Verb-first function names
- Noun-first property names

### Testing Approach
- Japanese test descriptions for business rules
- Arrange-Act-Assert pattern with ConstantsHelper
- Parallel test structure matching source
- Comprehensive Spark DataFrame testing

## Learnings and Project Insights

### Key Insights
- Clear separation of concerns is crucial
- Validation should be separate from business logic
- DataFrame handling requires careful schema management
- Type safety is a primary concern

### Best Practices
- ✅ Document all function signatures (implemented in UserAction and readers)
- ✅ Validate DataFrames in constructors (UserActionDataFrame)
- ✅ Use properties for DataFrame access (df property)
- ✅ Keep business logic pure and functional (implemented in get_latest_user_actions)
- ✅ Use Iterator pattern for database reads (implemented in SQLite reader)
