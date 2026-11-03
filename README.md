# Flatiron Cars - Car Routes Lab

## Overview

A simple Flask application that displays a welcome message and checks whether a car model exists in the company's fleet.

## Technologies
- Python
- Flask
- Pytest

## Available Routes

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Displays the welcome message |
| GET | `/<model>` | Checks whether a car model exists |

## Existing Car Models

- Beedle
- Crossroads
- M2
- Panique

## Example Responses

**Welcome route**

`GET /`

Response:
```text
Welcome to Flatiron Cars