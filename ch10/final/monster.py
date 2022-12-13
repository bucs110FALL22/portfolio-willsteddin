import requests
import random

class MonstersAPI:
  def __init__(self, pageNumber):
    self.pageNumber = pageNumber
    self.url = f"https://api.open5e.com/monsters/?format=json&page={self.pageNumber}"

  def getPage(self):
    page = requests.get(self.url)
    response = page.json()
    if response.get("results"):
      return response["results"]
    else:
      return None

  def getMonster(self, num):
    page = self.getPage()
    entry = page[num]
    return entry["name"]

  def getStats(self,num):
    page = self.getPage()
    entry = page[num]
    stats = [
      entry["strength"],
      entry["dexterity"],
      entry["constitution"],
      entry["intelligence"],
      entry["wisdom"],
      entry["charisma"]
    ]
    return stats




  