is_magician = False
is_expert = True


#Check if magicain and expert: "You are a master magician"
if is_magician and is_expert:
    print("You are a master magician.")

#check if magician but not expert: "At least you're getting in there"
elif is_magician and not is_expert:
    print("At least you're getting in there.")

#check if not magician: "You need magic powers"
elif not is_magician:
    print('You need magic powers')