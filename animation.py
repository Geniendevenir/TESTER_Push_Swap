import time
import itertools

from rich.console import Console
from rich.live import Live
from rich.text import Text

console = Console()

def loading_animation(stop_event, message):
	spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
	with Live("", refresh_per_second=10) as live:
		for frame in itertools.cycle(spinner):
			if stop_event.is_set():
				live.update("")
				break
			live.update(f"{message} {frame}")
			time.sleep(0.1)			
