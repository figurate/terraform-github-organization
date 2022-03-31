# diagram.py
from diagrams import Diagram
from diagrams.onprem.vcs import Github
from diagrams.onprem.client import User, Users

with Diagram("Github Organization", show=False, direction="RL"):
     Github("github organization") << [User("admin"), Users("membership")]
