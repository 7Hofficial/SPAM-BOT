import glob
from pathlib import Path
from SpamBots.utils import load_plugins
import logging
from . import 7H-Spam, 7H-Spam2, 7H-Spam3, 7H-Spam5 , 7H-Spam6, 7H-Spam7, 7H-Spam8, 7H-Spam9, 7H-Spam10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "SpamBots/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Successfully deployed!")
print("Enjoy! Do visit @CHAT_INJECTOR7H")

if __name__ == "__main__":
    7H-Spam.run_until_disconnected()
    
if __name__ == "__main__":
    7H-Spam2.run_until_disconnected()

if __name__ == "__main__":
    7H-Spam3.run_until_disconnected()
    
if __name__ == "__main__":
    7H-Spam4.run_until_disconnected()

if __name__ == "__main__":
    7H-Spam5.run_until_disconnected()
    
if __name__ == "__main__":
    7H-Spam6.run_until_disconnected()

if __name__ == "__main__":
    7H-Spam7.run_until_disconnected()
    
if __name__ == "__main__":
    7H-Spam8.run_until_disconnected()

if __name__ == "__main__":
    7H-Spam9.run_until_disconnected()
    
if __name__ == "__main__":
    7H-Spam10.run_until_disconnected()

