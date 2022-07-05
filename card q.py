# you get any card as an argument. your task is to return a suit of this card.our desk(is preloaded)
# eg:("3C")return'clubs'
# ("3d")return"daimonds"
# ("3h")return"heart"
# ("3s")return"spades


deck=["2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
"2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD","AD",
"2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH","AH",
"2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC","AC"]
def define_suit(card):
    card=input("enter any number:")
    if "s" in card:
        print("spades")
    elif "D" in card:
        print("daimonds")
    elif "H" in card:
        print("heart")
    elif "C" in card:
        print("clubs")
define_suit("card")
