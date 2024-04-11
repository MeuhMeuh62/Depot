import random

# données de : https://support.supercell.com/brawl-stars/en/articles/starr-drops-3.html

all_brawlers=["Shelly", "Nita", "Colt", "Bull", "Brock", "El Primo", "Barley", "Poco", "Rosa", "Jessie", "Dynamike", "Tick", "8-Bit", "Rico", "Darryl", "Penny", "Carl", "Jacky", "Gus", "Bo", "Emz", "Stu", "Piper", "Pam", "Frank", "Bibi", "Bea", "Nani", "Edgar", "Griff", "Grom", "Bonnie", "Gale", "Colette", "Belle", "Ash", "Lola", "Sam", "Mandy", "Maisie", "Hank", "Pearl", "Larry & Lawrie", "Angelo", "Mortis", "Tara", "Gene", "Max", "Mr. P", "Sprout", "Byron", "Squeak", "Lou", "Ruffs", "Buzz", "Fang", "Eve", "Janet", "Otis", "Buster", "Gray", "R-T", "Willow", "Doug", "Chuck", "Charlie", "Mico", "Spike", "Crow", "Leon", "Sandy", "Amber", "Meg", "Surge", "Chester", "Cordelius", "Kit"]
spray_en_plus=["Angel", "Arrow Heart", "Banana Peel", "Breaking Wall", "Champion", "Crying Mask", "Don’t Be Salty", "Denied", "Fire Punch", "Flaming", "Footprint", "Gem King", "Lightning Cloud", "Starr Logo", "Sweat Drop", "Thumbs Up", "Warning", "Tengu Mike", "Kitsune Lola", "Oni Otis", "Hanbok Mandy", "Cheerleader Rosa", "Nerd Squeak", "Bell Nani", "Sunken Chest Griff", "Kraken Surge", "Haunted House 8-Bit", "Stone Troll Lou", "Dark Fairy Janet", "Wood Spirit Chester", "Daruma Mr. P", "Leopard Max", "Sultan Carl", "Tempest Tara", "Scorpion Willow", "Raider Cordelius"]

def common_pin(a,b):
    if a==0:
        a="heureux."
    if a==1:
        a="fâché."
    if a==2:
        a="triste."
    print(f"Tu as gagné l'émote de {b} {a}")


def spray(a):
    print(f"Tu as obtenu le spray qui s'appelle : {a}")

def gain_rare(i):
    global coins,power_points,crédits,blings,double_xp
    if 0<=i<0.4190:
        print(f"Tu as obtenu : 50 pièces")
        coins+=50
        print(f"Tu as un total actuel de {coins} pièces")
    elif 0.4190<=i<0.7450:
        print(f"Tu as obtenu : 25 points de pouvoir")
        power_points+=25
        print(f"Tu as un total actuel de {power_points} points de pouvoir")
    elif 0.7450<=i<0.7680:
        print(f"Tu as obtenu : 10 crédits")
        crédits+=10
        print(f"Tu as un total actuel de {crédits} crédits")
    elif 0.7680<=i<0.7910:
        print(f"Tu as obtenu : 20 blings")
        blings+=20
        print(f"Tu as un total actuel de {blings} blings")
    else:
        print(f"Tu as obtenu : 200 doubleurs d'xp")
        double_xp+=200
        print(f"Tu as un total actuel de {double_xp} doubleurs d'xp")

def gain_super_rare(i):
    global coins,power_points,crédits,blings,double_xp
    if 0<=i<0.4238:
        print(f"Tu as obtenu : 100 pièces")
        coins+=100
        print(f"Tu as un total actuel de {coins} pièces")
    elif 0.4238<=i<0.7549:
        power_points+=50
    elif 0.7549<=i<0.7880:
        crédits+=30
    elif 0.7880<=i<0.8211:
        blings+=50
    elif 0.8211<=i<0.8542:
        common_pin(random.randrange(3),random.choice(all_brawlers))
    elif 0.8542<=i<0.8674:
        spray(random.choice(all_brawlers+spray_en_plus))
    else:
        double_xp+=200

def ouverture(i):
    if 0<=i<0.5:
        print("Prix Starr : Rare")
        gain_rare(round(random.random(),4))
    elif 0.5<=i<0.78:
        print("Prix Starr : Super rare")
        gain_super_rare(round(random.random(),4))
    elif 0.78<=i<0.93:
        print("Prix Starr : Epic")
    elif 0.93<=i<0.98:
        print("Prix Starr : Mythique")
    elif 0.98<=i<=1:
        print("Prix Starr : Légendaire")

fin=False
coins=0
power_points=0
crédits=0
blings=0
double_xp=0

while fin==False:
    input("Clique sur ENTREE pour ouvrir le prochain prix star !")
    ouverture(round(random.random(),2))



print(pièce)
print(power_points)
print(crédits)
print(blings)
print(double_xp)

exit()