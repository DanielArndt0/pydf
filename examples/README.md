# Examples

This folder contains small, commented examples showing the most common ways to use the library.

## Files

- `basic_usage.py`: minimal API usage
- `custom_regex_usage.py`: custom regex patterns for different PDF layouts
- `mysql_usage.py`: optional MySQL persistence
- `recursive_usage.py`: recursive PDF discovery in nested folders

## Running the examples

From the project root:

```bash
pip install -e .[dev]
python examples/basic_usage.py
python examples/custom_regex_usage.py
python examples/recursive_usage.py
```

The MySQL example requires a running MySQL server and a pre-created table.
