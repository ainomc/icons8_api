import sys
import os
from sys import platform
if "win" in platform:
	sys.path.append("..")
elif "linux" in platform:
	sys.path.append('/var/lib/jenkins/workspace/icons8api_tests')