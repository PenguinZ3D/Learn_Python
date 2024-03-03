#Dictionaries are formated as {key:value} ex. {USA: Washington D.C}

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi", 
            "China": "Beijing",
            "Russia": "Moscow"}

#print(capitals.get("India")) #Will report "New Delhi" because that is the value assosiated with that key
#print(capitals.get("Japan")) #Will report NONE because that key doesn't exist in the dictionary

#if capitals.get("Russia"):
#    print("That capital exists")
#else:
#    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"}) #Adds a new Key:Value pair to the dictionary
capitals.update({"USA": "Detroit"}) #Changes capital of USA from Washington to Detroit

print(capitals)