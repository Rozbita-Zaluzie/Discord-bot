import datetime
import discord
from discord import message, guild, Guild

def getGuild(id):
    if id == 618452274401902600:
        return "bjs.png"
    elif id == 772037458996101140:
        return "msr.jpg"

def parseChannel(id, channel):
    if id == 618452274401902600:
        return channel[1:-1]
    elif id == 772037458996101140:
        return channel[2:]

def on_ready(x, ms):
    fileR = open("log.html", "r")

    lines = fileR.readlines()
    lines = lines[:-1]

    fileW = open("log.html", "w")
    for l in lines:
        fileW.write(l)

    time = datetime.datetime.now()

    minute = time.minute
    if len(str(minute)) == 1:
        minute = "0" + str(minute)

    hour = time.hour
    if len(str(hour)) == 1:
        hour = "0" + str(hour)

    ms_status = "white"
    if ms <= 130:
        ms_status = "green"
    elif ms > 130 and ms < 200:
        ms_status = "orange"
    elif ms > 200:
        ms_status = "red"-

    fileW.write("    <block>\n")
    fileW.write(f"        <time>{time.day}.{time.month}.{time.year} - {hour}:{minute}</time>\n")
    fileW.write("        <br>\n")
    fileW.write("        <mess>\n")
    for xx in x:
        fileW.write(f"            <img src=\"{getGuild(xx.id)}\">\n")
    fileW.write("            <br>\n")
    for xx in x:
        fileW.write("            <txt class=\"green\">[loged] </txt>\n")
        fileW.write(f"            <txt class=\"white\">- {xx.name} </txt>\n")
        fileW.write("            <br>\n")
    fileW.write("            <txt class=\"green\">[loged] </txt>\n")
    fileW.write("            <txt class=\"white-\">-</txt>\n")
    fileW.write(f"            <txt class=\"{ms_status}\"> {ms}ms </txt>\n")
    fileW.write("        </mess>\n")
    fileW.write("        <br>\n")
    fileW.write("    </block>\n")
    fileW.write("</body>")

def on_member_join(guild, member):
    fileR = open("log.html", "r")

    lines = fileR.readlines()
    lines = lines[:-2]

    fileW = open("log.html", "w")
    for l in lines:
        fileW.write(l)

    fileW.write("        <mess>\n")
    fileW.write(f"            <img src=\"{getGuild(guild)}\">\n")
    fileW.write("            <br>\n")
    fileW.write("            <txt class=\"green\">[join] </txt>\n")
    fileW.write("            <txt class=\"blue\">- member </txt>\n")
    fileW.write(f"            <txt class=\"white\">- {member} </txt>\n")
    fileW.write("        </mess>\n")
    fileW.write("        <br>\n")
    fileW.write("    </block>\n")
    fileW.write("</body>")

def on_member_leave(guild, member):
    fileR = open("log.html", "r")

    lines = fileR.readlines()
    lines = lines[:-2]

    fileW = open("log.html", "w")
    for l in lines:
        fileW.write(l)

    fileW.write("        <mess>\n")
    fileW.write(f"            <img src=\"{getGuild(guild)}\">\n")
    fileW.write("            <br>\n")
    fileW.write("            <txt class=\"red\">[leave] </txt>\n")
    fileW.write("            <txt class=\"blue\">- member </txt>\n")
    fileW.write(f"            <txt class=\"white\">- {member} </txt>\n")
    fileW.write("        </mess>\n")
    fileW.write("        <br>\n")
    fileW.write("    </block>\n")
    fileW.write("</body>")

def on_command_error(guild, msg, channel, error):
    fileR = open("log.html", "r")
    lines = fileR.readlines()
    lines = lines[:-2]
    fileW = open("log.html", "w")
    for l in lines:
        fileW.write(l)

    fileW.write("        <mess>\n")
    fileW.write(f"            <img src=\"{getGuild(guild)}\">\n")
    fileW.write("            <br>\n")
    fileW.write(f"            <txt class=\"red\">[error] </txt>\n")
    fileW.write(f"            <txt class=\"blue\">- command </txt>\n")
    fileW.write(f"            <txt class=\"white\">- {msg} </txt>\n")
    fileW.write("            <br>")
    fileW.write(f"            <txt class=\"red\">[error] </txt>\n")
    fileW.write(f"            <txt class=\"blue\">- channel </txt>\n")
    fileW.write(f"            <txt class=\"white\">- {parseChannel(guild, channel)} </txt>\n")
    fileW.write("            <br>")
    fileW.write(f"            <txt class=\"red\">[error] </txt>\n")
    fileW.write(f"            <txt class=\"blue\">- error </txt>\n")
    fileW.write(f"            <txt class=\"white\">- {error} </txt>\n")
    fileW.write("        </mess>\n")
    fileW.write("        <br>\n")
    fileW.write("    </block>\n")
    fileW.write("</body>")

