def merge_the_tools(string, k):
    # your code goes here
    numsegments = int(len(string)/k)
    for i in range(numsegments):
        segment = string[i*k:(i+1)*k]
        ui = ''
        for j in range(len(segment)):
            if segment[j] not in ui:
                ui += segment[j]
        print(ui)
