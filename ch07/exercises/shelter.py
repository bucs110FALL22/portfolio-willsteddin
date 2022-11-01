from socketserver import StreamRequestHandler
import animal

def main():
  nezarec = animal.Animal("Pterodactyl", "Nezarec")
  nezarec.setAdopted()
  print(nezarec.type, nezarec.name, nezarec.id, nezarec.date, nezarec.adoption)

main()
  
