import xml.dom.minidom
import os

os.chdir("internet")

doc = xml.dom.minidom.parse("sample.xml")

print(doc.nodeName)
print(doc.firstChild.tagName)

skills = doc.getElementsByTagName("skill")
print("%d skills:" % skills.length)
for skill in skills:
    print(skill.getAttribute("name"))

# Append a new tag to the document
# Does not affect original xml file
newSkill = doc.createElement("skill")
newSkill.setAttribute("name", "bass guitar")
doc.firstChild.appendChild(newSkill)

# Print again
skills = doc.getElementsByTagName("skill")
print("%d skills:" % skills.length)
for skill in skills:
    print(skill.getAttribute("name"))