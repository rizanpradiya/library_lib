
## Context & Overview
Library_lib is a Command Line Interface (CLI) based application designed to manage book lending systems in public libraries.
This program is built using Python with the CRUD (Create, Read, Update, Delete) concept, utilizing collection types (lists and dictionaries) for data storage.

## Objectives
This project aims to provide a clear, hands-on example of a minimal yet complete library circulation system that beginners can read, run, and extend. Concretely.

## Users / Clients / Stakeholders
- **Library Admin** — manages the catalog (add, edit, delete, check stock) and records lending/returns.
- **Members** — represented operationally by the admin’s actions within this CLI.
- **Public Library Institution** — benefits from a simple, transparent record of collection and circulation.

## Key Features
- **Book CRUD + search** — add, list (with title search), update, and delete books.
- **Borrow/Return with stock sync** — lending decrements stock; returns increment; active loans are tracked.
- **Simple CLI menu** — function-based structure keeps the code readable and easy to extend.

## Limitations
- **Non-persistent data** — all data will be lost when exiting the program.
- **Single-user, console-only** — no roles or concurrent access.
- **Simple lookups** — linear search, intended for small learning datasets.

