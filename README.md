# log-to-telegram
Docker Telegram bot to send logs (or contents of a file) to Telegram chat

## Usage
Modify `docker-compose.yml` with your settings, in volumes replace `/path/to/log` with your logfile and for the environment variables, put your Telegram bot token and the chat ID you want the log to be forwarded to.
