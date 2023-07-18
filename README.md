<p align="center">
  <img width="442" height="90" src="https://github.com/logtracing/node-pkg/assets/55886451/a605b6fd-14c8-4d0d-9cfa-c8f0742aa5ec">
</p>

<p align="center">The <strong>LogTracing</strong> CLI app is a user-friendly tool providing access to log and exception data across your applications, enabling efficient debugging and performance analysis.</p>

## :book: Usage

### :wrench: Initial configuration
:exclamation: **You must have Python >= 3.6 installed**.

Clone this project:
```bash
git clone https://github.com/logtracing/cli.git logtracing-cli
```

Create & activate a virtual environment:
```bash
cd logtracing-cli/
python3 -m venv ./venv
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

You can run the tests by executing the next command:
```bash
python -m pytest tests/
```

## :rocket: Usage
### `config` command
#### Setting up your database (first time)
```bash
python -m logtracing config create \
    --db-user=<USER> \
    --db-pass=<PASSWORD> \
    --db-host=<HOST> \
    --db-port=<PORT> \
    --db-name=<DATABASE_NAME>
```

**Options:**
- `--force, -f`: Overwrite the current DB information.

#### Show your current configuration
```bash
python -m logtracing config show
```

### `log` command
#### Show stored logs
```bash
python -m logtracing log show --flow=<FLOW>
```

**Options:**
- `--limit, -l`: Limit the log list.

### `--help` option
You can use the `help` option for each command and subcommand
```bash
python -m logtracing --help

python -m logtracing config --help
python -m logtracing config show --help

python -m logtracing log --help
python -m logtracing log show --help
```
