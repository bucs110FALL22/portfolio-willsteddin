import pygame
import requests
import io
pygame.init()

class Chart:
  def __init__(self, str, dex, con, int, wis, cha, name):
    self.url = f"https://image-charts.com/chart?cht=bvs&chd=a:{str},{dex},{con},{int},{wis},{cha}&chxl=0:|Strength|Dexterity|Constitution|Intelligence|Wisdom|Charisma&chs=800x600&chbr=30&chco=FF0000|00FF00|FFA500|0000D1|FFFF00|710193&chl={str}|{dex}|{con}|{int}|{wis}|{cha}|&chtt={name}'s%20Stat%20Distribution&chxt=x,y"

  def showChart(self, window):
    r = requests.get(self.url)
    chart = io.BytesIO(r.content)
    chartImg = pygame.image.load(chart)
    window.blit(chartImg, (0,0))

#https://image-charts.com/chart?cht=bvs&chd=14,10,16,8,11,18&chxl=0:|Strength|Dexterity|Constitution|Intelligence|Wisdom|Charisma&chs=800x600&chbr=30&chco=FF0000|00FF00|FFA500|0000D1|FFFF00|710193&chl=14|10|16|8|11|18|&chtt=Dissimortuum's%20Stat%20Distribution&chxt=x,y
