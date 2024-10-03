from communication_inter import Communication

child_script = "child.py"

with Communication(child_script) as c:
    names = ["Aldo", "Bri", "Silvia", "Marly", "exit"]
    i = 0
    while not c.isfinish() or i == len(names):
        line_decoded = c.read()
        if line_decoded != None:
            print(line_decoded)
        else:
            break

        # When we see "What's your name?", we can send the next name
        if "What's your name?" == line_decoded:
            c.write(names[i])
            i += 1
            
