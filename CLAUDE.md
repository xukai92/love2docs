# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

love2docs is a Python tool that downloads Love2D (LÖVE) game engine documentation from the official wiki (love2d.org/wiki) and converts it to plain text format suitable for feeding to LLMs. The tool targets the Love2D API documentation under the "love" namespace plus key tutorial and documentation pages.

## Environment and Dependencies

- Use `uv` to manage the Python environment and dependencies
- Requires Python >=3.11
- Key dependencies: aiohttp, requests, click, beautifulsoup4

## Core Architecture

The main application consists of:

1. **Love2DWikiScraper class**: Core scraper that interfaces with the MediaWiki API
   - Uses MediaWiki API at `https://love2d.org/w/api.php`
   - Fetches page lists via `action=query&list=allpages`
   - Retrieves page content via `action=query&prop=revisions&rvprop=content`
   - Implements async/await pattern for concurrent page fetching

2. **Language filtering**: Automatically excludes non-English pages by filtering out titles containing language codes in parentheses (e.g., "(Español)", "(日本語)", etc.)

3. **Additional pages**: Includes specific tutorial and documentation pages beyond the API (Tutorial:Callback_Functions, Getting_Started, Building_LÖVE, Game_Distribution, Config_Files)

4. **CLI interface**: Click-based command-line interface with options for concurrency, output file, and page prefix

## Common Commands

```bash
# Install dependencies
uv sync

# Run the scraper with defaults (8 concurrent requests, output to love2d_docs.txt)
uv run main.py

# Run with custom concurrency
uv run main.py -c 16

# Run with custom output file
uv run main.py -o custom_output.txt

# Save each page as individual files in a folder
uv run main.py --save-each

# Save each page individually with custom folder name
uv run main.py --save-each -o my_docs

# Test MediaWiki API connectivity and response format
uv run python test_api.py

# Show CLI help
uv run main.py --help
```

## MediaWiki API Integration

The tool works with MediaWiki's API but this specific installation doesn't support the standard "extracts" extension. Instead, it uses:
- `prop=revisions&rvprop=content` to get raw wiki markup
- The content is saved with minimal processing (wiki markup preserved)

## Output Format

Generated files contain:
- Header: "# Love2D Wiki Documentation"
- Each page formatted as: `## {title}` followed by content
- Pages separated by `============` dividers
- Only pages with actual content are included

## Key Implementation Notes

- The scraper automatically handles MediaWiki pagination using continuation tokens
- Async implementation uses semaphores to limit concurrent requests
- Language filtering is comprehensive, covering 20+ language codes
- Error handling includes proper HTTP status checking and JSON parsing