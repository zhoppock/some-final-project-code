
firstClass = [["David Nimri", "Open"], ["Open", "Open"], ["Open", "Open"], ["Open", "Open"]]
coach = [["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"]]

def firstTable(f):
  group = ""
  # r increments to define the number of each row
  r = 1
  group += "\n\t\t========= First Class ======== \n"
  group += "      |    Seat A    |    Seat B    |\n"
  #the for loop prints each row with it's open seats, with 12 character spaces per seat
  for item in f:
    group += "Row " + str(r) + " | " + item[0] + " "*(12-len(item[0])) + " | " + item[1] + " "*(12-len(item[1])) + " |\n"
    r += 1
  return group

def coachTable(c):
  group = ""
  # r increments to define the number of each row
  r = 1
  group += "\n\t\t========= Coach Class ======== \n"
  group += "      |    Seat A    |    Seat B    |    Seat C    |    Seat D    |\n"
  #the for loop prints each row with it's open seats, with 12 character spaces per seat.  To make sure Row 10 doesn't push the table out of line, IF statements are implemented with slight different printing instructions
  for item in c:
    if r < 10:
      group += "Row " + str(r) + " | " + item[0] + " "*(12-len(item[0])) + " | " + item[1] + " "*(12-len(item[1])) + " | " + item[2] + " "*(12-len(item[2])) + " | " + item[3] + " "*(12-len(item[3])) + " |\n"
    if r == 10:
      group += "Row " + str(r) + "| " + item[0] + " "*(12-len(item[0])) + " | " + item[1] + " "*(12-len(item[1])) + " | " + item[2] + " "*(12-len(item[2])) + " | " + item[3] + " "*(12-len(item[3])) + " |\n"
    r += 1
  return group

print(firstTable(firstClass))
print(coachTable(coach))