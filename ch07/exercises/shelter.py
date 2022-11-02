from socketserver import StreamRequestHandler
import animal

def main():
  nezarec = animal.Animal("Nezarec", "Pterodactyl")
  nezarec.setAdopted()
  print(nezarec)

main()
  