def delete(guild, channel, messages):
    fileR = open("log.html", "r")
    lines = fileR.readlines()
    lines = lines[:-2]

    fileW = open("log.html", "w")
    for l in lines:
        fileW.write(l)

    fileW.write("        <mess>\n")
    fileW.write(f"            <img src=\"{getGuild(guild)}\">\n")
    fileW.write("            <br>\n")
    fileW.write("            <txt class=\"red\">[delete] </txt>\n")
    fileW.write("            <txt class=\"blue\">- channel </txt>\n")
    fileW.write(f"            <txt class=\"white\">- {parseChannel(guild, channel)} </txt>\n")
    fileW.write("            <br>")
    fileW.write("            <txt class=\"red\">[delete] </txt>\n")
    fileW.write("            <txt class=\"blue\">- messages </txt>\n")
    fileW.write(f"            <txt class=\"white\">- {messages} </txt>\n")
    fileW.write("        </mess>\n")
    fileW.write("        <br>\n")
    fileW.write("    </block>\n")
    fileW.write("</body>")

def delete_member(guild, channel, member, messages):
    fileR = open("log.html", "r")

    lines = fileR.readlines()
    lines = lines[:-2]

    fileW = open("log.html", "w")
    for l in lines:
        fileW.write(l)

    fileW.write("        <mess>\n")
    fileW.write(f"            <img src=\"{getGuild(guild)}\">\n")
    fileW.write("            <br>\n")
    fileW.write("            <txt class=\"red\">[delete] </txt>\n")
    fileW.write("            <txt class=\"blue\">- channel </txt>\n")
    fileW.write(f"            <txt class=\"white\">- {parseChannel(guild, channel)} </txt>\n")
    fileW.write("            <br>")
    fileW.write("            <txt class=\"red\">[delete] </txt>\n")
    fileW.write("            <txt class=\"blue\">- name </txt>\n")
    fileW.write(f"            <txt class=\"white\">- {member} </txt>\n")
    fileW.write("            <br>")
    fileW.write("            <txt class=\"red\">[delete] </txt>\n")
    fileW.write("            <txt class=\"blue\">- messages </txt>\n")
    fileW.write(f"            <txt class=\"white\">- {messages} </txt>\n")
    fileW.write("        </mess>\n")
    fileW.write("        <br>\n")
    fileW.write("    </block>\n")
    fileW.write("</body>")

def locker(guild, member, channel, channel2, time):
    fileR = open("log.html", "r")

    lines = fileR.readlines()
    lines = lines[:-2]

    fileW = open("log.html", "w")
    for l in lines:
        fileW.write(l)

    fileW.write("        <mess>\n")
    fileW.write(f"            <img src=\"{getGuild(guild)}\">\n")
    fileW.write("            <br>\n")
    fileW.write("            <txt class=\"red\">[locker] </txt>\n")
    fileW.write("            <txt class=\"blue\">- member </txt>\n")
    fileW.write(f"            <txt class=\"white\">- {member} </txt>\n")
    fileW.write("            <br>")
    fileW.write("            <txt class=\"red\">[locker] </txt>\n")
    fileW.write("            <txt class=\"blue\">- channel </txt>\n")
    fileW.write(f"            <txt class=\"white\">- {parseChannel(guild, channel)} </txt>\n")
    fileW.write("            <br>")
    fileW.write("            <txt class=\"red\">[locker] </txt>\n")
    fileW.write("            <txt class=\"blue\">- channel2 </txt>\n")
    fileW.write(f"            <txt class=\"white\">- {parseChannel(guild, channel2)} </txt>\n")
    fileW.write("            <br>")
    fileW.write("            <txt class=\"red\">[locker] </txt>\n")
    fileW.write("            <txt class=\"blue\">- time </txt>\n")
    fileW.write(f"            <txt class=\"white\">- {time} </txt>\n")
    fileW.write("            <br>")
    fileW.write("            <txt class=\"green\">[locker] </txt>\n")
    fileW.write("            <txt class=\"blue\">- member </txt>\n")
    fileW.write(f"            <txt class=\"white\">- {member} </txt>\n")
    fileW.write("        </mess>\n")
    fileW.write("        <br>\n")
    fileW.write("    </block>\n")
    fileW.write("</body>")

def added(guild, command):
    fileR = open("log.html", "r")

    lines = fileR.readlines()
    lines = lines[:-2]

    fileW = open("log.html", "w")
    for l in lines:
        fileW.write(l)

    fileW.write("        <mess>\n")
    fileW.write(f"            <img src=\"{getGuild(guild)}\">\n")
    fileW.write("            <br>\n")
    fileW.write("            <txt class=\"yellow\">[added] </txt>\n")
    fileW.write(f"            <txt class=\"white\">- {command} </txt>\n")
    fileW.write("        </mess>\n")
    fileW.write("        <br>\n")
    fileW.write("    </block>\n")
    fileW.write("</body>")