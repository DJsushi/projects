zisti_ci_mam_chybu = "()()(())"

# ak je prazdne
if not zisti_ci_mam_chybu:
  exit()

stack = [zisti_ci_mam_chybu[0]]

otvaracia = "("
zatvaracia = ")"

for c in zisti_ci_mam_chybu[1:]:
  if otvaracia == c:
    stack.append(c)
  elif zatvaracia == c:
    if not stack.pop() == otvaracia:
      print("ERROR")
      exit()

if (stack == []):
  print("Je validne.")
  exit()
  
print("ERROR")
