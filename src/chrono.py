import time


class Chrono:
    def __init__(self):
        self._start = time.perf_counter()
        self._end = None

        self._state = "run"

    def start(self):
        """Start the chronometer."""

        self._start = time.perf_counter()
        self._end = None
        self._state = "run"

    def stop(self) -> float:
        """Stop the chronometer and return the elapsed time in seconds."""

        self._end = time.perf_counter()
        self._state = "idle"
        return self._end - self._start

    def get(self) -> float:
        if self._state == "run":
            return time.perf_counter() - self._start
        else:
            return self._end - self._start

    @property
    def text(self) -> str:
        tot = self.get() * 1_000
        secs, msecs = divmod(tot, 1000)
        mins, secs = divmod(secs, 60)
        hours, _ = divmod(mins, 60)

        msecs = int(msecs)
        secs = int(secs)
        mins = int(mins)
        hours = int(hours)
        if hours != 0:
            return f"{hours} h, {mins} min, {secs} s, {msecs} ms"
        elif mins != 0:
            return f"{mins} min, {secs} s, {msecs} ms"
        elif secs != 0:
            return f"{secs} s, {msecs} ms"
        else:
            return f"{msecs} ms"
