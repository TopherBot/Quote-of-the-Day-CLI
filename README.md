# Quote‑of‑the‑Day CLI

A one‑file Python utility that prints a random quote to the console.

## Features
- No external dependencies – works with the Python standard library only.
- Cross‑platform (Windows, macOS, Linux).
- Fully type‑annotated and includes a quick‑start usage guide.

## Installation
```bash
# Clone the repo (or copy the single file)
git clone https://github.com/topherbot/quote-of-the-day-cli.git
cd quote-of-the-day-cli
```

## Usage
```bash
python quote_of_the_day.py
```
You will see a random quote like:
```
"The only way to do great work is to love what you do." – Steve Jobs
```

## How It Works
The script contains a hard‑coded list of quotes. On execution it:
1. Chooses a random entry using `random.choice`.
2. Prints the quote to `stdout`.

Feel free to extend the `QUOTES` list or adapt the script to pull from an online API.

---
*Happy coding!*