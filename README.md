# Utilitron-Discord-Bot
 A board/tabletop gaming utilities robot meant to ease the transition of analog games into digital spaces.
 
## Current commands
 The bot is given commands by prefacing your message with an @mention of the bot.

The currently available commands are:
 #### "cpath {integer} [backtrack]"
 
* This command generates an {int}-long path of Cardinal directions (i.e. "N", "S", "E", "W") which cannot backtrack by default. This means that once a step is taken to the North, a subsequent step will not backtrack South. This holds for all directions. The "backtrack" subcommand is optional and allows for creation of paths with backtracking.
  
 #### "opath {integer} [backtrack]"
 
* This command generates an {int}-long path of Ordinal directions (e.g. "N", "SE", "W", "NW") which cannot backtrack by default. This means that once a step is taken to the Northwest, a subsequent step will not backtrack Southeast. This holds for all directions. The "backtrack" subcommand is optional and allows for creation of paths with backtracking.

 #### "homeis ["channel-name"]"
 
 * This command, when given without the optional "channel-name" parameter, prompts Utilitron to send a message confirming where you have told it to post its messages, typically a bot channel, unless you have not already assigned a channel. If "channel-name" is given, it will confirm the given channel as its new home or respond appropriately if that channel does not exist. Requires the sender to have permission to manage channels.
 
 #### "homeishere"
 
 * This command is a convenience command. It sets the channel where this command is sent from as the bot channel for the server. Requires the sender to have permission to manage channels.
 
 #### "evict"
 
 * Removes an stored, bot channel information for the server. Requires the sender to have permission to manage channels.
 
 
 
