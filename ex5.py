for i in range(99, 0, -1):
	if i == 1:	
		print(f"{i} more bottle of beer on the wall, {i} more bottle of beer")
		print("Go to the store and buy some more, 99 bottles of beer on the wall…")
	elif  i == 2:	
		print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
		print(f"Take one down, pass it around , {i-1} bottle of beer on the wall…")
	else: 	
		print(f" {i} more bottles of beer on the wall, {i} more bottles of beer")
		print(f"Go to the store and buy some more, {i-1} bottles of beer on the wall…")
 
