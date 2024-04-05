# telegram-to-discord-forwarder

A simple script that awaits for messages in Telegram channel and forwards them to Discord channel.

## Usage

You will need a `config.json` file with the required API keys and other metadata to connect to Discord and Telegram.

The script operates in the following way:
1. Awaits for the messages with given structure in Telegram channel
2. Parses the message and sends a new one to Discord

Initially the script was configured to work with messages from **Arkham Intelligence** platform (received from alerts).

### Preparation

Install required modules: 

```
pip3 install telethon discord
```

Run the script:

```
python3 main.py
```

... receive a message in the channel.

### Telegram incoming message example
```
Smart Traders
From: CEX Exchange (0xDFd)
To: XXX Markets (0xD8D)
Value: 9,000.0000 LQTY ($9,953.08)
Network: Ethereum
Time: 2023-10-10 19:00:00 UTC

View on Arkham | View on Etherscan | Pause Alert
```

### Discord outgoing message example
```
:e_mail: From: CEX Exchange (0xDFd)
:envelope_with_arrow: To: XXX Markets (0xD8D)
:moneybag: Value: 9,000.0000 LQTY ($9,953.08)
:ringed_planet: Network: Ethereum
:timer: Time: 2023-10-10 19:00:00 UTC
---------------------------
```

\* emojis are displayed correctly in the Discord itself.
