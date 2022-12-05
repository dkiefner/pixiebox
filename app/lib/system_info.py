#!/usr/bin/env python

from lib.shell import Shell


class SystemInfo:

    @staticmethod
    def gpu_temp():
        return Shell.execute("vcgencmd measure_temp | cut -d\"=\" -f 2 | cut -d\"'\" -f 1")

    @staticmethod
    def cpu_temp():
        return Shell.execute("cpu=$(</sys/class/thermal/thermal_zone0/temp);echo $((cpu/1000))")

    @staticmethod
    def pixiebox_logs():
        return Shell.execute("sudo journalctl --unit=pixiebox --no-pager")

    @staticmethod
    def web_app_logs():
        return Shell.execute("sudo journalctl --unit=pixiebox_webapp --no-pager")

    @staticmethod
    def sleep_timer_logs():
        return Shell.execute("sudo journalctl --unit=sleep_timer --no-pager")
