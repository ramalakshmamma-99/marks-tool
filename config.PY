"""Read KEY=value settings from a .env file."""
def load_env(Path=".env"):
  settings = {}
with open(Path) as handle:
	for line in handle:
		line = line.strip()
		if not line or line.startswith("#"):
				continue
	
	key, _, value = line.partition("=") 
settings [Key.strip()] = value.strip()
return setting	
