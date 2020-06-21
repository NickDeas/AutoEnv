# AutoEnv
Package applications and websites into "environments" to easily prepare for recurring events.

# HowTo

## CLI
Create, edit, and open environments from the command line.
Preface all commands with "autoenv"

| Command | Function | Notes |
| --- | --- | --- |
| newEnv [env_name] | Create a new empty environment with the given name | |
| rename [env_name] [new_name] | Rename created environment | |
| rem_env [env_name] | Delete a created environment | |
| list | List created environments | |
| display [env_name] | Show applications and websites associated with environment | |
| addApp [env_name] [exe_location] | Add an application to given environment | file_location must from root i.e. "C:// ... /app.exe"|
| addUrl [env_name] [url_address] | Add a website to given environment | Only google chrome supported right now |
| remApp [env_name] [app_index] | Remove an application from given environment | View app index with display command |
| remUrl [env_name] [url_index] | Remove a website from given environment | View url index with display command |
| open [env_name] | Open all applications and websites associated with environment | |

### Getting file locations
Simply find a file in file explorer equivalent, and copy the address, including the executable/file name and extension

## GUI
