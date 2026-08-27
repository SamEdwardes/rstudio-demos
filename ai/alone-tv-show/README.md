# Alone TV Show

An MCP server that answers questions about the survival show *Alone*.

<https://en.wikipedia.org/wiki/Alone_(TV_series)>

## Data

[data/alone-contestants.csv](data/alone-contestants.csv) has 124 contestants from
seasons 1 to 12: age, hometown, days lasted, how their run ended, and the 10 items
they took.

Two things to know about the data:

- Season 4 was played by two-person teams. It has 14 contestants and two winners,
  so there are 13 winners across 12 seasons.
- Each season records the 10 items with different wording (`Sleeping bag` and
  `Sleeping Bag`, `Bow & arrows` and `Bow and 6 arrows`). The server folds the 65
  raw strings into 25 canonical items, so counts are correct.

## Run the server

```bash
uv run python server.py
```

The server listens on `http://127.0.0.1:8000/mcp`. Set `PORT` to use a different port.

## Connect an MCP client

With the server running:

```bash
claude mcp add --transport http alone http://127.0.0.1:8000/mcp
```

## Tools

| Tool | What it does |
| --- | --- |
| `dataset_overview` | Size, fields, and the values each field can take. Start here. |
| `search_contestants` | Filter by season, status, gender, country, hometown, age, days lasted, or item. |
| `season_summary` | Winners and survival statistics for one season or all of them. |
| `leaderboard` | Contestants ranked by days lasted. |
| `item_stats` | How often each item was chosen and how those contestants fared. |
| `group_stats` | Compare survival by season, status, gender, country, or age bracket. |

## Test

```bash
uv run pytest
```
