# love2docs

A Python tool that downloads Love2D (LÖVE) game engine documentation from the official wiki and converts it to plain text format, creating snapshots of the docs that can be provided as context for LLMs.

## Purpose

This tool snapshots the Love2D documentation into plain text so that it can be provided as context for Large Language Models (LLMs). The generated text files contain the complete Love2D API documentation plus key tutorial pages in a format optimized for AI consumption.

## Pre-generated Files

Instead of running the script yourself, you can download pre-generated documentation files from the [Releases page](https://github.com/xukai92/love2docs/releases). These files are automatically generated and updated when new releases are tagged.

## Usage

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation and Running

```bash
# Clone the repository
git clone https://github.com/xukai92/love2docs.git
cd love2docs

# Install dependencies
uv sync

# Run with default settings (8 concurrent requests, output to love2d_docs.txt)
uv run main.py

# Run with custom concurrency
uv run main.py -c 16

# Run with custom output file
uv run main.py -o my_love2d_docs.txt

# Show all available options
uv run main.py --help
```

### What Gets Downloaded

- All Love2D API functions (love.* namespace)
- Tutorial: Callback Functions
- Getting Started guide
- Building LÖVE guide
- Game Distribution guide  
- Config Files documentation
- English-only content (filters out 20+ other languages)

## Output Format

The generated files contain:
- Markdown-style headers for each page (`## PageName`)
- Raw wiki markup content (preserved for completeness)
- Page separators (`============`)
- Only pages with actual content

## License

MIT License