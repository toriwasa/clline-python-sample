# Active Context

## Current Work Focus

### Project Initialization
- Memory bank setup and documentation
- Project structure establishment
- Core architectural patterns documentation

### Development Environment
- Python environment with uv
- Code quality tools configuration
- Testing framework setup

## Recent Changes

### Documentation
- Created initial memory bank structure
- Documented architectural patterns
- Established technical context

### Project Structure
- Set up core directory structure
- Configured development tools
- Defined coding standards

## Next Steps

### Immediate Tasks
1. ✅ Implement base domain model structure (UserAction)
2. ✅ Set up DataFrame validation patterns (UserActionDataFrame)
3. ✅ Create infrastructure layer foundations (TSV/SQLite readers)
4. Establish testing framework

### Technical Setup
1. Configure Ruff for linting and formatting
2. Set up pyright type checking
3. Initialize pytest testing structure
4. Set up Spark environment

## Active Decisions and Considerations

### Architecture Decisions
- Using Spark DataFrame as primary data structure (implemented in UserActionDataFrame)
- Implementing strict validation in domain models (schema validation in constructors)
- Separating business logic from infrastructure (TSV/SQLite readers only handle data conversion)
- Maintaining functional purity in use cases (pending implementation)
- Supporting multiple data sources (TSV files and SQLite database)

### Code Quality Focus
- Strict type checking with pyright
- Consistent code formatting with Ruff
- Clear naming conventions
- Comprehensive documentation

## Important Patterns and Preferences

### Coding Style
- Snake case for functions and variables
- Camel case for classes
- Verb-first function names
- Noun-first property names

### Testing Approach
- Japanese test descriptions for business rules
- Arrange-Act-Assert pattern
- Parallel test structure
- Comprehensive unit testing

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
- Keep business logic pure and functional (pending use case implementation)
- Use Iterator pattern for database reads (implemented in SQLite reader)
